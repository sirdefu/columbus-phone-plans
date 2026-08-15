# -*- coding: utf-8 -*-
"""套餐数据集 —— 全部来自 2026-08-14 官网实抓。
fee = 每线每月运营商自收费（不是税）。tax_inc=True 表示广告价即到手价。
adv = 用户实际能拿到的常规月价（开 AutoPay 的按 AutoPay 价，因为绝大多数人会开）；
      raw = 不开 AutoPay 的牌价，单独展示。
promo = 限时/条件促销价，主排序不参与。
"""

BRANDS = [
    dict(name="Visible", short="VIS", net="Verizon", fee=0.0,
         blurb="Verizon 全资的纯线上品牌。全线税费已含、无 AutoPay 差价、无合约，牌价即到手价——在这张表里这点含金量极高。"
               "客服只有线上，没有实体店。",
         gotchas=["基础版 Visible 走的是【会被降优先级】的那条队列，Visible+ 才有优先数据",
                  "基础版不含 5G Ultra Wideband，Broadband Facts 里下行只有 34–149 Mbps",
                  "热点是「无限但锁速」：基础 5 Mbps / Visible+ 10 Mbps / Pro 15 Mbps，且限 1 台设备",
                  "年付不参加 SAVE6 / SUMMER 促销码，且激活后不退款"]),
    dict(name="Total Wireless", short="TOT", net="Verizon", fee=0.0,
         blurb="Verizon 旗下预付费价值品牌。官网只印 AutoPay 价，税费已含，并对新客提供 5 年锁价。"
               "$25 的 MAX 5G BYO 是全表最强的「Verizon 网络 + 含税」组合。",
         gotchas=["官网【不公布非 AutoPay 牌价】，所以「常规价」这一栏严格来说无法核实——原表把 $25 当无条件常规价是不准确的",
                  "5 年锁价只锁「当时的含税月费」，不含促销、附加包和 AutoPay 折扣本身",
                  "多线阶梯反常：STARTER 2 线每线 $37.50 比单线 $35 还贵；MAX 5G BYO 从 3 线起每线价不再下降",
                  "国际：官网 200+ 目的地清单为动态加载、未渲染，【中国是否在内无法确认】"]),
    dict(name="Verizon", short="VZW", net="Verizon", fee=3.99,
         blurb="直营后付费。当前主力只剩 Simplicity 一档无限套餐（$55 牌价 / $45 AutoPay / $30 转网），"
               "另有一条常被忽略的预付费产品线。税费一律另计。",
         gotchas=["Simplicity 的 $30 是【转网/携号专属】，需上传 45 天内的他家账单，不是长期常规价",
                  "AutoPay 折扣要求符合条件的付款方式 + 无纸账单",
                  "单线毫无价格优势（$45 AutoPay 换算到手约 $60），Verizon 的价值在 4–5 线",
                  "预付费 15GB 档的忠诚度折扣官网两处口径打架：一处写「9 个月后 $30」，另一处写「续费 3 次 −$5、续费 9 次再 −$5」"]),
    dict(name="Cricket", short="CKT", net="AT&T", fee=0.0,
         blurb="AT&T 全资预付费品牌。Broadband Facts 逐套餐标注 Government Taxes Included，"
               "是本表里税费口径最干净的 AT&T 入口，且在哥伦布有实体店。",
         gotchas=["年付 12-Month Unlimited $300（$25/月）【完全禁止热点】，官方原文 tethering is prohibited，且不可加购",
                  "低价无限档不含热点，要热点得上 $55 的 Supreme",
                  "$5 AutoPay credit 从【第 2 个月】才生效，首月按牌价收",
                  "促销位挂着「deal ends 8/4」但同段倒计时代码显示 355 天（2027-08-04），是官网自己的 bug，下单前建议截图"]),
    dict(name="AT&T", short="ATT", net="AT&T", fee=4.99,
         blurb="直营。后付费 Unlimited Your Way 2.0 四档 + 一条被严重低估的预付费线。"
               "在哥伦布 RootMetrics 1H2026 路测里 AT&T 综合并列第一、独得速度奖。",
         gotchas=["全线税费另计，且管理费 2026-08-05 刚从 $3.99 涨到 $4.99/线，是三大最高（八个月涨 43%）",
                  "AutoPay 的 $10/线折扣必须绑【银行账户或 AT&T Points Plus 信用卡】；普通借记卡只有 $5，多数信用卡是 $0",
                  "折扣「starts within 2 bills」——前两期账单先按原价收",
                  "预付费 $25 与 $35 档的高速数据【本身就被硬封在 3 Mbps】，不是拥堵才慢，是永远 3 Mbps",
                  "Build-A-Plan 是独立产品线，不在 att.com/plans/wireless/ 上；它 NO promotional offers / NO bill credits / "
                  "不能分期买机 / 不能以旧换新 / 每账户限 1 条线 / 仅线上办理"]),
    dict(name="T-Mobile", short="TMO", net="T-Mobile", fee=4.49,
         blurb="直营。哥伦布本地下载速度最快（RootMetrics 中位 480.9 Mbps）。"
               "最大的价值点是【学生价】：Essentials Saver 学生档 $30 AutoPay，比普通版便宜 $20/月。",
         gotchas=["2025-04 起 Experience 系列改为【税费另计】，历史上的「全包」卖点已终结",
                  "每条语音线额外 $4.49/月 Regulatory & Telco Recovery Fee（第三方广传的 $3.99 是 2026-01-21 涨价前的旧数）",
                  "AutoPay 折扣要求【银行账户或借记卡】，信用卡不算",
                  "Essentials 系列在拥堵时【常态低于】Experience 用户，超 50GB 再降一档",
                  "Essentials 全线热点是「无限但全程 3G」，Open Internet 政策给出的数字是最高 600 kbps",
                  "学生价需 45 天内完成学籍验证并按要求复验，掉验证最多加价 $20/线/月"]),
    dict(name="US Mobile", short="USM", net="三网可选", fee=0.0,
         blurb="唯一能在三张全国网之间选择甚至切换的品牌（代号 Warp / Dark Star / Light Speed——"
               "官网从不点名对应哪家运营商，映射为第三方推断）。税费已含，"
               "且官方直言「我们没有多线折扣，因为单线价已经是别人多线折扣后的水平」。",
         gotchas=["【三网归属是第三方推断，不是官方表述】usmobile.com 的 /networks 与 /plans 页【从不出现 Verizon、AT&T、T-Mobile 任何一个名字】，"
                  "只给代号与能力描述。Warp=Verizon / Dark Star=AT&T / Light Speed=T-Mobile 的映射来自 WhistleOut、BestMVNO 等第三方",
                  "【优先级口径三网不同】官方只对 Warp 用了 Priority Data 一词；Dark Star 的优先级是【付费加购项】"
                  "（Prioritized Data Add-on）；Light Speed 只写 High Speed Data——「高速」是流量口径，不是优先级口径",
                  "【选哪张网直接决定套餐质量】：同样 $25，Dark Star 给不限速无限高速，Warp/Light Speed 只给 70GB 且热点砍半（10GB vs 20GB）；"
                  "官方营销页统一写「20GB 热点」，是按最好情况写的",
                  "【官网自己前后矛盾】：套餐卡下写 Taxes &amp; fees included，同页 FAQ 却写可能另收 $2 Service Fee 与 $1–$5/线 Recovery Fee。"
                  "本页按「已含」计算，但下单前必须在结账页确认——若实际另收，它在 $25 档的优势会被吃掉",
                  "$199 首年价【只限新线】，第二年自动跳 $270（官方原文 Renews at full price）",
                  "该促销档期极短：官方 promo-archive 写明 2026-08-12 至 2026-08-18",
                  "年付需一次性付清，且这是本品牌唯一的价格杠杆（没有 AutoPay 折扣）"]),
    dict(name="Google Fi", short="FI", net="T-Mobile", fee=0.0,
         blurb="Google 自营的虚拟运营商。四档结构很清楚（一档按量付费 + 三档无限），阈值和降速数字是全表写得最直白的，"
               "但美国本地使用偏贵，而且入门档被阉割得很厉害。",
         gotchas=["【网络归属是第三方推断】fi.google.com 全篇不点名 T-Mobile 或任何运营商，只说 an ultra-reliable 5G network。"
                  "本页为了能在价格轴上和同网竞品并排，仍按 T-Mobile 归类，但这不是官方表述",
                  "【Unlimited Essentials 是个陷阱档】官方 Broadband Facts 逐字写 No hotspot capability——完全没有热点功能；"
                  "support 页原文 Does not work outside the US——出美国直接不能用。等于把 Fi 唯一的核心卖点砍掉了",
                  "【首次激活必须在美国境内】条款禁止境外首次激活，且要求先在美国实际使用至少 1 天才能在境外使用——"
                  "「落地前在国内先开好号」这条路走不通",
                  "【长住境外会被停国际数据】连续 90 天内若大部分用量发生在美国境外，Google 会停掉你的国际数据。"
                  "靠 Fi 保号过完整暑假甚至休学一年，属于条款打击范围",
                  "50% 促销条件很硬：必须自带 Google Pixel + 必须是新客 + 只管 12 个月，官网显示 Ends Sep 10",
                  "税费另计（Monthly prices do not include taxes and gov't fees），且 Fi 本身即自动扣款，无 AutoPay 折扣可谈"]),
    dict(name="Metro", short="MET", net="T-Mobile", fee=0.0,
         blurb="T-Mobile 全资预付费品牌，是 Cricket 在 T-Mobile 侧的对位者。官网对 $30/$40/$50/$60 四档逐条写明 "
               "Taxes and fees included，并带 5 年价格保证——原表有 Cricket 却没有 Metro，是结构性缺口，本页补上。",
         gotchas=["【官网没有公开的多线阶梯表】查过 7 个官方页面（/phone-plans、/plan-benefits、/deals、/deals/40period、"
                  "/deals/one-line-for-25-phone-plan、/deals/4-lines-for-100、/onlineplans）均未刊登 2/3/5 线每线价",
                  "那个「4 线 $100」就是单线价 $25 原样复制四份，而且写明【只能到店办】——多线优惠在数字上并不比单线促销价更便宜",
                  "5 年价格保证只锁 talk/text/5G 数据，有除外条款",
                  "打中国大陆【无法确认】：国际加装包清单已抓到（$10/月 Global Voice 覆盖 210+ 国家与地区），"
                  "但中国大陆是否在内、含多少分钟，页面用动态国家查询工具，抓不出结果；官网自己也提示要打电话确认"]),
    dict(name="Mint Mobile", short="MNT", net="T-Mobile", fee=2.09,
         blurb="T-Mobile 网络的预付费品牌，靠「一次性预付 3/6/12 个月」换低价。"
               "流量档在 2026 年做过升级：5GB→6GB、15GB→17GB、20GB→23GB。",
         gotchas=["【网络归属本次未取得官网原文】一个审计 agent 成功抓到 mintmobile.com/plans 并逐字引用了资费与促销条款，"
                  "另一个 agent 对同域名的两次尝试（WebFetch 与带完整浏览器 UA 的 curl）均返回 HTTP 403。"
                  "所以「跑 T-Mobile 网」这条本页标为未取得官方原文——历史上 Mint 的无限档阈值曾是 35GB/40GB，阈值口径变动频繁",
                  "税费另计（Recovery Fee $1.88–$2.29/月 + FUSF + 州税），这点常被忽略",
                  "$15 促销【只管第一个周期】，Unlimited 续费回到 $30/月",
                  "预付周期越短单价越贵：3 个月档的常规价比 12 个月档贵 $10–$20/月",
                  "官方 FAQ 白纸黑字承认【没有任何多线折扣】，所谓 Family Plan 只是账号管理界面",
                  "Unlimited 超 50GB 后拥堵时降优先级"]),
]

# ── 套餐 ──────────────────────────────────────────────────────────────
# adv=常规可得价(开AutoPay)；raw=非AutoPay牌价；promo=促销价
P = []
def add(**kw): P.append(kw)

# ── Visible ────────────────────────────────────────────────────────────
add(id="vis-base", brand="Visible", name="Visible（月付基础档）", adv=25, promo=None, tax_inc=True,
    oneline="Verizon 网络无限流量，税费全含，$25 就是账单数字",
    data="无限高速数据，无 GB 阈值。但【不含 5G Ultra Wideband】，只有 5G/4G LTE",
    depri="会被降优先级的那条队列。官网脚注原文：In times of traffic, your data may be temporarily slower than other traffic",
    hotspot="无限量，但全程锁速 5 Mbps，且限 1 台设备连接",
    video="最高 480p（基础档）", intl="含美国境内拨打/短信墨西哥、加拿大。Global Pass $10/天覆盖 140+ 国（清单里核对到中国大陆）。【不含打中国】",
    prepay="月付，无合约", autopay="无 AutoPay 差价", cond="需自带兼容解锁手机",
    notes="Broadband Facts 里本档下行只有 5G 34–149 Mbps——这是「不含 UW」的直接体现。",
    url="https://www.visible.com/plans", chips=[dict(t="无热点限制", k=""), dict(t="降优先级", k="warn")])
add(id="vis-base-yr", brand="Visible", name="Visible（年付 $275/年）", adv=22.92, promo=None, tax_inc=True,
    oneline="年付摊到每月 $22.92，但第一年反而比月付+促销码贵",
    data="同月付基础档", depri="同月付基础档", hotspot="无限量锁速 5 Mbps",
    video="最高 480p", intl="同月付基础档", prepay="一次性年付 $275，激活后不退款",
    autopay="无", cond="需自带兼容解锁手机",
    notes="年付在 Visible 体系里性价比最尴尬：第一年比「月付 + SAVE6」还贵，只有从第二年起才比裸价 $25 便宜。"
          "对刚落地、还不确定住哪/待多久的人风险偏高。SAVE6 与 SUMMER 促销码均明确写明不适用于年付。",
    url="https://www.visible.com/plans", chips=[dict(t="年付锁定", k="warn")])
add(id="vis-plus", brand="Visible", name="Visible+（月付）", adv=35, promo=29, tax_inc=True,
    oneline="有优先数据的那一档——这才是 Visible 值得推荐的版本",
    data="无限【高级优先】数据（premium/priority），含 5G Ultra Wideband",
    depri="【本次十家里官方措辞最硬的一条】脚注 5 逐字：Visible+ and Visible+ Pro give you unlimited premium data "
          "on Verizon's award-winning 5G &amp; 4G LTE networks when 5G Ultra Wideband is unavailable. "
          "Premium data means no data slowdowns due to prioritization. 且底层网络是官方点名 Verizon，不是第三方推断。",
    hotspot="无限量，锁速 10 Mbps（基础档的两倍）", video="1080p【只在 5G Ultra Wideband 覆盖下成立】；5G/LTE 下只有 720p",
    intl="含墨西哥/加拿大通话短信与数据漫游；每月含 1 天 Global Pass",
    prepay="月付", autopay="无 AutoPay 差价", cond="需自带兼容解锁手机",
    promo_terms="促销码 SAVE6：$6 off、前 12 个月，即 $29/月。官网首页与 /plans 页同时展示。不适用于年付档。",
    notes="基础版和 Visible+ 的真正差别不在流量数字，而在【优先级队列】和【UW 接入】。差 $10 买的是这两样。",
    url="https://www.visible.com/plans", chips=[dict(t="优先数据", k="good"), dict(t="含 5G UW", k="good")])
add(id="vis-pro", brand="Visible", name="Visible+ Pro（月付）", adv=45, promo=35, tax_inc=True,
    oneline="顶配：优先数据 + 15 Mbps 热点 + 更强国际",
    data="无限高级优先数据，含 5G UW", depri="不受常规降优先级条款约束",
    hotspot="无限量，锁速 15 Mbps", video="最高 1080p HD",
    intl="85+ 国拨打 / 200+ 国短信；含 Global Pass 额度", prepay="月付", autopay="无",
    cond="需自带兼容解锁手机",
    promo_terms="两个码并存，本档 SUMMER 更便宜：SUMMER $10 off 前 12 个月 → $35/月；SAVE6 $6 off → $39/月。年付另有 SAVEHALF 五折（$225/年）。",
    notes="Pro 与 Visible+ 的差价买的是热点速度（15 vs 10 Mbps）和国际范围。单纯在美国用手机的人不需要。",
    url="https://www.visible.com/plans", chips=[dict(t="优先数据", k="good")])

# ── Total Wireless ─────────────────────────────────────────────────────
add(id="tot-byo", brand="Total Wireless", name="Total MAX 5G BYO", adv=25, promo=20, tax_inc=True,
    oneline="全表最强的「Verizon 网络 + 含税 + 无降优先级」组合，前提是自带手机",
    data="无限 premium 5G 数据，含 5G Ultra Wideband。官网未设 GB 阈值",
    depri="【表述需限定】No network deprioritization or throttling 这句只出现在官方竞品对比营销页 /facts"
          "（该页自带免责：Data verified as of 5/13/2026），以及 Verizon 新闻稿的 won't slow you down。"
          "两个实际售卖页（/plans/ 与 /m/plans/smartphone）完全没有 deprioritization / premium data 字样。"
          "服务总条款则保留兜底权：跑进全网前 0.5% 重度用户会被压到 1.5 Mbps，且 certain Plans 内不同流量可被区别优先级。",
    hotspot="无限量，锁速 5 Mbps，限 1 台设备", video="官网未明确列出（未找到）",
    intl="140+ 国漫游（数据 10GB/月、通话 300 分钟/月、短信无限）。【中国是否在 140+ 名单内无法确认——官网清单为动态加载未渲染】",
    prepay="月付预付费", autopay="$25 即 AutoPay 价；官网不公布非 AutoPay 牌价（促销页写首月 $30）",
    cond="必须自带符合条件的解锁兼容设备，这是 BYO 专属档",
    promo_terms="官网当前横幅：首月 $30，之后 $20/月（36 个月约 $730）——比原表的 $25 每月还低 $5。"
                "新客另享 5 年锁价：只锁当时的含税月费，不含促销与附加包。",
    notes="原表把 $25 填在「常规价」列且促销价留空是不准确的——官网只印 AutoPay 价，非 AutoPay 牌价本次查不到。"
          "另外 AutoPay 的 $5 折扣是【每账户一个】(one per account)，不是每线一个——拼卡时不能按每人减 $5 算。",
    url="https://www.totalwireless.com/m/byop", chips=[dict(t="官方称不降优先级", k="good"), dict(t="5年锁价", k="good")])
add(id="tot-starter", brand="Total Wireless", name="Total STARTER", adv=35, promo=None, tax_inc=True,
    oneline="唯一会被常规降优先级的一档，单人不划算，拼卡才有意义",
    data="无限数据", depri="这一档【会】被降优先级（与 MAX 系列不同）",
    hotspot="含（额度见官网）", video="未找到", intl="未找到", prepay="月付预付费",
    autopay="$35 为 AutoPay 价", cond="可自带手机或买机",
    notes="这档的价值在 4 线：$95 总价即每线 $23.75，是 Total 全线拼卡最优解——不是看着最便宜的 MAX 5G BYO。",
    url="https://www.totalwireless.com/m/plans/smartphone", chips=[dict(t="会降优先级", k="warn")])
add(id="tot-max", brand="Total Wireless", name="Total MAX 5G", adv=50, raw=55, promo=None, tax_inc=True,
    oneline="不自带手机时的 MAX 档，配置与 BYO 版几乎一样",
    data="无限 premium 5G 数据，含 5G UW", depri="官方：No network deprioritization or throttling",
    hotspot="无限量锁速 5 Mbps", video="未找到",
    intl="140+ 国漫游（10GB 数据 / 300 分钟 / 无限短信）", prepay="月付预付费",
    autopay="$50 为 AutoPay 价，牌价 $55", cond="无需自带手机",
    notes="单人自带手机没有任何理由选这档——配置与 $25 的 BYO 版几乎完全一样（同为 premium data、同为无限 5 Mbps 热点、"
          "同为 140+ 漫游、同为 100GB 云盘），只差在是否必须自带手机。",
    url="https://www.totalwireless.com/m/plans/smartphone", chips=[dict(t="官方称不降优先级", k="good")])
add(id="tot-all", brand="Total Wireless", name="Total ALL ACCESS", adv=60, promo=None, tax_inc=True,
    oneline="顶配：热点提速到 10 Mbps + 1TB 云盘 + Disney+",
    data="无限 premium 5G 数据，含 5G UW", depri="官方：No network deprioritization or throttling",
    hotspot="无限量，锁速 10 Mbps（MAX 的两倍）", video="未找到",
    intl="140+ 国漫游 + $10 国际长途 credit。【中国是否覆盖无法确认】", prepay="月付预付费",
    autopay="$60 为 AutoPay 价；非 AutoPay 牌价官网未印（推算 $65，按铁律不填）",
    cond="可自带手机", notes="比 MAX 5G 贵 $10，换来热点 5→10 Mbps、云盘 100GB→1TB、Disney+ Premium。本来就付 Disney+ 的话这 $10 是赚的。",
    url="https://www.totalwireless.com/m/plans/smartphone", chips=[dict(t="官方称不降优先级", k="good")])

# ── Verizon ────────────────────────────────────────────────────────────
add(id="vzw-simp", brand="Verizon", name="Simplicity Plan", adv=45, raw=55, promo=30, tax_inc=False, fee=3.99,
    oneline="Verizon 直营当前唯一主力无限档，税费另计",
    data="手机本机无限数据；每账期超过 500GB 后降至 4 Mbps",
    depri="机制与 T-Mobile Essentials 完全不同：Simplicity 是【不做拥堵劣后、只在 500GB 后硬降速到 4 Mbps】——"
          "500GB 是速度天花板，不是优先级顺位。横向比较时不要把「500GB 后 4Mbps」和「50GB premium data」当同类项。",
    hotspot="10GB，之后本账期剩余时间降至 1 Mbps", video="5G/4G LTE 覆盖区内 720p",
    intl="美国境内无限拨打墨西哥和加拿大（受公平使用限制）", prepay="月付后付费，需查信用",
    autopay="$45 需 AutoPay + 无纸账单，付款方式需符合条件；不用 AutoPay 牌价 $55",
    cond="支持 BYOD，也支持新机分期",
    promo_terms="$30/月需 AutoPay + 转网/携号优惠（需上传 45 天内的他家账单）。这是【转网专属】，不是长期常规价。",
    notes="Simplicity 拿不到 Verizon 的大额手机抵扣——那些促销一律要求 Unlimited Plus 或 Ultimate。",
    url="https://www.verizon.com/support/verizon-simplicity-faqs/", chips=[dict(t="后付费·查信用", k="warn")])
add(id="vzw-pp15", brand="Verizon", name="Verizon Prepaid 15GB", adv=35, raw=45, promo=30, tax_inc=False, fee=0.0,
    oneline="Verizon 网络的小流量预付费档，不查信用",
    data="15GB 高速数据（5G/4G LTE），含无限通话短信", depri="超额规则见官网",
    hotspot="含（额度见官网）", video="未找到",
    intl="含发往 200+ 国的无限国际短信；国际通话需另购加装包", prepay="月付预付费，不查信用",
    autopay="$35 需 AutoPay（$10 折扣，首月不享）；牌价 $45",
    cond="需自带兼容手机或购机",
    promo_terms="忠诚度折扣后 $30/月。【官网两处口径不一致】：/plans/prepaid/ 表格写「9 个月后 $30」，"
                "而预付费 FAQ 写两级阶梯「续费 3 次 −$5、续费 9 次再 −$5」。下单前需确认。",
    notes="Verizon 目前【没有】像 AT&T/T-Mobile 那样的小流量后付费档，最小的可用流量档就是这个预付费 15GB。",
    url="https://www.verizon.com/plans/prepaid/", chips=[dict(t="不查信用", k="good")])
add(id="vzw-ppunl", brand="Verizon", name="Verizon Prepaid Unlimited", adv=50, raw=60, promo=None, tax_inc=False, fee=0.0,
    oneline="Verizon 网络无限流量，不查信用不需 SSN",
    data="无限数据", depri="见官网", hotspot="含（额度见官网）", video="未找到",
    intl="含 200+ 国无限国际短信", prepay="月付预付费",
    autopay="$50 需 AutoPay（$10 折扣，首月不享）；牌价 $60", cond="需自带兼容手机或购机",
    notes="与 Simplicity 的 $45 AutoPay 相比，换算到手价后其实相当接近，但这档不查信用、没有 $3.99 管理费。",
    url="https://www.verizon.com/plans/prepaid/", chips=[dict(t="不查信用", k="good")])
add(id="vzw-ppplus", brand="Verizon", name="Verizon Prepaid Unlimited Plus", adv=60, raw=70, promo=50, tax_inc=False, fee=0.0,
    oneline="预付费顶配，忠诚度折扣后 $50",
    data="无限数据", depri="见官网", hotspot="含", video="未找到",
    intl="含 200+ 国无限国际短信", prepay="月付预付费",
    autopay="$60 需 AutoPay；牌价 $70", cond="需自带兼容手机或购机",
    promo_terms="忠诚度折扣后 $50/月。", notes="",
    url="https://www.verizon.com/plans/prepaid/", chips=[dict(t="不查信用", k="good")])

# ── Cricket ────────────────────────────────────────────────────────────
add(id="ckt-12mo", brand="Cricket", name="12-Month Unlimited（年付 $300）", adv=25, promo=None, tax_inc=True,
    oneline="$300 一次付清、含税、无限流量的 AT&T 网络——代价是完全禁止热点",
    data="无限数据。官方未公布高速阈值 GB 数",
    depri="Cricket【没有任何 premium data / priority data 概念】，官网通篇不出现该词。唯一表述是 "
          "Cricket may temporarily slow data speeds if the network is busy。无固定降速数值、无阈值。"
          "（注：Total Wireless 对比页把 Cricket 描述为 Always on the lowest priority 属竞品营销说法，Cricket 官方并未如此披露）",
    hotspot="【完全不含且不可加购】。官方原文：Tethering or use of device as a mobile hot spot is prohibited",
    video="Cricket 对【所有】套餐做视频降码率：we aim to render content identified as streaming video in "
          "standard-definition (max of 1.5 to 2 Mbps)",
    intl="见官网", prepay="一次性预付 $300 覆盖 12 个月，不退款",
    autopay="不适用——多月档不走 AutoPay 折扣机制",
    cond="需新开单线账户（不能并入现有账户）、必须自带手机、【仅限线上办理】",
    promo_terms="Broadband Facts 明确写 This Monthly Price is not an introductory rate——【这不是促销价，是常态定价】。官网未公布截止日期。",
    notes="对确定要在哥伦布待满一年、且不需要热点的人，这是全表性价比最高的档之一。代价是 $300 不退、禁热点、"
          "加不了任何功能，且转成月付后回不去。",
    url="https://www.cricketwireless.com/cell-phone-plans/multi-month-unlimited",
    chips=[dict(t="非促销价", k="good"), dict(t="禁止热点", k="bad"), dict(t="仅线上", k="warn")])
add(id="ckt-sens", brand="Cricket", name="Sensible 10GB", adv=30, raw=35, promo=None, tax_inc=True,
    oneline="AT&T 网络的小流量含税档",
    data="10GB 高速数据", depri="超额后见官网", hotspot="见官网", video="可能限制为 SD",
    intl="见官网", prepay="月付预付费", autopay="$30 需 AutoPay（$5 credit，自第 2 个月起生效）；牌价 $35",
    cond="需自带兼容手机",
    notes="多线【零折扣】：$30×线数，别被套餐列表并排展示误导。超额后降至 128 Kbps。"
          "国际功能被阉割：这一档【连国际短信都不可用】，也没有墨西哥/加拿大通话。",
    url="https://www.cricketwireless.com/plans/phone", chips=[dict(t="小流量", k="")])
add(id="ckt-select", brand="Cricket", name="Select Unlimited", adv=35, raw=40, promo=None, tax_inc=True,
    oneline="AT&T 网络含税无限档，但不含热点",
    data="无限数据", depri="仅拥堵时可能临时降速；Select 未见高级优先级声明",
    hotspot="【不含】。要热点需上 $55 的 Supreme（含 50GB）；中间档 Smart Unlimited $45 含 15GB",
    video="限制为 SD（Cricket 全线降码率 max 1.5–2 Mbps）",
    intl="只有对墨西哥/加拿大的通话短信；官网同样标注【国际短信不可用】。所谓 200+ 国家是【可加购范围】，"
         "不是套餐自带也不是不限量——按国家单买加装包 $10/月起，且是 a set amount of calling minutes（有分钟上限）",
    prepay="月付预付费",
    autopay="$35 需 AutoPay（$5 credit，自第 2 个月起生效）；牌价 $40", cond="需自带兼容手机",
    notes="原表把 $40 当「常规价」、$35 当「促销价」是反的——$35 才是长期常在价，$40 只存在第一个月。"
          "官网另标注 New lines only、账户内所有线必须同为 Select Unlimited。",
    url="https://www.cricketwireless.com/plans/phone", chips=[dict(t="不含热点", k="bad")])
add(id="ckt-smart", brand="Cricket", name="Smart Unlimited", adv=45, raw=50, promo=None, tax_inc=True,
    oneline="中档，含税，含 15GB 热点", data="无限数据", depri="仅拥堵时可能临时降速", hotspot="15GB（审计复核官网确认）",
    video="可能限制为 SD", intl="见官网", prepay="月付预付费",
    autopay="$45 需 AutoPay（自第 2 个月起）；牌价 $50", cond="需自带兼容手机", notes="",
    url="https://www.cricketwireless.com/plans/phone", chips=[])
add(id="ckt-sup", brand="Cricket", name="Supreme Unlimited", adv=55, raw=60, promo=None, tax_inc=True,
    oneline="Cricket 唯一含大额热点的档（50GB）", data="无限数据",
    depri="仅拥堵时可能临时降速", hotspot="50GB", video="见官网",
    intl="比 Select 更强的国际功能", prepay="月付预付费",
    autopay="$55 需 AutoPay（官方原文 $55/month with Auto Pay after $5 credit in month 2）；牌价 $60",
    cond="需自带兼容手机", notes="", url="https://www.cricketwireless.com/plans/phone",
    chips=[dict(t="50GB 热点", k="good")])

# ── AT&T ───────────────────────────────────────────────────────────────
add(id="att-pp12", brand="AT&T", name="Prepaid 12-Month Unlimited（$240/年）", adv=20, promo=None, tax_inc=False, fee=2.63,
    oneline="全线最便宜的 AT&T 入口，$240 一次付清覆盖 360 天",
    data="每 30 天 16GB 高速额度，之后不断网但全面降速",
    depri="【硬降速】法律原文：If 16GB high-speed data allowance is used in a 30-day period, all data speeds including video are reduced to a max. of 1.5Mbps for the remainder of the 30 days",
    hotspot="10GB 高速，之后降至 128 Kbps（该速度下热点基本不可用）", video="超额后同样受 1.5 Mbps 限制",
    intl="美国境内使用；数据仅限美国", prepay="一次性预付 $240 覆盖 360 天，不退款",
    autopay="不适用——法律原文 Not eligible for AutoPay discount or multi-line accounts",
    cond="仅线上办理、仅单线",
    notes="对确定待满一年的人性价比极高；对可能中途换号/回国的人风险大（不退款）。每次缴费另收 $2.63 管理费。",
    url="https://www.att.com/prepaid/plans/", chips=[dict(t="16GB 后 1.5Mbps", k="warn"), dict(t="仅线上单线", k="warn")])
add(id="att-pp25", brand="AT&T", name="Prepaid $25 Unlimited（5 年锁价）", adv=25, promo=None, tax_inc=False, fee=2.63,
    oneline="月付里最便宜的 AT&T，但速度被硬封在 3 Mbps",
    data="每 30 天 30GB，且这 30GB 【本身就被封顶在 3 Mbps】",
    depri="【硬降速 + 高速档本身限速，双重限制】法律原文：Plan includes 30GB of data per 30-day period at a maximum speed of 3Mbps in the U.S. If 30GB is used, all data speeds are reduced to a max of 1.5Mbps",
    hotspot="【不含】。可另加 5GB 热点包 $10/月 + 税", video="受 3 Mbps 限制",
    intl="见官网", prepay="月付预付费", autopay="不适用——锁价条款排除 AutoPay 折扣",
    cond="仅线上、仅新单线客户",
    promo_terms="5 年锁价。但条款写明：If you cancel your service, change to an ineligible plan, or add a line to your account, your price lock will end——以后想加室友的线，锁价直接作废。",
    notes="3 Mbps 不是「网络忙才慢」，是永远 3 Mbps。刷 1080p 视频勉强，4K 不行，大文件下载会很难受。",
    url="https://www.att.com/prepaid/plans/", chips=[dict(t="全程 3Mbps 封顶", k="bad"), dict(t="5年锁价", k="good")])
add(id="att-ppsaver", brand="AT&T", name="Prepaid Unlimited Saver", adv=35, promo=None, tax_inc=False, fee=2.63,
    oneline="配置与 $25 档一模一样，却贵 $10——基本没有存在价值",
    data="每 30 天 30GB，速度封顶 3 Mbps",
    depri="与 $25 档完全相同的硬降速条款", hotspot="不含，可加 5GB 包 $10/月",
    video="受 3 Mbps 限制", intl="见官网", prepay="月付预付费",
    autopay="不适用——法律原文 Not eligible for Auto Pay discount or Multi-Line account", cond="可店内/Walmart 办理",
    notes="流量、速度、热点、国际功能与 $25 档完全一致，唯一差别是 $25 档限「仅线上 + 新单线客户」，本档没有这个限制。"
          "能线上办且是新客的话，直接选 $25 档。",
    url="https://www.att.com/prepaid/plans/", chips=[dict(t="全程 3Mbps 封顶", k="bad"), dict(t="不推荐", k="bad")])
add(id="att-ppplus", brand="AT&T", name="Prepaid Unlimited Enhanced Plus", adv=45, promo=None, tax_inc=False, fee=2.63,
    oneline="预付费里第一个真「无限量」（无 GB 阈值）的档",
    data="美国和墨西哥境内无限量数据，无 GB 高速阈值；加拿大 25GB 后降至 512 Kbps",
    depri="仅拥堵时降优先级，但【无用量门槛保护】——任何时候基站忙都可能降速",
    hotspot="10GB 高速，之后 128 Kbps", video="见官网", intl="含墨西哥；加拿大 25GB 后降速",
    prepay="月付预付费", autopay="不适用——不可与 AutoPay 折扣合用",
    cond="这是预付费里第一个能拼室友卡的档（Multi-Line 门槛正是 $45）",
    notes="同价位的后付费 Value 2.0 只要 $50（AutoPay）就有 5GB 优先保护 + 后付费信用建立，但要查信用。",
    url="https://www.att.com/prepaid/plans/", chips=[dict(t="不查信用", k="good"), dict(t="无优先保护", k="warn")])
add(id="att-bap-sd", brand="AT&T", name="Build-A-Plan · Unlimited SD（无热点）", adv=35, promo=None, tax_inc=False, fee=4.99,
    oneline="官方自定义套餐：$15 基础 + $20 无限 SD 数据 = $35，仅线上、仅单线",
    data="无限量数据，但【视频硬限 SD】且速度标注 max 2 Mbps（5G）/ 1.5 Mbps（4G）",
    depri="AT&T 称网络繁忙时可能临时降速；本行未找到硬性高速阈值",
    hotspot="【默认不含】。可加购 5GB(+$5)=$40、25GB(+$15)=$50、50GB(+$20)=$55",
    video="硬限 SD", intl="Build-A-Plan 官方页未清楚列出包含的国际功能",
    prepay="月付，可按月调整配置", autopay="【要求 AutoPay，但没有 AutoPay 折扣】——官方原文 AutoPay is REQUIRED. There is NO AutoPay discount.",
    cond="仅线上办理；必须自带已付清、已解锁、支持 eSIM 的手机；【每账户限 1 条线】，室友拼卡完全用不了",
    notes="审计确认：$35 就是 AT&T 官方价目矩阵里 Unlimited SD 的总价，不是拼算出来的。"
          "但这个产品线 NO promotional offers、NO switcher credits、NO bill credits，不能分期买机也不能以旧换新——"
          "想要补贴手机只能走传统 Unlimited 2.0。门店买不到。",
    url="https://www.att.com/plans/build-a-plan/",
    chips=[dict(t="限 1 条线", k="bad"), dict(t="视频硬限 SD", k="bad"), dict(t="拿不到任何促销", k="warn")])
add(id="att-bap-sd25", brand="AT&T", name="Build-A-Plan · Unlimited SD + 25GB 热点", adv=50, promo=None, tax_inc=False, fee=4.99,
    oneline="Build-A-Plan 加满热点后的价格，和后付费 Value 2.0 同价",
    data="无限量数据，视频硬限 SD，速度 max 2 Mbps（5G）", depri="繁忙时可能临时降速",
    hotspot="25GB（+$15 加购）", video="硬限 SD", intl="官方页未清楚列出",
    prepay="月付", autopay="要求 AutoPay 但无折扣", cond="仅线上、仅单线、必须 eSIM",
    notes="到了这个价位就该重新算账：同为 $50 的后付费 Value 2.0 视频不限 SD、有 5GB 优先保护、能拼卡、能买机分期——"
          "Build-A-Plan 只在「$35 无热点」那一档有意义。",
    url="https://www.att.com/plans/build-a-plan/", chips=[dict(t="限 1 条线", k="bad"), dict(t="视频硬限 SD", k="bad")])
add(id="att-value", brand="AT&T", name="Value 2.0（后付费）", adv=50, raw=60, promo=None, tax_inc=False, fee=4.99,
    oneline="AT&T 后付费入门档，热点只有 3GB 是硬伤",
    data="无限量数据 + 5GB 高速优先额度（超 5GB 不断网、不硬降速，只是失去优先保护）",
    depri="仅拥堵时降优先级。官方支持页：Unlimited plus 5GB of high-speed data. After 5GB, AT&T may temporarily slow data speeds if the network is busy",
    hotspot="3GB，之后降至最高 128 Kbps", video="见官网", intl="见官网",
    prepay="月付后付费，需查信用", autopay="$50 需 AutoPay + 无纸账单（$10 折扣，绑银行账户或 AT&T Points Plus 卡才给足额）；牌价 $60",
    cond="支持 BYOD 与分期购机",
    notes="对比 AT&T Prepaid $25 档：现金支出明显更高，但换来「仅拥堵降优先级」（无 3 Mbps 硬顶）和后付费信用记录。",
    url="https://www.att.com/plans/wireless/", chips=[dict(t="后付费·查信用", k="warn"), dict(t="热点仅 3GB", k="bad")])
add(id="att-ppultra", brand="AT&T", name="Prepaid Unlimited Ultra", adv=60, promo=None, tax_inc=False, fee=2.63,
    oneline="预付费里唯一承诺「不因用量降速」的一档，30GB 热点",
    data="真·无限高速数据，无 GB 阈值、不因用量降速。卡片原文：Data that can't slow down based on how much you use",
    depri="【不因用量降速——预付费里唯一有此承诺的一档】。加拿大 25GB 后降至 512 Kbps",
    hotspot="30GB 高速，之后 128 Kbps", video="见官网", intl="含美国与墨西哥无限数据",
    prepay="月付预付费", autopay="该档条款未提及 AutoPay 折扣（与 $35/$45 档明确写「不可合用」不同）",
    cond="不查信用、不需 SSN",
    notes="与后付费 Extra 2.0 的 AutoPay 价 $70 只差 $10，但 Extra 2.0 有 100GB 高速保护 + 50GB 热点。"
          "对不想查信用又要大流量+大热点的人，这是最合适的一档。",
    url="https://www.att.com/prepaid/plans/", chips=[dict(t="不因用量降速", k="good"), dict(t="不查信用", k="good")])
add(id="att-extra", brand="AT&T", name="Unlimited Extra 2.0（后付费）", adv=70, raw=80, promo=None, tax_inc=False, fee=4.99,
    oneline="AT&T 官方标注 Most popular——100GB 高速 + 50GB 热点，是全线性价比拐点",
    data="无限量数据 + 100GB 高速优先额度",
    depri="仅拥堵时降优先级：After 100GB, AT&T may temporarily slow data speeds if the network is busy",
    hotspot="50GB，之后 128 Kbps", video="见官网", intl="见官网",
    prepay="月付后付费，需查信用", autopay="$70 需 AutoPay + 无纸账单；牌价 $80", cond="支持 BYOD 与分期购机",
    notes="相比 Value 2.0 多 $20/月，换来 95GB 高速保护和 47GB 热点。四人拼卡每人 $40（AutoPay）+ 税费。"
          "AT&T 的大额手机抵扣主要挂在这一档和 Premium。",
    url="https://www.att.com/plans/wireless/", chips=[dict(t="100GB 优先", k="good"), dict(t="50GB 热点", k="good")])
add(id="att-prem", brand="AT&T", name="Unlimited Premium 2.0（后付费）", adv=90, raw=100, promo=None, tax_inc=False, fee=4.99,
    oneline="彻底去掉 GB 阈值 + 100GB 热点",
    data="真·无限高速数据，无 GB 阈值",
    depri="【不因用量降速】——本档法律条款中不存在 Value/Extra 那种 After XGB 降速句",
    hotspot="100GB，之后 128 Kbps", video="见官网", intl="含拉美漫游",
    prepay="月付后付费，需查信用", autopay="$90 需 AutoPay + 无纸账单；牌价 $100", cond="支持 BYOD 与分期购机",
    notes="从 Extra（$70）升到 Premium（$90）多花 $20 买两样：去掉 100GB 阈值、热点 50→100GB，外加拉美漫游和平板/手表 5 折。"
          "对普通用户通常不划算——100GB 高速已经够用。",
    url="https://www.att.com/plans/wireless/", chips=[dict(t="不因用量降速", k="good")])

# ── T-Mobile ───────────────────────────────────────────────────────────
add(id="tmo-stu-saver", brand="T-Mobile", name="Essentials Saver + 学生优惠 2.0", adv=30, raw=35, promo=None, tax_inc=False, fee=4.49,
    oneline="T-Mobile 全线对学生最便宜的一档，比普通版便宜 $20/月",
    data="无限 5G/4G LTE，其中 50GB 为 premium 优先数据",
    depri="不是降到固定速度，是降优先级，且 Essentials 常态优先级就低。官网脚注：Essentials 2.0 customers may notice speeds lower than other customers and further reduction if using >50GB/month",
    hotspot="无限量但【全程 3G】，无高速额度。Open Internet 政策给出的数字是最高 600 kbps",
    video="SD", intl="基础国际功能", prepay="月付后付费，需查信用（Credit approval & deposit may be required）",
    autopay="$30 需 AutoPay（要求银行账户或借记卡，信用卡不算）；牌价 $35",
    cond="需在 45 天内完成学籍验证，并按要求复验",
    promo_terms="非限时促销，是学籍资格价。掉验证会被加价至多 $20/线/月。线上下单每次最多 2 台设备。",
    notes="OSU 在读就能用。换算到手价约 $42，仍是 T-Mobile 网络里最便宜的后付费入口。",
    url="https://www.t-mobile.com/cell-phone-plans/student-discounts",
    chips=[dict(t="学生价", k="good"), dict(t="热点仅 3G", k="bad"), dict(t="拥堵常态劣后", k="warn")])
add(id="tmo-pp-unl", brand="T-Mobile", name="Prepaid Unlimited Monthly", adv=45, raw=50, promo=None, tax_inc=False, fee=0.0,
    oneline="不查信用、不需 SSN，且没有 $4.49 附加费——纯资费上比 Essentials Saver 更划算",
    data="无限数据", depri="见官网", hotspot="见官网", video="见官网", intl="见官网",
    prepay="月付预付费，不查信用", autopay="$45 需 AutoPay；牌价 $50（也是首月价）",
    cond="需自带兼容手机或购机",
    notes="Broadband Facts 显示预付费 Provider Monthly Fees 已包含在月费内，只有政府税另计——"
          "所以它没有后付费那 $4.49 的 Regulatory & Telco Recovery Fee。",
    url="https://prepaid.t-mobile.com/prepaid-plans", chips=[dict(t="不查信用", k="good"), dict(t="无 $4.49 附加费", k="good")])
add(id="tmo-saver", brand="T-Mobile", name="Essentials Saver 2.0", adv=50, raw=55, promo=None, tax_inc=False, fee=4.49,
    oneline="普通人能拿到的最便宜 T-Mobile 后付费档",
    data="无限 5G/4G LTE，其中 50GB 为 premium 优先数据",
    depri="仅降优先级，且 Essentials 常态低于 Experience 用户；超 50GB 再降一档",
    hotspot="无限量但全程 3G（最高 600 kbps）", video="SD", intl="基础国际功能",
    prepay="月付后付费，需查信用", autopay="$50 需 AutoPay（银行账户或借记卡，信用卡不算）；牌价 $55",
    cond="支持 BYOD", notes="原表用的 $55 是【未含 AutoPay】的 Broadband Facts 价，而同表 Verizon 用的是含 AutoPay 的 $45——口径不一致。",
    url="https://www.t-mobile.com/cell-phone-plans", chips=[dict(t="热点仅 3G", k="bad"), dict(t="拥堵常态劣后", k="warn")])
add(id="tmo-stu-more", brand="T-Mobile", name="Experience More + 学生优惠 2.0", adv=65, raw=70, promo=None, tax_inc=False, fee=4.49,
    oneline="学生价中档：无限优先数据 + 60GB 热点 + 中国漫游 5GB",
    data="无限 premium 优先数据（官网未给具体降级阈值）",
    depri="官网未给 Experience More 的具体阈值。Open Internet 通则把 Heavy Data User 定义为「一般 50GB 或 100GB」",
    hotspot="60GB 高速，之后最高 3G（600 kbps）", video="见官网",
    intl="中国漫游含 5GB 高速——对经常回国的人实用", prepay="月付后付费，需查信用",
    autopay="$65 需 AutoPay；牌价 $70", cond="需学籍验证",
    notes="含 Netflix 带广告版 + Apple TV $3/月，折算下来能抵掉一部分与 Essentials Saver 学生价的差额。",
    url="https://www.t-mobile.com/cell-phone-plans/student-discounts",
    chips=[dict(t="学生价", k="good"), dict(t="60GB 热点", k="good")])
add(id="tmo-stu-beyond", brand="T-Mobile", name="Experience Beyond + 学生优惠 2.0", adv=80, raw=85, promo=None, tax_inc=False, fee=4.49,
    oneline="学生价顶配：250GB 热点 + 中国漫游 15GB + 卫星短信",
    data="无限 premium 优先数据", depri="官网未给具体阈值",
    hotspot="无限量，其中 250GB 为高速（注意：卡面脚注里的 250GB 指的是热点额度，不是数据阈值）",
    video="见官网", intl="中国漫游 15GB 高速；T-Satellite 可在无信号野外发短信",
    prepay="月付后付费，需查信用", autopay="$80 需 AutoPay；牌价 $85", cond="需学籍验证",
    notes="比普通 Experience Beyond 便宜 $20/月。经常回国的话这档的国际额度是全表最强之一。",
    url="https://www.t-mobile.com/cell-phone-plans/student-discounts",
    chips=[dict(t="学生价", k="good"), dict(t="250GB 热点", k="good")])
add(id="tmo-more", brand="T-Mobile", name="Experience More 2.0", adv=85, raw=90, promo=None, tax_inc=False, fee=4.49,
    oneline="普通消费者主力中档", data="无限 premium 优先数据",
    depri="官网未给具体阈值", hotspot="60GB 高速，之后 3G", video="见官网",
    intl="中国漫游 5GB 高速", prepay="月付后付费，需查信用", autopay="$85 需 AutoPay；牌价 $90",
    cond="支持 BYOD", notes="有学籍就别买这档——学生价同档只要 $65。",
    url="https://www.t-mobile.com/cell-phone-plans", chips=[dict(t="60GB 热点", k="good")])
add(id="tmo-beyond", brand="T-Mobile", name="Experience Beyond 2.0", adv=100, raw=105, promo=None, tax_inc=False, fee=4.49,
    oneline="普通消费者顶配", data="无限 premium 优先数据", depri="官网未给具体阈值",
    hotspot="无限量，其中 250GB 高速", video="见官网", intl="中国漫游 15GB",
    prepay="月付后付费，需查信用", autopay="$100 需 AutoPay；牌价 $105", cond="支持 BYOD",
    notes="有学籍就别买这档——学生价同档只要 $80。", url="https://www.t-mobile.com/cell-phone-plans",
    chips=[dict(t="250GB 热点", k="good")])

# ── US Mobile ──────────────────────────────────────────────────────────
add(id="usm-flex", brand="US Mobile", name="Unlimited Flex（仅年付 $210）", adv=17.50, promo=None, tax_inc=True,
    oneline="仅提供年付，官方标注 ANNUAL PLAN ONLY",
    data="见官网各网络差异", depri="随所选网络变化", hotspot="见官网", video="随网络/套餐变化",
    intl="见官网", prepay="仅年付 $210 一次性付清", autopay="无 AutoPay 折扣",
    cond="需解锁兼容手机；可在三网间选择", notes="Broadband Facts 标注 $17.50/mo、not introductory——这是常态价不是促销。",
    url="https://www.usmobile.com/plans", chips=[dict(t="仅年付", k="warn")])
add(id="usm-starter", brand="US Mobile", name="Unlimited Starter", adv=25, promo=16.58, tax_inc=True,
    oneline="三网可选、税费全含的主力档；促销首年 $199 但档期只到 8/18",
    data="【按网络差异极大】Dark Star 上是真·不限速无限高速；Warp 与 Light Speed 上是 70GB 高速数据，之后降速",
    depri="是明确降速到阈值后，不是仅拥堵降优先级。官方 /plans 页：you may experience slower speeds after 70 GB（适用 Warp / Light Speed）。"
          "两点必须补：①「Dark Star 无限高速」是【流量不设阈值】，不等于不被拥堵劣后——官方对 Dark Star 只承诺 High Speed Data；"
          "②【降速后的具体速率官网完全没有公布】，任何写死的数字都是编造。",
    hotspot="按网络差异：Dark Star 20GB、Warp 与 Light Speed 10GB。官方两处自相矛盾——帮助页写 10GB，/plans 页写 "
            "20 GB hotspot on Dark Star。本页取 20GB 是【按 Dark Star 口径】。"
            "【超过热点额度后的速度：官网四处均未找到】",
    video="随所选网络/套餐变化，官网未给统一数值", intl="年付 Starter 含 1GB 国际漫游数据、200 分钟通话和 250 条短信",
    prepay="月付 $25，或年付 $270（$22.50/月）", autopay="无独立 AutoPay 折扣——年付预付是本品牌唯一的价格杠杆",
    cond="需解锁兼容手机",
    promo_terms="$199 首年 = $16.58/月。官方 promo-archive：档期 2026-08-12 至 2026-08-18。"
                "限制：必须一次性年付、【仅限新线】、Renews at full price（第二年跳 $270）。",
    notes="原表把 $16.58 填进「促销价」列与别家月付促销并列，是不可比的——那是年付摊算，且只管第一年。",
    url="https://www.usmobile.com/plans", chips=[dict(t="三网可选", k="good"), dict(t="促销 8/18 截止", k="warn")])
add(id="usm-prem", brand="US Mobile", name="Unlimited Premium", adv=32.50, promo=24.90, tax_inc=True,
    oneline="US Mobile 顶配，官方称无限优先数据",
    data="官方称无限优先数据", depri="Premium 官方称无限优先级数据",
    hotspot="见官网", video="随网络变化", intl="见官网",
    prepay="年付 $390（$32.50/月）；促销 $299 首年（$24.90/月）", autopay="无独立 AutoPay 折扣，但 AutoPay 是学生折扣与 Perk 返现的必要条件",
    cond="需解锁兼容手机",
    promo_terms="$299 首年 = $24.90/月，同为 2026-08-12 至 2026-08-18 档期，仅限新线，续年回全价。",
    notes="3 条以上 Premium 月付线可送 1 个 perk（最高价值 $15/月）——这是 US Mobile 唯一的多线好处。"
          "官方另有学生折扣页，需 AutoPay。",
    url="https://www.usmobile.com/plans", chips=[dict(t="三网可选", k="good"), dict(t="无限优先", k="good")])

# ── Google Fi ──────────────────────────────────────────────────────────
add(id="fi-flex", brand="Google Fi", name="Flexible（按量付费）", adv=20, promo=None, tax_inc=False, fee=0.0,
    oneline="$20 只买通话短信，数据 $10/GB 另算——用一点点就不便宜了",
    data="无固定额度，按 $10/GB 计费，有 Bill Protection 封顶（单人 6GB 后数据免费）",
    depri="硬降速。Broadband Facts 原文：超过 15GB（跨本人所有设备）降至 256 kbps 直到下个账期",
    hotspot="含高速热点，无单独 GB 上限，但【计入本人月度高速数据总量】（脚注 1：Hotspot tethering counts towards "
            "your monthly high-speed data usage），所以实际上限就是 15GB。可同时分享给最多 10 台设备",
    video="官网未标注（未找到）",
    intl="支持 200+ 目的地漫游（中国大陆在覆盖列表内）。国际高速数据上限 15GB/人，之后 256 kbps，且计入月度总量",
    prepay="月付", autopay="无 AutoPay 折扣——Fi 本身即通过 Google Pay 自动扣款",
    cond="需兼容手机；Pixel 兼容性最好",
    promo_terms="【本档不参加当前 50% 促销】——促销只适用于三个无限档。",
    notes="只对每月 1–2GB 以内的极轻度用户成立。$20 是光杆通话短信价：用 1GB 就 $30，用 3GB 就 $50，"
          "很快就被 Unlimited Standard 反超。打中国大陆按 voice.google.com 费率 $0.30/分钟（固话与手机同价），国际短信免费。",
    url="https://fi.google.com/about/plans/flexible", chips=[dict(t="按量付费", k="warn"), dict(t="15GB 后 256kbps", k="warn")])
add(id="fi-ess", brand="Google Fi", name="Unlimited Essentials", adv=35, promo=17.50, tax_inc=False, fee=0.0,
    oneline="全表最被阉割的一档：没有热点功能，而且出美国直接不能用",
    data="30GB 高速/人，之后降至 256 kbps 直到下个账期",
    depri="硬降速到具体数字，不是仅拥堵降优先级。Broadband Facts 逐字给出 30GB → 256 kbps",
    hotspot="【完全不支持】。官方 Broadband Facts 与套餐对比页均写 No hotspot capability——不是额度小，是没有这个功能",
    video="官网未标注（未找到）",
    intl="【完全不支持境外漫游】。support.google.com 原文：Unlimited Essentials: Does not work outside the US。"
         "要出国得先升级到 Unlimited Premium",
    prepay="月付", autopay="无 AutoPay 折扣", cond="需兼容手机；促销要求自带 Google Pixel",
    promo_terms="Get 50% off for 12 months when you bring a Google Pixel phone。必须新客、必须自带 Pixel、"
                "以每月账单抵扣形式发放（非直接改价），12 个月后回到 $35。官网显示 Ends Sep 10。",
    notes="换算到手价约 $43.51，比 Visible+ 的 $35 含税还贵，却没有热点、不能出国、还要 30GB 就降速。"
          "这一档的存在意义基本只是把你引到 Standard 去。打中国大陆 $0.30/分钟，国际短信免费。",
    url="https://fi.google.com/about/plans/unlimited-essentials",
    chips=[dict(t="无热点功能", k="bad"), dict(t="出美国不能用", k="bad"), dict(t="30GB 后 256kbps", k="warn")])
add(id="fi-std", brand="Google Fi", name="Unlimited Standard", adv=50, promo=25, tax_inc=False, fee=0.0,
    oneline="Fi 的主力档，阈值和热点都写得很清楚",
    data="50GB 高速/人，之后降至 256 kbps。可按 $10/GB 购买额外高速数据恢复全速",
    depri="硬降速到具体数字。官方原文给出 Flexible 15GB / Essentials 30GB / Standard 50GB / Premium 100GB 四档阈值",
    hotspot="25GB 高速热点。【是否计入 50GB 总量：官网该页没有写明，本次未找到】——原表写「计入总量」属未核实",
    video="官网未标注（未找到）", intl="含加拿大/墨西哥数据；200+ 目的地漫游",
    prepay="月付", autopay="无 AutoPay 折扣", cond="需兼容手机；促销要求自带 Google Pixel",
    promo_terms="同 Essentials：自带 Pixel + 新客，50% off 前 12 个月（$25/月），账单抵扣形式，官网显示 Ends Sep 10。",
    notes="到手价约 $62.05。同价位的 AT&T Prepaid Ultra（$60 广告价 / 约 $78 到手）给的是不因用量降速 + 30GB 热点；"
          "Fi 的优势不在价格，在阈值透明和账户体验。打中国只免费打加拿大墨西哥，中国仍按分钟计费。",
    url="https://fi.google.com/about/plans/unlimited-standard", chips=[dict(t="50GB 后 256kbps", k="warn"), dict(t="25GB 热点", k="good")])
add(id="fi-prem", brand="Google Fi", name="Unlimited Premium", adv=65, promo=32.50, tax_inc=False, fee=0.0,
    oneline="真正为国际使用买的那一档",
    data="100GB 高速/人，之后降至 256 kbps",
    depri="硬降速到具体数字（100GB 阈值）",
    hotspot="官网该页未单独列出 Premium 的热点额度（未找到）",
    video="官网未标注（未找到）",
    intl="含【从美国免费拨打 50+ 国家和地区】——但<b>那份 50+ 国清单官网没有公开，无法确认中国大陆是否在内</b>。"
         "国际高速数据上限 50GB/人。200+ 目的地漫游",
    prepay="月付", autopay="无 AutoPay 折扣", cond="需兼容手机；促销要求自带 Google Pixel",
    promo_terms="自带 Pixel + 新客，50% off 前 12 个月（$32.50/月），官网显示 Ends Sep 10。",
    notes="到手价约 $80.58。它值不值全看那份 50+ 国清单含不含你要打的地方——而 Google 没公开这份清单，"
          "这在全表里是个相当离谱的信息缺失。经常出国的话 Fi 的漫游体验确实省心（落地自动连、不用买当地卡）。",
    url="https://fi.google.com/about/plans/unlimited-premium", chips=[dict(t="100GB 后 256kbps", k="warn"), dict(t="国际最强", k="good")])

# ── Metro by T-Mobile ──────────────────────────────────────────────────
add(id="met-25", brand="Metro", name="$25 BYOD 档", adv=25, raw=30, promo=None, tax_inc=True,
    oneline="T-Mobile 网络 + 税费全含 + 5 年锁价的最低入口，自带手机专属",
    data="无限流量", depri="见官网", hotspot="本档不含（$30 档起含 10GB）", video="见官网",
    intl="基础国际功能；加装包 $5/月 墨加、$10/月 Global Voice（210+ 国）",
    prepay="月付预付费，不查信用", autopay="$25 为 AutoPay 价，首月 $30",
    cond="需自带兼容解锁手机（BYOD 网络专属价）",
    notes="这是 $25 这一档里唯一跑 T-Mobile 网、且税费全含的选项——正好补上 Cricket（AT&T）、"
          "Total/Visible（Verizon）之外的第三张网。另有 6 个月无限套餐 $120 一次付清（$20/月，新客 BYOD，含税）。",
    url="https://www.metrobyt-mobile.com/phone-plans",
    chips=[dict(t="税费全含", k="good"), dict(t="5年锁价", k="good"), dict(t="不含热点", k="warn")])
add(id="met-30", brand="Metro", name="$30 档（含 10GB 热点）", adv=30, raw=35, promo=None, tax_inc=True,
    oneline="加 $5 换 10GB 热点", data="无限流量", depri="见官网", hotspot="10GB", video="见官网",
    intl="基础国际功能", prepay="月付预付费", autopay="$30 为 AutoPay 价，首月 $35",
    cond="需自带兼容解锁手机", notes="", url="https://www.metrobyt-mobile.com/phone-plans",
    chips=[dict(t="税费全含", k="good")])
add(id="met-35", brand="Metro", name="$35 档（含墨加 + 10GB 热点）", adv=35, raw=40, promo=None, tax_inc=True,
    oneline="含墨西哥/加拿大 + 10GB 热点", data="无限流量", depri="见官网", hotspot="10GB",
    video="见官网", intl="含墨西哥与加拿大", prepay="月付预付费",
    autopay="$35 为 AutoPay 价，首月 $40", cond="需自带兼容解锁手机", notes="",
    url="https://www.metrobyt-mobile.com/phone-plans", chips=[dict(t="税费全含", k="good")])
add(id="met-40", brand="Metro", name="$40 Period（不需 AutoPay）", adv=40, promo=None, tax_inc=True,
    oneline="唯一不要求 AutoPay 的档，$40 就是 $40",
    data="无限流量", depri="见官网", hotspot="见官网", video="见官网", intl="基础国际功能",
    prepay="月付预付费", autopay="【不需要 AutoPay】——这是它的卖点", cond="需自带兼容解锁手机",
    notes="四线 $100（每线 $25，含税）是这家宣传的合租方案，但【只能到店办】。",
    url="https://www.metrobyt-mobile.com/deals/40period", chips=[dict(t="税费全含", k="good"), dict(t="无需 AutoPay", k="good")])
add(id="met-60", brand="Metro", name="$60 Unlimited Premium", adv=60, raw=65, promo=None, tax_inc=True,
    oneline="顶配，含 Amazon Prime", data="无限流量", depri="见官网", hotspot="见官网",
    video="见官网", intl="基础国际功能", prepay="月付预付费", autopay="$60 为 AutoPay 价，首月 $65",
    cond="需自带兼容解锁手机", notes="官网对本档写「4 线省 20%」，即约 $48/线。",
    url="https://www.metrobyt-mobile.com/phone-plans", chips=[dict(t="税费全含", k="good"), dict(t="含 Amazon Prime", k="good")])

# ── Mint Mobile ────────────────────────────────────────────────────────
add(id="mint-6", brand="Mint Mobile", name="6GB/月（12 个月预付）", adv=15, promo=None, tax_inc=False, fee=2.09,
    oneline="T-Mobile 网络小流量档，12 个月预付才是这个价",
    data="6GB 高速（原 5GB 档已升级）", depri="超额后降速，见官网",
    hotspot="含", video="SD / 约 480p", intl="有国际通话/短信选项",
    prepay="12 个月 $180 一次付清；6 个月档 $20/月；3 个月档 $25/月",
    autopay="无 AutoPay 折扣，需预先付款", cond="需兼容且已解锁手机",
    notes="预付周期越短单价越贵——3 个月档比 12 个月档贵 $10/月。", url="https://www.mintmobile.com/plans/",
    chips=[dict(t="需 12 个月预付", k="warn")])
add(id="mint-17", brand="Mint Mobile", name="17GB/月（12 个月预付）", adv=20, promo=15, tax_inc=False, fee=2.09,
    oneline="原 15GB 档已升级为 17GB", data="17GB 高速", depri="超额后降速",
    hotspot="含", video="SD / 约 480p", intl="有国际通话/短信选项",
    prepay="12 个月 $240；6 个月 $25/月；3 个月 $35/月", autopay="无", cond="需兼容且已解锁手机",
    promo_terms="新客首期任意档 $15/月，需一次性预付 $45(3月)/$90(6月)/$180(12月)。仅限初始周期，之后回全价。",
    notes="", url="https://www.mintmobile.com/plans/", chips=[dict(t="需 12 个月预付", k="warn")])
add(id="mint-23", brand="Mint Mobile", name="23GB/月（12 个月预付）", adv=25, promo=15, tax_inc=False, fee=2.09,
    oneline="原 20GB 档已升级为 23GB", data="23GB 高速", depri="超额后降速",
    hotspot="含", video="SD / 约 480p", intl="有国际通话/短信选项",
    prepay="12 个月 $300；6 个月 $35/月；3 个月 $45/月", autopay="无", cond="需兼容且已解锁手机",
    promo_terms="新客首期 $15/月，仅限初始周期。", notes="", url="https://www.mintmobile.com/plans/",
    chips=[dict(t="需 12 个月预付", k="warn")])
add(id="mint-unl", brand="Mint Mobile", name="Unlimited（12 个月预付）", adv=30, promo=15, tax_inc=False, fee=2.09,
    oneline="Mint 的无限档，税费另计这点常被忽略",
    data="无限，50GB 阈值", depri="超过 50GB 后，在网络繁忙时优先级低于其他流量",
    hotspot="20GB", video="SD / 约 480p", intl="有国际通话/短信选项；国际漫游不是它的强项",
    prepay="12 个月 $360；6 个月 $35/月；3 个月 $40/月", autopay="无 AutoPay 折扣，需预先付款",
    cond="需兼容且已解锁手机",
    promo_terms="新客首期 $15/月（一次性预付 $45/$90/$180）。仅限初始周期，续费回 $30/月。",
    notes="换算到手价约 $39，已经不比 Visible+ 的 $35 含税便宜——Mint 的低价光环有相当一部分来自「税费另计」这个口径差。",
    url="https://www.mintmobile.com/plans/", chips=[dict(t="需 12 个月预付", k="warn")])
