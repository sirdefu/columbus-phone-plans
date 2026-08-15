#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""价格变更哨兵。

设计取舍（重要，改之前先读）：

1. **只检测「变了没有」，不解析「现在多少钱」。** 给每家写定向价格解析器很脆——
   页面一改版就静默失效，然后自信地写入错误数字。错数字比过期数字更糟。
   所以这里提取的是「页面上所有带 $ 的文本片段」的集合，比对集合差异。

2. **diff 必须人能读。** 报告里直接列出新增/消失的价格片段原文，
   而不是「哈希从 a1b2 变成 c3d4」。这样你扫一眼就知道值不值得让我重跑分析。

3. **抓不到 ≠ 变了。** 403/超时/DNS 失败一律单独归类为「无法核实」，
   绝不当成变更，也绝不写进 baseline 覆盖掉上次的好数据。

4. **噪声过滤是保守的。** 宁可多报几条也不要漏掉真实降价。
   已知会被过滤掉的：纯脚本/样式、长十六进制串、明显的时间戳。
"""

import json, os, re, sys, time, html as _html
from urllib import request, error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sites import SITES

BASELINE = os.path.join(HERE, "baseline.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

# ── 抓取 ──────────────────────────────────────────────────────────────
def fetch(url, timeout=30, retries=2):
    """返回 (html, None) 或 (None, 失败原因)。失败原因是给人看的字符串。"""
    last = None
    for attempt in range(retries + 1):
        try:
            req = request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            })
            with request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace"), None
        except error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (403, 401, 429):   # 反爬/限流，重试没意义
                break
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        if attempt < retries:
            time.sleep(2 * (attempt + 1))
    return None, last or "unknown"

# ── 提取价格片段 ──────────────────────────────────────────────────────
TAG = re.compile(r"<(script|style|noscript)\b.*?</\1>", re.S | re.I)
COMMENT = re.compile(r"<!--.*?-->", re.S)
ANYTAG = re.compile(r"<[^>]+>")
HEXY = re.compile(r"\b[0-9a-f]{12,}\b", re.I)          # 构建哈希 / nonce
ISOISH = re.compile(r"\b\d{4}-\d{2}-\d{2}T[\d:.]+Z?\b") # 时间戳
LONGNUM = re.compile(r"\b\d{10,}\b")                    # epoch / id
PRICE = re.compile(r"\$\s?\d")

def snippets(raw):
    """把页面压成一组「含 $ 的规范化文本片段」。"""
    t = TAG.sub(" ", raw)
    t = COMMENT.sub(" ", t)
    t = ANYTAG.sub(" ", t)
    t = _html.unescape(t)
    t = HEXY.sub("«hash»", t)
    t = ISOISH.sub("«ts»", t)
    t = LONGNUM.sub("«id»", t)
    t = t.replace(" ", " ")

    out = set()
    # 按句子/短语切，只保留含价格的片段，并裁剪长度避免整段正文进来
    for chunk in re.split(r"[\n\r]+|(?<=[.。!?！？])\s+|\s{3,}", t):
        chunk = re.sub(r"\s+", " ", chunk).strip()
        if not chunk or not PRICE.search(chunk):
            continue
        if len(chunk) > 180:
            # 太长的话只截价格周围的上下文，避免大段法务文本造成噪声
            for m in PRICE.finditer(chunk):
                a = max(0, m.start() - 60); b = min(len(chunk), m.end() + 60)
                out.add(("…" if a else "") + chunk[a:b].strip() + ("…" if b < len(chunk) else ""))
        else:
            out.add(chunk)
    return sorted(out)

# ── 主流程 ────────────────────────────────────────────────────────────
def load_baseline():
    if os.path.exists(BASELINE):
        with open(BASELINE, encoding="utf-8") as f:
            return json.load(f)
    return {}

def main():
    init = "--init" in sys.argv
    base = load_baseline()
    now = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())

    changed, unreachable, ok, new_sites = [], [], [], []

    for key, brand, url, note in SITES:
        raw, err = fetch(url)
        if err:
            unreachable.append((key, brand, url, note, err))
            continue
        snaps = snippets(raw)
        if not snaps:
            unreachable.append((key, brand, url, note, "抓到页面但未发现任何价格字样（可能改成纯 JS 渲染）"))
            continue

        prev = base.get(key, {}).get("snippets")
        if prev is None:
            new_sites.append((key, brand, url, note, len(snaps)))
        else:
            added = [s for s in snaps if s not in set(prev)]
            removed = [s for s in prev if s not in set(snaps)]
            if added or removed:
                changed.append((key, brand, url, note, added, removed))
            else:
                ok.append((key, brand))

        base[key] = {"brand": brand, "url": url, "note": note,
                     "checked": now, "count": len(snaps), "snippets": snaps}

    # 无法核实的站点：保留上次的 baseline，只更新 checked 状态
    for key, brand, url, note, err in unreachable:
        e = base.setdefault(key, {"brand": brand, "url": url, "note": note, "snippets": None})
        e["last_error"] = err
        e["last_error_at"] = now

    with open(BASELINE, "w", encoding="utf-8") as f:
        json.dump(base, f, ensure_ascii=False, indent=1, sort_keys=True)

    report = render(now, changed, unreachable, ok, new_sites, init)
    with open(os.path.join(HERE, "report.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)

    # 给 workflow 用：有变更才开 issue
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")
            f.write(f"count={len(changed)}\n")
    return 0

def render(now, changed, unreachable, ok, new_sites, init):
    L = []
    if init:
        L.append(f"# 哨兵基线已建立 · {now}\n")
        L.append(f"首次运行，为 {len(new_sites)} 个页面建立基线，本次不报告变更。\n")
    else:
        L.append(f"# 资费变更检测 · {now}\n")
        if changed:
            L.append(f"**{len(changed)} 个页面的价格文本发生变化。** 下面是逐条 diff——"
                     f"先自己扫一眼判断是不是实质变动（很多是营销文案微调），"
                     f"确认重要再让 Claude 重跑完整分析并更新页面。\n")
        else:
            L.append("**所有可访问页面的价格文本均无变化。**\n")

    if changed:
        L.append("\n## 发生变化\n")
        for key, brand, url, note, added, removed in changed:
            L.append(f"### {brand} — `{key}`\n")
            L.append(f"盯的是：{note}  \n<{url}>\n")
            if removed:
                L.append(f"\n**消失了 {len(removed)} 条：**\n```diff")
                for s in removed[:25]:
                    L.append(f"- {s}")
                if len(removed) > 25: L.append(f"… 另有 {len(removed)-25} 条")
                L.append("```")
            if added:
                L.append(f"\n**新出现 {len(added)} 条：**\n```diff")
                for s in added[:25]:
                    L.append(f"+ {s}")
                if len(added) > 25: L.append(f"… 另有 {len(added)-25} 条")
                L.append("```")
            L.append("")

    if new_sites:
        L.append("\n## 新纳入监控\n")
        for key, brand, url, note, n in new_sites:
            L.append(f"- **{brand}** `{key}` — 建立基线，{n} 条价格片段。盯：{note}")
        L.append("")

    if unreachable:
        L.append("\n## 无法核实\n")
        L.append("这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。\n")
        for key, brand, url, note, err in unreachable:
            L.append(f"- **{brand}** `{key}` — `{err}`  \n  <{url}>")
        L.append("\n> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；"
                 "但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。\n"
                 "> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。\n")

    if ok:
        L.append(f"\n## 无变化（{len(ok)} 个）\n")
        L.append("、".join(f"{b}" for _, b in ok) + "\n")

    L.append("\n---\n")
    L.append("*本报告只检测「页面上的价格文本变没变」，不解析具体价格——"
             "定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*\n")
    L.append("*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*\n")
    return "\n".join(L)

if __name__ == "__main__":
    sys.exit(main())
