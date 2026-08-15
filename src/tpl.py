# -*- coding: utf-8 -*-
"""HTML 模板：CSS + 页面骨架 + 交互 JS。数据由 build.py 注入。"""

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#f7f6f3; --bg2:#fffefb; --card:#ffffff; --ink:#1a1917; --ink2:#55524c; --ink3:#8a857c;
  --line:#e5e1d8; --line2:#d3cec2;
  --accent:#8a3324; --accent2:#c2410c; --accent-bg:#fdf2ee;
  --good:#2f6b3e; --good-bg:#eef6f0; --warn:#8a6116; --warn-bg:#fdf6e7; --bad:#9c2c2c; --bad-bg:#fcefef;
  --vz:#c2261c; --att:#0b6ba8; --tmo:#c8127f; --mvno:#6b5b95;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
  --shadow:0 1px 2px rgba(26,25,23,.05),0 4px 14px rgba(26,25,23,.05);
}
@media (prefers-color-scheme:dark){
 :root:not([data-theme="light"]){
  --bg:#16151a; --bg2:#1c1b21; --card:#212027; --ink:#eceaf0; --ink2:#a8a4b0; --ink3:#78747f;
  --line:#302e38; --line2:#3d3a46;
  --accent:#ff9d7a; --accent2:#ffb694; --accent-bg:#2c1f1c;
  --good:#7fd39a; --good-bg:#17291d; --warn:#e8c46a; --warn-bg:#2b2517; --bad:#ff8f8f; --bad-bg:#2e1a1a;
  --vz:#ff6b60; --att:#5cb3e8; --tmo:#f76bc0; --mvno:#a898d8;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
 }}
:root[data-theme="dark"]{
  --bg:#16151a; --bg2:#1c1b21; --card:#212027; --ink:#eceaf0; --ink2:#a8a4b0; --ink3:#78747f;
  --line:#302e38; --line2:#3d3a46;
  --accent:#ff9d7a; --accent2:#ffb694; --accent-bg:#2c1f1c;
  --good:#7fd39a; --good-bg:#17291d; --warn:#e8c46a; --warn-bg:#2b2517; --bad:#ff8f8f; --bad-bg:#2e1a1a;
  --vz:#ff6b60; --att:#5cb3e8; --tmo:#f76bc0; --mvno:#a898d8;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.75;letter-spacing:.01em;
  font-feature-settings:"tnum" 0;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px 120px}
@media (max-width:700px){.wrap{padding:0 14px 80px}body{font-size:14.5px}}

/* ── 头部 ── */
header.top{padding:56px 0 28px;border-bottom:2px solid var(--ink);margin-bottom:34px}
h1{font-size:clamp(26px,4.6vw,42px);line-height:1.2;margin:0 0 12px;letter-spacing:-.02em;font-weight:750}
.sub{color:var(--ink2);font-size:15px;max-width:62ch;margin:0 0 18px}
.meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:12.5px;color:var(--ink3);font-family:var(--mono)}
.meta b{color:var(--ink2);font-weight:600}

/* ── 通用 ── */
section{margin:0 0 64px;scroll-margin-top:74px}
h2{font-size:clamp(20px,3vw,27px);margin:0 0 6px;letter-spacing:-.015em;font-weight:700;
   display:flex;align-items:baseline;gap:11px;flex-wrap:wrap}
h2 .num{font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:600;
        border:1.5px solid var(--accent);border-radius:5px;padding:1px 7px;letter-spacing:0}
h2 .num.plain{border:none;padding:0}
h3{font-size:17px;margin:30px 0 10px;font-weight:680;letter-spacing:-.01em}
h4{font-size:14.5px;margin:20px 0 7px;font-weight:650;color:var(--ink2)}
.lede{color:var(--ink2);margin:0 0 22px;max-width:74ch;font-size:14.5px}
p{margin:0 0 13px}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 32%,transparent)}
a:hover{border-bottom-color:var(--accent)}
code,.mono{font-family:var(--mono);font-size:.9em}
.card{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:19px 21px;box-shadow:var(--shadow)}
.muted{color:var(--ink3);font-size:12.5px;line-height:1.65}
.hl{background:var(--accent-bg);color:var(--accent);padding:.5px 5px;border-radius:4px;font-weight:600}
mark{background:color-mix(in srgb,var(--warn) 26%,transparent);color:inherit;padding:.5px 3px;border-radius:3px}

/* ── 结论条 ── */
.verdict{background:var(--card);border:2px solid var(--ink);border-radius:13px;padding:22px 24px;margin:0 0 30px;
  box-shadow:5px 5px 0 var(--accent)}
.verdict h3{margin:0 0 9px;font-size:15px;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);font-family:var(--mono)}
.verdict p{font-size:16.5px;line-height:1.72;margin:0 0 9px}
.verdict p:last-child{margin-bottom:0}

/* ── 徽章 ── */
.tag{display:inline-flex;align-items:center;gap:4px;font-size:11.5px;font-weight:640;padding:2px 8px;border-radius:20px;
  border:1px solid var(--line2);color:var(--ink2);background:var(--bg2);white-space:nowrap;font-family:var(--mono);letter-spacing:.01em}
.tag.good{color:var(--good);border-color:color-mix(in srgb,var(--good) 42%,transparent);background:var(--good-bg)}
.tag.warn{color:var(--warn);border-color:color-mix(in srgb,var(--warn) 42%,transparent);background:var(--warn-bg)}
.tag.bad{color:var(--bad);border-color:color-mix(in srgb,var(--bad) 42%,transparent);background:var(--bad-bg)}
.tag.vz{color:var(--vz);border-color:color-mix(in srgb,var(--vz) 40%,transparent)}
.tag.att{color:var(--att);border-color:color-mix(in srgb,var(--att) 40%,transparent)}
.tag.tmo{color:var(--tmo);border-color:color-mix(in srgb,var(--tmo) 40%,transparent)}
.tag.multi{color:var(--mvno);border-color:color-mix(in srgb,var(--mvno) 40%,transparent)}

/* ── 开关 ── */
.switchbar{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--bg) 93%,transparent);
  backdrop-filter:saturate(180%) blur(14px);-webkit-backdrop-filter:saturate(180%) blur(14px);
  border-bottom:1px solid var(--line);margin:0 -24px 30px;padding:11px 24px;
  display:flex;gap:14px;align-items:center;flex-wrap:wrap}
@media (max-width:700px){.switchbar{margin:0 -14px 22px;padding:9px 14px;gap:9px}}
.seg{display:inline-flex;background:var(--bg2);border:1px solid var(--line2);border-radius:9px;padding:2.5px;gap:2.5px}
.seg button{font:inherit;font-size:12.5px;font-weight:640;border:0;background:transparent;color:var(--ink2);
  padding:5.5px 13px;border-radius:6.5px;cursor:pointer;white-space:nowrap;font-family:var(--mono)}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--bg);box-shadow:0 1px 3px rgba(0,0,0,.18)}
.seg button:hover:not([aria-pressed="true"]){color:var(--ink)}
.switchbar .lbl{font-size:11.5px;color:var(--ink3);font-family:var(--mono);letter-spacing:.03em}

/* ── 价格轴 ── */
.axis{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px 22px 14px;box-shadow:var(--shadow);overflow-x:auto}
.axis-inner{min-width:1130px;position:relative}
.axis-row{display:grid;grid-template-columns:112px 1000px;gap:12px;align-items:center;margin-bottom:9px}
.axis-lab{font-size:12px;font-family:var(--mono);color:var(--ink2);text-align:right;font-weight:620;line-height:1.3}
.axis-track{position:relative;border-left:1px solid var(--line);border-right:1px solid var(--line)}
.axis-track::before{content:"";position:absolute;left:0;right:0;top:0;bottom:0;background:repeating-linear-gradient(to right,var(--line) 0 1px,transparent 1px 100px);opacity:.55}
.dot{position:absolute;transform:translate(-50%,-50%);height:21px;border-radius:11px;padding:0 8px;
  display:flex;align-items:center;font-size:11px;font-family:var(--mono);font-weight:660;cursor:pointer;
  border:1.5px solid;white-space:nowrap;transition:transform .12s,box-shadow .12s;z-index:2}
.dot:hover,.dot.on{transform:translate(-50%,-50%) scale(1.13);box-shadow:0 3px 12px rgba(0,0,0,.22);z-index:5}
.dot.vz{background:var(--card);border-color:var(--vz);color:var(--vz)}
.dot.att{background:var(--card);border-color:var(--att);color:var(--att)}
.dot.tmo{background:var(--card);border-color:var(--tmo);color:var(--tmo)}
.dot.multi{background:var(--card);border-color:var(--mvno);color:var(--mvno)}
.axis-scale{display:grid;grid-template-columns:112px 1000px;gap:12px;margin-top:2px}
.axis-ticks{position:relative;height:19px}
.tick{position:absolute;transform:translateX(-50%);font-size:10.5px;font-family:var(--mono);color:var(--ink3)}
.band{position:absolute;top:0;bottom:0;background:color-mix(in srgb,var(--accent) 12%,transparent);
  border-left:1px dashed var(--accent);border-right:1px dashed var(--accent);z-index:1;pointer-events:none}

/* ── 品牌抽屉 ── */
.brandgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:10px;margin-bottom:22px}
.brandbtn{background:var(--card);border:1.5px solid var(--line2);border-radius:10px;padding:13px 14px;cursor:pointer;
  text-align:left;font:inherit;color:var(--ink);transition:border-color .13s,transform .13s,box-shadow .13s;display:block;width:100%}
.brandbtn:hover{border-color:var(--ink3);transform:translateY(-2px);box-shadow:var(--shadow)}
.brandbtn[aria-expanded="true"]{border-color:var(--accent);border-width:2px;background:var(--accent-bg)}
.brandbtn .bn{font-weight:700;font-size:15px;display:block;margin-bottom:3px;letter-spacing:-.01em}
.brandbtn .bm{font-size:11.5px;color:var(--ink3);font-family:var(--mono);display:block;line-height:1.5}

.panel{display:none}
.panel.open{display:block;animation:fade .22s ease}
@keyframes fade{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:none}}
.panel-head{border-left:4px solid var(--accent);padding:3px 0 3px 15px;margin:0 0 18px}
.panel-head h3{margin:0 0 5px;font-size:21px}
.panel-head .pm{font-size:13px;color:var(--ink2);line-height:1.68}

/* ── 套餐卡 ── */
.plan{background:var(--card);border:1px solid var(--line);border-radius:12px;margin-bottom:13px;overflow:hidden;box-shadow:var(--shadow)}
.plan-main{display:grid;grid-template-columns:1fr auto;gap:16px;padding:16px 19px;align-items:start;cursor:pointer}
.plan-main:hover{background:var(--bg2)}
.plan-name{font-weight:700;font-size:16px;margin:0 0 5px;letter-spacing:-.01em}
.plan-chips{display:flex;flex-wrap:wrap;gap:5px;margin:7px 0 0}
.price-box{text-align:right;white-space:nowrap}
.price{font-family:var(--mono);font-size:25px;font-weight:700;letter-spacing:-.03em;line-height:1.1}
.price .cur{font-size:15px;vertical-align:.16em;margin-right:1px;font-weight:600}
.price-sub{font-size:11px;color:var(--ink3);font-family:var(--mono);margin-top:3px;line-height:1.45}
.price-was{font-size:12px;color:var(--ink3);text-decoration:line-through;font-family:var(--mono)}
.promo{color:var(--good);font-weight:660}

.plan-body{display:none;border-top:1px dashed var(--line2);padding:17px 19px 19px;background:var(--bg2)}
.plan.open .plan-body{display:block}
.spec{display:grid;grid-template-columns:88px 1fr;gap:5px 13px;font-size:13.2px;margin-bottom:5px;align-items:baseline}
.spec dt{color:var(--ink3);font-size:11.5px;font-family:var(--mono);text-align:right;padding-top:2.5px;line-height:1.55}
.spec dd{margin:0;color:var(--ink2);line-height:1.68}

/* ── 同价位对手 ── */
.rivals{margin-top:17px;border-top:2px solid var(--ink);padding-top:14px}
.rivals-h{font-size:12px;font-family:var(--mono);font-weight:660;color:var(--accent);letter-spacing:.05em;
  text-transform:uppercase;margin:0 0 11px;display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.rivals-h .rn{color:var(--ink3);font-weight:500;text-transform:none;letter-spacing:0}
.rival{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:11px;align-items:center;padding:9px 11px;border-radius:8px;
  background:var(--card);border:1px solid var(--line);margin-bottom:6px;font-size:13.2px}
.rival.self{border-color:var(--accent);border-width:1.5px;background:var(--accent-bg)}
.rival .rb{font-weight:660;white-space:nowrap}
.rival .rd{display:block;color:var(--ink3);font-size:11.8px;line-height:1.55;min-width:0;margin-top:1px}
.rival .rp{font-family:var(--mono);font-weight:700;font-size:15.5px;white-space:nowrap;text-align:right}
.rival .delta{font-size:10.5px;font-family:var(--mono);display:block;font-weight:600;line-height:1.3}
.d-up{color:var(--bad)} .d-dn{color:var(--good)} .d-eq{color:var(--ink3)}
.empty{color:var(--ink3);font-size:13px;font-style:italic;padding:9px 0}

/* ── 表格 ── */
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:11px;background:var(--card);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:13.2px;min-width:660px}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.62}
thead th{background:var(--bg2);font-size:11.5px;font-family:var(--mono);font-weight:660;color:var(--ink2);
  letter-spacing:.02em;position:sticky;top:0;z-index:2;border-bottom:1.5px solid var(--line2);white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--bg2)}
td.num,th.num{font-family:var(--mono);text-align:right;white-space:nowrap}
td.best{color:var(--good);font-weight:700}
.rowlab{font-weight:660;white-space:nowrap}

/* ── 审计 ── */
.finding{border-left:4px solid var(--line2);padding:2px 0 2px 15px;margin:0 0 19px}
.finding.bad{border-color:var(--bad)} .finding.warn{border-color:var(--warn)} .finding.good{border-color:var(--good)}
.finding h4{margin:0 0 5px;font-size:14.8px;color:var(--ink);font-weight:680;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.finding p{margin:0 0 6px;font-size:13.6px;color:var(--ink2);line-height:1.72}
.finding .was{font-size:12.6px;color:var(--ink3);font-family:var(--mono);background:var(--bg2);
  border:1px solid var(--line);border-radius:6px;padding:6px 10px;margin:6px 0;line-height:1.6}

/* ── 锐评 ── */
.roast{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:0 11px 11px 0;padding:16px 19px;margin:0 0 13px;box-shadow:var(--shadow)}
.roast h4{margin:0 0 6px;font-size:15.5px;color:var(--ink);display:flex;gap:9px;align-items:baseline;flex-wrap:wrap;font-weight:700}
.roast p{margin:0;font-size:14px;color:var(--ink2);line-height:1.78}
.roast .kicker{font-family:var(--mono);font-size:11px;color:var(--accent);font-weight:660;letter-spacing:.04em;text-transform:uppercase}

/* ── 推荐 ── */
.rec{display:grid;grid-template-columns:auto 1fr;gap:16px;padding:17px 19px;border:1px solid var(--line);
  border-radius:11px;background:var(--card);margin-bottom:12px;box-shadow:var(--shadow)}
.rec .rank{font-family:var(--mono);font-size:31px;font-weight:750;color:var(--accent);line-height:1;padding-top:2px;letter-spacing:-.04em}
.rec h4{margin:0 0 5px;font-size:16.5px;color:var(--ink);font-weight:700}
.rec p{margin:0 0 6px;font-size:13.8px;color:var(--ink2);line-height:1.72}
.rec .who{font-size:12.5px;color:var(--ink3);font-family:var(--mono);line-height:1.6}

/* ── 来源 ── */
.srclist{font-size:12.5px;color:var(--ink3);line-height:1.85}
.srclist a{word-break:break-all}
details.src{margin-top:11px}
details.src summary{cursor:pointer;font-size:12px;font-family:var(--mono);color:var(--ink3);
  padding:5px 0;list-style:none;user-select:none}
details.src summary::-webkit-details-marker{display:none}
details.src summary::before{content:"▸ ";color:var(--accent)}
details.src[open] summary::before{content:"▾ "}

/* ── TOC ── */
nav.toc{position:fixed;right:20px;top:50%;transform:translateY(-50%);z-index:50;
  background:color-mix(in srgb,var(--card) 94%,transparent);backdrop-filter:blur(12px);
  border:1px solid var(--line);border-radius:11px;padding:10px 8px;box-shadow:var(--shadow);max-width:172px}
nav.toc a{display:block;font-size:11.5px;color:var(--ink3);padding:3.5px 9px;border-radius:6px;border:0;
  line-height:1.45;font-family:var(--mono);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
nav.toc a:hover{background:var(--bg2);color:var(--ink)}
nav.toc a.active{color:var(--accent);background:var(--accent-bg);font-weight:660}
@media (max-width:1420px){nav.toc{display:none}}

footer{border-top:1px solid var(--line);padding-top:22px;margin-top:60px;font-size:12.5px;color:var(--ink3);line-height:1.8}
.warnbox{background:var(--warn-bg);border:1px solid color-mix(in srgb,var(--warn) 38%,transparent);
  border-radius:10px;padding:14px 17px;font-size:13.2px;color:var(--ink2);line-height:1.72;margin:0 0 18px}
.warnbox b{color:var(--warn)}
"""

JS = r"""
(function(){
"use strict";
var MODE="landed";           // landed | adv
var PROMO=false;             // 是否用促销价
var RANGE=6;                 // 同价位带宽 ±$
var openBrand=null;

function money(v){ return v==null?"—":("$"+(Math.round(v*100)/100).toFixed(2).replace(/\.00$/,"")); }
function netClass(n){ return n==="Verizon"?"vz":(n==="AT&T"?"att":(n==="T-Mobile"?"tmo":"multi")); }

// 取一个套餐在当前口径下的比较价
function px(p){
  var base = (PROMO && p.promo!=null) ? p.promo : p.adv;
  if(base==null) return null;
  if(MODE==="adv") return base;
  if(p.tax_inc) return base;                       // 已含税：广告价即到手价
  return base*(1+DATA.tax.combined/100) + (p.fee||0) + DATA.tax.ng911;
}
function priceNote(p){
  if(MODE==="adv") return p.tax_inc?"广告价·已含税":"广告价·税费另计";
  return p.tax_inc?"到手价 = 广告价（已含税费）":"到手价（含税+每线固定费）";
}

/* ─── 价格轴 ─── */
var AX_MIN=0, AX_MAX=120;
function buildAxis(){
  var host=document.getElementById("axis"); if(!host) return;
  var groups={};
  DATA.plans.forEach(function(p){ var v=px(p); if(v==null) return;
    (groups[p.net]=groups[p.net]||[]).push({p:p,v:v}); });
  var order=["Verizon","AT&T","T-Mobile"];
  Object.keys(groups).forEach(function(n){ if(order.indexOf(n)<0) order.push(n); });
  order=order.filter(function(n){ return groups[n] && groups[n].length; });
  var maxv=0; DATA.plans.forEach(function(p){var v=px(p); if(v!=null&&v>maxv)maxv=v;});
  AX_MAX=Math.ceil((maxv+10)/10)*10;   // 右侧留白，避免末端标签被切
  var h='<div class="axis-inner"><div id="band" class="band" style="display:none"></div>';
  var TRACK_W=1000, LANE_H=26;   // 与 CSS min-width 对应
  order.forEach(function(net){
    var arr=(groups[net]||[]).sort(function(a,b){return a.v-b.v;});
    // 泳道排布：每个点估算像素宽度，放进第一条不碰撞的泳道
    var lanes=[];
    arr.forEach(function(o){
      var label=o.p.brand_short+' '+money(o.v);
      var wpx=label.length*6.6+18;                       // 估算标签像素宽
      var xpx=(o.v-AX_MIN)/(AX_MAX-AX_MIN)*TRACK_W;
      var L=xpx-wpx/2, R=xpx+wpx/2;
      var li=0;
      while(lanes[li] && lanes[li].some(function(u){return !(R<u.L-4 || L>u.R+4);})) li++;
      if(!lanes[li]) lanes[li]=[];
      lanes[li].push({L:L,R:R,o:o,x:xpx,label:label});
    });
    var nl=Math.max(1,lanes.length);
    h+='<div class="axis-row" style="grid-template-rows:auto"><div class="axis-lab">'+net
      +'<br><span style="color:var(--ink3);font-weight:400">'+arr.length+' 档</span></div>'
      +'<div class="axis-track" style="height:'+(nl*LANE_H+8)+'px">';
    lanes.forEach(function(lane,li){
      lane.forEach(function(u){
        h+='<button class="dot '+netClass(net)+'" data-id="'+u.o.p.id+'" '
          +'style="left:'+(u.x/TRACK_W*100).toFixed(3)+'%;top:'+(li*LANE_H+LANE_H/2+4)+'px" '
          +'title="'+u.o.p.brand+' '+u.o.p.name+' — '+money(u.o.v)+'">'+u.label+'</button>';
      });
    });
    h+='</div></div>';
  });
  h+='<div class="axis-scale"><div></div><div class="axis-ticks">';
  for(var t=0;t<=AX_MAX;t+=10){ h+='<span class="tick" style="left:'+((t-AX_MIN)/(AX_MAX-AX_MIN)*100).toFixed(2)+'%">$'+t+'</span>'; }
  h+='</div></div></div>';
  host.innerHTML=h;
  host.querySelectorAll(".dot").forEach(function(d){
    d.addEventListener("click",function(){ jumpTo(d.dataset.id); });
  });
}
function highlightBand(v){
  var b=document.getElementById("band"); if(!b) return;
  var lo=(v-RANGE-AX_MIN)/(AX_MAX-AX_MIN)*100, hi=(v+RANGE-AX_MIN)/(AX_MAX-AX_MIN)*100;
  b.style.display="block"; b.style.left=Math.max(0,lo)+"%"; b.style.width=Math.max(0,Math.min(100,hi)-Math.max(0,lo))+"%";
}

/* ─── 同价位对手 ─── */
function rivalsHTML(p){
  var v=px(p); if(v==null) return '<div class="empty">该套餐无可比价格。</div>';
  var list=DATA.plans.filter(function(q){ var w=px(q); return w!=null && Math.abs(w-v)<=RANGE; })
    .map(function(q){ return {q:q,w:px(q)}; })
    .sort(function(a,b){ return a.w-b.w; });
  if(list.length<=1) return '<div class="empty">在 ±'+money(RANGE)+' 区间内，没有其他品牌的套餐——这个价位它独一档。</div>';
  var h="";
  list.forEach(function(o){
    var self=o.q.id===p.id, d=o.w-v;
    var dc = Math.abs(d)<0.5?"d-eq":(d>0?"d-up":"d-dn");
    var ds = Math.abs(d)<0.5?"同价":(d>0?"+"+money(d):"−"+money(-d));
    h+='<div class="rival'+(self?" self":"")+'">'
      +'<span class="tag '+netClass(o.q.net)+'">'+o.q.net+'</span>'
      +'<span style="min-width:0"><span class="rb">'+o.q.brand+'</span> · '+o.q.name
      +(self?' <span class="tag" style="border-color:var(--accent);color:var(--accent)">当前</span>':'')
      +'<span class="rd">'+o.q.oneline+'</span></span>'
      +'<span class="rp">'+money(o.w)+'<span class="delta '+dc+'">'+ds+'</span></span></div>';
  });
  return h;
}

/* ─── 渲染 ─── */
function planHTML(p){
  var v=px(p), showPromo = PROMO && p.promo!=null;
  return '<article class="plan" id="plan-'+p.id+'" data-id="'+p.id+'">'
   +'<div class="plan-main">'
     +'<div><div class="plan-name">'+p.name+'</div>'
       +'<div class="muted">'+p.oneline+'</div>'
       +'<div class="plan-chips">'
         +'<span class="tag '+netClass(p.net)+'">'+p.net+'</span>'
         +'<span class="tag '+(p.tax_inc?"good":"warn")+'">'+(p.tax_inc?"税费已含":"税费另计")+'</span>'
         +(p.chips||[]).map(function(c){return '<span class="tag'+(c.k?" "+c.k:"")+'">'+c.t+'</span>';}).join("")
       +'</div></div>'
     +'<div class="price-box"><div class="price'+(showPromo?" promo":"")+'"><span class="cur">$</span>'
        +(v==null?"—":(Math.round(v*100)/100).toFixed(2).replace(/\.00$/,"").replace(/^\$/,""))+'</div>'
        +(showPromo?'<div class="price-was">常规 '+money(MODE==="adv"?p.adv:(p.tax_inc?p.adv:p.adv*(1+DATA.tax.combined/100)+(p.fee||0)+DATA.tax.ng911))+'</div>':'')
        +'<div class="price-sub">'+priceNote(p)+'</div></div>'
   +'</div>'
   +'<div class="plan-body">'+specHTML(p)
     +'<div class="rivals"><div class="rivals-h">同价位横向对比 <span class="rn">口径：'+(MODE==="landed"?"到手价":"广告价")+'，区间 ±'+money(RANGE)+'</span></div>'
     +rivalsHTML(p)+'</div></div></article>';
}
function specHTML(p){
  var rows=[["高速数据",p.data],["超额后",p.depri],["热点",p.hotspot],["视频",p.video],
            ["国际",p.intl],["付款",p.prepay],["AutoPay",p.autopay],["条件",p.cond],
            ["促销",p.promo_terms],["备注",p.notes]];
  var h='<dl class="spec">';
  rows.forEach(function(r){ if(r[1]) h+='<dt>'+r[0]+'</dt><dd>'+r[1]+'</dd>'; });
  h+='</dl>';
  if(p.url) h+='<div class="muted" style="margin-top:9px">出处：<a href="'+p.url+'" target="_blank" rel="noopener">'+p.url+'</a></div>';
  return h;
}
function renderBrands(){
  var g=document.getElementById("brandgrid"), h="";
  DATA.brands.forEach(function(b){
    var ps=DATA.plans.filter(function(p){return p.brand===b.name;});
    var vals=ps.map(px).filter(function(x){return x!=null;});
    var lo=vals.length?Math.min.apply(null,vals):null, hi=vals.length?Math.max.apply(null,vals):null;
    h+='<button class="brandbtn" data-brand="'+b.name+'" aria-expanded="false">'
      +'<span class="bn">'+b.name+'</span>'
      +'<span class="bm">'+b.net+' · '+ps.length+' 档<br>'+(lo!=null?money(lo)+" – "+money(hi):"—")+'</span></button>';
  });
  g.innerHTML=h;
  g.querySelectorAll(".brandbtn").forEach(function(btn){
    btn.addEventListener("click",function(){ toggleBrand(btn.dataset.brand); });
  });
}
function toggleBrand(name){
  var p=document.getElementById("panel");
  if(openBrand===name){ openBrand=null; p.className="panel"; p.innerHTML=""; syncBrandBtns(); return; }
  openBrand=name; syncBrandBtns();
  var b=DATA.brands.filter(function(x){return x.name===name;})[0];
  var ps=DATA.plans.filter(function(x){return x.brand===name;})
    .sort(function(a,c){ var x=px(a),y=px(c); return (x==null?1e9:x)-(y==null?1e9:y); });
  p.className="panel open";
  p.innerHTML='<div class="panel-head"><h3>'+b.name+'</h3><div class="pm">'+b.blurb+'</div></div>'
    +(b.gotchas&&b.gotchas.length?'<div class="warnbox"><b>这家的坑：</b> '+b.gotchas.join(' <b>·</b> ')+'</div>':'')
    +ps.map(planHTML).join("");
  bindPlans(p);
  p.scrollIntoView({behavior:"smooth",block:"nearest"});
}
function syncBrandBtns(){
  document.querySelectorAll(".brandbtn").forEach(function(b){
    b.setAttribute("aria-expanded", b.dataset.brand===openBrand ? "true":"false"); });
}
function bindPlans(root){
  root.querySelectorAll(".plan-main").forEach(function(m){
    m.addEventListener("click",function(){
      var a=m.closest(".plan"), was=a.classList.contains("open");
      root.querySelectorAll(".plan.open").forEach(function(o){o.classList.remove("open");});
      if(!was){ a.classList.add("open");
        var p=DATA.plans.filter(function(x){return x.id===a.dataset.id;})[0];
        var v=px(p); if(v!=null) highlightBand(v);
        document.querySelectorAll(".dot").forEach(function(d){ d.classList.toggle("on", d.dataset.id===a.dataset.id); });
      } else { var b=document.getElementById("band"); if(b)b.style.display="none";
        document.querySelectorAll(".dot.on").forEach(function(d){d.classList.remove("on");}); }
    });
  });
}
function jumpTo(id){
  var p=DATA.plans.filter(function(x){return x.id===id;})[0]; if(!p) return;
  if(openBrand!==p.brand) toggleBrand(p.brand);
  setTimeout(function(){
    var el=document.getElementById("plan-"+id); if(!el) return;
    document.querySelectorAll(".plan.open").forEach(function(o){o.classList.remove("open");});
    el.classList.add("open");
    var v=px(p); if(v!=null) highlightBand(v);
    document.querySelectorAll(".dot").forEach(function(d){ d.classList.toggle("on", d.dataset.id===id); });
    el.scrollIntoView({behavior:"smooth",block:"center"});
  },60);
}
function rerender(){
  buildAxis(); renderBrands();
  var keep=openBrand; openBrand=null; if(keep) toggleBrand(keep);
  document.querySelectorAll("[data-lp]").forEach(function(el){
    var p=DATA.plans.filter(function(x){return x.id===el.dataset.lp;})[0];
    if(p){ var v=px(p); el.textContent = v==null?"—":money(v); }
  });
}

/* ─── 开关绑定 ─── */
function initControls(){
  document.querySelectorAll("[data-mode]").forEach(function(b){
    b.addEventListener("click",function(){
      MODE=b.dataset.mode;
      document.querySelectorAll("[data-mode]").forEach(function(x){x.setAttribute("aria-pressed", x===b?"true":"false");});
      rerender();
    });
  });
  document.querySelectorAll("[data-promo]").forEach(function(b){
    b.addEventListener("click",function(){
      PROMO = b.dataset.promo==="1";
      document.querySelectorAll("[data-promo]").forEach(function(x){x.setAttribute("aria-pressed", x===b?"true":"false");});
      rerender();
    });
  });
  document.querySelectorAll("[data-range]").forEach(function(b){
    b.addEventListener("click",function(){
      RANGE=+b.dataset.range;
      document.querySelectorAll("[data-range]").forEach(function(x){x.setAttribute("aria-pressed", x===b?"true":"false");});
      rerender();
    });
  });
}
/* ─── TOC ─── */
function initTOC(){
  var secs=[].slice.call(document.querySelectorAll("section[id]"));
  var links=[].slice.call(document.querySelectorAll("nav.toc a"));
  if(!("IntersectionObserver" in window)) return;
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){
      links.forEach(function(l){ l.classList.toggle("active", l.getAttribute("href")==="#"+e.target.id); }); } });
  },{rootMargin:"-15% 0px -75% 0px"});
  secs.forEach(function(s){io.observe(s);});
}
document.addEventListener("DOMContentLoaded",function(){
  initControls(); rerender(); initTOC();
});
})();
"""
