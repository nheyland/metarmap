(this.webpackJsonpsite=this.webpackJsonpsite||[]).push([[0],{18:function(e,t,s){},40:function(e,t,s){"use strict";s.r(t);var c=s(2),n=s.n(c),i=s(9),r=s.n(i),a=s(10),o=s(1),l=function(){return Object(o.jsx)("div",{className:"title",children:Object(o.jsx)("div",{className:"row title",children:Object(o.jsxs)("div",{className:"col",children:[Object(o.jsx)("h2",{className:"header",children:"MetarMap"}),Object(o.jsxs)("div",{className:"row",children:[Object(o.jsx)(a.a,{size:24}),Object(o.jsx)("h4",{className:"subheader",children:"The MetarMap controller"})]})]})})})},h=(s(18),s(4)),j=s(11),u=s.n(j);s(39);var d=function(e){var t=e.apiip,s=Object(c.useState)(!1),n=Object(h.a)(s,2),i=n[0],r=n[1],a=function(e){r(!0),fetch("http://".concat(t,":3333/").concat(e)).then((function(e){return e.json()})).then((function(e){return"success"===e.status&&r(!1)}))};return Object(o.jsxs)("div",{className:"map",children:[Object(o.jsx)("h2",{className:"header",children:"Map Controls"}),Object(o.jsx)("hr",{}),i&&Object(o.jsx)("div",{className:"center",children:Object(o.jsx)(u.a,{type:"TailSpin",color:"#253031",height:100,width:100})})||Object(o.jsxs)(o.Fragment,{children:[Object(o.jsx)("button",{onClick:function(){return a("america")},children:" America"}),Object(o.jsx)("button",{onClick:function(){return a("metars")},children:" Metars"}),Object(o.jsx)("button",{onClick:function(){return a("red")},children:" Red"}),Object(o.jsx)("button",{onClick:function(){return a("blue")},children:" Blue"}),Object(o.jsx)("button",{onClick:function(){return a("green")},children:" Green"}),Object(o.jsx)("button",{onClick:function(){return a("off")},children:" Off"})]})]})};var b=function(e){var t=e.setApiip,s=e.apiip,n=Object(c.useState)(""),i=Object(h.a)(n,2),r=i[0],a=i[1];return Object(o.jsxs)("div",{className:"ip",children:[Object(o.jsx)("h2",{className:"info",children:'This is the "KEY_IP" printed out when running the boot file. It is also the IP address of this site.'}),Object(o.jsx)("br",{}),Object(o.jsx)("h2",{className:"info",children:'Example: "192.168.0.12"'}),Object(o.jsxs)("div",{className:"info",children:[Object(o.jsx)("input",{type:"text",value:r,onChange:function(e){return a(e.target.value)}}),Object(o.jsx)("button",{onClick:function(){return t(r),a(""),void localStorage.setItem("ip_address_for_metar_map",s)},children:"Assign IP"}),Object(o.jsx)("h2",{className:"info special",children:"This will be saved in cookies for the next time you access this site"})]})]})};var p=function(){return Object(o.jsxs)("div",{className:"attrib",children:[Object(o.jsx)("h2",{children:"Created by Nick Heyland"}),Object(o.jsxs)("h2",{children:["For assistance please email me at",Object(o.jsx)("a",{href:"mailto:snheyland@gmail.com<",children:" nheyland@gmail.com"})]}),Object(o.jsxs)("h2",{children:["For source code and instructions click",Object(o.jsx)("a",{href:"https://github.com/nheyland/metarmap",children:" here"})]}),Object(o.jsx)("h2",{children:"This software is not intended for sale or redistribution"}),Object(o.jsxs)("h2",{children:["Interested in the iOS App? Click",Object(o.jsxs)("a",{href:"https://apps.apple.com/us/app/mapremote/id1576002389\nhttps://apps.apple.com/us/app/mapremote/id1576002389",children:[" ","here"]})]})]})},O=s(12),m=s(6);var x=function(e){var t=e.apiip,s=e.setApiip,n=Object(c.useState)(!1),i=Object(h.a)(n,2),r=(i[0],i[1]),a=Object(c.useState)(2),l=Object(h.a)(a,2),j=l[0],u=l[1],d=Object(c.useState)(""),b=Object(h.a)(d,2),p=b[0],x=b[1],f={},v=function(e){r(!0),fetch("http://".concat(t,":3333/").concat(e)).then((function(e){return e.json()})).then((function(e){return"success"===e.status&&r(!1)}))};return Object(o.jsxs)("div",{className:"setup",children:[Object(o.jsx)("h2",{className:"setup-text",children:"Welcome! Lets get this set up, if you are seeing this, you are connected to the metarmap. Fill out these settings to setup the map."}),Object(o.jsx)("div",{className:"setup-row",children:Object(o.jsx)(m.a,{size:36,className:"ctr"})}),Object(o.jsxs)("h2",{className:"setup-text",children:["Before we start, we need the ip. The ip for this is the ip of the device that we are setting. The ip is the base url of this site, example: 192.168.0.33",Object(o.jsx)("br",{}),Object(o.jsx)("input",{type:"text",value:p,onChange:function(e){return x(e.target.value)}}),Object(o.jsx)("button",{onClick:function(){return s(p),x(""),void localStorage.setItem("ip_address_for_metar_map",t)},children:"Assign IP"}),Object(o.jsx)("h2",{className:"info special",children:"This will be saved in cookies for the next time you access this site"})]}),Object(o.jsx)("div",{className:"setup-row",children:Object(o.jsx)(m.a,{size:36,className:"ctr"})}),Object(o.jsx)("h2",{className:"setup-text",children:"First lets run a test, press this button to test all the lights. You should see them turn all the color selected"}),Object(o.jsxs)("div",{className:"setup-row",children:[Object(o.jsx)("button",{className:"ctr",onClick:function(){return v("green")},children:"Test Green"}),Object(o.jsx)("button",{className:"ctr",onClick:function(){return v("red")},children:"Test Red"}),Object(o.jsx)("button",{className:"ctr",onClick:function(){return v("blue")},children:"Test Blue"})]}),Object(o.jsx)("h2",{className:"setup-text",children:"All the colors should shine through the map. Make adjustments to the physical map now"}),Object(o.jsx)("div",{className:"setup-row",children:Object(o.jsx)(m.a,{size:36,className:"ctr"})}),Object(o.jsx)("h2",{className:"setup-text",children:"Lets check the amount of LEDs you have, set a number below and we can light up that many LEDs to confirm"}),Object(o.jsxs)("div",{className:"setup-row",children:[Object(o.jsx)("input",{onChange:function(e){u(e.target.value)},type:"number"}),Object(o.jsxs)("button",{onClick:function(){return v("testAmount/".concat(j))},children:["Power ",j," LEDs"]})]}),Object(o.jsx)("h2",{className:"info special",children:"Once you enter the airports, DO NOT CHANGE THIS, otherwise your work will disappear"}),Object(o.jsx)("h2",{className:"setup-text",children:"Keep testing this setting to see how many Leds are lighting up, do this until you know how many you have"}),Object(o.jsx)("div",{className:"setup-row",children:Object(o.jsx)(m.a,{size:36,className:"ctr"})}),Object(o.jsx)("h2",{className:"setup-text",children:"Lets get the airports, heres how we can do it..."}),Object(o.jsx)("h2",{className:"setup-text",children:"For each row below, type in the identifier of the airport in order. The first light is the closest to the pi"}),Object(o.jsx)("div",{className:"airports"}),Object(O.a)(Array(Number(j))).map((function(e,t){return Object(o.jsxs)("div",{className:"airports-row",children:[Object(o.jsx)("h2",{children:t+1}),Object(o.jsx)("input",{maxLength:"4",id:t,type:"text",onChange:function(e){return t=e.target.id,s=e.target.value,void(f[t]=s.toUpperCase());var t,s}},t)]})})),Object(o.jsx)("h2",{className:"setup-text",children:'Thats it! Hit the send to device button, and the information will be saved on device! Now return to the home screen and hit "metars"!'}),Object(o.jsx)("button",{onClick:function(){return console.log(f),void fetch("http://".concat(t,":3333/setAirports"),{"Access-Control-Allow-Origin":"*",method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(f)}).then((function(e){return e.json()})).then((function(e){return"success"===e.status&&r(!1)}))},children:"Send to device!"})]})},f=function(){var e=Object(c.useState)(null),t=Object(h.a)(e,2),s=t[0],n=t[1],i=Object(c.useState)(!1),r=Object(h.a)(i,2),a=r[0],l=r[1];return Object(c.useEffect)((function(){null!==localStorage.getItem("ip_address_for_metar_map")&&n(localStorage.getItem("ip_address_for_metar_map"))}),[]),Object(o.jsxs)("div",{className:"content",children:[Object(o.jsx)("hr",{}),!a&&Object(o.jsxs)(o.Fragment,{children:[s&&Object(o.jsx)(d,{apiip:s,setApiip:n})||Object(o.jsx)(b,{apiip:s,setApiip:n}),Object(o.jsx)("button",{onClick:function(){l(!0)},children:"Setup"}),Object(o.jsx)("button",{onClick:function(){return n(null)},children:"Reset IP"})]})||Object(o.jsx)(x,{apiip:s,setApiip:n}),Object(o.jsx)(p,{})]})};var v=function(){return Object(o.jsxs)("div",{className:"App",children:[Object(o.jsx)(l,{}),Object(o.jsx)(f,{})]})};r.a.render(Object(o.jsx)(n.a.StrictMode,{children:Object(o.jsx)(v,{})}),document.getElementById("root"))}},[[40,1,2]]]);
//# sourceMappingURL=main.462a69f8.chunk.js.map