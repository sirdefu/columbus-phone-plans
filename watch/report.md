# 资费变更检测 · 2026-08-24 13:53 UTC

**2 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Total Wireless — `total_byop`

盯的是：BYO 专属价与条件  
<https://www.totalwireless.com/m/byop>


**消失了 1 条：**
```diff
- Bring your phone for $20/mo
```

**新出现 2 条：**
```diff
+ $20 /mo
+ First month $30.
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 7 条：**
```diff
- Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $599.99 – iPhone 17e 256GB).
- Get Apple TV for just $3/mo.
- Must have GOTO USB-C Wired Earbuds BLK, PG Liquid Glass w/ $300 warranty, and Nimble Champ 10K battery in cart to receive discount.
- Plus tax & $35 device connection charge.
- Qualifying credit and service ($60+/mo.
- Save $70 on the college bundle.
- Up to $630 via 24 or 36 monthly bill credits, depending on finance agreement term; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
```

**新出现 5 条：**
```diff
+ $143/yr value
+ Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $1,099.99– Galaxy S26+ 256GB).
+ For well-qualified customers; plus tax & $35 device connection charge.
+ Qualifying credit and service ($85+/mo.
+ Up to $1,100 via bill credits, depending on finance agreement term; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（15 个）

Visible、Cricket、Cricket、Total Wireless、Metro、T-Mobile、T-Mobile、AT&T、AT&T、AT&T、AT&T、Verizon、Verizon、Google Fi、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
