# -*- coding: utf-8 -*-
"""体检结论 / 推荐 / 锐评。AUDIT 在审计 agent 返回后合并。"""

VERDICT_LINE = """
<div class="verdict">
<h3>一句话结论</h3>
<p>你那份表的<b>事实基本没错，但口径是乱的</b>——含税价和不含税价混在一起排名、AutoPay 折扣一家算一家不算、
首月价当常规价、年付摊算价当月付促销价。把这些拉平之后，<b>排名会明显变样</b>。</p>
<p>拉平后单线自带手机的答案很集中：<b>$25 这一档挤了五家税费全含的，三张网都有</b>——
Total MAX 5G BYO 与 Visible（Verizon）、Cricket 年付（AT&amp;T）、Metro（T-Mobile）、US Mobile Starter（三网可选）。
而三大直营在同一价位换算成到手价后要贵 $10–$11（同样标价 $25，到手是 $35.14–$36.14），
Verizon Simplicity 标价 $45 更是要到 $59.86。
除非你需要后付费账户、实体店或大额购机补贴，否则没有理由为直营多付这笔钱。</p>
<p class="muted" style="font-size:13.5px">另外补一句原表没覆盖、但对选择影响很大的事实：在哥伦布，
<b>2026 上半年 RootMetrics 路测的赢家是 AT&amp;T 和 T-Mobile，不是 Verizon</b>——Verizon 八个单项奖一项未得。
所以「买 Verizon 网就等于买覆盖最好」这个默认前提，在这座城市并不成立。</p>
</div>
"""

# ── 推荐排序（单线 · 自带手机 · 开 AutoPay · 含税到手价 · 促销不计入排序） ──
RECS = [
    dict(title="Total Wireless — MAX 5G BYO　$25 到手（官网当前促销 $20）",
         why="每块钱买到的东西最多的一档：跑 Verizon 网络且含 5G Ultra Wideband，热点无限（锁速 5 Mbps），"
             "税费全含，新客有 5 年锁价，官网当前横幅还挂着首月 $30、之后 $20/月。"
             "同价位的其他四家各缺一块：Cricket 年付完全禁热点、Metro $25 档不含热点、"
             "Visible 基础版会被降优先级、US Mobile 要看你选到哪张网——只有它没有明显短板。",
         who="自带解锁手机、愿意开 AutoPay、想要一个便宜且不折腾的长期号",
         caveat="<b>我必须把这条的证据强度说清楚，因为它和大多数攻略写的不一样：</b>"
                "「No network deprioritization or throttling」这句<b>只出现在官方竞品对比营销页 /facts</b>"
                "（该页自带免责 Data verified as of 5/13/2026），两个实际售卖页完全没有这个字样；"
                "服务总条款还保留兜底权——跑进全网前 0.5% 重度用户会被压到 1.5 Mbps。"
                "所以它是「官方营销页这么说」，不是「合同这么保证」。"
                "如果你要的是白纸黑字的保证，往下看 Visible+。"
                "另外：官网只印 AutoPay 价，非 AutoPay 牌价查不到；$5 AutoPay 折扣是每账户一个不是每线；"
                "多线阶梯反常，别拿它拼卡；国际 200+ 目的地清单未渲染，中国是否在内无法确认。"),
    dict(title="Cricket — 12-Month Unlimited　$25 到手（$300 一次付清）",
         why="唯一一个「AT&T 网络 + 税费全含 + 官方标明这不是促销价」的组合。"
             "而 AT&T 恰好是哥伦布 2026 上半年 RootMetrics 路测的综合并列第一、速度单项独得冠军。"
             "Broadband Facts 白纸黑字写 This Monthly Price is not an introductory rate——不会到期跳价，这点比任何促销都值钱。",
         who="确定要在哥伦布待满一年、手机上网为主、不需要给笔记本开热点的人",
         caveat="代价很硬：官方原文 tethering is prohibited，完全禁止热点且不可加购；$300 不退款；"
                "仅限线上办理、必须新开单线账户、必须自带手机；转成月付后回不去。"),
    dict(title="Visible+ — $35 到手（促销码 SAVE6 首年 $29）　【条款最硬的一档】",
         why="如果你要的是<b>写在条款里、不是写在营销页上</b>的保证，选它。本次十家里官方措辞最硬的一条就是它的脚注 5："
             "<span class='mono'>Premium data means no data slowdowns due to prioritization.</span>"
             "——直接定义了 premium data 等于不因优先级降速。而且它的底层网络是<b>官方点名 Verizon</b>，"
             "不像 US Mobile / Spectrum / Google Fi 那样只能靠第三方推断。"
             "再加上真月付、随时走、税费全含、无 AutoPay 折腾、10 Mbps 无限热点。"
             "基础版 $25 便宜 $10，但买到的是「拥堵时排在别人后面」+ 不含 UW，这 $10 该花。",
         who="不愿预付、要一个能对着条款讲道理的保证、需要 10 Mbps 无限热点的人",
         caveat="客服只有线上，哥伦布<b>没有实体店</b>——出问题不能走进店里解决。"
                "热点虽无限但锁速 10 Mbps 且限 1 台设备，多设备同连会更慢。"
                "另外「1080p」只在 5G Ultra Wideband 覆盖下成立，5G/LTE 下是 720p。"),
    dict(title="Metro — $25 BYOD 档　$25 到手　【$25 档里唯一的 T-Mobile】",
         why="$25 这一档挤了五家，但前四家全在 Verizon 或 AT&T 上。Metro 是唯一一个"
             "「跑 T-Mobile 网 + 税费全含 + 5 年锁价」的选项——而 T-Mobile 在哥伦布的中位下载速度是三家最快（480.9 Mbps）。"
             "原表有 Cricket（AT&T 侧的对位品牌）却没有 Metro，是个结构性缺口。",
         who="想要 T-Mobile 的速度、又不想付 T-Mobile 直营价的人；主要在市区活动",
         caveat="$25 这一档<b>不含热点</b>，要热点得上 $30 档。"
                "另外 Metro 在北郊偏弱——FCC「行车中」口径 T-Mobile 在 Worthington 只有 68.42%、Dublin 79.90%、"
                "Delaware County 61.90%，而同区 AT&T/Verizon 普遍 96–100%。常跑外县要谨慎。"
                "还有：官网<b>没有任何一张公开的多线阶梯表</b>，那个「4 线 $100」只是单线价复制四份且只能到店办。"),
    dict(title="US Mobile — Unlimited Starter　$25 到手",
         why="唯一能在三张网之间挑的品牌，税费全含。落地初期不确定住处信号如何时，这个灵活性很实在。"
             "官方那句「我们没有多线折扣，因为单线价已经是别人多线折扣后的水平」也算诚实。",
         who="还不确定哪张网在你住处/教室信号最好、想先试再定的人",
         caveat="<b>三网归属是第三方推断</b>——usmobile.com 的 /networks 与 /plans 页从不出现 Verizon、AT&T、T-Mobile 任何一个名字。"
                "而且<b>选哪张网直接决定套餐质量</b>：Dark Star 流量不设阈值且热点 20GB，Warp 与 Light Speed 只给 70GB 然后降速、热点砍半到 10GB。"
                "官方只对 Warp 用了 Priority Data 一词；Dark Star 的优先级是<b>付费加购项</b>，Light Speed 只写 High Speed Data。"
                "降速后的具体速率官网完全没公布。热点数字官方两处还打架（帮助页 10GB vs /plans 页 20GB）。"
                "另外 $199 首年促销仅限新线、档期 2026-08-12 至 08-18、第二年跳 $270。"),
    dict(title="T-Mobile — Essentials Saver + 学生优惠　$30 广告价 / 约 $42 到手",
         why="如果你要的是直营后付费账户（建信用记录、能分期买机、有实体店），这是 T-Mobile 全线最便宜的入口，"
             "比同档非学生版便宜 $20/月。T-Mobile 在哥伦布的中位下载速度是三家最快（480.9 Mbps）。",
         who="在读学生、想要直营后付费账户、市区活动为主的人",
         caveat="三重代价：Essentials 系列<b>常态优先级就低于</b> Experience 用户，超 50GB 再降一档；"
                "热点是「无限但全程 3G」，Open Internet 政策给的数字是最高 600 kbps；"
                "AutoPay 折扣要求银行账户或借记卡，信用卡不算。另需 45 天内完成学籍验证并按要求复验。"),
    dict(title="AT&T — Prepaid Unlimited Ultra　$60 广告价 / 约 $78 到手",
         why="重度用户的答案。预付费里<b>唯一</b>承诺「不因用量降速」的一档（卡片原文 Data that can't slow down based on how much you use），"
             "30GB 高速热点，不查信用不需 SSN。同档后付费 Extra 2.0 要 $70 AutoPay 且要查信用。",
         who="每月流量很大、要给笔记本开热点、不想跑信用的人",
         caveat="贵。而且 AT&T 预付费每次缴费另收 $2.63 管理费。如果你的用量其实到不了 100GB，"
                "Extra 2.0 的 100GB 高速保护 + 50GB 热点性价比更高。"),
]

# ── 锐评 ──────────────────────────────────────────────────────────────
ROAST = [
    dict(tag="词义通胀", title="「无限」这个词在美国手机套餐里已经不含信息量了",
         body="这次实抓到的「无限」至少有五种互不相同的意思：AT&T 预付费 $25 的无限，是 30GB 且这 30GB 本身就被封顶在 3 Mbps，"
              "用完再降到 1.5 Mbps；Cricket 年付的无限，是给你无限流量但<b>明令禁止</b>开热点；"
              "T-Mobile Essentials 的无限，是「你可以一直用，但拥堵时你常态排在别人后面」；"
              "Google Fi Unlimited Essentials 的无限，是 30GB 后砍到 256 kbps <b>而且完全没有热点功能、出美国直接不能用</b>；"
              "而真正敢把话写死的只有两家：Visible+ 的脚注 5 直接定义 <span class='mono'>Premium data means no data "
              "slowdowns due to prioritization</span>，AT&T Prepaid Ultra 的卡片写 <span class='mono'>Data that can't "
              "slow down based on how much you use</span>。"
              "至于 Total MAX 那句被到处引用的「无降优先级」——我核到的实情是：它<b>只出现在官方竞品对比营销页</b>，"
              "两个实际售卖页一个字都没有，服务总条款还留着「全网前 0.5% 重度用户压到 1.5 Mbps」的兜底权。"
              "看到「Unlimited」四个字请直接跳过，去找降速条款的原文，并且注意那句话印在哪一页上。"),
    dict(tag="口径即定价", title="「税费另计」是完全合法的价格操纵，而且在便宜档位杀伤力最大",
         body="俄亥俄的政府税费是 23.59%，再加每线固定的运营商自收费（AT&T $4.99 / T-Mobile $4.49 / Verizon $3.99）。"
              "因为固定费不随价格缩放，<b>套餐越便宜，倍率越高</b>：$25 档要乘 1.41–1.45，$90 档只乘 1.28–1.29。"
              "结果就是 Mint Unlimited 标价 $30 看着比 Visible+ 的 $35 便宜 $5，"
              "换算成到手价却是 <b>$39 对 $35——反过来了</b>。"
              "你那份原表把这两个数字放进同一列排名，正好踩在这个陷阱上。"),
    dict(tag="自相残杀", title="Verizon 最大的对手是 Verizon",
         body="Visible 和 Total Wireless 都是 Verizon 全资，跑同一张网，都含 5G Ultra Wideband，都税费全包，$25–$35。"
              "而 Verizon 直营的 Simplicity 标价 $45（还得开 AutoPay），换算到手约 <b>$60</b>。"
              "为这 $25–$35 的差价，你买到的是后付费账户、实体店和大额购机补贴的<b>资格</b>——"
              "注意是资格，因为 Simplicity 本身<b>拿不到</b>那些免费 iPhone，那些促销一律要求 Unlimited Plus 或 Ultimate。"
              "所以 Simplicity 用户付了直营的价，却既没拿到子品牌的便宜，也没拿到旗舰套餐的补贴。"),
    dict(tag="锁三年", title="「免费 iPhone」的真实标价是你 36 个月的选择权",
         body="Verizon 现在的旗舰抵扣一律只认最贵的 Unlimited Ultimate。如果你本来只想要 Welcome，"
              "为拿机升到 Ultimate 是 +$30/月 × 36 = <b>$1,080</b>——iPhone Air、17 Pro、17 Pro Max 三台全部<b>倒亏约 $80</b>，"
              "Pixel 11 Pro 更是倒亏 $340（抵扣只有 $739.99 却和 iPhone Pro 一样强制 Ultimate）。"
              "而且每条优惠标题里都写着 New line req'd.——为拿机去开一条你用不到的线，那条线 36 个月要 $1,620 起。"
              "更狠的是退出成本：没有 ETF，但降档、离网、甚至<b>提前把手机分期一次性付清</b>，都会让剩余抵扣立即作废、欠款一次性到期。"
              "这不是买手机，是用三年的自由换一台机器。"),
    dict(tag="绕过价格锁", title="管理费是运营商绕开「价格锁」加价的正规通道",
         body="AT&T 的 Administrative & Regulatory Cost Recovery Fee 在八个月内涨了两次：2025-12 从 $3.49 到 $3.99，"
              "2026-08-05 再到 <b>$4.99</b>，累计 43%。T-Mobile 2026-01-21 从 $3.99 涨到 $4.49。"
              "Verizon 的两年涨了约 80%，而且官网<b>刻意不公布金额</b>（我抓了 verizon.com/support/surcharges，页面只解释用途、不给数字）。"
              "这些都不是税，是运营商自收的；它们<b>不受任何价格保证条款保护</b>。"
              "所以「5 年锁价」锁的是月费那一栏，附加费那一栏想涨随时涨。"),
    dict(tag="卖了网还在讲故事", title="Boost 把自己的 5G 网卖了，Metro 从来没公布过多线价目表",
         body="EchoStar 在 2025-08-26 把 3.45GHz + 600MHz 共 50MHz 全国频谱以约 230 亿美元卖给 AT&T，"
              "Boost 自有的 5G 无线接入网关停，全部用户在 2025-11-15 迁到 AT&T 网络。"
              "今天的 Boost 实质是跑 AT&T 的混合 MVNO——而且它并没有在做激进旗舰补贴，实抓其苹果列表页全部原价。"
              "Metro 这边则是另一种：我查了它 7 个官方页面，<b>找不到任何 2/3/5 线的每线价目表</b>，"
              "它那个「4 线 $100」就是把单线价 $25 原样复制四份，而且写明只能到店办。"
              "所谓多线优惠，在数字上并不比它的单线促销价更便宜。"),
    dict(tag="用词欺骗", title="Mint 的「family plan」不省一分钱，而且它自己承认",
         body="Mint 官方 FAQ 的原话是：<span class='mono'>although there aren't any discounts</span>。"
              "所谓 Modern Family Plan 只是把 2–5 条独立线放进同一个管理界面，价格分毫不动。"
              "同一类问题还有 US Mobile（官方直说没有多线折扣，但至少它把单线价降下来了，算诚实）、"
              "Spectrum（每线固定价，省钱全靠捆绑宽带）、和 Visible 基础版（纯线性，Inner Circle 只对中高档生效）。"
              "四家里只有 Mint 一边说没折扣、一边把功能叫做 family plan。"),
    dict(tag="被低估的档位", title="这次翻出来最值的两个档，原表一个都没有",
         body="其一是 <b>Cricket 12-Month Unlimited</b>：$300 一年、含税、AT&T 网络、"
              "Broadband Facts 明写这不是促销价。其二是 <b>AT&T Prepaid 12-Month Unlimited</b>：$240 一年（$20/月等效），"
              "16GB 高速后降 1.5 Mbps、含 10GB 热点。这两档都藏在官网的多月预付页面里，"
              "主套餐页不会展示，比价网站也基本不收录。代价都是同一个：钱不退、走人就作废。"
              "但如果你确定要在哥伦布待满一年，这是全表最划算的两个选项。"),
    dict(tag="查无实据", title="有三家连自己跑谁的网都不肯说",
         body="Cricket 官方点名 AT&T，Visible 和 Total Wireless 官方点名 Verizon——这三家可以当事实写。"
              "但 <b>Spectrum Mobile、US Mobile、Google Fi 三家官网全站不点名任何底层运营商</b>。"
              "Spectrum 的统一措辞是 America's most reliable 5G network；US Mobile 只给 Warp / Dark Star / Light Speed 三个代号；"
              "Google Fi 只说 an ultra-reliable 5G network。"
              "所以你在任何攻略里看到的「Spectrum = Verizon」「Warp = Verizon」，全部是第三方推断，"
              "而不是可以拿去跟客服讲道理的官方承诺。这不是文字游戏——它意味着<b>覆盖出问题时你没有依据</b>。"
              "US Mobile 更进一步：官方只对 Warp 用了 Priority Data 这个词，Dark Star 的优先级是<b>付费加购项</b>，"
              "Light Speed 只写 High Speed Data——「高速」是流量口径，不是优先级口径，这两件事经常被混为一谈。"),
    dict(tag="传闻辟谣", title="三条在中文攻略里流传、但这次核不出来的说法",
         body="① <b>Helium Mobile 的「$0 免费套餐」</b>：官网当前套餐区只有 Air $15/10GB 和 Infinity $30 无限两档，"
              "免费档本次完全查不到。② <b>Mobile X</b>：mobilex.com 已 301 跳转到 mobilexec.com——一家做 Outlook 日历软件的<b>企业软件公司</b>，"
              "TLS 证书 altnames 也只剩 www.mobilexec.com，备用域名是「Launching Soon」占位页。拿不到官方价格，不能进表。"
              "③ <b>「落地前在国内先激活 eSIM」</b>：至少两家已确证不成立——Verizon Prepaid 激活时会用定位验证你人在美国境内；"
              "Google Fi 条款明确禁止境外首次激活。其余品牌官网均未写明是否允许境外激活，属未明示，不能默认可以。"),
    dict(tag="年龄陷阱", title="Consumer Cellular 是这次最容易让人多花钱的一家",
         body="它那个到处被引用的「$35 无限量」<b>仅限 50 岁以上并需年龄验证</b>。"
              "18–49 岁的无限量档是 <b>$60/月</b>，另加每月 $3.99 运营商合规费 + $0.88 USF + 每线 $10 开通费 + 税。"
              "也就是说同样的服务，年轻人要付将近两倍。任何把它列进「省钱清单」而不写年龄门槛的说法，都是有误导的。"
              "同类还有 AT&T 55+ 和 T-Mobile Essentials Choice 55——资格不符会被每线加收 $20/月。"),
    dict(tag="口径不一致", title="回到你那份表：它最大的问题不是错，是不公平",
         body="Verizon 填的 $45 是<b>含 AutoPay</b> 的价，T-Mobile 填的 $55 是<b>不含 AutoPay</b> 的 Broadband Facts 价，"
              "然后按数字排名——T-Mobile 垫底有相当一部分是这么来的。"
              "Cricket 填的 $40 是只存在一个月的首月价，$35 那个长期常在价反而被标成「促销价」，"
              "于是 Cricket 被压到第 8。US Mobile 的 $16.58 是年付摊算、只管第一年，却和别家的月付促销并列。"
              "这些单看每一条都有注释说明，但排名表只吃数字不吃注释——<b>注释救不了排序</b>。"),
]

# ── 落选名单 ──────────────────────────────────────────────────────────
CUTLIST = [
    dict(name="Spectrum Mobile",
         why="硬性要求你同时是 Spectrum 宽带客户（官方 FAQ 直接问答确认），否则每线加 $10。"
             "手机侧<b>零多线折扣</b>，$30/$40/$50 每线固定。所谓省钱完全来自「第 1 条无限线免费 1 年」这个捆绑补贴。"
             "把宽带算进去，4 线 36 个月是手机 $3,960 + 宽带约 $2,160 ≈ <b>$6,120</b>。"
             "只有「本来就要装 Spectrum 宽带」的人才成立；为了这个手机价去买宽带是倒因为果。"
             "另外它的购机促销是本组最深的坑：36 个月账单返还 + 必须以旧换新 + 必须一直留着宽带，"
             "官网原文 Disconnecting service or upgrading early forfeits remaining credits。"),
]

CUTLIST += [
    dict(name="Boost Mobile —— 值得知道，但已不是你以为的那家",
         why="<b>$25/月（AutoPay）拿 30GB 优质数据，官网写「$25/mo Forever」</b>，新客 $10/月 × 3 个月是本轮最低的短期入口价。"
             "税费另计。哥伦布门店密度很高（本次抓到 14 处以上，含离 OSU 较近的 1168 E Weber Rd、1300 Bethel Rd、3250 S High St），"
             "但多为授权代理点，政策执行可能不统一。"
             "<b>最重要的更正：Boost 已经没有自建网络了。</b>EchoStar 2025-08-26 把 3.45GHz + 600MHz 共 50MHz 全国频谱"
             "以约 230 亿美元卖给 AT&T，Boost 自有 5G 无线接入网关停，全部用户 2025-11-15 迁到 AT&T 网络，"
             "只保留自己的云原生 5G 核心网，T-Mobile 作为次级/漫游层。没进主表是因为它在 $25 档相对 Cricket（同为 AT&T 网、且税费全含）没有优势。"),
    dict(name="Tello —— 小流量真空的答案",
         why="主表最低档基本是 $25 起的无限量，但如果你主要靠校园和公寓 Wi-Fi，那些流量根本用不到。"
             "Tello 跑 T-Mobile 网：<b>2GB $10 / 10GB $15 / 20GB $20</b>，未用完的流量还能结转，"
             "每档都送 60+ 国家免费拨打 + 欧洲免费漫游（限时到 2026-09-30）。"
             "没进主表只是因为主表按「无限量单线」这条主线组织；如果你的真实用量在 10GB 以内，"
             "Tello 的 $15/10GB 会比主表任何一档都省。注意：它的无限量 $15×3 个月促销官网写着 8/24 截止。"),
    dict(name="Red Pocket —— 年付超低价 + 三网自选",
         why="年付 Essentials 3GB <b>首年 $80</b>（官网折算 $9.17/月），续费 $110/年；"
             "GSMA / GSMT / CDMA 三网可随时切换（CoverageGenius），这一点全表只有 US Mobile 有对标。"
             "适合「只要有个号、流量很少、又想压到最低」的场景。税费口径官网未写明，本次标为未找到。"),
    dict(name="TextNow —— 唯一的零月费选项",
         why="<b>$0/月</b>的全美 5G 通话短信 + 550MB，只付一次性 $3.99 SIM 费；往上 $18.99/月 20GB。"
             "作为落地过渡卡、备用卡、或长期只用来收验证码的第二号码，有不可替代性。"
             "没进主表是因为它不构成一个「主力号」的答案，但值得单独知道。"),
    dict(name="Lycamobile —— 打中国大陆的唯一确证选项",
         why="<b>这是本次核查里唯一一家把中国大陆写进套餐自带国际通话清单、且明确固话与手机都含的品牌。</b>"
             "法务清单里 China 位于 Include Landline &amp; Mobile 组（同组还有 Hong Kong、Macau、South Korea；"
             "Taiwan 与 Japan 只在 Landline Only 组）。如果「能直接拨打国内手机」是你的刚需，它的性价比结构和其它家完全不同。"
             "<b>但有三个硬伤</b>：① 促销价是全场最低（18GB 只要 $7.50/30 天），但官网明写 Promo Price for 6 Months，"
             "6 期后回到 $33，是 2–4 倍的价格悬崖；② 官网购买另收 <b>5% regulatory recovery fee</b>，不是税费全含，标价要再乘 1.05；"
             "③ 条款写明 SIM 与号码在<b>停用 60 天后作废</b>——回国过暑假不续费，号码会被回收，绑在这个号上的银行、学校、Zelle 验证短信全部失效。"),
    dict(name="Ultra Mobile —— 只在四线时有意义",
         why="单线不划算，真正的点是 <b>4 条无限量线共 $100/月</b>，且每档都含 90+ 国家无限拨打。与主表内 Mint 同集团。"
             "单人选卡用不上，列在这里是为了在你将来要和室友拼卡时有个对照。"),
    dict(name="Xfinity Mobile —— 在哥伦布可用性存疑，且你多半没资格",
         why="Mobile Select $30/月、新客首年 $0，两档都含 215+ 国家的无限通话短信数据，看着很好。"
             "但<b>硬前提是必须先有 Xfinity 家庭宽带</b>——它不是独立可办的手机业务，是宽带会员的附属权益。"
             "住宿舍、住包网公寓、或短租一年不打算自己装宽带的话，实际上没有资格。"
             "另外哥伦布可用性也存疑：官网确有 /local/oh/columbus 页且可下单，但同页 Ohio 城市清单其余几乎全在俄亥俄东部"
             "（Steubenville、Youngstown 等），必须按具体门牌地址查，不能默认可装。"),
    dict(name="Straight Talk / Tracfone —— 全面被主表压制",
         why="Straight Talk 同跑 Verizon，无限量 $45 + 税，而主表内 Visible 已是 $25 且税费全含，全面劣势。"
             "Tracfone 同属 Verizon 体系，$30 换 10GB（Tello 同量只要 $15）、$50 无限量（Boost $25），全线无优势。"
             "Tracfone 唯一值得提的是 $125 管 365 天的备用机场景。"),
    dict(name="Gen Mobile / Helium Mobile —— 各有一个小理由，都不够强",
         why="Gen Mobile：12 个月预付 8GB $16/月锁价，但每一档都被 Tello 压住，只有「锁一年不涨价」有差异化。"
             "Helium Mobile：官网当前只有 Air $15/10GB 与 Infinity $30 无限两档——"
             "<b>中文攻略里流传的「$0 免费套餐」本次在官网套餐区完全查不到</b>，如果你在别处看到过，请以官网为准。"),
    dict(name="Consumer Cellular —— 有年龄门槛，不要被 $35 骗了",
         why="它的 <b>$35 无限量仅限 50 岁以上且需年龄验证</b>；18–49 岁的无限量档是 <b>$60/月</b>，"
             "另加每月 $3.99 运营商合规费 + $0.88 USF + 每线 $10 开通费 + 税。任何把它列进「省钱清单」而不写年龄门槛的说法都是有误导的。"),
    dict(name="Mobile X —— 官网已经不存在了",
         why="mobilex.com 已 <b>301 跳转到 mobilexec.com</b>（Mobile Executive，一家做 Outlook 日历软件和 HCL BigFix 的企业软件公司），"
             "TLS 证书 altnames 也只剩 www.mobilexec.com；备用域名 mobilexglobal.com 是「Launching Soon」占位页。"
             "在拿不到任何官方价格的前提下不能进表，也不该出现在任何 2026 年的推荐清单里。"),
]

CUTLIST_EXTRA = True
AUDIT = [
    # ── 口径类（我通读表格本身即可判定，不需联网） ──
    dict(title="AutoPay 口径两套标准，直接扭曲了排名", verdict="有误导", severity="高",
         was="Verizon Simplicity 填 $45（表内自注：不用 AutoPay 是 $55）；T-Mobile Essentials Saver 填 $55（表内自注：未含 AutoPay）。然后按数字 1–10 排名。",
         now="一家按折后算、一家按折前算。T-Mobile 的 AutoPay 价是 $50，与 Verizon 的 $45 只差 $5，"
             "而不是表面上的 $10。T-Mobile 被排到第 10 名，有相当一部分是这个口径造成的。",
         why="本页统一按「愿意开 AutoPay」计算——这是绝大多数人的实际情况；不开 AutoPay 的牌价单列在每个套餐的详情里。"),
    dict(title="含税价与不含税价直接比大小", verdict="有误导", severity="高",
         was="排名按价格数字排，但 Visible / Total / US Mobile / Spectrum / Cricket 是税费已含，Verizon / Mint / Google Fi / AT&T / T-Mobile 是税费另计。",
         now="俄亥俄的政府税费是 23.59%，再加每线固定的运营商自收费。在 $25–$30 这个档位，倍率高达 1.38–1.40。"
             "所以「$30 另计」和「$30 已含」根本不是同一个价位——前者到手约 $41–$42。",
         why="典型翻转：Mint Unlimited $30 看着比 Visible+ $35 便宜，到手价却是 $39 对 $35，反了。"),
    dict(title="Cricket 的常规价与促销价填反了", verdict="错误", severity="高",
         was="Cricket Select Unlimited：常规价 40 / 促销价 35。",
         now="联网复核确认：$35 才是长期常在的 AutoPay 价，$40 只存在第一个月（$5 AutoPay credit 自第 2 个月起生效）。"
             "把只存在一个月的首月价当常规价，系统性高估了 Cricket，把它压到第 8 名。",
         why="同一个错误方向在整张表里只出现在 Cricket 身上，别家用的都是长期价。"),
    # ── 联网复核查出的实质错误 ──
    dict(title="Spectrum：没有宽带根本开不了，不是「多付 $10 就能买」", verdict="有误导", severity="高",
         was="Spectrum Mobile Unlimited $30/线，需 Spectrum Internet，否则每线 +$10。排名第 5。",
         now="官网开户区块原文：Spectrum Internet is required for new Mobile service.——没有宽带<b>根本无法开通</b>，"
             "不存在「多付 $10 就能买」的选项。那个 $10 是<b>事后违约性加价</b>：条款写的是你把宽带断掉之后，"
             "才会被加收 $10.00 per-month per-line。另外 $30 是「每条附加线」的价格，官网同时写着第 1 条 Unlimited 线首年免费，表里也没写。",
         why="对住宿舍、短租、不会单独装 Spectrum 宽带的人，这一档实际上是拿不到的，却被排进了十家对比的第 5 名。"),
    dict(title="Spectrum：30GB 后的降速数字张冠李戴", verdict="错误", severity="中",
         was="30GB 后降至 1 Mbps 下载 / 512 Kbps 上传，并降低数据优先级。",
         now="官方宽带披露对住宅版 Unlimited 的原文是<b>纯降优先级、不给任何固定速率数字</b>："
             "After a line uses 30 GB of data it may experience speeds slower than other customers due to data prioritization。"
             "表里那组 1 Mbps / 512 Kbps 出自完全不相干的条款——Business Unlimited Plus 的<b>国际漫游</b>超 10GB 之后。",
         why="体感差别很大：降优先级只在基站拥堵时慢，不拥堵仍是全速；而不是被硬锁在 1 Mbps。"),
    dict(title="T-Mobile：整份表没出现学生档", verdict="有误导", severity="高",
         was="T-Mobile 代表档为 Essentials Saver 2.0，$55，排名第 10（最后一名）。",
         now="$55 这个数字本身准确，但官网<b>同一页</b>的 Broadband Facts 列表里就有 Essentials Saver Student 2.0："
             "1 线 $35 / 2 线 $70，AutoPay 后 $30。配置同级，却便宜 $20/月（一年 $240）。",
         why="只报 $55 会让人直接把 T-Mobile 判为最贵而排除掉。学生档需在 45 天内完成学籍验证并按要求复验。"),
    dict(title="Total Wireless：现在有更低的 $20/月在售", verdict="过时", severity="中",
         was="Total MAX 5G BYO $25，促销价栏留空。",
         now="官网当前横幅：Bring your phone for $20/mo ... First month $30, then $20/mo after。"
             "按 $25 做预算会比实际每月多算 $5（一年 $60）。",
         why="另外要补两个条件：首月是 $30（AutoPay 折扣次月才生效），且 $5 AutoPay 折扣是"
             "<b>每账户一个</b>（one per account），拼卡时不能按每人减 $5 算。"),
    dict(title="Total Wireless：有条件价占了「无条件常规价」的位置", verdict="有误导", severity="中",
         was="常规价填 $25，促销价栏留空，注释里才说明需 BYO + AutoPay。",
         now="官网<b>只印 AutoPay 价</b>，非 AutoPay 牌价本次遍查未获。所以严格说这一栏无法核实为「常规价」。"
             "同时它要求 BYO <b>和</b> AutoPay 两个条件同时成立。",
         why="排名表只吃数字不吃注释——注释救不了排序。"),
    dict(title="核对日期写成了未来时间", verdict="错误", severity="中",
         was="「结论与排序」页：已于 2026-08-15 按当时可访问的官方页面联网核对。",
         now="今天是 2026-08-14（美东）。声称的核对日期比当前日期晚一天，这个核对不可能已经发生。",
         why="价格新鲜度的承诺是选卡决策的前提，日期写错会让人误以为数据比实际更新。"),
    dict(title="多处「热点无限」漏掉了限速上限", verdict="有误导", severity="中",
         was="Visible+「手机热点无限」；Total MAX「热点无限」；T-Mobile「手机热点无限」。",
         now="三个都是「无限量但锁速」：Visible+ 全程锁 10 Mbps（基础版 5、Pro 15，且限 1 台设备）；"
             "Total MAX 锁 5 Mbps（ALL ACCESS 10 Mbps）；T-Mobile Essentials 全程 3G，"
             "Open Internet 政策给出的数字是最高 600 kbps。",
         why="「无限热点」和「能当宽带用」是两回事。600 kbps 基本只够收邮件。"),
    dict(title="T-Mobile「50GB premium data」抄了卖点没抄脚注", verdict="有误导", severity="高",
         was="Essentials Saver 2.0：50GB premium data。",
         now="官方套餐卡确实写 50GB of premium data，但它挂的<b>脚注 1</b> 原文是："
             "<span class='mono'>Essentials 2.0 customers may notice speeds lower than other customers and further "
             "reduction if using &gt;50GB/month, due to data prioritization.</span>"
             "——也就是<b>没超 50GB 就已经可能比其他 T-Mobile 用户慢</b>，超过 50GB 是「再降一档」。"
             "T-Mobile 自己在同页 FAQ 对 Premium Data 的定义也只承诺「高于重度用户」，不承诺「与高价套餐同级」。",
         why="这和 Visible+ 那种「premium data = 不因优先级降速」不是同一个东西，不能并列比较。"),
    dict(title="Total MAX 的「无降优先级」表述过于绝对", verdict="有误导", severity="中",
         was="Total MAX 5G BYO：无降优先级。（原表注释：官方 BYOP 页面称该 BYO 行无网络降优先级或限速）",
         now="这句话的官方依据只有两处，<b>都不是售卖页的法务承诺</b>：① totalwireless.com/facts 竞品对比表，"
             "该页自带免责 <span class='mono'>Chart does not depict an exhaustive list… Data verified as of 5/13/2026</span>；"
             "② Verizon 新闻稿的 won't slow you down。而 /plans/ 与 /m/plans/smartphone 两个实际售卖页<b>完全没有</b>"
             "deprioritization / premium data 字样；服务总条款则明确保留兜底权：跑进全网前 0.5% 会被压到 1.5 Mbps，"
             "且 certain Plans 内不同流量可被区别优先级。",
         why="建议的准确写法是「官方营销页称不降优先级（对比数据核验日 2026-05-13）；条款保留对全网前 0.5% 重度用户降至 1.5 Mbps 的权利」。"),
    dict(title="三家品牌的底层网络归属，官方从未点名", verdict="有误导", severity="中",
         was="表中把 Spectrum Mobile 当作跑 Verizon、US Mobile 三网映射到三大、Google Fi 跑 T-Mobile，均作为事实陈述。",
         now="<b>Spectrum、US Mobile、Google Fi 三家官网全站不点名任何底层运营商。</b>"
             "Spectrum 的统一措辞是 America's most reliable 5G network；"
             "US Mobile 的 /networks 与 /plans 页从不出现 Verizon、AT&amp;T、T-Mobile 任何一个名字，只给 Warp / Dark Star / "
             "Light Speed 三个代号与能力描述；Google Fi 只说 an ultra-reliable 5G network。"
             "反过来，Cricket 官方点名 AT&amp;T、Visible 与 Total Wireless 官方点名 Verizon，这三家可以当事实写。",
         why="差别不是文字游戏：官方没点名，意味着覆盖出问题时你没有可援引的依据。"),
    dict(title="Cricket 的「200+ 国家」是可加购范围，不是套餐自带", verdict="有误导", severity="高",
         was="按 Cricket 营销信息，Select Unlimited 含拨打/短信至墨西哥和加拿大；Supreme 有更多国际功能。",
         now="原表这句本身没错，但漏了更重要的一层：Cricket 宣传的 200+ 国家指的是<b>可加购范围</b>，"
             "不是套餐自带、也不是不限量。基础套餐自动含的只有墨西哥和加拿大；打其它国家需按国家单买加装包，"
             "$10/月起，而且是 <span class='mono'>a set amount of calling minutes</span>——<b>有分钟上限</b>。"
             "更关键的是低价档被阉割：<b>Sensible 10GB 与 Select Unlimited 连国际短信都不可用</b>。",
         why="预算敏感的人若选这两档，等于完全放弃了国际功能。"),
    dict(title="Mint 这一行本次存在核实冲突", verdict="无法核实", severity="中",
         was="Mint Unlimited：常规 30 / 促销 15 / 税费另计 / 50GB 后拥堵时降优先级 / 热点 20GB / 480p。",
         now="两个审计 agent 结果不一致：价格审计成功抓到 mintmobile.com/plans 并<b>逐字引用</b>了促销条款与 3/6/12 个月价目网格；"
             "网络审计对同域名的两次尝试（WebFetch 与带完整浏览器 UA 的 curl）<b>均返回 HTTP 403</b>，help.mintmobile.com 域名解析失败。",
         why="所以本页对 Mint 的资费与促销按已核实处理，但<b>网络归属与 50GB 阈值标为未取得官网原文</b>。"
             "历史上 Mint 的无限档阈值曾是 35GB/40GB，口径变动频繁——下单前建议自己打开官网 fine print 页确认。"),
    # ── 虚惊一场：原表其实是对的 ──
    dict(title="US Mobile 的 $16.58 标注正确", verdict="正确", severity="低",
         was="月付 25；首年年付 199 即 16.58，续费 270 即 22.50。",
         now="没有被当成月付，标注方式与官网一致（官网卡片逐字：$16.58/mo First year $199, renews at $270）。"
             "$199÷12=16.58、$270÷12=22.50 均对。70GB 说法也出自官网 FAQ 原文。",
         why="但两处要补：热点 20GB 官网写的是 20 GB hotspot on Dark Star，<b>跟网络绑定</b>；"
             "以及「税费已包含」官网自身前后矛盾——卡片写 included，同页 FAQ 却写可能另收 $2 Service Fee 与 $1–$5/线 Recovery Fee。"),
    dict(title="Verizon 的 $30 确实标注了是转网价", verdict="正确", severity="低",
         was="常规 45（需 AutoPay+无纸化），无 AutoPay 基础价 55；促销 30（转网）。",
         now="三档价格与条件全部准确，官方 FAQ 逐条确认。$30 需要 $15 Switch &amp; Save（从竞对转入，要交当前账单）"
             "或 $15 Bring a Number（携号转入）。",
         why="表格没写的一层：<b>刚落地、没有可携旧号、也不是从合资格运营商转入的人拿不到这 $15，实付就是 $45</b>。"
             "另有一条可行路径——官方把「从 Verizon Prepaid 转到 Simplicity」也算作 Bring a Number。"),
    dict(title="AT&T 的 $35 不是拼算出来的", verdict="正确", severity="低",
         was="AT&T Build-A-Plan with Unlimited SD $35（表内注明：按 $15 基础 + $20 数据选项计算）。",
         now="$35 就是 AT&T 官方价目矩阵里 Unlimited SD 的<b>总价</b>，官方表格逐行：Unlimited SD | Unlimited | +$20/mo. | $35/mo.。"
             "完整矩阵：无热点 $35 / 5GB 热点 $40 / 25GB $50 / 50GB $55。AutoPay 亦确认：AutoPay is REQUIRED. There is NO AutoPay discount.",
         why="但三个关键的坑表格没写：<b>每账户限 1 条线</b>（室友拼卡完全用不了）；"
             "Unlimited SD 的视频被硬限在 SD 且标注 max 2 Mbps（5G）/ 1.5 Mbps（4G）；"
             "该产品线 NO promotional offers、NO switcher credits，且门店买不到。"),
    dict(title="Google Fi 的促销没有过期", verdict="正确", severity="低",
         was="促销 25（自带 Pixel 12 个月 5 折，9 月 10 日结束）。",
         now="今天 2026-08-14 仍在售，截止日 Sep 10 尚在未来。官网原文：Get 50% off for 12 months when you bring a Google Pixel phone. "
             "Join any unlimited plan ... Ends Sep 10.。$50 单线价、50GB 后 256 kbps、25GB 热点、税费另计，全部逐字吻合。",
         why="两项官网未写、无法确认：「热点 25GB 计入 50GB 总量」与「480p」——官网既未说明热点是否计入总额度，也未标注视频清晰度上限。"),
    dict(title="Mint 全部字段与官网一致", verdict="正确", severity="低",
         was="常规 30（12 个月预付）；促销 15（首个周期）；税费另计；50GB 后拥堵时降优先级；热点 20GB；480p。",
         now="逐字吻合官网促销条款与 3/6/12 个月价目网格。",
         why="要补的两点：$15 要<b>一次性预付整期</b>（12 个月 = $180 一次付清）且仅限新客；"
             "「480p」官网只写 Video streams in SD，没有给出具体分辨率数字。"),
    dict(title="Visible+ 的价格与税费口径完全正确", verdict="正确", severity="低",
         was="常规 35 / 促销 29（SAVE6 首年）/ 税费已包含 / 无限 premium 数据 / 1080p。",
         now="官网套餐卡逐字：Best value Visible+ $29/mo Taxes &amp; fees included Reg. $35/mo Use code SAVE6。",
         why="一处表述不完整：<b>1080p 只在 5G Ultra Wideband 覆盖下成立</b>，脚注写明 5G/LTE 下只有 720p。"
             "另外同页还有并存的 SUMMER 码——Visible+ 用 SAVE6 更划算（$29 vs $30），"
             "但 Visible+ Pro 用 SUMMER（$35）比 SAVE6（$39）一年省 $48，结账时两个码都值得试。"),
    dict(title="T-Mobile 的 $55 数字与口径本身都对", verdict="正确", severity="低",
         was="$55（Broadband Facts，未含 AutoPay）；税费另计；50GB premium data；热点无限但 3G 速度；SD 视频。",
         now="官方 Broadband Facts 逐字确认，并给了税费明细：Regulatory programs / Telco recovery fee $4.49/线，"
             "联邦与地方附加费典型 $0.36–$4.79/线，另有一次性 Device connection charge $35/线。",
         why="问题不在这个数字准不准，而在它和表里别家的口径不一致（见本节第一条）。"),
]
