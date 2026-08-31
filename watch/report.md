# 资费变更检测 · 2026-08-31 19:25 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Total Wireless — `total`

盯的是：MAX 5G BYO $25/$20、四档价、5 年锁价  
<https://www.totalwireless.com/m/plans/smartphone>


**消失了 1 条：**
```diff
- Bring your phone for $20/mo
```

### Metro — `metro`

盯的是：$25/$30/$35/$40/$60 档、税费全含声明  
<https://www.metrobyt-mobile.com/phone-plans>


**消失了 1 条：**
```diff
- You will need to purchase a gateway device for $49.99.
```

**新出现 3 条：**
```diff
+ Metro by T-Mobile 's most affordable phone plan starts at $25/month with
+ Metro offers plans starting at $25/month with AutoPay , with taxes and fees included when you…
+ You will need to purchase a gateway device for $9.99.
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 2 条：**
```diff
- Yes, you can save $20/month on 5G Home Internet
- when bundling with a Student Perks Savings voice plan — that’s $5/month more than T-Mobile ’s standard bundle discount — with the monthly price for internet locked for five years.
```

**新出现 4 条：**
```diff
+ Verify student enrollment status for account holder within 45 days, maintain student line, & re-verify annually; otherwise additional cost up to $20/line per month.
+ Yes, you can save $20/month on 5G Home Internet when bundling with a Student Per…
+ …et when bundling with a Student Perks Savings plan — that’s $5/month more than T-Mobile ’s standard bundle discount — with…
+ …without the Student Savings discount costing an additional $20/month/line.
```

### AT&T — `att_prepaid`

盯的是：预付费 $240 年付 / $20 月等效 / Level Up  
<https://www.att.com/prepaid/>


**消失了 2 条：**
```diff
- Pay $240 today, get a year of unlimited talk, text, and data.
- Save all year Get 12 months of unlimited for $20/mo.
```

**新出现 5 条：**
```diff
+ After 6 months, plan is $60/mo.
+ Get 12 months of unlimited for $20/mo.
+ Pay $240 today for a year of unlimited talk, text, and data.
+ Save $15/mo.
+ for 6 months Our best plan for $45/mo.
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 1 条：**
```diff
- $16.97/mo
```

**新出现 10 条：**
```diff
+ $6.98/mo perk savings based on the current $8.99/mo for
+ $9.99/mo perk savings based on the
+ $9.99/mo perk savings based on the current $19.99/mo that Disney+, Hulu, ESPN+ (With Ads) Subscribers pay for the bundle less the cost of the Disney perk added to Simplicity Plan.
+ Discounted calls to an additional 160+ countries from $0.05/min.
+ Netflix Standard with ads and $10.99/mo for HBO Max Basic with Ads plan less $13/mo perk added to
+ Premium Video Streaming available for $10/mo+ taxes per capable device enrolled.
+ Premium Video Streaming available for $10/mo+taxes & fees (where applicable) per capable device enrolled.
+ Save $16.97/mo
+ Unlimited Hotspot available for $15/mo per line + taxes & fees (where applicable) per device enrolled.
+ current $19.99/mo that Disney+, Hulu, ESPN+ (With Ads) Subscribers pay for the bundle less the $10/mo
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Visible、Cricket、Cricket、Total Wireless、T-Mobile、T-Mobile、AT&T、AT&T、AT&T、Verizon、Google Fi、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
