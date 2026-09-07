# 资费变更检测 · 2026-09-07 18:09 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Metro — `metro`

盯的是：$25/$30/$35/$40/$60 档、税费全含声明  
<https://www.metrobyt-mobile.com/phone-plans>


**消失了 2 条：**
```diff
- With AutoPay and a Metro voice line (the first month is $50).
- You will need to purchase a gateway device for $9.99.
```

**新出现 2 条：**
```diff
+ Metro customers adding 5G Home Internet to a new voice account can pay $50 the first month, then $45/mo.
+ You will need to purchase a gateway device for $4.99.
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 5 条：**
```diff
- Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $309.99–moto g stylus 2026).
- Grab the new moto g stylus for under $10.
- Plus tax & $35 device connection charge.
- Save $300 when you activate a new line on most plans.
- Up to $300.99 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
```

**新出现 5 条：**
```diff
+ Qualifying credit, service ($85+/mo.
+ Save up to $800 when you trade-in an eligible device on an Experience More or Experience Beyond plan.
+ Up to $800 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ plan w/AutoPay; plus taxes/fees) and trade-in (e.g., Save: $800: Samsung Galaxy S24; Save $550: Samsung Galaxy A54) required.
+ …stop & balance on required finance agreement is due (e.g., $799.99–Samsung Galaxy S26 FE 256GB).
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**新出现 3 条：**
```diff
+ Get a $5 movie ticket every month–so you can catch the latest release without stretching your student budget.
+ Last year, T-Mobile offered over $900 in Tuesday savings with free stuff, weekly perks, and deals from brands students actually use, all in the T-Life app.
+ Take movie night off campus for only $5.
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

**新出现 3 条：**
```diff
+ $34.98/mo
+ $37.95/mo
+ Save $12.95/mo
```

### Verizon — `verizon_pre`

盯的是：预付费各档与忠诚度折扣  
<https://www.verizon.com/plans/prepaid/>


**消失了 2 条：**
```diff
- Verizon Prepaid + Home discount $15/mo savings on Verizon Fios Home Internet plan or Frontier Fiber Internet services when combined with any eligible Verizon Prepaid phone plan.
- save $15/mo on
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Visible、Cricket、Cricket、Total Wireless、Total Wireless、T-Mobile、AT&T、AT&T、AT&T、AT&T、Google Fi、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
