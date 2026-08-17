import pathlib, base64, re
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def svg_inline(p,w):
    s=pathlib.Path(p).read_text()
    return re.sub(r'<svg ', f'<svg style="width:{w};height:auto;display:block" ', s, count=1)

NR=b64("newsreader-500-opsz21.ttf")
NRI=b64("node_modules/@fontsource-variable/newsreader/files/newsreader-latin-standard-italic.woff2")
I5=b64("node_modules/@fontsource/inter/files/inter-latin-500-normal.woff2")
I6=b64("node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2")
I7=b64("node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2")
EHO=b64("equal-housing.png"); QR=b64("qr-vcard.png")
IT8=b64("node_modules/@fontsource/inter-tight/files/inter-tight-latin-800-normal.woff2")
GOLD="#C08A2D"
BUST=b64("panel-white.jpg"); FIG=b64("fig-right.png")
INK="#0E1B2A"; PAPER="#FFFFFF"; STEEL="#33506F"; MUTED="#5D6B7A"; LINE="#DBE1E8"

CSS=f"""
@font-face{{font-family:NR;src:url(data:font/ttf;base64,{NR}) format('truetype');font-weight:500;font-style:normal}}
@font-face{{font-family:NR;src:url(data:font/woff2;base64,{NRI}) format('woff2');font-weight:200 800;font-style:italic}}
@font-face{{font-family:IN;src:url(data:font/woff2;base64,{I5}) format('woff2');font-weight:500}}
@font-face{{font-family:IN;src:url(data:font/woff2;base64,{I6}) format('woff2');font-weight:600}}
@font-face{{font-family:IN;src:url(data:font/woff2;base64,{I7}) format('woff2');font-weight:700}}
@font-face{{font-family:IT;src:url(data:font/woff2;base64,{IT8}) format('woff2');font-weight:800}}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
@page{{size:3.75in 2.25in;margin:0}}
html,body{{width:3.75in}}
.card{{width:3.75in;height:2.25in;position:relative;overflow:hidden;page-break-after:always;font-family:IN,Arial,sans-serif}}
.card:last-child{{page-break-after:auto}}
.paper{{background:{PAPER}}} .navy{{background:{INK}}}
.safe{{position:absolute;left:.25in;top:.25in;right:.25in;bottom:.25in}}
.nm{{white-space:nowrap;font-family:NR,serif;font-weight:500;color:{INK};font-size:19pt;line-height:1;letter-spacing:.004em}}
.role{{font-family:IN;font-weight:700;font-size:6pt;letter-spacing:.15em;text-transform:uppercase;color:{STEEL};margin-top:5.5pt}}
.nmls{{font-family:IN;font-weight:600;font-size:6.4pt;color:{MUTED};margin-top:3.5pt;letter-spacing:.01em}}
.rule{{height:.6pt;background:{LINE};margin:7.5pt 0 7pt;max-width:1.55in}}
.org{{font-family:IN;font-weight:600;font-size:7pt;color:{INK};line-height:1.45}}
.org span{{font-weight:500;color:{MUTED}}}
.con{{font-family:IN;font-weight:500;font-size:7.6pt;color:{INK};line-height:1.62}}
.con .u{{font-size:6.2pt;letter-spacing:.005em}}
.con .u{{color:{STEEL};font-weight:600}}
.foot{{position:absolute;left:0;bottom:0;display:flex;align-items:flex-end;gap:9pt}}
.eho{{width:14pt;opacity:.5}}
/* photo treatments */
.panelbox{{position:absolute;left:0;top:0;bottom:0;width:1.32in;overflow:hidden}}
.panelboxR{{position:absolute;right:0;top:0;bottom:0;width:1.32in;overflow:hidden}}
.panelboxR img{{width:100%;height:100%;object-fit:cover;object-position:50% 50%;display:block}}

.panelbox img{{width:100%;height:100%;object-fit:cover;object-position:50% 50%;display:block}}
.panelbox::after{{content:"";position:absolute;right:0;top:0;bottom:0;width:.34in;
      background:linear-gradient(90deg,rgba(245,247,249,0) 0%,{PAPER} 92%)}}
.fig{{position:absolute;right:.20in;bottom:-.04in;width:1.32in;height:auto}}
/* back */
.bk{{height:100%;display:flex;flex-direction:column;justify-content:space-between}}
.stmt{{font-family:NR,serif;font-weight:500;color:#fff;font-size:16.5pt;line-height:1.14;max-width:2.05in}}
.stmt em{{font-style:italic;font-weight:400;color:#9db8d4}}
.four{{display:grid;grid-template-columns:1fr;gap:2.6pt;margin-top:9pt}}
.four div{{font-family:IN;font-weight:600;font-size:6.3pt;letter-spacing:.055em;text-transform:uppercase;color:#a9c0d6}}
.rowq{{display:flex;align-items:flex-end;justify-content:space-between;gap:10pt}}
.qr{{width:.90in;height:.90in;flex:0 0 auto;background:#fff;border-radius:3pt;padding:2pt}}
.qr img{{width:100%;height:100%;display:block}}
.qrl{{font-family:IN;font-weight:400;font-size:5.8pt;letter-spacing:.02em;line-height:1.3;color:#9fb6cc;margin-top:5pt;text-align:center;width:.94in;margin-left:auto;margin-right:auto}}
.types{{display:grid;grid-template-columns:1fr;gap:5.5pt}}
.types div{{font-family:IN;font-weight:600;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;color:#FFFFFF}}
.types div span{{color:#9fb6cc;font-weight:400;font-size:7pt}}
.mid{{height:100%;display:flex;align-items:center;justify-content:space-between;gap:14pt}}
.nmlsline{{position:absolute;left:0;right:0;bottom:0;font-family:IN;font-weight:500;font-size:5.2pt;color:#b9cbdb;letter-spacing:.012em;white-space:nowrap}}
.tiny{{font-family:IN;font-weight:500;font-size:5pt;line-height:1.5;color:#7f93a8}}
.qrwrap{{position:absolute;right:0;top:.02in;text-align:center}}
"""

def ident():
    return f"""
  <div class="nm">Andrew Durden</div>
  <div class="role">Mortgage Loan Originator</div>
  <div class="nmls">NMLS #2774438</div>
  <div class="rule"></div>
  <div class="org">Loan Factory, Inc. <span>NMLS #320841</span></div>"""

def contact(width):
    return f"""
  <div class="foot" style="max-width:{width}">
    <div class="con">
      (561) 419-5308<br>
      andrew.durden@loanfactory.com
    </div>
    <img class="eho" src="data:image/png;base64,{EHO}">
  </div>"""

FRONT_BUST = f"""
<div class="card paper">
  <div class="panelbox"><img src="data:image/jpeg;base64,{BUST}"></div>
  <div class="safe" style="left:1.46in">{ident()}{contact("2.0in")}</div>
</div>"""

FRONT_FIG = f"""
<div class="card paper">
  <img class="fig" src="data:image/png;base64,{FIG}">
  <div class="safe" style="right:1.60in">{ident()}{contact("2.0in")}</div>
</div>"""

BACK = f"""
<div class="card navy"><div class="safe"><div class="mid">
      <div class="types">
        <div>Purchase <span>&middot; Florida</span></div>
        <div>Refinance <span>&middot; Florida</span></div>
        <div>DSCR rental <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>
      <div style="text-align:center;width:.94in">
        <div class="qr"><img src="data:image/png;base64,{QR}"></div>
        <div class="qrl">Scan to save</div>
      </div>
</div></div></div>"""

BACK2 = f"""
<div class="card navy"><div class="safe"><div class="mid">
      <div class="types">
        <div>Purchase <span>&middot; Florida</span></div>
        <div>Refinance <span>&middot; Florida</span></div>
        <div>DSCR rental <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>
      <div style="text-align:center;width:.94in">
        <div class="qr"><img src="data:image/png;base64,{QR}"></div>
        <div class="qrl">Scan to save</div>
      </div>
</div>
  <div class="nmlsline">Andrew Durden NMLS #2774438 &middot; Loan Factory, Inc. NMLS #320841 &middot; Equal Housing Lender</div>
</div></div>"""

def page(cards,name):
    pathlib.Path(name).write_text(f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(cards)}</body></html>")
page([FRONT_BUST,BACK],"v1-bust.html")
page([FRONT_FIG,BACK],"v2-figure.html")
page([FRONT_BUST,BACK2],"v1-bust-nmls.html")
page([FRONT_FIG,BACK2],"v2-figure-nmls.html")
page([BACK,BACK2],"backs.html")
print("built")

TYPES_B = """      <div class="types">
        <div>Home purchase <span>&middot; Florida</span></div>
        <div>Refinance <span>&middot; Florida</span></div>
        <div>DSCR rental <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""
TYPES_C = """      <div class="types" style="gap:8pt">
        <div>Home loans <span>&middot; Florida, purchase and refinance</span></div>
        <div>DSCR rental loans <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""
QRB = f"""      <div style="text-align:center;width:.94in">
        <div class="qr"><img src="data:image/png;base64,{QR}"></div>
        <div class="qrl">Scan to save</div>
      </div>"""
BACK_B = f"""<div class="card navy"><div class="safe"><div class="mid">{TYPES_B}
{QRB}</div></div></div>"""
BACK_C = f"""<div class="card navy"><div class="safe"><div class="mid">{TYPES_C}
{QRB}</div></div></div>"""
page([BACK,BACK_B,BACK_C],"backopts.html")

FRONT_PANEL_R = f"""
<div class="card paper">
  <div class="panelboxR"><img src="data:image/jpeg;base64,{BUST}"></div>
  <div class="safe" style="right:1.46in">{ident()}{contact("2.0in")}</div>
</div>"""
page([FRONT_BUST,BACK2],"f-left.html")
page([FRONT_PANEL_R,BACK2],"f-right.html")
page([FRONT_BUST,FRONT_PANEL_R,BACK2],"f-both.html")

TYPES_D = """      <div class="types" style="gap:9pt">
        <div>Home loans <span>&middot; Florida</span></div>
        <div>DSCR rental loans <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""
TYPES_E = """      <div class="types" style="gap:9pt">
        <div>Home purchase &amp; refinance <span>&middot; Florida</span></div>
        <div>DSCR rental loans <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""
NMLSLINE = '<div class="nmlsline">Andrew Durden NMLS #2774438 &middot; Loan Factory, Inc. NMLS #320841 &middot; Equal Housing Lender</div>'
BACK_D = f"""<div class="card navy"><div class="safe"><div class="mid">{TYPES_D}
{QRB}</div>{NMLSLINE}</div></div>"""
BACK_E = f"""<div class="card navy"><div class="safe"><div class="mid">{TYPES_E}
{QRB}</div>{NMLSLINE}</div></div>"""
page([BACK_D,BACK_E],"back-white.html")
page([FRONT_BUST,BACK_D],"card-final-left.html")
page([FRONT_PANEL_R,BACK_D],"card-final-right.html")

PENCIL_A = f"""      <div style="margin-top:11pt;padding-top:9pt;border-top:.6pt solid rgba(255,255,255,.16)">
        <div style="font-family:IT;font-weight:800;font-size:10pt;color:#fff;letter-spacing:-.012em;line-height:1">Pencil<span style="color:{GOLD}">.</span></div>
        <div style="font-family:IN;font-weight:500;font-size:5.9pt;color:#9fb6cc;letter-spacing:.02em;margin-top:3.5pt;white-space:nowrap">
          My free tool. Does the deal pencil? &middot; pencildscr.com</div>
      </div>"""
PENCIL_B = f"""      <div style="margin-top:12pt;padding:8pt 10pt;background:rgba(192,138,45,.10);border-left:1.6pt solid {GOLD};border-radius:0 3pt 3pt 0">
        <div style="font-family:IT;font-weight:800;font-size:10pt;color:#fff;letter-spacing:-.012em;line-height:1">Pencil<span style="color:{GOLD}">.</span></div>
        <div style="font-family:IN;font-weight:500;font-size:5.9pt;color:#cfe0ef;letter-spacing:.02em;margin-top:3pt">
          My free tool. Does the deal pencil?<br>pencildscr.com</div>
      </div>"""
TYPES_P = """      <div class="types" style="gap:8pt">
        <div>Home loans <span>&middot; Florida</span></div>
        <div>DSCR rental loans <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""
FRONT_R = f"""
<div class="card paper">
  <div class="panelboxR"><img src="data:image/jpeg;base64,{BUST}"></div>
  <div class="safe" style="right:1.46in">{ident()}{contact("2.0in")}</div>
</div>"""
def backp(pencil):
    return f"""<div class="card navy"><div class="safe">
  <div style="display:flex;justify-content:space-between;gap:12pt">
    <div style="flex:1">{TYPES_P}
{pencil}
    </div>
{QRB}
  </div>
  {NMLSLINE}
</div></div>"""
BACK_P1 = backp(PENCIL_A); BACK_P2 = backp(PENCIL_B)
page([FRONT_R,BACK_P1],"pencil-a.html")
page([FRONT_R,BACK_P2],"pencil-b.html")
page([FRONT_R,BACK_P1,BACK_P2],"pencil-both.html")

LINES = [("Does a rental pencil? Know in under 60 seconds.", "final")]
def pencil_line(txt):
    return f"""      <div style="margin-top:11pt;padding-top:9pt;border-top:.6pt solid rgba(255,255,255,.16)">
        <div style="font-family:IT;font-weight:800;font-size:10pt;color:#fff;letter-spacing:-.012em;line-height:1">Pencil<span style="color:{GOLD}">.</span></div>
        <div style="font-family:IN;font-weight:500;font-size:6pt;color:#9fb6cc;letter-spacing:.02em;margin-top:3.5pt;line-height:1.45;max-width:1.98in">
          My free tool. {txt}</div>
        <div style="font-family:IN;font-weight:600;font-size:6pt;color:#cfe0ef;letter-spacing:.02em;margin-top:1.5pt">pencildscr.com</div>
      </div>"""
def backline(txt):
    return f"""<div class="card navy"><div class="safe">
  <div style="display:flex;justify-content:space-between;gap:12pt">
    <div style="flex:1">{TYPES_P}
{pencil_line(txt)}
    </div>
{QRB}
  </div>
  {NMLSLINE}
</div></div>"""
page([FRONT_R, backline(LINES[0][0])], "card-FINAL.html")
