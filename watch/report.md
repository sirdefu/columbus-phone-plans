# 资费变更检测 · 2026-11-09 22:54 UTC

**9 个页面的价格文本发生变化。** 下面是逐条 diff——先自己扫一眼判断是不是实质变动（很多是营销文案微调），确认重要再让 Claude 重跑完整分析并更新页面。


## 发生变化

### Visible — `visible`

盯的是：三档月费/年费、促销码、税费口径  
<https://www.visible.com/plans>


**消失了 1 条：**
```diff
- $ 450
```

**新出现 6 条：**
```diff
+ $450 /yr $ 225
+ Get 50% off Visible+ Pro annual plan (that’s like paying $18.75/mo) with code BLACKFRIDAY
+ New members get $225 off the Visible+ Pro annual plan (reg.
+ Promo code <b>BLACKFRIDAY</b> and payment of $225 required at checkout.</p>\r\n<p>&nbsp;</p>\r\n<p>1.
+ Promo code <b>BLACKFRIDAY</b> and payment of $225 required at checkout.</p>\r\n<p>&nbsp;</p>\r\n<p>Promo is not transferable, not redeemable for cash and has no cash value.
+ Promo code BLACKFRIDAY and payment of $225 required at checkout.
```

### Total Wireless — `total_byop`

盯的是：BYO 专属价与条件  
<https://www.totalwireless.com/m/byop>


**消失了 2 条：**
```diff
- First month $30, then $20/mo after on a Total MAX 5G BYO plan.
- Switch to Total Wireless for $20/mo
```

**新出现 1 条：**
```diff
+ First month $30, then $20/mo after.
```

### T-Mobile — `tmobile`

盯的是：Essentials/Experience 各档、$4.49 恢复费  
<https://www.t-mobile.com/cell-phone-plans>


**消失了 82 条：**
```diff
- $0 due at sale; device cost, taxes, and fees financed over the term of financing agreement.
- $1,099.99 – Pixel 11 Pro 256 GB).
- $100 Rebate:
- $100 Virtual Prepaid Mastercard, Limit of 4/Account / New Accounts only — Switch (ID260686)
- $110
- $120
- $135
- $145
- $15
- $20
- $25 per line
- $260
- $30
- $35 device connection charge due at sale.
- $35 per line
- $40 per line
- $50 per line
- $55 per line
- $899.99 – Pixel 11 256 GB).
- 1 Optional Hulu/Disney+/ESPN+ (w/ Ads) Verizon bundle for $12/mo.
- 3 $5/month.
- Apple TV just $3/month
- Apple TV just $3/month Experience Beyond, Experience More™, including Experi…
- Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $629.99 – iPhone 15 128GB).
- Contact us before cancelling entire account to continue remaining bill credits, or credits stop & balance on required finance agreement is due (e.g., $999.99 – Galaxy S26 256GB).
… 另有 57 条
```

**新出现 34 条：**
```diff
+ $0/mo est.
+ $10/mo per phone line or home internet line
+ $10/mo.
+ $115
+ $125
+ $155
+ $165
+ $170
+ $195
+ $20-This is a 2 line Max plan
+ $240
+ $25 for the 6th line
+ $285
+ $30 - This is a 2 line Max plan
+ $35 for 7to 12 lines
+ $35 for the 6th line
+ $40
+ $45 for the 6th line
+ $45/line for 7to 12 lines
+ $5/mo per watch, tablet, or other line
+ $5/mo.
+ $50 for 7 to 12 lines
+ $60
+ $65 -This is a 2 line Max plan
+ $70 -This is a 2 line Max plan
… 另有 9 条
```

### T-Mobile — `tmobile_stu`

盯的是：学生档 $35/$30 是否仍在  
<https://www.t-mobile.com/cell-phone-plans/student-discounts>


**消失了 36 条：**
```diff
- $11.99/mo value
- $110
- $12.49/mo.
- $120
- $135
- $145
- $15
- $20
- $25 per line
- $260
- $30
- $35 per line
- $40 per line
- $50 per line
- $55 per line
- - an annual savings of $143.
- 3 $5/month.
- After 12 months or upon ineligibility, DashPass auto-renews at the then-current DashPass monthly plan membership fee (currently $9.99/month + tax) until canceled.
- After free period or upon ineligibility, subscription auto-renews (currently $9.99/mo.
- After you sign up for a T-Mobile plan with Student Perks, share a referral link and earn $100 virtual prepaid Mastercard® (up to $500 a year) when your friends join!
- Apple TV for just $3/mo.
- Apple TV just $3/month
- Get Apple TV for just $3/mo.
- Get a Student Perks phone plan and America’s fastest 5G home internet for just $30/mo.
- Get up to $800 off an iPhone 18 Pro Max when you add a new line and bring your number on an Experience Beyond plan with Student Savings 2.0.
… 另有 11 条
```

**新出现 39 条：**
```diff
+ $1,200 via bill credits; line with promo must be active and in good standing to receive credits; allow 2 bill cycles.
+ $10/mo per phone line or home internet line
+ $10/mo.
+ $115
+ $125
+ $155
+ $165
+ $170
+ $195
+ $20-This is a 2 line Max plan
+ $240
+ $25 for the 6th line
+ $285
+ $30 - This is a 2 line Max plan
+ $35 for 7to 12 lines
+ $35 for the 6th line
+ $40
+ $45 for the 6th line
+ $45/line for 7to 12 lines
+ $5/mo per watch, tablet, or other line
+ $5/mo.
+ $50 for 7 to 12 lines
+ $60
+ $65 -This is a 2 line Max plan
+ $70 -This is a 2 line Max plan
… 另有 14 条
```

### T-Mobile — `tmobile_switch`

盯的是：Essentials Saver $50 AutoPay 价、$35 设备接入费  
<https://www.t-mobile.com/switch/savings>


**消失了 1 条：**
```diff
- Included with Experience Beyond or $10/mo.; auto renews monthly.
```

**新出现 1 条：**
```diff
+ Available on qualifying T-Mix plans or $10/mo.; auto renews monthly.
```

### AT&T — `att`

盯的是：后付费头图价（分档价是客户端渲染的，抓不到，靠下面那条补）  
<https://www.att.com/plans/wireless/>


**新出现 18 条：**
```diff
+ $ 25.00 /mo.
+ $ 35.00 /mo.
+ $ 40.00 /mo.
+ $ 45.00 /mo.
+ $ 50.00 /mo.
+ $ 60.00 /mo.
+ $ 65.00 /mo.
+ $ 80.00 /mo.
+ Get more with Unlimited Your Way Plus, get an extra $5/mo.
+ Now $25.00.
+ Now $35.00.
+ Now $45.00.
+ Now $65.00.
+ Plan price after $10/mo.
+ Was $40.00 per month..
+ Was $50.00 per month..
+ Was $60.00 per month..
+ Was $80.00 per month..
```

### Verizon — `verizon`

盯的是：Simplicity $55/$45/$30  
<https://www.verizon.com/plans/unlimited/>


**消失了 1 条：**
```diff
- $37.95/mo
```

**新出现 1 条：**
```diff
+ $15/mo
```

### Verizon — `verizon_pre`

盯的是：预付费各档与忠诚度折扣  
<https://www.verizon.com/plans/prepaid/>


**消失了 3 条：**
```diff
- Get iPhone 16e for $349.99
- data-aria-label="Save $150 on a Samsung Galaxy A15 5G">
- iPhone 16e (128GB) originally for $599.99, instant discount of $250 at checkout." data-tooltip-type="icon" data-aria-label="Get iPhone 16e for $349.99">
```

**新出现 16 条：**
```diff
+ $200 discount applied at checkout."
+ Get a Samsung Galaxy A37 5G for $339.99
+ Get a Samsung Galaxy S26 FE for $499.99 when you
+ Requires activation of a new line on any Verizon Prepaid Unlimited phone plan ($150 discount applied at checkout)."
+ Samsung Galaxy A37 5G (128 GB) originally $489.99.
+ Samsung Galaxy S26 FE (128 GB) originally $699.99.
+ Save $150
+ Save $150 on a Samsung Galaxy A37 5G Offer ends 1/31/27 or while supplies last.
+ Save $150 when you activate on any new
+ Save $200 on Galaxy S26 FE
+ Save $200 on a Samsung Galaxy S26 FE Offer ends 1/31/27 or while supplies last.
+ data-tooltip-type="icon" data-aria-label="Get 2 Unlimited lines for just$80/mo.">
+ data-tooltip-type="icon" data-aria-label="Save $150 on Samsung Galaxy A37 5G">
+ data-tooltip-type="icon" data-aria-label="Save $200 on Galaxy S26 FE">
+ for $349.99
+ iPhone 16e (128GB) originally for $599.99, instant discount of $250 at checkout." data-tooltip-type="icon" data-aria-label="Free Samsung Galaxy A17 5G">
```

### US Mobile — `usmobile`

盯的是：Starter/Flex/Premium 年付价、促销档期（预期 403）  
<https://www.usmobile.com/plans>


**消失了 4 条：**
```diff
- $15 Unlimited
- $25
- Renews at $25/mo.
- Renews at $44/mo.
```

**新出现 4 条：**
```diff
+ $15 monthly Starter
+ $25 monthly Premium
+ Renews at $25/mo after 6 mos.
+ Renews at $44/mo after 6 mos.
```


## 无法核实

这些页面本次没抓到。**这不等于价格变了**，baseline 保持上次的值不动。

- **Mint Mobile** `mint` — `HTTP 403`  
  <https://www.mintmobile.com/plans/>

> Mint 与 US Mobile 有已知反爬，长期 403 属预期之内；但如果某天它们变成 200，说明反爬撤了，那本身是个好消息。
> 其余站点若连续多周无法核实，说明监控失效了，需要人工看一眼。


## 无变化（8 个）

Cricket、Cricket、Total Wireless、Metro、AT&T、AT&T、AT&T、Google Fi


---

*本报告只检测「页面上的价格文本变没变」，不解析具体价格——定向解析器会随改版静默失效并写入错误数字，那比过期数字更危险。*

*误报来源：营销文案调整、A/B 测试、地区化差异。真实降价一定会出现在这里，但不是每条都值得动。*
