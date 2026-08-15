# -*- coding: utf-8 -*-
import json, sys, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from tpl import CSS, JS
from data_extra import TAX, LINE_FEES, ACTIVATION, COVERAGE, MULTILINE, DEVICE
from data_plans import BRANDS, P
from data_audit import AUDIT, ROAST, RECS, CUTLIST, VERDICT_LINE

DATE = "2026-08-14"
# 输出路径：默认写到仓库根目录；可用 `python3 src/build.py <输出路径>` 覆盖
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, f"Columbus_手机套餐对比_{DATE}.html")

BRAND_BY = {b["name"]: b for b in BRANDS}

def landed(p, use_promo=False):
    base = p.get("promo") if (use_promo and p.get("promo") is not None) else p.get("adv")
    if base is None: return None
    if p.get("tax_inc"): return base
    fee = p.get("fee", BRAND_BY[p["brand"]].get("fee", 0.0))
    return base * (1 + TAX["combined"] / 100) + fee + TAX["ng911"]

def money(v):
    if v is None: return "—"
    s = f"{v:.2f}"
    if s.endswith(".00"): s = s[:-3]
    return "$" + s

def esc(s): return html.escape(str(s), quote=False)

import re as _re
_AMP = _re.compile(r'&(?!(?:[a-zA-Z][a-zA-Z0-9]{1,8}|#\d{1,7}|#x[0-9a-fA-F]{1,6});)')
def rich(s):
    """用于我手写、内含 <b>/<span> 标签的叙述字段：只把裸 & 补成 &amp;，标签原样保留。"""
    return _AMP.sub('&amp;', str(s))

# ── 组装 JS 数据 ──────────────────────────────────────────────────────
plans_js = []
for p in P:
    b = BRAND_BY[p["brand"]]
    plans_js.append(dict(
        id=p["id"], brand=p["brand"], brand_short=b["short"], net=b["net"],
        name=p["name"], adv=p["adv"], promo=p.get("promo"), tax_inc=bool(p.get("tax_inc")),
        fee=p.get("fee", b.get("fee", 0.0)), oneline=p.get("oneline", ""),
        data=p.get("data", ""), depri=p.get("depri", ""), hotspot=p.get("hotspot", ""),
        video=p.get("video", ""), intl=p.get("intl", ""), prepay=p.get("prepay", ""),
        autopay=p.get("autopay", ""), cond=p.get("cond", ""),
        promo_terms=p.get("promo_terms", ""), notes=p.get("notes", ""),
        url=p.get("url", ""), chips=p.get("chips", []),
    ))
DATA_JS = dict(
    date=DATE,
    tax=dict(combined=TAX["combined"], ng911=TAX["ng911"]),
    brands=[dict(name=b["name"], short=b["short"], net=b["net"], blurb=b["blurb"],
                 gotchas=b.get("gotchas", [])) for b in BRANDS],
    plans=plans_js,
)

# ── 分节渲染 ──────────────────────────────────────────────────────────
def money2(v):
    """换算表专用：固定两位小数，保证列对齐。"""
    return "—" if v is None else f"${v:.2f}"

def sec_tax():
    rows = ""
    for lvl in [20, 25, 30, 35, 45, 50, 70, 90]:
        r_vz = lvl * (1 + TAX["combined"] / 100) + 3.99 + TAX["ng911"]
        r_att = lvl * (1 + TAX["combined"] / 100) + 4.99 + TAX["ng911"]
        r_tmo = lvl * (1 + TAX["combined"] / 100) + 4.49 + TAX["ng911"]
        mult = r_att / lvl
        rows += (f"<tr><td class='num rowlab'>{money(lvl)}</td><td class='num'>{money2(r_vz)}</td>"
                 f"<td class='num'>{money2(r_att)}</td><td class='num'>{money2(r_tmo)}</td>"
                 f"<td class='num'>×{mult:.2f}</td><td class='num best'>{money(lvl)}</td></tr>")
    fees = "".join(
        f"<tr><td class='rowlab'>{k}</td><td class='num'>{money(v['fee'])}</td><td>{esc(v['detail'])}</td></tr>"
        for k, v in LINE_FEES.items())
    act = "".join(
        f"<tr><td class='rowlab'>{esc(a[0])}</td><td>{esc(a[1])}</td><td>{esc(a[2])}</td>"
        f"<td><span class='tag'>{esc(a[4])}</span></td></tr>" for a in ACTIVATION)
    src = "".join(f"<li><a href='{s[1]}' target='_blank' rel='noopener'>{esc(s[0])}</a></li>" for s in TAX["src"])
    return f"""
<section id="tax"><h2><span class="num">01</span>口径：把所有价格换算成「到手价」</h2>
<p class="lede">这是整份对比的地基。原表最大的问题就是拿<b>含税价</b>和<b>不含税价</b>直接比大小排名。
俄亥俄的话费税加运营商自收费不是小数——在低价档能吃掉 40%。不换算，「同价位对比」就是假的。</p>

<div class="verdict"><h3>换算公式</h3>
<p><span class="mono">到手价 = 广告价 × {1 + TAX['combined']/100:.4f} + 每线固定费 + ${TAX['ng911']:.2f}</span></p>
<p class="muted" style="margin-top:8px">政府税费 <b>{TAX['combined']}%</b>（俄亥俄州+地方 {TAX['state_local_tf']}% + 联邦 USF {TAX['usf_q3_2026']}%）
· 每线固定费 Verizon $3.99 / AT&amp;T $4.99 / T-Mobile $4.49 · 俄亥俄 NG911 ${TAX['ng911']:.2f}/线/月</p></div>

<div class="warnbox"><b>我对权威数据做了一处修正。</b> Tax Foundation 2025 版给俄亥俄的合计税率是 {TAX['combined_tf']}%，
但它用的是 2025 年三季度的联邦 USF 缴费系数（36.0%）。FCC 已在 2026-06-15 核准 Q3 2026 系数为
<b>38.8%</b>（历史最高）。按 38.8% × 37.1% 安全港 = {TAX['usf_q3_2026']}%，俄亥俄实际应为 <b>{TAX['combined']}%</b>。
直接抄 Tax Foundation 会低估约 1 个百分点。</div>

<h3>广告价 → 到手价对照</h3>
<div class="tw"><table>
<thead><tr><th class="num">广告价</th><th class="num">Verizon</th><th class="num">AT&amp;T</th><th class="num">T-Mobile</th>
<th class="num">倍率</th><th class="num">税费已含品牌</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="muted" style="margin-top:9px">{esc(TAX['note'])}</p>

<h3>每线固定费——比价时最常被漏掉的一块</h3>
<div class="tw"><table><thead><tr><th>运营商</th><th class="num">每线每月</th><th>说明</th></tr></thead>
<tbody>{fees}</tbody></table></div>
<p class="muted" style="margin-top:9px">这三笔<b>都不是税</b>，是运营商自收的。Tax Foundation 的税率<b>不覆盖</b>这部分，
这正是多数比价文章算错的地方。AT&amp;T 的 $4.99 是 2026-08-05 刚涨的，八个月内从 $3.49 连涨两次到 $4.99，累计 43%。</p>

<h3>一次性开卡费</h3>
<div class="tw"><table><thead><tr><th>品牌</th><th>金额</th><th>说明</th><th>置信度</th></tr></thead>
<tbody>{act}</tbody></table></div>

<details class="src"><summary>本节来源</summary><ul class="srclist">{src}</ul></details>
</section>"""

def sec_axis():
    return """
<section id="axis-sec"><h2><span class="num">02</span>价格轴：谁和谁在同一个价位</h2>
<p class="lede">按当前口径把所有套餐排在一条轴上，按底层网络分三行。
<b>点任意一个点</b>可跳到该套餐并展开它的同价位对手清单。</p>
<div class="axis" id="axis"></div>
<p class="muted" style="margin-top:11px">同一个网络里价格重叠得越密，说明这一档的竞争越充分、你越不该多付钱。
注意 Verizon 行的两端差距——同样是 Verizon 的网，$25 和 $60 都能买到「无限」。</p>
</section>"""

def sec_brands():
    return """
<section id="brands"><h2><span class="num">03</span>按品牌逐档对比</h2>
<p class="lede">点开任意品牌看它的<b>全部</b>套餐档位（原表每家只列了 1 个）。
再点开任意套餐，会自动列出<b>所有品牌在这个价位区间内的竞品</b>，并在上方价格轴高亮该区间。</p>
<div class="brandgrid" id="brandgrid"></div>
<div class="panel" id="panel"></div>
</section>"""

def sec_multiline():
    out = ""
    for brand, m in MULTILINE.items():
        rows = ""
        for pname, arr in m["plans"].items():
            cells = ""
            best = min([x for x in arr if x is not None], default=None)
            for v in arr:
                if v is None:
                    cells += "<td class='num muted'>未公布</td>"
                else:
                    cells += f"<td class='num{' best' if v == best and arr.count(v) < 5 else ''}'>{money(v)}</td>"
            rows += f"<tr><td class='rowlab'>{esc(pname)}</td>{cells}</tr>"
        out += f"""<h3>{esc(brand)}</h3>
<div class="tw"><table><thead><tr><th>套餐</th><th class="num">1 线</th><th class="num">2 线</th>
<th class="num">3 线</th><th class="num">4 线</th><th class="num">5 线</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="muted" style="margin:8px 0 4px"><b>税费</b>：{esc(m['tax'])} · <b>AutoPay</b>：{esc(m['autopay'])} · <b>混搭</b>：{esc(m['mix'])}</p>
<div class="warnbox" style="margin:8px 0 26px"><b>坑：</b> {esc(m['trap'])}
<div style="margin-top:6px"><a href="{m['src']}" target="_blank" rel="noopener">出处</a></div></div>"""
    return f"""
<section id="multiline"><h2><span class="num">04</span>多线拼卡：每线到底多少</h2>
<p class="lede">表里的数字是<b>每线每月</b>（不是账单总价），均为 BYOD、不含设备。
先说结论：<b>有四家根本没有多线折扣</b>，官方自己承认——Mint、US Mobile、Spectrum、Visible 基础版。
所谓「family plan」在这几家只是账号管理界面。</p>
{out}
</section>"""

def sec_device():
    v = DEVICE["Verizon"]
    cases = "".join(
        f"<tr><td class='rowlab'>{esc(c[0])}</td><td class='num'>{money(c[1]) if c[1] else '—'}</td>"
        f"<td class='num'>{money(c[2]) if c[2] else '—'}</td><td>{esc(c[3])}</td><td>{esc(c[4])}</td>"
        f"<td><span class='tag {'good' if c[5]=='值' else 'bad'}'>{esc(c[5])}</span></td></tr>"
        for c in v["cases"])
    t = DEVICE["T-Mobile"]
    tcases = "".join(
        f"<tr><td class='rowlab'>{esc(c[0])}</td><td>{esc(c[1])}</td><td>{esc(c[2])}</td>"
        f"<td><span class='tag {'good' if c[3]=='值' else 'bad'}'>{esc(c[3])}</span></td></tr>"
        for c in t["cases"])
    a = DEVICE["AT&T"]
    acounter = "".join(f"<li>{esc(x)}</li>" for x in a["counterintuitive"])
    m = DEVICE["MVNO"]
    mbest = "".join(f"<li>{esc(x)}</li>" for x in m["best3"])
    return f"""
<section id="device"><h2><span class="num">05</span>合约送手机：把净账算给你看</h2>
<p class="lede">「免费 iPhone」是本次调研里<b>翻车最多</b>的一块。判断只有一条算式：
<span class="mono">为拿补贴多付的套餐月差价 × 返还月数</span> 是否小于 <span class="mono">补贴总额</span>。
超了就是净亏，而且你还被锁 36 个月。</p>

<div class="verdict"><h3>三条与主流攻略相反的实抓结论</h3>
<p>① <b>Verizon 现在的免费手机不需要以旧换新</b>——机型页 Available offers 面板里根本没有 trade-in 选项。
第三方（WhistleOut 等 2026-08-13 更新）仍在写「需以旧换新」，与官网当前落地页不符。</p>
<p>② <b>AT&amp;T Build-A-Plan 完全不能参与任何设备促销</b>——官方文档逐条写明 NO promotional offers、NO bill credits、
不能分期买机、不能以旧换新。想要补贴手机只能走传统 Unlimited 2.0。</p>
<p>③ <b>Boost 已经没有自建网络了</b>——EchoStar 2025-08-26 把频谱卖给 AT&amp;T，Boost 用户 2025-11-15 全部迁到 AT&amp;T 网络。
今天的 Boost 实质是跑 AT&amp;T 的混合 MVNO，而且它并没有在做激进旗舰补贴（旗舰全部原价）。</p></div>

<h3>Verizon：升档成本 vs 手机抵扣</h3>
<p>硬条件：{esc(' / '.join(v['hard_conditions']))}。<b>{esc(v['step'])}</b>。</p>
<div class="tw"><table><thead><tr><th>机型</th><th class="num">零售价</th><th class="num">抵扣</th>
<th>要求档位</th><th>从 Welcome 出发的净账</th><th>判断</th></tr></thead><tbody>{cases}</tbody></table></div>
<div class="warnbox" style="margin-top:12px"><b>离网/降档：</b>{esc(v['exit'])}
<div style="margin-top:7px"><b>更大的隐藏成本：</b>{esc(v['hidden'])}</div></div>

<h3>T-Mobile：盈亏平衡线 = 补贴 ÷ 36</h3>
<p>{esc(t['bombshell'])}</p>
<div class="tw"><table><thead><tr><th>升档路径</th><th>成本</th><th>结果</th><th>判断</th></tr></thead><tbody>{tcases}</tbody></table></div>
<div class="warnbox" style="margin-top:12px"><b>官网两处口径打架，下单页必须复核：</b>{esc(t['conflict'])}</div>
<p class="muted">{esc(t['saver'])}</p>
<p class="muted"><b>离网条款：</b>{esc(t['exit'])}</p>

<h3>AT&amp;T：三个反直觉发现</h3>
<ul>{acounter}</ul>
<div class="warnbox"><b>Build-A-Plan vs 传统促销的净账：</b>{esc(a['vs_bap'])}</div>
<p class="muted"><b>隐藏变量：</b>{esc(a['hidden'])}</p>
<p class="muted"><b>离网条款：</b>{esc(a['exit'])}</p>

<h3>预付费 / MVNO 阵营</h3>
<p><b>结构上的关键差异：</b>{esc(m['structure'])}</p>
<p class="muted">{esc(m['who_cuts_flagship'])}</p>
<p class="muted"><b>Mint 的标题夸大：</b>{esc(m['mint_exaggeration'])}</p>
<div class="warnbox">{esc(m['visible_notfound'])}</div>
<h4>本组最省钱的三个真实答案</h4><ul>{mbest}</ul>
<p class="muted"><b>转网/保号条件：</b>{esc(m['port_req'])}</p>
<p class="muted"><b>最短保号期：</b>{esc(m['min_hold'])}</p>
<div class="warnbox"><b>官网自身的两处缺陷：</b>{esc(m['page_bugs'])}</div>
</section>"""

def sec_coverage():
    rm = COVERAGE["rootmetrics"]
    rows = "".join(
        f"<tr><td class='rowlab'>{esc(r[0])}</td><td class='num'>{r[1]}</td><td class='num'>{esc(r[2])}</td>"
        f"<td class='num'>{esc(r[3])}</td><td>{esc(r[4])}</td></tr>" for r in rm["rows"])
    fcc = "".join(
        f"<tr><td class='rowlab'>{esc(r[0])}</td><td class='num'>{esc(r[1])}</td><td class='num'>{esc(r[2])}</td></tr>"
        for r in COVERAGE["fcc"]["metro"])
    weak = "".join(
        f"<div class='finding'><h4>{esc(w[0])} <span class='tag'>{esc(w[2])}</span></h4><p>{esc(w[1])}</p></div>"
        for w in COVERAGE["weakspots"])
    return f"""
<section id="coverage"><h2><span class="num">06</span>哥伦布本地实际覆盖</h2>
<p class="lede">{esc(COVERAGE['headline'])}</p>

<h3>RootMetrics 驱车路测（{esc(rm['period'])}）</h3>
<div class="tw"><table><thead><tr><th>运营商</th><th class="num">RootScore</th><th class="num">中位下载</th>
<th class="num">中位上传</th><th>单项奖</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="muted" style="margin-top:8px"><a href="{rm['src']}" target="_blank" rel="noopener">出处：RootMetrics Columbus OH 1H2026</a></p>

<h3>FCC 官方覆盖地图</h3>
<p class="muted">{esc(COVERAGE['fcc']['note'])}</p>
<div class="tw"><table><thead><tr><th>运营商</th><th class="num">室外静止</th><th class="num">行车中</th></tr></thead>
<tbody>{fcc}</tbody></table></div>
<p class="muted" style="margin-top:8px">{esc(COVERAGE['fcc']['city'])}</p>

<h3>已知弱覆盖点</h3>
{weak}

<div class="warnbox"><b>别为 mmWave 买单。</b> {esc(COVERAGE['mmwave'])}</div>
<div class="warnbox"><b>没查到的部分（如实说明）：</b> {esc(COVERAGE['notfound'])}</div>
</section>"""

INTL_ROWS = [
    ("打中国大陆通话", "本次<b>唯一</b>抓到官方费率表白纸黑字含中国大陆（固话+手机都含）的只有两家："
     "<b>Verizon Global Calling Plus</b> 加装包——官方费率表中国大陆一行是 <span class='mono'>China | $0 | $0</span>，"
     "即加装后打中国固话与手机均不限量（注意这是加装包，基础套餐不含）；"
     "以及 <b>Lycamobile</b>——法务清单里 China 位于 Include Landline &amp; Mobile 组。", "已核实"),
    ("Cricket 打中国", "200+ 国家是<b>可加购范围</b>不是自带，按国家单买 $10/月起且有分钟上限。"
     "低价的 Sensible 10GB 与 Select Unlimited <b>连国际短信都不可用</b>。中国大陆的具体月费与分钟数需用官网国家查询工具查，本次抓不出来。", "部分未找到"),
    ("T-Mobile 预付费打中国", "预付费线上<b>根本没有面向中国的通话产品</b>——能买到的国际加装包只有 Mexico &amp; Canada +$5/月 和 "
     "North America international calling +$15/月。国际短信到 215+ 国仅 Unlimited Plus 与 Unlimited Promo 两档自带，"
     "Starter 与 Unlimited 基础档连国际短信都不含。", "已核实"),
    ("T-Mobile 后付费 Stateside International Talk", "该产品页在 t-mobile.com 上已找不到，多个历史 URL 全部 404，"
     "主国际页被重定向到卖套餐的页面。<b>不能确认该 $15 加装包在 2026-08 是否仍在售。</b>", "无法核实"),
    ("Metro / Boost 打中国", "两家的国际加装包清单都抓到了（Metro $10/月 Global Voice 覆盖 210+ 国家与地区；"
     "Boost $10/月 Global Talk &amp; Text 宣称 100+ 国家不限量），"
     "但<b>中国大陆是否在覆盖内、含多少分钟，页面用动态查询工具，抓不出结果</b>。Metro 官网自己也提示要打电话确认。", "无法核实"),
    ("AT&T 打中国", "抓不到官方费率。att.com/international/ 是 JS 壳页面，只有栏目导航没有价格；国际通话子页多个路径全部 404。"
     "不用第三方博客价格冒充官网价，故留空——需到店或致电确认。", "无法核实"),
    ("Google Fi 打中国", "结构已核实：Unlimited Premium 含从美国免费打 50+ 国家和地区；Flexible 与 Standard 只免费打加拿大和墨西哥、"
     "其余按分钟计费；<b>Unlimited Essentials 完全不支持国际</b>。全部套餐国际短信免费。"
     "但那份 50+ 国清单官网没有公开，<b>无法确认中国大陆是否在内</b>。（另：Fi 打中国按 voice.google.com 费率表为 $0.30/分钟）", "部分未找到"),
    ("回国期间保号 · Verizon", "<b>网传的 vacation hold 是错的。</b>官方 FAQ 直接否认长期出国可以挂起。"
     "只有两种挂起：Lost or Stolen（最长 30 天，每线每 12 个月仅一次，到期未恢复会自动断线并丢失号码）与 "
     "Military Deployment（需资格）。回国期间只能继续全额付费保号，或转成便宜的预付费档。", "已核实"),
    ("回国期间保号 · Lycamobile", "条款写明 SIM 与号码<b>停用 60 天后作废</b>。回国过暑假（通常 2–3 个月）如果不继续充值，"
     "号码会被回收，绑在这个号上的银行、学校、Zelle 等验证短信会全部失效。", "已核实"),
    ("回国长住 · Google Fi", "Fi 有明确的境外使用比例条款：<b>连续 90 天内若大部分用量发生在美国境外，Google 会停掉你的国际数据。</b>"
     "靠 Fi 保号过完整暑假甚至休学一年，属于条款打击范围。", "已核实"),
    ("落地前在国内先激活 eSIM", "<b>这条常见建议至少对两家已确证不成立</b>：Verizon Prepaid 激活时 My Verizon app 会调用定位验证你人在美国境内；"
     "Google Fi 条款明确禁止境外首次激活，且要求先在美国实际使用至少 1 天才能在境外使用。"
     "其余品牌（Visible、Total、US Mobile、T-Mobile、AT&amp;T、Metro、Boost、Lyca）的 eSIM 页面本次<b>均未写明</b>是否允许境外激活，"
     "属未明示，不能默认可以。安全做法是把「落地当天靠机场 Wi-Fi 激活」当基准方案。", "部分已核实"),
    ("无 SSN 能否开卡", "<b>本次核查的所有品牌官网，没有任何一家写过「无需 SSN」或「可用护照/I-20 代替」。</b>"
     "能确证的只是「预付费不查信用」这一件事——而不查信用<b>不等于</b>不要 SSN，更不等于接受护照。"
     "准确的表述是「官网未把 SSN 列为条件」，不能升级成「官方承诺不需要」。"
     "Verizon 后付费的信用审核/押金政策更是完全查不到：专门的 credit-check FAQ 已下线（302 后 404），"
     "押金开卡的说法只见于社区论坛旧帖，不能作为 2026 年现行政策。", "重要限定"),
]

def sec_intl():
    badge = {"已核实": "good", "部分已核实": "good", "部分未找到": "warn", "无法核实": "bad", "重要限定": "bad"}
    rows = "".join(
        f"<div class='finding {badge.get(r[2],'')}'><h4>{esc(r[0])} "
        f"<span class='tag {badge.get(r[2],'')}'>{esc(r[2])}</span></h4><p>{r[1]}</p></div>"
        for r in INTL_ROWS)
    return f"""
<section id="intl"><h2><span class="num">07</span>国际、打回中国、以及回国怎么保号</h2>
<p class="lede">这一块原表完全没覆盖，但它决定了「便宜的卡到底能不能用」。
先说最反直觉的一条：<b>能确证「套餐自带打中国大陆」的只有两家</b>，其余全是加装包、有分钟上限、或者官网根本查不出来。</p>
{rows}
</section>"""

def sec_audit():
    if not AUDIT:
        return ""
    sev = {"高": "bad", "中": "warn", "低": ""}
    items = ""
    for f in AUDIT:
        items += (f"<div class='finding {sev.get(f.get('severity',''),'')}'>"
                  f"<h4>{rich(f['title'])} <span class='tag {sev.get(f.get('severity',''),'')}'>{esc(f.get('verdict',''))}</span>"
                  f"<span class='tag'>严重度 {esc(f.get('severity',''))}</span></h4>"
                  f"<div class='was'><b>原表：</b>{rich(f['was'])}</div>"
                  f"<p><b>实际：</b>{rich(f['now'])}</p>"
                  + (f"<p class='muted'>{rich(f['why'])}</p>" if f.get("why") else "")
                  + "</div>")
    return f"""
<section id="audit"><h2><span class="num">08</span>原表体检：哪些对、哪些错</h2>
<p class="lede">逐条核对你那份 xlsx 的每一个价格与条款。分四类：<b>正确</b>（照抄没问题）、
<b>过时</b>（当时对、现在变了）、<b>错误</b>（当时就不对）、<b>有误导</b>（数字对但口径会让人选错）。</p>
{items}
</section>"""

def sec_rec():
    if not RECS: return ""
    out = ""
    for i, r in enumerate(RECS, 1):
        out += (f"<div class='rec'><div class='rank'>{i}</div><div>"
                f"<h4>{rich(r['title'])}</h4><p>{rich(r['why'])}</p>"
                f"<div class='who'>适合：{rich(r['who'])}</div>"
                + (f"<div class='who' style='margin-top:4px'>注意：{rich(r['caveat'])}</div>" if r.get("caveat") else "")
                + "</div></div>")
    cuts = ""
    if CUTLIST:
        cuts = ("<h3>落选名单：为什么没进主表</h3>"
                + "".join(f"<div class='finding'><h4>{rich(c['name'])}</h4><p>{rich(c['why'])}</p></div>" for c in CUTLIST))
    return f"""
<section id="rec"><h2><span class="num">09</span>推荐排序</h2>
<p class="lede">口径统一为：单线、自带手机、开 AutoPay、换算成含税到手价。促销价不参与排序（因为都会到期）。</p>
{out}{cuts}
</section>"""

def sec_roast():
    if not ROAST: return ""
    out = "".join(
        f"<div class='roast'><h4><span class='kicker'>{esc(r['tag'])}</span>{rich(r['title'])}</h4><p>{rich(r['body'])}</p></div>"
        for r in ROAST)
    return f"""
<section id="roast"><h2><span class="num">10</span>锐评</h2>
<p class="lede">以下是把营销话术剥掉之后的实话。</p>
{out}</section>"""

TOC = [("tax", "01 口径换算"), ("axis-sec", "02 价格轴"), ("brands", "03 品牌逐档"),
       ("multiline", "04 多线拼卡"), ("device", "05 合约送机"), ("coverage", "06 本地覆盖"),
       ("intl", "07 国际·回国"), ("audit", "08 原表体检"), ("rec", "09 推荐排序"),
       ("roast", "10 锐评"), ("limits", "11 限制")]

def build():
    toc = "".join(f'<a href="#{i}">{esc(t)}</a>' for i, t in TOC)
    n_plans, n_brands = len(P), len(BRANDS)
    doc = f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>哥伦布手机套餐对比 · {DATE}</title>
<style>{CSS}</style></head><body>
<nav class="toc">{toc}</nav>
<div class="wrap">
<header class="top">
<h1>哥伦布手机套餐<br>严谨横向对比</h1>
<p class="sub">{n_brands} 个品牌 · {n_plans} 个套餐档位 · 全部价格换算成俄亥俄含税到手价后再比较。
点品牌看全部档位，点档位看同价位所有竞品。</p>
<div class="meta"><span><b>地点</b> Columbus, Ohio</span><span><b>口径日期</b> {DATE}</span>
<span><b>范围</b> 单线 BYOD + 多线 + 合约购机</span><span><b>数据来源</b> 官网实抓</span></div>
</header>

<div class="switchbar">
<span class="lbl">价格口径</span>
<div class="seg"><button data-mode="landed" aria-pressed="true">到手价</button><button data-mode="adv" aria-pressed="false">广告价</button></div>
<span class="lbl">用哪个价</span>
<div class="seg"><button data-promo="0" aria-pressed="true">常规价</button><button data-promo="1" aria-pressed="false">促销价</button></div>
<span class="lbl">同价位区间</span>
<div class="seg"><button data-range="4" aria-pressed="false">±$4</button><button data-range="6" aria-pressed="true">±$6</button><button data-range="10" aria-pressed="false">±$10</button></div>
<span class="fresh f-ok" id="fresh" title="正在计算…"><span class="dotled"></span>口径 {DATE}</span>
</div>

{VERDICT_LINE}
{sec_tax()}{sec_axis()}{sec_brands()}{sec_multiline()}{sec_device()}{sec_coverage()}{sec_intl()}{sec_audit()}{sec_rec()}{sec_roast()}

<section id="limits"><h2><span class="num">11</span>限制与免责</h2>
<div class="warnbox">
<b>价格会变，而且变得比你想象的快。</b> 本页所有数字来自 {DATE} 当天实际抓取的官方页面。
运营商页面会按地址、登录状态、是否携号转入、设备、AutoPay、付款方式和宽带绑定动态变化——
<b>真正下单前必须在结账页再确认一次总价</b>。
</div>
<div class="warnbox">
<b>到手价是估算，不是账单。</b> 换算公式的误差带是 ±3~6 个百分点。最大误差源是联邦 USF：
Tax Foundation 假设运营商全额采用 37.1% 安全港，但运营商可改用自家流量研究，实际账单上的 FUSC 常低于 {TAX['usf_q3_2026']}%。
其次是 USF 系数每季度变（Q2→Q3 2026 就跳了 1.8 个点）、哥伦布实际销售税 {TAX['columbus_sales']}% 与全州加权 {TAX['state_local_tf']}% 的差异、
以及 AutoPay 折扣在税前还是税后计算。保守可用 ×1.19，激进用 ×1.24。
</div>
<div class="warnbox">
<b>覆盖是逐街区的事。</b> 都会区级别的路测和 FCC 面积覆盖<b>不能</b>替代你实际去住处、教室、办公室和通勤路线上测。
室内覆盖可能按建筑差异极大。最稳的做法是先用支持免费试用/eSIM 试用的品牌实测再定。
</div>
<div class="warnbox">
<b>凡是本页写「未找到」的地方，就是真的没查到。</b> 我没有用记忆或常识去填补任何一个数字。
最典型的几处：Total Wireless 的非 AutoPay 牌价、Total 的 200+ 国际目的地是否含中国、
US Mobile 热点超额后的速度、Metro 的 2/3/5 线官方每线价、T-Mobile Experience 系列的具体优先数据阈值。
</div>
<footer>
生成于 {DATE} · 数据来自各运营商官网、FCC National Broadband Map、RootMetrics、Tax Foundation、俄亥俄州税务厅。
每个数字旁的链接都可点开核对原始出处。<br>
本页不含任何论坛传闻——Reddit 在抓取环境中不可访问，因此宁可留空也没有凭记忆补写。
</footer>
</section>
</div>
<script>const DATA = {json.dumps(DATA_JS, ensure_ascii=False)};</script>
<script>{JS}</script>
</body></html>"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print("written:", OUT, len(doc), "bytes")
    print("plans:", n_plans, "brands:", n_brands)
    # 排序预览
    rows = sorted([(landed(p), p["brand"], p["name"]) for p in P if landed(p) is not None])
    for v, b, n in rows[:14]:
        print(f"  {money(v):>8}  {b:<15} {n}")

if __name__ == "__main__":
    build()
