(this.webpackJsonpsite = this.webpackJsonpsite || []).push([
  [0],
  {
    13: function (e, t, n) {},
    14: function (e, t, n) {
      "use strict";
      n.r(t);
      var c = n(2),
        r = n.n(c),
        s = n(4),
        i = n.n(s),
        j = n(7),
        a = n(5),
        u = n(6),
        o = n(1),
        l = function (e) {
          var t = e.setMenu,
            n = e.menu;
          return Object(o.jsx)("div", {
            className: "title",
            children: Object(o.jsxs)("div", {
              className: "row title",
              children: [
                Object(o.jsxs)("div", {
                  className: "col",
                  children: [
                    Object(o.jsx)("h2", {
                      className: "header",
                      children: "MetarMap",
                    }),
                    Object(o.jsxs)("div", {
                      className: "row",
                      children: [
                        Object(o.jsx)(a.a, { size: 24 }),
                        Object(o.jsx)("h4", {
                          className: "subheader",
                          children: "The MetarMap controller by Nick Heyland",
                        }),
                      ],
                    }),
                  ],
                }),
                Object(o.jsx)(u.a, {
                  size: 35,
                  onClick: function () {
                    return t(!n);
                  },
                  className: "pointer",
                }),
              ],
            }),
          });
        },
        b = function (e) {
          var t = e.menu,
            n = e.setMenu,
            r = Object(c.useRef)();
          return (
            Object(c.useEffect)(
              function () {
                document.addEventListener("mousedown", function (e) {
                  return !r.current.contains(e.target) && n(!1);
                });
              },
              [n]
            ),
            Object(o.jsxs)("nav", {
              ref: r,
              style: { width: t ? "15rem" : "0" },
              children: [
                Object(o.jsx)("a", { id: "home", href: "/", children: "Home" }),
                Object(o.jsx)("a", {
                  id: "about",
                  href: "/",
                  children: "About",
                }),
                Object(o.jsx)("a", {
                  id: "contact",
                  href: "/",
                  children: "Contact",
                }),
                Object(o.jsx)("a", { href: "html", children: "Settings" }),
              ],
            })
          );
        };
      n(13);
      var d = function () {
          var e = function (e) {
            return fetch("{{serverip}}/".concat(e));
          };
          return Object(o.jsxs)("div", {
            className: "map",
            children: [
              Object(o.jsx)("h2", {
                className: "header",
                children: "Map Controls",
              }),
              Object(o.jsx)("hr", {}),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("america");
                },
                children: " America",
              }),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("metars");
                },
                children: " Metars",
              }),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("red");
                },
                children: " Red",
              }),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("blue");
                },
                children: " Blue",
              }),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("green");
                },
                children: " Green",
              }),
              Object(o.jsx)("button", {
                onClick: function () {
                  return e("off");
                },
                children: " Off",
              }),
            ],
          });
        },
        h = function () {
          return Object(o.jsxs)("div", {
            className: "content",
            children: [Object(o.jsx)("hr", {}), Object(o.jsx)(d, {})],
          });
        };
      var O = function () {
        var e = Object(c.useState)(!1),
          t = Object(j.a)(e, 2),
          n = t[0],
          r = t[1];
        return Object(o.jsxs)("div", {
          className: "App",
          children: [
            Object(o.jsx)(l, { menu: n, setMenu: r }),
            Object(o.jsx)(b, { menu: n, setMenu: r }),
            Object(o.jsx)(h, {}),
          ],
        });
      };
      i.a.render(
        Object(o.jsx)(r.a.StrictMode, { children: Object(o.jsx)(O, {}) }),
        document.getElementById("root")
      );
    },
  },
  [[14, 1, 2]],
]);
//# sourceMappingURL=main.817994c9.chunk.js.map
