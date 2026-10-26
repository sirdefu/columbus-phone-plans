# 资费变更检测 · 2026-10-26 19:04 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Total Wireless — `total`

盯的是：MAX 5G BYO $25/$20、四档价、5 年锁价  
<https://www.totalwireless.com/m/plans/smartphone>


**新出现 1 条：**
```diff
+ Disney+ Basic (With Ads) is currently $12.49/month tax and Disney Premium (No Ads) is currently $21.49/month tax.
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 1 条：**
```diff
- Get up to $1000 off an iPhone 18 Pro Max when you add a new line and bring your number on an Experience Beyond plan with Student Savings 2.0.
```

**新出现 1 条：**
```diff
+ Get up to $800 off an iPhone 18 Pro Max when you add a new line and bring your number on an Experience Beyond plan with Student Savings 2.0.
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 3 条：**
```diff
- $31.98/mo
- $35.95/mo
- Save $10.95/mo
```

**新出现 4 条：**
```diff
+ $23/mo
+ $34.98/mo
+ $37.95/mo
+ Save $12.95/mo
```

### Verizon — `verizon_pre`

盯的是：预付费各档与忠诚度折扣  
<https://www.verizon.com/plans/prepaid/>


**消失了 1 条：**
```diff
- You can choose prepaid plans starting at $35/mo with Auto Pay, and you'll get a 3-year price guarantee for your base monthly rate on every Verizon Prepaid phone plan.
```

**新出现 14 条：**
```diff
+ 15 GB plan : The 15 GB plan costs $45/month, or $35/month with Auto Pay after the first month.
+ Add an additional Unlimited Plus phone line for $40/month with the multiline discount.
+ Add an additional Unlimited phone line for $30/month with the multiline discount.
+ Auto Pay discount : Enroll in Auto Pay with a credit or debit card to save $10/month on eligible prepaid phone plans priced at $45 or more.
+ If you don't use a lot of data, the Verizon Prepaid 15 GB plan at $35 per month with Auto Pay would be a good choice.
+ Loyalty discount : Eligible prepaid phone plans priced at $45 or more can receive a $5/month loyalty discount after thre…
+ Multiline discount : Add additional Verizon Prepaid Unlimited phone lines to your account and save $20/month per line.
+ So you could get two additional Unlimited phone lines for $40/month each before the Auto Pay discount.
+ The Talk & Text plan is eligible for a $5/month Auto Pay discount.
+ Unlimited Plus plan : The Unlimited Plus plan costs $70 for the first month and $60/month with Auto Pay.
+ Unlimited plan : The Unlimited plan costs $60 for the first month and $50/month with Auto Pay.
+ …ble prepaid phone plans priced at $45 or more can receive a $5/month loyalty discount after three months of service and an…
+ …ditional $5/month after nine months, for a total savings of $10/month.
+ …ty discount after three months of service and an additional $5/month after nine months, for a total savings of $10/month.
```

### US Mobile — `usmobile`

盯的是：Starter/Flex/Premium 年付价、促销档期（预期 403）  
<https://www.usmobile.com/plans>


**消失了 4 条：**
```diff
- $10 /mo
- $10 monthly Starter w/ code
- $20 /mo
- $20 monthly Premium w/ code
```

**新出现 4 条：**
```diff
+ $15 /mo
+ $15 monthly Starter w/ code
+ $25 /mo
+ $25 monthly Premium w/ code
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Visible、Cricket、Cricket、Total Wireless、Metro、T-Mobile、T-Mobile、AT&T、AT&T、AT&T、AT&T、Google Fi


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
