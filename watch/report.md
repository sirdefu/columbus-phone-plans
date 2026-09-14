# 资费变更检测 · 2026-09-14 18:25 UTC

**5 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Visible — `visible`

盯的是：三档月费/年费、促销码、税费口径  
<https://www.visible.com/plans>


**消失了 1 条：**
```diff
- Save $15 a month on Verizon Home Internet, when you bundle it with any Visible phone plan ( offer details ).
```

### Cricket — `cricket_multi`

盯的是：12 个月 $300 年付档是否还在  
<https://www.cricketwireless.com/cell-phone-plans/multi-month-unlimited>


**消失了 1 条：**
```diff
- Pay in advance and save $300
```

**新出现 1 条：**
```diff
+ Pay in advance and save $300 with a 12 month Multi-Month Unlimited Plan from Cricket Wireless
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 9 条：**
```diff
- If you cancel entire account before receiving all bill credits, credits stop and balance on required finance agreement is due (e.g., $829.99 – iPhone 17 256GB).
- Qualifying credit, port-in (AT&T, Verizon, or another eligible carrier, see complete list at T-Mobile .com/port), and new voice line ($85+/mo.
- Up to $1,100 via 24 or 36 monthly bill credits, depending on finance…
- Up to $1,300 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
- Up to $315 via 24 or 36 monthly bill credits, depending on finance agreement term; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
- Up to $830 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
- plan w/AutoPay; plus taxes/fees) & trade-in (e.g., Save $1,300: Pixel 10/ Save $650: Pixel 5) required.
- …stop & balance on required finance agreement is due (e.g., $1,299.99 – Google Pixel 11 Pro XL 256 GB).
- …top and balance on required finance agreement is due (e.g., $1,099.99 – Apple iPhone 17 Pro 256 GB).
```

**新出现 15 条：**
```diff
+ $1,099.99 – Pixel 11 Pro 256 GB).
+ If you cancel entire account before receiving all bill credits, credits stop and balance on required finance agreement is due (e.g., $1,199.99 – Apple iPhone 18 Pro 256GB).
+ Qualifying credit & service ($60+/mo.
+ Qualifying credit, add a new line, and service ($60+/mo.
+ Qualifying credit, add a new line, port-in (AT&T, Verizon, or another eligible carrier, see complete list at T-Mobile .com/port), & service ($85+/mo.
+ Qualifying credit, add a new line, service ($100+/mo.
+ Up to $1,200 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ Up to $900 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ Up to $930 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ Up to 50% or up to $315 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ plan w/AutoPay, plus taxes & fees), & eligible trade-in (e.g., Save $1,200: iPhone 16; Save $930: iPhone 14; Save $500: iPhone 6) required.
+ plan w/AutoPay; plus taxes/fees) & trade-in (e.g., Save $1,100: Pixel 10/ Save $550: Pixel 5) required.
+ plan w/AutoPay; plus taxes/fees) & trade-in (e.g., Save $900: Pixel 7; $450: Pixel 4) required.
+ …stop & balance on required finance agreement is due (e.g., $1,099.99 – Google Pixel 11 Pro 256 GB).
+ …stop & balance on required finance agreement is due (e.g., $899.99 – Google Pixel 11 256GB).
```

### T-Mobile — `tmobile_switch`

盯的是：Essentials Saver $50 AutoPay 价、$35 设备接入费  
<https://www.t-mobile.com/switch/savings>


**消失了 4 条：**
```diff
- Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $599.99 – iPhone 17e 256GB).
- Get 2 lines for $90/mo.
- Qualifying credit and service ($45+/mo.
- Up to $630 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
```

**新出现 5 条：**
```diff
+ Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $699.99 – iPhone 17e 256GB).
+ For well-qualified customers; plus tax & $35 device connection charge.
+ Get 2 lines for $80/mo.
+ Qualifying credit, add a new line, service ($60+/mo.
+ Up to $700 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
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


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（12 个）

Cricket、Total Wireless、Total Wireless、Metro、T-Mobile、AT&T、AT&T、AT&T、AT&T、Verizon、Verizon、US Mobile


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
