# -*- coding: utf-8 -*-
"""哥伦布手机套餐对比 —— 非套餐类数据模块
全部来自 2026-08-14 联网实抓，出处见每条 src 字段。
"""

# ── 税费换算模型（俄亥俄州 / 哥伦布 Franklin County） ──────────────────
TAX = {
    "state_local_tf": 9.20,        # Tax Foundation 2025版 全州加权
    "columbus_sales": 8.0,         # 州5.75 + Franklin郡1.25 + COTA公交1.0
    "usf_q3_2026": 14.39,          # 38.8% × 37.1% 安全港
    "usf_tf_stale": 13.36,         # TF 用的 Q3 2025 系数（已过时）
    "combined": 23.59,             # 9.20 + 14.39
    "combined_tf": 22.56,          # TF 原值（低估约1个点）
    "ng911": 0.25,                 # 每线每月固定，俄亥俄州税务厅
    "note": "倍率随档位递减，因为固定费不随价格缩放：本页实算（取 AT&T 上界）$20档 ×1.50 / $25档 ×1.45 / "
            "$30档 ×1.41 / $35档 ×1.39 / $45档 ×1.35 / $50档 ×1.34 / $70档 ×1.31 / $90档 ×1.29。"
            "所以不存在单一的「×1.3」——套餐越便宜，税费咬得越狠。"
            "固定费必须单加，不能并入百分比。误差带 ±3~6 个百分点，最大误差源是联邦 USF 安全港口径。",
    "src": [
        ("Tax Foundation 2025 版无线税率表（俄亥俄行 9.20/13.36/22.56）",
         "https://taxfoundation.org/data/all/state/wireless-taxes-cell-phone-tax-rates-by-state-2025/"),
        ("FCC Q3 2026 USF 缴费系数升至历史最高 38.8%",
         "https://broadbandbreakfast.com/usf-contribution-factor-hits-record-38-8-in-third-quarter/"),
        ("俄亥俄州税务厅 NG911 费官方 PDF（2025-10-01 起 $0.25/线/月）",
         "https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/sales_and_use/information_releases/NG2023_Replacement_of_the_Wireless_9-1-1_Fee.pdf"),
        ("哥伦布本地销售税 8.0%（州5.75+郡1.25+COTA1.0）",
         "https://www.salestaxhandbook.com/ohio/rates/columbus"),
    ],
}

# 每线固定运营商自收费（不是税，是运营商自收，比价时必须硬加）
LINE_FEES = {
    "Verizon":  {"fee": 3.99, "detail": "Administrative & Telco Recovery $3.78 + Regulatory $0.21。两年累计涨约80%，官网刻意不公布金额。",
                 "src": "https://www.verizon.com/support/surcharges/"},
    "AT&T":     {"fee": 4.99, "detail": "Administrative & Regulatory Cost Recovery，2026-08-05 刚由 $3.99 涨到 $4.99，三大最高。八个月涨43%。",
                 "src": "https://www.androidauthority.com/att-new-fee-hike-3680584/"},
    "T-Mobile": {"fee": 4.49, "detail": "Regulatory Programs $0.50 + Telco Recovery $3.99，2026-01-21 上调。第三方广传的 $3.99 是旧数。",
                 "src": "https://www.t-mobile.com/responsibility/consumer-info/additional-info/regulatory-programs-fee"},
}

ACTIVATION = [
    ("Verizon", "$0（但必须自己去 App 加入 Verizon Loyalty，不自动生效）",
     "2026-06-16 起永久取消 $40 激活费/升级费，是2026年三大里唯一真取消的。不加入则仍收 $40/线。",
     "https://www.verizon.com/about/news/verizon-puts-customers-first", "高"),
    ("AT&T", "$25–$35/线（口径冲突，未锁定）",
     "后付费一说 $35 一说 $25，官网 403 无法直抓。预付费 $15，线上常免。学生/工会/AARP 可减免——签约前当场问清。",
     "https://blog.dealszo.com/verizon-att-tmobile-activation-fee-comparison/", "低"),
    ("T-Mobile", "$35/线 Device Connection Charge",
     "后付费激活与升级均收，预付费豁免；2026-03 起通过 Apple 渠道购机也照收。",
     "https://www.t-mobile.com/responsibility/consumer-info/additional-info/regulatory-programs-fee", "中高"),
    ("Cricket", "到店开通费最高 $25/线（线上办理常免）", "一次性。", "https://www.cricketwireless.com/", "中"),
    ("Metro", "$0（当前促销免开卡费）", "促销性质，可能变。", "https://www.metrobyt-mobile.com/phone-plans", "中"),
]

# ── 哥伦布本地覆盖（RootMetrics 1H2026 路测 + FCC 官方地图） ──────────
COVERAGE = {
    "headline": "2026 上半年哥伦布路测：AT&T 与 T-Mobile 并列第一，Verizon 第三且八个单项奖一项未得。",
    "rootmetrics": {
        "period": "2026/3/25–4/4 驱车路测，覆盖人口 1,567,254",
        "src": "https://rootmetrics.com/en-US/rootscore/map/metro/columbus-oh/2026/1H",
        "rows": [
            # 品牌, RootScore, 中位下载, 中位上传, 单项奖
            ("AT&T", 99.7, "369.0 Mbps", "33.7 Mbps",
             "Overall / Reliability / Speed(独得) / Data / Call(掉话0) / Text / Video —— 七项在手"),
            ("T-Mobile", 99.6, "480.9 Mbps（最快）", "19.1 Mbps",
             "Overall / Reliability / Data / Call / Text / Video / Responsiveness(独得)"),
            ("Verizon", 99.1, "334.1 Mbps（较上轮 379.7 下滑）", "未列",
             "本轮 0 项获奖"),
        ],
    },
    "fcc": {
        "note": "FCC National Broadband Map，数据截止 2025-12-31，2026-08-04 发布。口径为「任一移动技术、面积覆盖」。",
        "src": "https://broadbandmap.fcc.gov/",
        "metro": [  # 品牌, 室外静止, 行车中
            ("Verizon", "98.77%", "78.27%"),
            ("AT&T", "97.29%", "85.38%"),
            ("T-Mobile", "86.35%", "52.50%"),
        ],
        "city": "Columbus 市界内 5G(7/1) 面积覆盖 100%、5G(35/3) 99.89%；都会区 86.51% 面积可达 35/3 级 5G（全美仅 39.45%）。",
    },
    "weakspots": [
        ("OSU 校园", "曾经确实弱。校报 The Lantern 2024/9 报道，因在校人数增长与新建筑 shadowing，Verizon 以 neutral host 方式扩建 DAS：2022年8个 + 2024年9个共17个小基站，覆盖 Ohio Stadium、Bowen/Raney/Scott 宿舍、Ohio Union、Schottenstein Center。2024–25 学年起已大幅补强。", "官方报道"),
        ("北郊（T-Mobile 弱）", "FCC「行车中」口径：Worthington 68.42%、Upper Arlington 76.42%、Dublin 79.90%、Delaware County（Polaris 北侧）61.90%；同区 AT&T/Verizon 普遍 96–100%。", "FCC 官方"),
        ("Grandview Heights", "三家均 100%，无差异。", "FCC 官方"),
        ("High St / Short North / Clintonville / Easton", "未找到任何有出处的弱覆盖记录——不代表没有，只代表本次查不到可引用证据。", "未找到"),
    ],
    "mmwave": "把 mmWave 当哥伦布选网理由不成立。Verizon 2019 年底就把 Columbus 列入 5G UW 城市，但今天的 UW 是 mmWave+C-band 混称且不公布街区清单；"
              "AT&T 官网（©2026）明写高频 5G+ 只铺「高流量场所、大型场馆和机场」，全页无 Columbus/Ohio 字样；T-Mobile 本地 Ultra Capacity 等于 2.5GHz 中频。"
              "你日常看到的高速全部来自中频。",
    "notfound": "Ookla 的 Columbus 城市级排名——未找到（ookla.com/speedtest.net 在本环境被封）。"
                "Opensignal 只有全国/大区视角（全国 T-Mobile 12/16 奖，Reliability 942 vs AT&T 939 vs Verizon 932）。"
                "Reddit r/Columbus 口碑——未找到（三条访问路径全被封），因此本页不含任何论坛传闻。"
                "众包站 CoverageMap 给出与专业路测相反的结果（AT&T 251 > T-Mobile 206 > Verizon 143），但样本量 29000:4700:3300 严重失衡且未标数据期，只能当旁证。",
}

# ── 多线拼卡（每线/月，BYOD，不含设备） ──────────────────────────────
# fmt: 品牌 -> {plan: [1线,2线,3线,4线,5线]}  值为「每线价」，None=官网未公布
MULTILINE = {
    "Verizon": {
        "tax": "另计", "autopay": "已含 AutoPay+无纸账单（不开每线+$10）",
        "mix": "各线可选不同档，不要求同档",
        "plans": {
            "Unlimited Welcome": [65, 55, 36.67, 27.50, 28],
            "Unlimited Plus": [80, 70, 51.67, 42.50, 43],
            "Unlimited Ultimate": [95, 85, 66.67, 57.50, 58],
        },
        "trap": "3+线的 $10/月 credit 是【账户级一份、不是每线】，36个月后到期。到期后 Welcome 4线从 $27.50/线 涨回 $30/线。"
                "另外广告价「4线 $25/线」的 tooltip 写明需 4 条全新线（转网/新开），老账户加线拿不到。",
        "src": "https://www.verizon.com/plans/unlimited/myplan/",
    },
    "AT&T": {
        "tax": "另计", "autopay": "已含 $10/线 AutoPay+无纸账单",
        "mix": "唯一允许各线混搭不同档（Mix and match any of our best unlimited plans on any line）",
        "plans": {
            "Value 2.0": [50, 45, 35, 30, 30],
            "Extra 2.0": [70, 60, 50, 40, 40],
            "Premium 2.0": [90, 80, 65, 50, 50],
            "Elite 2.0": [110, 100, 85, 70, 70],
        },
        "trap": "$10/线的 AutoPay 折扣只有绑【银行账户或 AT&T Points Plus 信用卡】才给足额；普通借记卡只有 $5，多数信用卡是 $0。"
                "只刷普通信用卡的人 4线每年多付 $480。而且折扣「starts within 2 bills」——前两期先按原价收。",
        "src": "https://www.att.com/plans/wireless/",
    },
    "T-Mobile": {
        "tax": "另计（2025-04 起 Experience 系列改为税费另计，历史「全包」卖点已终结）",
        "autopay": "已含 AutoPay+无纸账单", "mix": "允许混搭",
        "plans": {
            "Essentials / Saver 2.0": [55, 45, None, 30, 30],
            "Experience More 2.0": [90, 75, 61.67, 55, 51],
            "Experience Beyond 2.0": [105, 90, 76.67, 70, 66],
        },
        "trap": "「第3线免费」是 bill credit，官方原文：credits stop if you cancel any lines——砍任何一条线，credit 全停。"
                "另外每条语音线还有 $4.49/月恢复费。Essentials 的 4线 $30/线 是限时档，官网未列 3 线价。",
        "src": "https://www.t-mobile.com/cell-phone-plans",
    },
    "Google Fi": {
        "tax": "另计", "autopay": "无需 AutoPay", "mix": "允许混搭",
        "plans": {
            "Unlimited Essentials": [35, 30, 27, 23, 23],
            "Unlimited Standard": [50, 40, 30, 25, 25],
            "Unlimited Premium": [65, 55, 45, 40, 40],
        },
        "trap": "阶梯是【真降价、不是 bill credit】，减线不会触发 credit 停发——这点比 T-Mobile 干净。"
                "但 Premium 从4线起锁死 $40/线不再降，Standard 从4线起锁 $25/线，所以人多时 Standard 性价比碾压 Premium。",
        "src": "https://fi.google.com/about/plans/",
    },
    "Cricket": {
        "tax": "已包含", "autopay": "已含 $5/月账户级 credit（不开则整单+$5）",
        "mix": "要求全部线路同档（all lines must be on the same plan）",
        "plans": {
            "Sensible 10GB": [30, 30, 30, 30, 30],
            "Select Unlimited": [35, 32.50, 30, 25, 24],
            "Smart Unlimited": [45, 37.50, 31.67, 27.50, 26],
            "Supreme Unlimited": [55, 45, 36.67, 32.50, 32],
        },
        "trap": "Sensible 10GB 挂着「多线」的名义，实际 $30×线数、零折扣，别被套餐列表并排展示误导。"
                "真正的加线优惠只在三档 Unlimited：Select 逐线增量 +$30/+$25/+$10/+$20。",
        "src": "https://www.cricketwireless.com/support/plans-and-features/family-plans.html",
    },
    "Boost": {
        "tax": "另计", "autopay": "已含（不开每线+$5）",
        "mix": "所有线必须在 Unlimited+ / Premium 两档之内",
        "plans": {
            "Unlimited ($25 档)": [25, 25, 25, 25, 25],
            "Unlimited+": [50, 40, 36.67, 30, 30],
            "Unlimited Premium": [60, 50, 46.67, 40, 40],
        },
        "trap": "天天打广告的「$25/mo Forever」入门档【完全不参加多线折扣】，5条线就是 $125。"
                "折扣结构本身很实在（第4线一次减 $40，是全表最激进的单线减免），但首单最多3线，想开4线拿 $30/线必须先激活3条再补第4条。",
        "src": "https://www.boostmobile.com/plans/multiline",
    },
    "Visible": {
        "tax": "已包含（Broadband Facts: Government Taxes Included / Provider Monthly Fees None）",
        "autopay": "无需", "mix": "每人独立账户各付各的",
        "plans": {
            "Visible ($25 基础)": [25, 25, 25, 25, 25],
            "Visible+ (Inner Circle)": [35, 30, 30, 30, 30],
            "Visible+ Pro (Inner Circle)": [45, 40, 40, 40, 40],
        },
        "trap": "没有传统家庭套餐。基础版是纯线性、一分不省；Inner Circle 每人固定省 $5，最多7人，且【基础版不参加】。"
                "年付更便宜：Visible $275/年(≈$22.92) / Visible+ $375/年(≈$31.25) / Pro $450/年(≈$37.50)。",
        "src": "https://www.visible.com/plans/inner-circle",
    },
    "Total Wireless": {
        "tax": "页面未明示", "autopay": "已含 $5 账户级折扣（第一个月拿不到）",
        "mix": "要求全账户同档（All phone lines will be on the same new plan）",
        "plans": {
            "Total STARTER": [35, 37.50, 28.33, 23.75, 25],
            "Total MAX 5G BYO": [25, 27.50, 28.33, 26.25, 27],
            "Total MAX 5G": [50, 40, 31.67, 26.25, 27],
            "Total ALL ACCESS": [60, 45, 35, 28.75, 29],
        },
        "trap": "阶梯【不单调】，这是全表最反常的一家：STARTER 2线每线 $37.50 比单线 $35 还贵；"
                "MAX 5G BYO 从3线起每线价不再下降（3线$28.33→4线$26.25→5线$27）。"
                "真要拼卡，这家最优解是 STARTER 4线 $23.75/线，不是看着最便宜的 MAX 5G BYO。",
        "src": "https://www.totalwireless.com/shop/plans",
    },
    "Mint Mobile": {
        "tax": "另计（Recovery Fee $1.88–$2.29/月 + FUSF + 州税）",
        "autopay": "无需，但要一次性预付整期", "mix": "可混搭不同档",
        "plans": {"Unlimited": [30, 30, 30, 30, 30], "6GB": [15, 15, 15, 15, 15],
                  "17GB": [20, 20, 20, 20, 20], "23GB": [25, 25, 25, 25, 25]},
        "trap": "官方 FAQ 白纸黑字自认没有多线折扣：「although there aren't any discounts」。"
                "所谓 Modern Family Plan 只是把2-5条独立线放进一个管理界面，价格一分不变——别被「family plan」四个字骗到。"
                "另外 3个月短约的常规价比 12个月档贵 $10–$20/月。",
        "src": "https://www.mintmobile.com/family-phone-plans/",
    },
    "US Mobile": {
        "tax": "部分档已包含（非全包档 recovery fee 约 $1–$5/线）",
        "autopay": "无需", "mix": "可混搭",
        "plans": {"Unlimited Starter(年付)": [16.60] * 5, "Unlimited Flex(年付)": [17.50] * 5,
                  "Unlimited Premium(年付)": [24.90] * 5},
        "trap": "官方原话：「we do not have multi-line discounts (we just lowered our prices so that even a single line "
                "costs what one used to get after a multi-line discount)」。定位就是「单线也给你多线价」，人多不会再便宜。"
                "唯一多线好处：3条以上 Premium 月付线送1个 perk（最高 $15/月）。注意列价是【年付首年价】，续年价官网未说明。",
        "src": "https://www.usmobile.com/plans",
    },
    "Metro": {
        "tax": "已包含 + 5年锁价（talk/text/5G数据，有除外条款）",
        "autopay": "已含", "mix": "未公布",
        "plans": {"$25 BYOD 档": [25, 25, 25, 25, 25], "$30 档": [30, 30, 30, 30, 30],
                  "$60 Premium": [60, None, None, 48, None]},
        "trap": "Metro【没有一张公开的多线阶梯表】——查过7个官方页面（/phone-plans、/plan-benefits、/deals、/deals/40period、"
                "/deals/one-line-for-25-phone-plan、/deals/4-lines-for-100、/onlineplans）均未刊登 2/3/5 线价。"
                "它的「4线$100」就是单线价 $25 原样复制4份，且写明【只能到店办】。也就是说 Metro 的多线优惠在数字上并不比单线促销价更便宜。",
        "src": "https://www.metrobyt-mobile.com/phone-plans",
    },
    "Spectrum Mobile": {
        "tax": "服务税费已含，激活费与设备税另计", "autopay": "强制", "mix": "可混搭",
        "plans": {"Unlimited": [30, 30, 30, 30, 30], "Unlimited Plus": [40, 40, 40, 40, 40],
                  "Unlimited Plus Premium": [50, 50, 50, 50, 50]},
        "trap": "手机侧【零多线折扣】，每线固定价。省钱完全来自「必须先买 Spectrum 宽带、第1条无限线免费1年」的捆绑补贴。"
                "把宽带算进去：4线36个月手机 $3,960 + 宽带约 $2,160 = 约 $6,120。为了这个价去买宽带就不划算了。",
        "src": "https://www.spectrum.com/mobile/plans",
    },
}

# ── 合约送手机 / 以旧换新 真实净账 ──────────────────────────────────
DEVICE = {
    "Verizon": {
        "bombshell": "2026年8月的 Verizon 主力「免费手机」促销【不需要以旧换新】。机型页 Available offers 面板里根本没有 trade-in 选项，"
                     "筛选器的 Offers 分类只有 Bill credit / Free / Online only 三种。以旧换新项目还在，但只是按二手市值折价，不是免费机的前提。"
                     "WhistleOut 等第三方（2026-08-13 更新）仍在写「需以旧换新」「需 port-in」，与官网当前落地页不符。",
        "hard_conditions": ["必须开【新线路】（New line req'd. 写在每条优惠标题里）",
                            "必须上指定档位：$830以下机器要 Plus 或 Ultimate；$830以上旗舰【一律只认最贵的 Ultimate】",
                            "抵扣分 36 个月按月返，不是立减",
                            "Simplicity 套餐拿不到这些大额抵扣"],
        "step": "每升一档固定 +$15/月/线 = $540/36个月；Welcome 直跳 Ultimate = +$30/月 = $1,080/36个月",
        "cases": [
            # 机型, 零售价, 抵扣, 要求档位, 从Welcome出发净账, 判断
            ("iPhone 17 (256GB)", 829.99, 830, "Plus 或 Ultimate", "+$540 → 净省 $290", "值"),
            ("Galaxy S26+", None, None, "Plus", "净省 $560", "值"),
            ("iPhone Air", 999.99, 1000, "只认 Ultimate", "+$1,080 → 倒亏 $80", "坑"),
            ("iPhone 17 Pro", 1099.99, 1000, "只认 Ultimate", "+$1,080 → 倒亏 $80", "坑"),
            ("iPhone 17 Pro Max", 1199.99, 1000, "只认 Ultimate", "+$1,080 → 倒亏 $80", "坑"),
            ("Galaxy S26 Ultra", 1299.99, 1119.99, "只认 Ultimate", "只省 $39.99，基本白折腾", "坑"),
            ("Pixel 11 Pro", 1099.99, 739.99, "只认 Ultimate", "+$1,080 → 倒亏 $340（最坑）", "坑"),
        ],
        "exit": "无 ETF（Broadband Facts: Early Termination Fee: None），但降档/取消/提前付清/提前升级 → 抵扣立即全停。"
                "例：iPhone 17 Pro Max 第18个月走人 → 只拿到约 $500 抵扣，剩余设备欠款 $600 一次性付清，另 $500 抵扣作废。等于被锁36个月。",
        "hidden": "「New line req'd.」意味着如果为拿机去开一条你根本用不到的线，那条线36个月的费用（Plus第4线 $45×36=$1,620）远超任何一台手机的价值。",
        "src": "https://www.verizon.com/smartphones/",
    },
    "AT&T": {
        "bombshell": "Build-A-Plan【完全不能参与任何设备促销】。三重官方证据：法律条款要求自带解锁 eSIM 设备且每账户限1台；"
                     "官方文档 att.com/ai-instructions/build-a-plan.html（v1.2.2, 2026-06-23）逐条写明「NO promotional offers, NO switcher credits, "
                     "and NO bill credits」「Device installment plans = No」「Trade-in offers = No」；每份设备促销条款都要求 eligible postpaid "
                     "unlimited 套餐并点名 Value/Extra/Premium/Elite 2.0。想要补贴手机只能走传统 Unlimited 2.0。",
        "counterintuitive": [
            "iPhone 17 Pro Max「最高 $1,100 off」是最大的坑：抵扣要 Extra 2.0（单线$80/月），改用 Value 2.0 只给 $500，"
            "但36个月话费省 $720 > 抵扣少拿 $600 → 【Value 2.0 净成本反而低 $120.09】（$2,624.99 vs $2,745.08），旧机门槛还从 TiV≥$290 降到 ≥$130。",
            "Galaxy Z Fold8「$0」不是免费：机器净价确实 $0，但强制加买 Next Up Anytime（$10/月×36=$360，条款写明不冲抵机器余额且不退）"
            "+ 预付税约 $142.50 + 激活 $35 + 交出 TiV≥$290 旧机 ≈ 实付 $828，并锁在 Premium 2.0 $100/月上36个月。",
            "Pixel 11 Pro XL $1,350 off 是本次最优：Extra 2.0 路线比 Value 2.0 便宜 $129.99，真实机器成本约 $336 换 $1,349.99 的机器，"
            "且有「任何年份任何成色 Pixel」的低门槛档。",
        ],
        "vs_bap": "同一台 iPhone 17 Pro Max 256GB，36个月：Build-A-Plan 无限SD（$35/月）+ 自购裸机 = $2,549.99 且旧机留在手上；"
                  "AT&T Extra 2.0 + $1,100抵扣 = $2,745.08 且要交出 TiV≥$290 旧机 → 【前者省 $195.09，算上保住的旧机实际优势约 $485】。"
                  "代价是 SD 串流（5G 上限 2Mbps）、无热点、仅1条线、仅线上办理。",
        "exit": "离网→抵扣立停且分期余额立即到期；降档→抵扣停发或缩水，收到通知后30天内换回才能救；开新线后90天内取消同账号任何其他线→抵扣停发。"
                "实算：iPhone 17 Pro Max 第12个月离网，剩余余额 $799.91 立即到期，这台机器共实付 $833.27 外加已交出的旧机，而原价买只要 $1,199.99。",
        "hidden": "所有净账里的 $10/月自动扣款折扣需绑【银行账户】；绑借记卡只有 $5，绑其他信用卡为 $0——只用信用卡的人36个月多付 $360，"
                  "吃掉「$1,100抵扣」的三分之一。另外 BYOD 的 $5/月抵扣与「在 AT&T 分期买机」结构性互斥：想要补贴手机就拿不到最低月费。",
        "src": "https://www.att.com/deals/",
    },
    "T-Mobile": {
        "bombshell": "补贴已从传统24个月拉长到36个月按月返还，等于把你锁进套餐3年。判断只有一条算式：【盈亏平衡月差价 = 补贴总额 ÷ 36】。"
                     "$1,100 补贴对应 $30.56/月，$1,300 对应 $36.11/月——为拿补贴多付的套餐月差价一旦超过这个数，就是净亏。",
        "cases": [
            ("Essentials $70 → Experience More $90", "多付 $20×36=$720，换 $1,100 机器", "净赚 $380（唯一真划算的一档）", "值"),
            ("Essentials $70 → Experience Beyond $105", "多付 $35×36=$1,260", "净亏 $160", "坑"),
            ("Essentials Saver $55 → Experience Beyond $105", "多付 $50×36=$1,800", "净亏 $700（最亏）", "坑"),
            ("Experience More $90 → Beyond $105（为 Pixel 11 Pro XL 的 $1,300）", "多付 $15×36=$540，只多拿 $200 补贴", "净亏 $340", "坑"),
        ],
        "saver": "Essentials Saver 几乎只能拿到 BYOD 优惠：官网 /offers 上唯一明确挂它的设备类优惠是「自带手机返 $720」（需携号转网，$20/月×36）。"
                 "旗舰 On Us 全部要求 Experience More/Beyond。官网套餐页自己承认这条分层：「Popular plans unlock better device offers than discounted plans.」",
        "exit": "① 取消服务时 all remaining EIP balances become due immediately，且不能用没返完的补贴抵剩余分期；"
                "② 2024-07-01 后参加的活动，【提前一次性付清分期也会作废剩余补贴】；③ 降档套餐等于自己掐断返还。"
                "例：iPhone 17 Pro 满12个月离网，已返约 $366，剩余分期约 $733 立刻全额到期，补贴归零。",
        "conflict": "官网两处口径打架，务必在下单页复核：① 以旧换新是否必需——/offers 写 iPhone 17 Pro「无需以旧换新、需转网」，"
                    "机型页却写「new line, port, and any condition trade-in」三者都要。② 「零首付」——/offers 写「No taxes. No fees. No money down.」，"
                    "但通用条款写「plus tax & $35 device connection charge」，iPhone 17 更明写「Tax on pre-credit price due at sale」（按未抵扣前全价当场交税）。"
                    "③ 返还月数：官方多处写36个月，Galaxy Z Flip8 细则写「24 or 36 monthly bill credits, depending on finance agreement term」——"
                    "这直接决定盈亏平衡线是 $45.83/月还是 $30.56/月，签约前必须确认。",
        "src": "https://www.t-mobile.com/offers",
    },
    "MVNO": {
        "bombshell": "两条与常见认知不符的更正：① 【Boost 已经没有自建网络了】。EchoStar 2025-08-26 把 3.45GHz+600MHz 共 50MHz 全国频谱"
                     "以约230亿美元卖给 AT&T，Boost 自有 5G RAN 关停，全部无线用户 2025-11-15 迁到 AT&T 网络，只保留自己的云原生5G核心网，"
                     "T-Mobile 作为次级/漫游层，AT&T 网络服务义务至少到 2031 年。今天的 Boost 实质是【跑 AT&T 的混合 MVNO】。"
                     "② 【Boost 并没有做激进旗舰补贴】——实抓其苹果列表页：iPhone 17 $829.99 / 17 Pro $1,099.99 / 17 Pro Max $1,199.99 / Air $999.99，"
                     "全部原价零折扣。猛药全在中低端（16e $149.99、17e $249.99、Pixel 10a $49.99、A27 5G $0）。",
        "who_cuts_flagship": "真正在砍旗舰的是 Cricket（S26 省$500、S26 Ultra 省$600）、US Mobile（Pixel 11 系列省 $360–530，解锁机、立减不返还）、Mint（S26 立减$500）。",
        "structure": "【最该看的一点】Boost / Cricket / Total Wireless / Metro 用的是「购机立减 + 预付2–3个月话费」，钱一次性省掉，"
                     "没有24/36个月账单返还，提前走人不倒扣——这是本组最干净的结构。"
                     "Spectrum Mobile 则相反：所谓「免费旗舰」是36个月账单返还 + 必须以旧换新 + 必须一直有 Spectrum 宽带，"
                     "官网原文「Disconnecting service or upgrading early forfeits remaining credits」，是本组最深的坑。",
        "mint_exaggeration": "Mint 的「GET SAMSUNG GALAXY S26 ON US」标题夸大：实际只立减 $500（S26 $900→$400），"
                             "要真到 $0 得再拿 iPhone 16 以上 / Galaxy S25 以上 / Pixel 10 以上去换，那些机器市价远高于 $400，"
                             "而且退款是 Allstate 开支票、不是当场抵扣。",
        "visible_notfound": "【一条重要的「查无此物」】Visible 官网 /deals 页今天（浏览器实载）完全没有任何手机促销，只有资费促销"
                            "（SAVEHALF、SAVE6、Apple Watch、Inner Circle、Back Market 翻新机）。抓取工具先拿到的那份 Visible"
                            "「Pixel 10 五折 / Galaxy S26 送 $480 / iPhone 17e 送 $600」是缓存旧页，截止日写着 2026年4月，全部早已过期，不能采信。",
        "port_req": "必须携号转入：Cricket 的 A17 5G / A37 5G / edge 2026 / iPhone 16e；Metro 的 16e / A37 / A17 / NXTPAPER / 17e；Boost 全部线下专享。"
                    "不需转网、开新线即可：Cricket 的 moto g power 2026 / moto g 2026 / A16 5G / moto g play / Icon 系列；Metro 的 moto g–2026；"
                    "Boost 线上单；US Mobile 与 Mint 全线。",
        "min_hold": "最短保号期：Boost 预付2个月｜Cricket 16e 需买满3个月 $60 套餐｜Metro 需连续3个月出账才能拿 $100 返卡｜"
                    "Mint 12个月预付｜Spectrum 36个月返还期｜Visible 年付锁12个月。",
        "best3": ["纯自带机最省：Total Wireless MAX 5G BYO 首月 $30 之后 $20/月，36个月 $730，官网明示税费已含 + 5年价格保证。",
                  "要一台免费安卓机：Metro Galaxy A37 5G $0 + $40/月，36个月共 $1,440，免开卡费。",
                  "要旗舰且不想被锁：US Mobile Pixel 11 立减到 $539，解锁机、无账单返还、无倒扣，配 Unlimited Premium 年付 $299。"],
        "page_bugs": "Cricket 促销位挂着「this deal ends 8/4」，但同段倒计时代码显示「355 days」（即 2027-08-04），是 Cricket 自己的页面 bug，"
                     "建议下单前截图留证。Total Wireless 首页大字「iPhone 16e ON US」与同页商品卡「$199.99 w/ Total ALL ACCESS 3-mo plan」互相打架，"
                     "「ON US」实际挂钩 Glow Financial Services 的 0% APR 分期，不是白送。",
        "src": "https://www.boostmobile.com/",
    },
}
