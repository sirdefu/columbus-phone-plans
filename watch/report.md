# 资费变更检测 · 2026-09-28 20:02 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Total Wireless — `total`

盯的是：MAX 5G BYO $25/$20、四档价、5 年锁价  
<https://www.totalwireless.com/m/plans/smartphone>


**消失了 2 条：**
```diff
- $10 international calling credit 3
- …ions2 Roaming in 140+ countries, including Canada & Mexico1 $10 international calling credit3 included with ALL ACCESS
```

**新出现 2 条：**
```diff
+ $10 international calling credit 6
+ …ions3 Roaming in 140+ countries, including Canada & Mexico4 $10 international calling credit6 included with ALL ACCESS
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 2 条：**
```diff
- plan w/AutoPay; plus taxes/fees) & trade-in (e.g., Save $900: Pixel 7; $450: Pixel 4) required.
- …stop & balance on required finance agreement is due (e.g., $899.99 – Google Pixel 11 256GB).
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 3 条：**
```diff
- $143/yr value
- Monthly Regulatory Programs & Telco Recovery Fees totaling up to $2.10 per line, and federal and local surcharges apply.
- Regulatory Programs & Telco Recovery Fees totaling up to $4.49 per line, and federal and local surcharges apply.
```

**新出现 3 条：**
```diff
+ $12.49/mo.
+ Monthly Regulatory Programs & Telco Recovery Fees totaling up to $2.10 ($2.60 eff.
+ Regulatory Programs & Telco Recovery Fees totaling up to $4.49 ($5.49 eff.
```

### T-Mobile — `tmobile_switch`

盯的是：Essentials Saver $50 AutoPay 价、$35 设备接入费  
<https://www.t-mobile.com/switch/savings>


**消失了 1 条：**
```diff
- Monthly Regulatory Programs & Telco Recovery Fees totaling up to $3.99 per line, and federal and local surcharges apply.
```

**新出现 1 条：**
```diff
+ Monthly Regulatory Programs & Telco Recovery Fees totaling up to $4.49 ($5.49 eff.
```

### US Mobile — `usmobile`

盯的是：Starter/Flex/Premium 年付价、促销档期（预期 403）  
<https://www.usmobile.com/plans>


**消失了 1 条：**
```diff
- Unlimited from $17/mo when paid annually
```

**新出现 2 条：**
```diff
+ Plus, get a $10 prepaid Mastercard®!
+ Unlimited for less than $17/mo.
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Visible、Cricket、Cricket、Total Wireless、Metro、AT&T、AT&T、AT&T、AT&T、Verizon、Verizon、Google Fi


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
