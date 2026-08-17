import pathlib, base64

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

NR  = b64("newsreader-500-opsz21.ttf")
I5  = b64("node_modules/@fontsource/inter/files/inter-latin-500-normal.woff2")
I6  = b64("node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2")
I7  = b64("node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2")
IT8 = b64("node_modules/@fontsource/inter-tight/files/inter-tight-latin-800-normal.woff2")
EHO = b64("equal-housing.png")
QR  = b64("qr-vcard.png")
BUST = b64("panel-white.jpg")

INK="#0E1B2A"; PAPER="#FFFFFF"; STEEL="#33506F"; MUTED="#5D6B7A"; LINE="#DBE1E8"; GOLD="#C08A2D"

CSS = f"""
@font-face{{font-family:NR;src:url(data:font/ttf;base64,{NR}) format('truetype');font-weight:500;font-style:normal}}
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
.foot{{position:absolute;left:0;bottom:0;display:flex;align-items:flex-end;gap:9pt}}
.eho{{width:14pt;opacity:.5}}
.panelboxR{{position:absolute;right:0;top:0;bottom:0;width:1.32in;overflow:hidden}}
.panelboxR img{{width:100%;height:100%;object-fit:cover;object-position:50% 50%;display:block}}
.mid{{height:100%;display:flex;align-items:center;justify-content:space-between;gap:14pt}}
.types{{display:grid;grid-template-columns:1fr;gap:8pt}}
.types div{{font-family:IN;font-weight:600;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;color:#FFFFFF}}
.types div span{{color:#9fb6cc;font-weight:400;font-size:7pt}}
.qr{{width:.90in;height:.90in;flex:0 0 auto;background:#fff;border-radius:3pt;padding:2pt}}
.qr img{{width:100%;height:100%;display:block}}
.qrl{{font-family:IN;font-weight:400;font-size:5.8pt;letter-spacing:.02em;line-height:1.3;color:#9fb6cc;margin-top:5pt;text-align:center;width:.94in;margin-left:auto;margin-right:auto}}
.nmlsline{{position:absolute;left:0;right:0;bottom:0;font-family:IN;font-weight:500;font-size:5.2pt;color:#b9cbdb;letter-spacing:.012em;white-space:nowrap}}
"""

IDENT = f"""
  <div class="nm">Andrew Durden</div>
  <div class="role">Mortgage Loan Originator</div>
  <div class="nmls">NMLS #2774438</div>
  <div class="rule"></div>
  <div class="org">Loan Factory, Inc. <span>NMLS #320841</span></div>"""

CONTACT = f"""
  <div class="foot" style="max-width:2.0in">
    <div class="con">(561) 419-5308<br>andrew.durden@loanfactory.com</div>
    <img class="eho" src="data:image/png;base64,{EHO}">
  </div>"""

FRONT = f"""
<div class="card paper">
  <div class="panelboxR"><img src="data:image/jpeg;base64,{BUST}"></div>
  <div class="safe" style="right:1.46in">{IDENT}{CONTACT}</div>
</div>"""

TYPES = """      <div class="types">
        <div>Home loans <span>&middot; Florida</span></div>
        <div>DSCR rental loans <span>&middot; 40+ states</span></div>
        <div>Commercial <span>&middot; nationwide</span></div>
      </div>"""

PENCIL = f"""      <div style="margin-top:11pt;padding-top:9pt;border-top:.6pt solid rgba(255,255,255,.16)">
        <div style="font-family:IT;font-weight:800;font-size:10pt;color:#fff;letter-spacing:-.012em;line-height:1">Pencil<span style="color:{GOLD}">.</span></div>
        <div style="font-family:IN;font-weight:500;font-size:6pt;color:#9fb6cc;letter-spacing:.02em;margin-top:3.5pt;line-height:1.45;max-width:1.98in">
          Does a rental pencil?<br>Know in under 60 seconds.</div>
        <div style="font-family:IN;font-weight:600;font-size:6pt;color:#cfe0ef;letter-spacing:.02em;margin-top:1.5pt">pencildscr.com</div>
      </div>"""

QRB = f"""      <div style="text-align:center;width:.94in">
        <div class="qr"><img src="data:image/png;base64,{QR}"></div>
        <div class="qrl">Scan to save</div>
      </div>"""

NMLSLINE = '<div class="nmlsline">Andrew Durden NMLS #2774438 &middot; Loan Factory, Inc. NMLS #320841 &middot; Equal Housing Lender</div>'

BACK = f"""<div class="card navy"><div class="safe">
  <div style="display:flex;justify-content:space-between;gap:12pt">
    <div style="flex:1">{TYPES}
{PENCIL}
    </div>
{QRB}
  </div>
  {NMLSLINE}
</div></div>"""

def page(cards, name):
    pathlib.Path(name).write_text(
        f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(cards)}</body></html>")

page([FRONT, BACK], "card-FINAL.html")
page([FRONT], "front-only.html")
print("built card-FINAL.html")
