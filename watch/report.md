# 资费变更检测 · 2026-09-21 18:32 UTC

**6 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Visible — `visible`

盯的是：三档月费/年费、促销码、税费口径  
<https://www.visible.com/plans>


**消失了 4 条：**
```diff
- $15/mo off Home Internet
- \r\n<li>Global Pass starting at $5/day</li>\r\n<li>$15/mo off&nbsp;<a style=\"text-decoration: underline;\" href=…
- \r\n<li>Global Pass starting at $5/day</li>\r\n<li>$15/mo off&nbsp;<a style=\"text-decoration:…
- …class=\"hidden-content\">super script 10</span></li>\r\n<li>$15/mo off&nbsp;<a style=\"text-decoration: underline;\" href=…
```

**新出现 2 条：**
```diff
+ \r\n<li>Global Pass starting at $5/day</li>\r\n<li>Free 2-day device shipping</li>\r\n</ul>\r\n"}}" id="text-386aee00f5" class="cmp-text" style="padding-top:;
+ \r\n<li>Global Pass starting at $5/day</li>\r\n<li>Free 2-day device shipping</li>\r\n</ul>\r\n"}}" id="text-cf6a10e8ef" class="cmp-text" style="padding-top:;
```

### Cricket — `cricket_multi`

盯的是：12 个月 $300 年付档是否还在  
<https://www.cricketwireless.com/cell-phone-plans/multi-month-unlimited>


**新出现 6 条：**
```diff
+ $45/mo.
+ $75 price includes Cricket Home Internet ($45/mo.
+ Auto Pay Credit: $5/mo credit requires enrollment in Auto Pay and will apply starting on second service charge.
+ Fees: $5 Customer Assistance Fee applies to rep-assisted and automated phone system payments.
+ Internet Gateway: Activation and use of Cricket Home Internet requires purchase of Cricket Internet Gateway for $49.99 + applicable sales tax.
+ after discounts), Cricket Sensible 10GB phone plan ($35/mo.), and $5 Auto Pay Credit.
```

### Metro — `metro`

盯的是：$25/$30/$35/$40/$60 档、税费全含声明  
<https://www.metrobyt-mobile.com/phone-plans>


**消失了 2 条：**
```diff
- Endless entertainment and fast, free shipping on over 100 million items with Prime, on our $60/mo.
- with AutoPay plan.​ That’s a $14.99/mo.
```

**新出现 6 条：**
```diff
+ $130
+ $55 UNL w/AutoPay-$60 Month
+ $55/mo.
+ $95
+ Unlimited $55/mo.
+ with AutoPay $60 for the first month.
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**新出现 5 条：**
```diff
+ Get iPhone 18 Pro Max for under $100
+ If you cancel entire account before receiving all bill credits, credits stop and balance on required finance agreement is due (e.g., $1,299.99 – iPhone 18 Pro Max 256GB).
+ Qualifying credit, add a new line, port-in (AT&T, Verizon, or another eligible carrier, see complete list at T-Mobile .com/port), & service ($100+/mo.
+ Up to $1200 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ plan w/AutoPay, plus taxes and fees) & trade-in (e.g., Save $1,200: iPhone 16; Save $930: iPhone 14; Save $500: iPhone 6) required.
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 1 条：**
```diff
- Verify student enrollment status for account holder within 45 days, maintain student line, & re-verify when requested; otherwise additional cost up to $20/line per month.
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 5 条：**
```diff
- $23/mo
- $34.98/mo
- $37.95/mo
- $39.97/mo
- Save $12.95/mo
```

**新出现 6 条：**
```diff
+ $31.98/mo
+ $35.95/mo
+ $41.97/mo
+ $47.98/mo
+ Save $10.95/mo
+ Save $22.98/mo
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（11 个）

Cricket、Total Wireless、Total Wireless、T-Mobile、AT&T、AT&T、AT&T、AT&T、Verizon、Google Fi、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
