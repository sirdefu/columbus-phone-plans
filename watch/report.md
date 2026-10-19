# 资费变更检测 · 2026-10-19 19:07 UTC

**7 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Visible — `visible`

盯的是：三档月费/年费、促销码、税费口径  
<https://www.visible.com/plans>


**新出现 9 条：**
```diff
+ Bring your phone and pay $75 upfront for your first 6 months of the Visible plan.
+ New members who bring their own device get the Visible plan for just $75 upfront for the first 6 months of service.
+ New members who bring their own device get the Visible plan for just $75 upfront for the first 6 months.
+ Standard rate ($25/mo for the Visible plan) applies starting month 7, with service renewing monthly.
+ Standard rate ($25/mo for the Visible plan) applies starting month 7, with se…
+ Standard service rates ($25/mo) apply starting month 7, with service renewing monthly.
+ …he first 6 months of service.&nbsp; Standard service rates ($25/mo) apply starting month 7, with service renewing monthly.…
+ …rs who bring their own device get the Visible plan for just $75 upfront for the first 6 months of service.&nbsp; Standard…
+ …rs who bring their own device get the Visible plan for just $75 upfront for the first 6 months.
```

### Metro — `metro`

盯的是：$25/$30/$35/$40/$60 档、税费全含声明  
<https://www.metrobyt-mobile.com/phone-plans>


**消失了 7 条：**
```diff
- 5G Home Internet for $45/mo.
- After your first month, pay $45/month when you sign up for AutoPay to receive a $5 monthly discount (or pay $50/month without AutoPay).
- Get 5G Home Internet for $45/month with AutoPay ($50 for your first month or without AutoPay).
- Get fast, reliable 5G Home Internet for just $45/mo.
- Metro customers adding 5G Home Internet to a new voice account can pay $50 the first month, then $45/mo.
- Pay $50 for your first month of service.
- You will need to purchase a gateway device for $4.99.
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**新出现 3 条：**
```diff
+ Get yours and save $1000 when you switch to T-Mobile and bring your number, or trade in an eligible device in any condition , on an Experience Beyond plan.
+ If you cancel entire account before receiving all bill credits, credits stop and balance on required finance agreement is due (e.g., $1,999.99 – Apple iPhone Duo 256GB).
+ Yours for $1000 off.​ No trade-in needed.
```

### T-Mobile — `tmobile_switch`

盯的是：Essentials Saver $50 AutoPay 价、$35 设备接入费  
<https://www.t-mobile.com/switch/savings>


**消失了 1 条：**
```diff
- Included with Experience Beyond plans or $10/mo.; auto renews monthly.
```

**新出现 7 条：**
```diff
+ $11.99/mo value
+ $12.49/mo.
+ - an annual savings of $143.
+ Apple TV for just $3/mo.
+ Get Apple TV for just $3/mo.
+ Included with Experience Beyond or $10/mo.; auto renews monthly.
+ Receive Apple TV discount (up to $11.99/mo.
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 2 条：**
```diff
- Save $20.98/mo
- Save $44.99/mo
```

**新出现 2 条：**
```diff
+ Get $10/mo off for 6 mos.
+ bills at $10/mo unless perk is canceled or unregistered.
```

### Verizon — `verizon_pre`

盯的是：预付费各档与忠诚度折扣  
<https://www.verizon.com/plans/prepaid/>


**新出现 1 条：**
```diff
+ You can choose prepaid plans starting at $35/mo with Auto Pay, and you'll get a 3-year price guarantee for your base monthly rate on every Verizon Prepaid phone plan.
```

### US Mobile — `usmobile`

盯的是：Starter/Flex/Premium 年付价、促销档期（预期 403）  
<https://www.usmobile.com/plans>


**消失了 7 条：**
```diff
- $16.58 /mo
- $17.50 /mo
- $210 per year
- $24.92 /mo
- First year $199, renews at $270
- First year $299, renews at $390
- Unlimited for less than $17/mo.
```

**新出现 6 条：**
```diff
+ $10 /mo
+ $10 monthly Starter w/ code
+ $20 /mo
+ $20 monthly Premium w/ code
+ Renews at $25/mo.
+ Renews at $44/mo.
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（10 个）

Cricket、Cricket、Total Wireless、Total Wireless、T-Mobile、AT&T、AT&T、AT&T、AT&T、Google Fi


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
