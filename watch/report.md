# 资费变更检测 · 2026-11-24 00:37 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Cricket — `cricket_multi`

盯的是：12 个月 $300 年付档是否还在  
<https://www.cricketwireless.com/cell-phone-plans/multi-month-unlimited>


**新出现 4 条：**
```diff
+ Must bring your number to Cricket on a new line on the Supreme Unlimited Plan ($55/mo.
+ Pay first three months of $60/mo.
+ after $5 Auto Pay credit starting second month).
+ iPhone 16e on us or iPhone 17e $99.99
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 1 条：**
```diff
- Watch & tablet lines just $5/month
```

**新出现 1 条：**
```diff
+ $10 per line discount with AutoPay enabled & eligible payment method
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 1 条：**
```diff
- Watch & tablet lines just $5/month
```

**新出现 1 条：**
```diff
+ $10 per line discount with AutoPay enabled & eligible payment method
```

### AT&T — `att_prepaid`

盯的是：预付费 $240 年付 / $20 月等效 / Level Up  
<https://www.att.com/prepaid/>


**消失了 4 条：**
```diff
- $ 45.00 /mo.
- $ 60.00
- Now $45.00.
- Was $60.00.
```

**新出现 3 条：**
```diff
+ Limited time offer Get the latest phones—with a $1 initial payment
+ Save $15/mo.
+ for six months Our best plan for $45/mo.
```

### Google Fi — `googlefi`

盯的是：三档无限 + 自带 Pixel 五折促销截止日  
<https://fi.google.com/about/plans>


**消失了 1 条：**
```diff
- …monthly YouTube Premium subscription at the current rate of $15.99/month (rate subject to change) and the monthly charge w…
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Visible、Cricket、Total Wireless、Total Wireless、Metro、T-Mobile、AT&T、AT&T、AT&T、Verizon、Verizon、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
