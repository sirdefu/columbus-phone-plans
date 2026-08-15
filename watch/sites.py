# -*- coding: utf-8 -*-
"""被监控的官方页面清单。

只放**价格与条款所在的页面**。加站点时请同时填 note，说明这一页负责盯什么，
将来 diff 报告里会带上，方便判断变动重不重要。
"""

SITES = [
    # key,            品牌,             URL,                                                        这一页盯什么
    ("visible",       "Visible",        "https://www.visible.com/plans",                            "三档月费/年费、促销码、税费口径"),
    ("cricket",       "Cricket",        "https://www.cricketwireless.com/cell-phone-plans",         "四档无限 + Sensible、AutoPay 价"),
    ("cricket_multi", "Cricket",        "https://www.cricketwireless.com/cell-phone-plans/multi-month-unlimited", "12 个月 $300 年付档是否还在"),
    ("total",         "Total Wireless", "https://www.totalwireless.com/m/plans/smartphone",         "MAX 5G BYO $25/$20、四档价、5 年锁价"),
    ("total_byop",    "Total Wireless", "https://www.totalwireless.com/m/byop",                     "BYO 专属价与条件"),
    ("metro",         "Metro",          "https://www.metrobyt-mobile.com/phone-plans",              "$25/$30/$35/$40/$60 档、税费全含声明"),
    ("tmobile",       "T-Mobile",       "https://www.t-mobile.com/cell-phone-plans",                "Essentials/Experience 各档、$4.49 恢复费"),
    ("tmobile_stu",   "T-Mobile",       "https://www.t-mobile.com/cell-phone-plans/student-discounts", "学生档 $35/$30 是否仍在"),
    ("tmobile_switch","T-Mobile",       "https://www.t-mobile.com/switch/savings",                  "Essentials Saver $50 AutoPay 价、$35 设备接入费"),
    ("att",           "AT&T",           "https://www.att.com/plans/wireless/",                      "后付费头图价（分档价是客户端渲染的，抓不到，靠下面那条补）"),
    # att.com/plans/wireless/ 的分档价由 JS 渲染，静态抓取只能拿到营销语。
    # AT&T 自己发布的机器可读规格页反而是静态的、含完整价目矩阵，用它当主信号源。
    ("att_bap_spec",  "AT&T",           "https://www.att.com/ai-instructions/build-a-plan.html",    "Build-A-Plan 完整价目矩阵（$15 基础 + 各数据/热点档）"),
    ("att_bap",       "AT&T",           "https://www.att.com/plans/build-a-plan/",                  "Build-A-Plan 头图价"),
    # /prepaid/plans/ 抓不到价格文本，/prepaid/ 反而能拿到 $240 年付与 $20/mo 两个关键档
    ("att_prepaid",   "AT&T",           "https://www.att.com/prepaid/",                             "预付费 $240 年付 / $20 月等效 / Level Up"),
    ("verizon",       "Verizon",        "https://www.verizon.com/plans/unlimited/",                 "Simplicity $55/$45/$30"),
    ("verizon_pre",   "Verizon",        "https://www.verizon.com/plans/prepaid/",                   "预付费各档与忠诚度折扣"),
    ("googlefi",      "Google Fi",      "https://fi.google.com/about/plans",                        "三档无限 + 自带 Pixel 五折促销截止日"),
    # 以下两家有反爬，预期会 403。保留在清单里是**故意的**：
    # 它们从「403」变成「200」本身就是值得知道的信号，而且能防止我们默默忘掉这两家。
    ("mint",          "Mint Mobile",    "https://www.mintmobile.com/plans/",                        "四档 3/6/12 个月价、$15 促销（预期 403）"),
    ("usmobile",      "US Mobile",      "https://www.usmobile.com/plans",                           "Starter/Flex/Premium 年付价、促销档期（预期 403）"),
]
