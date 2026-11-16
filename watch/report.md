# 资费变更检测 · 2026-11-16 22:46 UTC

**8 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Visible — `visible`

盯的是：三档月费/年费、促销码、税费口径  
<https://www.visible.com/plans>


**消失了 1 条：**
```diff
- It’s like paying $38/mo.
```

**新出现 1 条：**
```diff
+ its like paying $18.75/mo.
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 4 条：**
```diff
- For MI lines $0.12 is applied to the RPF and $1.98 is applied to the TRF.
- Of the $4.49 total charge for voice lines, $0.50 is applied to the RPF and $3.99 is applied to the TRF.
- …('TRF') (not a government required tax or charge) totaling $4.49 for Voice Lines and $2.10 for Mobile Internet lines ('MI…
- …required tax or charge) totaling $4.49 for Voice Lines and $2.10 for Mobile Internet lines ('MI') (subject to change with…
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 1 条：**
```diff
- Verify student enrollment status for account holder within 45 days, maintain student line, & re-verify annually; otherwise additional cost up to $20/line per month.
```

**新出现 2 条：**
```diff
+ Verify student enrollment status for account holder within 45 days, maintain student line, & re-verify annually; otherwise additional cost up to $15/line per month.
+ …an will lose Student Savings at an additional cost of up to $15/line per month.
```

### AT&T — `att_prepaid`

盯的是：预付费 $240 年付 / $20 月等效 / Level Up  
<https://www.att.com/prepaid/>


**消失了 2 条：**
```diff
- Save $15/mo.
- for six months Our best plan for $45/mo.
```

**新出现 4 条：**
```diff
+ $ 45.00 /mo.
+ $ 60.00
+ Now $45.00.
+ Was $60.00.
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 2 条：**
```diff
- $30/mo
- Save $34.99/mo
```

**新出现 3 条：**
```diff
+ $35/mo
+ $37.95/mo
+ Save $29.99/mo
```

### Verizon — `verizon_pre`

盯的是：预付费各档与忠诚度折扣  
<https://www.verizon.com/plans/prepaid/>


**消失了 16 条：**
```diff
- $70 Prepaid Unlimited Plus smartphone plan
- 15 GB plan : The 15 GB plan costs $45/month, or $35/month with Auto Pay after the first month.
- Add an additional Unlimited Plus phone line for $40/month with the multiline discount.
- Add an additional Unlimited phone line for $30/month with the multiline discount.
- Auto Pay discount : Enroll in Auto Pay with a credit or debit card to save $10/month on eligible prepaid phone plans priced at $45 or more.
- Global Choice for our $70 Unlimited Plus Prepaid Plan.
- If you don't use a lot of data, the Verizon Prepaid 15 GB plan at $35 per month with Auto Pay would be a good choice.
- Loyalty discount : Eligible prepaid phone plans priced at $45 or more can receive a $5/month loyalty discount after thre…
- Multiline discount : Add additional Verizon Prepaid Unlimited phone lines to your account and save $20/month per line.
- So you could get two additional Unlimited phone lines for $40/month each before the Auto Pay discount.
- The Talk & Text plan is eligible for a $5/month Auto Pay discount.
- Unlimited Plus plan : The Unlimited Plus plan costs $70 for the first month and $60/month with Auto Pay.
- Unlimited plan : The Unlimited plan costs $60 for the first month and $50/month with Auto Pay.
- …ble prepaid phone plans priced at $45 or more can receive a $5/month loyalty discount after three months of service and an…
- …ditional $5/month after nine months, for a total savings of $10/month.
- …ty discount after three months of service and an additional $5/month after nine months, for a total savings of $10/month.
```

**新出现 1 条：**
```diff
+ Global Choice to get unlimited calls to one country/month and discounted rates to 220+ countries (included in our $65 Unlimited Plus smartphone plan)
```

### Google Fi — `googlefi`

盯的是：三档无限 + 自带 Pixel 五折促销截止日  
<https://fi.google.com/about/plans>


**新出现 8 条：**
```diff
+ $12
+ $13
+ $14
+ $15
+ $57
+ $63
+ $68
+ $75
```

### US Mobile — `usmobile`

盯的是：Starter/Flex/Premium 年付价、促销档期（预期 403）  
<https://www.usmobile.com/plans>


**消失了 6 条：**
```diff
- $15 monthly Starter
- $25 $15 /mo
- $25 monthly Premium
- $44 $25 /mo
- Renews at $25/mo after 6 mos.
- Renews at $44/mo after 6 mos.
```

**新出现 7 条：**
```diff
+ $17.50 /mo
+ $210 per year
+ $22.50 $16.58 /mo
+ $32.50 $24.92 /mo
+ First year $199, renews at $270
+ First year $299, renews at $390
+ Unlimited less than $17/mo.
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（9 个）

Cricket、Cricket、Total Wireless、Total Wireless、Metro、T-Mobile、AT&T、AT&T、AT&T


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
