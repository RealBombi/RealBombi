"""Generates the animated SVG assets for the RealBombi profile README.

Edit the text/colors below, then run:  python scripts/build_assets.py
"""
import os, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

W = 1000
SANS = "'Inter','Segoe UI',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular','JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',Menlo,monospace"
BG, PANEL, BORDER = "#0a0e16", "#0d1320", "#1c2533"
CYAN, BLUE, VIOLET = "#00c2ff", "#2f6bff", "#8b5cf6"
TEXT, MUTED, DIM = "#e6edf3", "#8b949e", "#566377"
GREEN, AMBER, ORANGE, RED = "#2ee59d", "#f5b342", "#ff8a3d", "#ff4d6d"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, body, style="", defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none">
<defs>{defs}</defs>
<style>
.s{{font-family:{SANS}}} .m{{font-family:{MONO}}}
{style}
</style>
{body}
</svg>
'''


def save(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)


def card(w, h):
    return f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="{BG}" stroke="{BORDER}"/>'


def label(x, y, txt, anchor="start", color=DIM):
    return f'<text x="{x}" y="{y}" class="m" font-size="12" letter-spacing="3" fill="{color}" text-anchor="{anchor}">{esc(txt)}</text>'


def pulse_dot(x, y, color, r=4.5, dur=2):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity=".45">'
            f'<animate attributeName="r" values="{r};{r*3}" dur="{dur}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values=".5;0" dur="{dur}s" repeatCount="indefinite"/></circle>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')


# ---------------------------------------------------------------- hero
def hero():
    w, h = W, 380
    defs = f'''
<clipPath id="c"><rect width="{w}" height="{h}" rx="20"/></clipPath>
<radialGradient id="g1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".9"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".75"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<radialGradient id="g3"><stop offset="0" stop-color="{CYAN}" stop-opacity=".6"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="38"/></filter>
<filter id="glow" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="16"/></filter>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.1" fill="#fff" fill-opacity=".11"/></pattern>
<radialGradient id="fade" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>
<mask id="mk"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{w}" y2="0" spreadMethod="repeat">
  <stop offset="0" stop-color="#eef7ff"/><stop offset=".36" stop-color="#eef7ff"/>
  <stop offset=".47" stop-color="{CYAN}"/><stop offset=".55" stop-color="#b6a1ff"/>
  <stop offset=".66" stop-color="#eef7ff"/><stop offset="1" stop-color="#eef7ff"/>
  <animateTransform attributeName="gradientTransform" type="translate" from="-{w} 0" to="{w} 0" dur="7s" repeatCount="indefinite"/>
</linearGradient>
<linearGradient id="sweep" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="{VIOLET}" stop-opacity=".55"/></linearGradient>
'''
    style = '''
.b1{animation:d1 16s ease-in-out infinite alternate}
.b2{animation:d2 19s ease-in-out infinite alternate}
.b3{animation:d3 13s ease-in-out infinite alternate}
@keyframes d1{to{transform:translate(240px,50px)}}
@keyframes d2{to{transform:translate(-230px,-40px)}}
@keyframes d3{to{transform:translate(-120px,60px)}}
.sw{animation:sw 8s cubic-bezier(.6,0,.4,1) infinite}
@keyframes sw{0%{transform:translateX(-300px) skewX(-20deg)}55%,100%{transform:translateX(1200px) skewX(-20deg)}}
.in{animation:in 1.2s cubic-bezier(.2,.8,.2,1) both}
.i1{animation-delay:.1s}.i2{animation-delay:.3s}.i3{animation-delay:.5s}.i4{animation-delay:.7s}
@keyframes in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
'''
    cx = w / 2
    corners = ""
    for (x, y, dx, dy) in [(22, 22, 1, 1), (w-22, 22, -1, 1), (22, h-22, 1, -1), (w-22, h-22, -1, -1)]:
        corners += f'<path d="M{x} {y+dy*14}V{y}H{x+dx*14}" stroke="#ffffff" stroke-opacity=".25" stroke-width="1.5"/>'
    body = f'''
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="#05080e"/>
  <g filter="url(#blur)">
    <circle class="b1" cx="230" cy="110" r="210" fill="url(#g1)"/>
    <circle class="b2" cx="790" cy="270" r="230" fill="url(#g2)"/>
    <circle class="b3" cx="600" cy="40" r="160" fill="url(#g3)"/>
  </g>
  <rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#mk)"/>
  <rect class="sw" x="0" y="-60" width="180" height="{h+120}" fill="url(#sweep)"/>
  {corners}
  <g class="in i1">
    {pulse_dot(50, 52, GREEN, 3.5)}
    <text x="64" y="56.5" class="m" font-size="12" letter-spacing="3" fill="#9fb0c7">ONLINE</text>
    <text x="{w-50}" y="56.5" class="m" font-size="12" letter-spacing="3" fill="#9fb0c7" text-anchor="end">~/REALBOMBI</text>
  </g>
  <g class="in i1">
    <rect x="{cx-215}" y="96" width="430" height="34" rx="17" fill="#ffffff" fill-opacity=".04" stroke="#ffffff" stroke-opacity=".14"/>
    <text x="{cx}" y="118" class="m" font-size="12.5" letter-spacing="3.2" fill="#b9c6d8" text-anchor="middle">IT OPERATIONS  /  AI BUILDER  /  HOMELAB</text>
  </g>
  <g class="in i2">
    <text x="{cx}" y="222" class="s" font-size="96" font-weight="800" letter-spacing="-3" fill="{CYAN}" opacity=".45" text-anchor="middle" filter="url(#glow)">Mads Ihle</text>
    <text x="{cx}" y="222" class="s" font-size="96" font-weight="800" letter-spacing="-3" fill="url(#shine)" text-anchor="middle">Mads Ihle</text>
  </g>
  <text x="{cx}" y="270" class="s in i3" font-size="19" fill="#9fb0c7" text-anchor="middle">Building, breaking, hosting, fixing, and occasionally over-engineering things.</text>
  <g class="in i4">
    <text x="50" y="{h-46}" class="m" font-size="12" letter-spacing="3" fill="#6f8098">NORWAY  ·  CET</text>
    <text x="{w-50}" y="{h-46}" class="m" font-size="12" letter-spacing="3" fill="#6f8098" text-anchor="end">CLAUDE  ·  CODEX  ·  PROXMOX</text>
  </g>
</g>
<rect x=".75" y=".75" width="{w-1.5}" height="{h-1.5}" rx="19.5" stroke="url(#edge)" stroke-width="1.5"/>
'''
    save("hero.svg", svg(w, h, body, style, defs))


# ---------------------------------------------------------------- terminal
def terminal():
    w = W
    fs, lh, x0 = 17, 34, 36
    prompt = [("mads", CYAN), ("@", DIM), ("homelab", VIOLET), (":", DIM), ("~", "#7aa2ff"), ("$ ", DIM)]
    pw = x0 + 16 * 11  # prompt width incl. left padding; clip starts here
    lines = [
        ("cmd", "whoami", 0.5, 0.45),
        ("out", [("Mads Ihle", TEXT), ("  //  ", DIM), ("IT Operations Coordinator", CYAN), ("  //  ", DIM), ("Norway", TEXT)], 1.05),
        ("cmd", "cat ~/focus.txt", 1.6, 0.7),
        ("out", [("ai tooling   infrastructure   servers   automation   security", "#c9d1d9")], 2.45),
        ("cmd", "systemctl list-units --homelab", 3.0, 1.0),
        ("out", [("proxmox ", "#c9d1d9"), ("active", GREEN), ("   docker ", "#c9d1d9"), ("active", GREEN),
                 ("   plex ", "#c9d1d9"), ("active", GREEN), ("   linux ", "#c9d1d9"), ("active", GREEN)], 4.15),
        ("cmd", "ai --stack", 4.7, 0.5),
        ("out", [("claude", "#ff9b73"), ("  codex", TEXT), ("    ", DIM), ("idea -> prototype, way faster", MUTED)], 5.35),
        ("cmd", "git log --oneline -1", 5.9, 0.75),
        ("out", [("a1b2c3d ", AMBER), ("rebuild homelab (again). this time it's clean. promise.", "#c9d1d9")], 6.8),
    ]
    top = 44
    y = top + 46
    body_lines = ""
    defs = ""
    for i, ln in enumerate(lines):
        if ln[0] == "cmd":
            _, cmd, s, d = ln
            T = s + d
            full = pw + len(cmd) * 11.5 + 12
            defs += (f'<clipPath id="l{i}"><rect x="0" y="{y-lh+8}" width="{full}" height="{lh}">'
                     f'<animate attributeName="width" values="{pw};{pw};{full}" keyTimes="0;{s/T:.3f};1" dur="{T}s" fill="freeze"/></rect></clipPath>')
            spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in prompt) + f'<tspan fill="{TEXT}">{esc(cmd)}</tspan>'
            body_lines += (f'<g clip-path="url(#l{i})"><text x="{x0}" y="{y}" class="m" font-size="{fs}" xml:space="preserve">{spans}</text>'
                           f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{s/(s+.05):.3f};{(s+.01)/(s+.05):.3f};1" dur="{s+.05}s" fill="freeze"/></g>')
            y += lh
        else:
            _, parts, s = ln
            spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in parts)
            body_lines += (f'<text x="{x0}" y="{y}" class="m" font-size="{fs}" xml:space="preserve">{spans}'
                           f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{s/(s+.35):.3f};1" dur="{s+.35}s" fill="freeze"/></text>')
            y += lh + 12
    s = 7.35
    spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in prompt)
    body_lines += (f'<g><text x="{x0}" y="{y}" class="m" font-size="{fs}" xml:space="preserve">{spans}'
                   f'<tspan fill="{CYAN}">\u2588<animate attributeName="fill-opacity" values="1;0" dur="1.06s" calcMode="discrete" repeatCount="indefinite"/></tspan></text>'
                   f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{s/(s+.05):.3f};1" dur="{s+.05}s" fill="freeze"/></g>')
    h = y + 34
    dots = "".join(f'<circle cx="{28+i*20}" cy="22" r="6" fill="{c}"/>' for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]))
    body = f'''
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14" fill="{BG}" stroke="{BORDER}"/>
<path d="M.5 14.5a14 14 0 0 1 14-14h{w-29}a14 14 0 0 1 14 14V{top}H.5z" fill="{PANEL}"/>
<line x1="0" y1="{top}" x2="{w}" y2="{top}" stroke="{BORDER}"/>
{dots}
<text x="{w/2}" y="27" class="m" font-size="13" fill="{DIM}" text-anchor="middle">mads@homelab: ~  (zsh)</text>
{body_lines}
'''
    save("terminal.svg", svg(w, h, body, "", defs))


# ---------------------------------------------------------------- status
def status():
    w = W
    pad, gap = 22, 14
    tw = (w - 2 * pad - 2 * gap) / 3
    th = 128
    services = [
        ("mads.service", "OPERATIONAL", GREEN, "Running on coffee, zero downtime", "g"),
        ("it-ops.service", "OPERATIONAL", GREEN, "Weekdays, 08:00 to 16:00 CET", "g"),
        ("ai-copilots.service", "OPERATIONAL", GREEN, "Claude and Codex on shift", "g"),
        ("homelab.service", "DEGRADED", AMBER, "Mid-rebuild. Cleaner this time.", "a"),
        ("side-projects.service", "OVER CAPACITY", ORANGE, "Spawning faster than they finish", "o"),
        ("sleep.service", "MAJOR OUTAGE", RED, "Commits at 02:00 say it all", "r"),
    ]
    rnd = random.Random(7)
    head = 64
    tiles = ""
    style = ".bar{animation:bar .5s ease-out both}@keyframes bar{from{opacity:0;transform:scaleY(.2)}to{opacity:1;transform:none}}.bar{transform-box:fill-box;transform-origin:bottom}"
    for i, (name, st, col, note, kind) in enumerate(services):
        cx = pad + (i % 3) * (tw + gap)
        cy = head + (i // 3) * (th + gap)
        bars = ""
        n, bw, bg_ = 26, 7, 3.6
        for b in range(n):
            r = rnd.random()
            if kind == "g":
                c = GREEN if r > .04 else AMBER
            elif kind == "a":
                c = AMBER if (r < .35 or b > 21) else GREEN
            elif kind == "o":
                c = ORANGE if r < b / n + .1 else GREEN
            else:
                c = RED if r < .78 else GREEN
            delay = .2 + i * .12 + b * .025
            bars += f'<rect class="bar" style="animation-delay:{delay:.2f}s" x="{cx+18+b*(bw+bg_):.1f}" y="{cy+96}" width="{bw}" height="16" rx="2" fill="{c}" fill-opacity=".85"/>'
        tiles += f'''
<rect x="{cx:.1f}" y="{cy}" width="{tw:.1f}" height="{th}" rx="12" fill="{PANEL}" stroke="{BORDER}"/>
<text x="{cx+18:.1f}" y="{cy+31}" class="m" font-size="15" fill="{TEXT}">{name}</text>
{pulse_dot(cx+tw-22, cy+26, col, 4, 1.6 + i*.2)}
<text x="{cx+18:.1f}" y="{cy+55}" class="m" font-size="11" letter-spacing="2" fill="{col}">{st}</text>
<text x="{cx+18:.1f}" y="{cy+79}" class="s" font-size="14" fill="{MUTED}">{esc(note)}</text>
{bars}'''
    h = head + 2 * th + gap + pad
    body = f'''
{card(w, h)}
{label(pad+2, 38, "SYSTEM STATUS")}
{pulse_dot(w-pad-190, 34, AMBER, 3.5)}
<text x="{w-pad-2}" y="38.5" class="m" font-size="12" letter-spacing="2" fill="{MUTED}" text-anchor="end">MOSTLY OPERATIONAL</text>
{tiles}
'''
    save("status.svg", svg(w, h, body, style))


# ---------------------------------------------------------------- pipeline
def pipeline():
    w, h = W, 212
    pad = 22
    nodes = [("IDEA", "random thought"), ("PROMPT", "claude / codex"), ("PROTOTYPE", "make it run"),
             ("BREAK IT", "on purpose"), ("DEBUG", "learn why"), ("SHIP", "...sometimes")]
    nw, nh = 132, 66
    gap = (w - 2 * pad - 6 * nw) / 5
    y = 70
    style = f'''
.flow{{stroke-dasharray:3 7;animation:flow 1s linear infinite}}
@keyframes flow{{to{{stroke-dashoffset:-10}}}}
.hl{{opacity:0;animation:hl 6s ease-in-out infinite}}
@keyframes hl{{0%,4%{{opacity:0}}9%,16%{{opacity:1}}22%,100%{{opacity:0}}}}
'''
    defs = f'''<linearGradient id="hg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
<filter id="ng" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="8"/></filter>'''
    nodes_y = 70
    spark_path = "M" + " L".join(f"{pad + i * (nw + gap) + nw / 2:.1f} {nodes_y + nh / 2}" for i in range(6))
    spark = (f'<circle r="3.5" fill="{CYAN}"><animateMotion dur="6s" repeatCount="indefinite" path="{spark_path}"/></circle>'
             f'<circle r="9" fill="{CYAN}" opacity=".25"><animateMotion dur="6s" repeatCount="indefinite" path="{spark_path}"/></circle>')
    body = card(w, h) + spark + label(pad + 2, 38, "HOW I BUILD") + \
        f'<text x="{w-pad-2}" y="38.5" class="m" font-size="12" letter-spacing="2" fill="{MUTED}" text-anchor="end">LOOP UNTIL IT WORKS</text>'
    centers = []
    for i, (t, sub) in enumerate(nodes):
        x = pad + i * (nw + gap)
        centers.append((x + nw / 2, y + nh / 2))
        if i < 5:
            body += f'<line class="flow" x1="{x+nw+4:.1f}" y1="{y+nh/2}" x2="{x+nw+gap-4:.1f}" y2="{y+nh/2}" stroke="{DIM}" stroke-width="2"/>'
        body += f'''
<rect class="hl" style="animation-delay:{i}s" x="{x:.1f}" y="{y}" width="{nw}" height="{nh}" rx="12" fill="url(#hg)" opacity="0" filter="url(#ng)"/>
<rect x="{x:.1f}" y="{y}" width="{nw}" height="{nh}" rx="12" fill="{PANEL}" stroke="{BORDER}"/>
<rect class="hl" style="animation-delay:{i}s" x="{x:.1f}" y="{y}" width="{nw}" height="{nh}" rx="12" stroke="url(#hg)" stroke-width="1.5" fill="none"/>
<text x="{x+nw/2:.1f}" y="{y+29}" class="m" font-size="14" font-weight="700" letter-spacing="1.5" fill="{TEXT}" text-anchor="middle">{esc(t)}</text>
<text x="{x+nw/2:.1f}" y="{y+49}" class="s" font-size="13" fill="{MUTED}" text-anchor="middle">{esc(sub)}</text>'''
    # loop back: DEBUG -> PROTOTYPE
    (x1, _), (x2, _) = centers[4], centers[2]
    yb = y + nh
    loop = f"M{x1} {yb+4} C{x1} {yb+52} {x2} {yb+52} {x2} {yb+8}"
    body += f'<path class="flow" d="{loop}" stroke="{VIOLET}" stroke-opacity=".7" stroke-width="2"/>'
    body += f'<path d="M{x2-5} {yb+15} L{x2} {yb+7} L{x2+5} {yb+15}" stroke="{VIOLET}" stroke-opacity=".8" stroke-width="2"/>'
    body += f'<text x="{(x1+x2)/2}" y="{yb+56}" class="m" font-size="11.5" letter-spacing="2" fill="#8f7ad6" text-anchor="middle">REPEAT</text>'
    save("pipeline.svg", svg(w, h, body, style, defs))


# ---------------------------------------------------------------- timeline
def timeline():
    w, h = W, 262
    pad = 22
    ly = 112
    xs = [180, 500, 820]
    items = [
        ("2022 - 2023", "Full-Stack Developer", "Omega 365  /  part-time", "Real-world development projects", CYAN, False),
        ("2023 - NOW", "IT Operations Coordinator", "Infrastructure  /  operations", "Servers, systems and keeping things up", GREEN, True),
        ("NEXT", "Leveling up", "Kubernetes  /  Azure  /  AI agents", "Cleaner deployments, more automation", VIOLET, False),
    ]
    style = '''
.draw{stroke-dasharray:700;stroke-dashoffset:700;animation:draw 1.8s cubic-bezier(.6,0,.2,1) .2s forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.dash{stroke-dasharray:4 7;animation:flow 1.2s linear infinite}
@keyframes flow{to{stroke-dashoffset:-11}}
.in{animation:in .9s cubic-bezier(.2,.8,.2,1) both}
@keyframes in{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
'''
    defs = f'<linearGradient id="lg" gradientUnits="userSpaceOnUse" x1="52" y1="0" x2="500" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity=".2"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>'
    body = card(w, h) + label(pad + 2, 38, "CAREER.LOG")
    body += f'<line x1="{pad+30}" y1="{ly}" x2="{w-pad-30}" y2="{ly}" stroke="{BORDER}" stroke-width="2"/>'
    body += f'<line class="draw" x1="{pad+30}" y1="{ly}" x2="{xs[1]}" y2="{ly}" stroke="url(#lg)" stroke-width="2.5"/>'
    body += f'<line class="dash" x1="{xs[1]+14}" y1="{ly}" x2="{w-pad-30}" y2="{ly}" stroke="{VIOLET}" stroke-opacity=".6" stroke-width="2"/>'
    for i, (yr, title, sub, desc, col, now) in enumerate(items):
        x = xs[i]
        d = f"animation-delay:{.4+i*.35:.2f}s"
        node = pulse_dot(x, ly, col, 6, 1.8) if now else (
            f'<circle cx="{x}" cy="{ly}" r="6" fill="{BG}" stroke="{col}" stroke-width="2"' + (' stroke-dasharray="3 3"' if i == 2 else '') + '/>')
        body += f'''<g class="in" style="{d}">
<text x="{x}" y="{ly-26}" class="m" font-size="12.5" letter-spacing="2.5" fill="{col}" text-anchor="middle">{yr}</text>
{node}
<text x="{x}" y="{ly+46}" class="s" font-size="19" font-weight="700" fill="{TEXT if i < 2 else '#c4b5fd'}" text-anchor="middle">{esc(title)}</text>
<text x="{x}" y="{ly+72}" class="m" font-size="12.5" fill="{MUTED}" text-anchor="middle">{esc(sub)}</text>
<text x="{x}" y="{ly+98}" class="s" font-size="14" fill="{DIM}" text-anchor="middle">{esc(desc)}</text>
</g>'''
    save("timeline.svg", svg(w, h, body, style, defs))


# ---------------------------------------------------------------- footer
def footer():
    w, h = W, 230
    defs = f'''
<clipPath id="c"><rect width="{w}" height="{h}" rx="20"/></clipPath>
<radialGradient id="g1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".7"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".6"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.1" fill="#fff" fill-opacity=".08"/></pattern>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".5"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".5"/></linearGradient>
'''
    style = '''
.b1{animation:d1 15s ease-in-out infinite alternate}
.b2{animation:d2 18s ease-in-out infinite alternate}
@keyframes d1{to{transform:translate(300px,30px)}}
@keyframes d2{to{transform:translate(-300px,-20px)}}
'''
    body = f'''
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="#05080e"/>
  <g filter="url(#blur)">
    <circle class="b1" cx="260" cy="200" r="190" fill="url(#g1)"/>
    <circle class="b2" cx="760" cy="40" r="190" fill="url(#g2)"/>
  </g>
  <rect width="{w}" height="{h}" fill="url(#dots)"/>
  <text x="{w/2}" y="96" class="s" font-size="34" font-weight="700" letter-spacing="-1" fill="#eef7ff" text-anchor="middle">Always learning. Usually building with AI.</text>
  <text x="{w/2}" y="132" class="s" font-size="18" fill="#9fb0c7" text-anchor="middle">Occasionally documenting it.</text>
  {pulse_dot(w/2-150, 176, GREEN, 3.5)}
  <text x="{w/2-136}" y="180.5" class="m" font-size="12.5" letter-spacing="2.5" fill="#8fa0b8">AVAILABLE WEEKDAYS  08:00 - 16:00 CET</text>
</g>
<rect x=".75" y=".75" width="{w-1.5}" height="{h-1.5}" rx="19.5" stroke="url(#edge)" stroke-width="1.5"/>
'''
    save("footer.svg", svg(w, h, body, style, defs))


# ---------------------------------------------------------------- section header
def section(slug, num, title, light=False):
    w, h = W, 56
    tcol = "#1f2328" if light else TEXT
    defs = f'<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".7"/><stop offset=".4" stop-color="{VIOLET}" stop-opacity=".35"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>' \
           f'<linearGradient id="gl" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    style = '.gl{animation:gl 5s ease-in-out infinite}@keyframes gl{0%{transform:translateX(-120px)}60%,100%{transform:translateX(1000px)}}'
    tx = 70 + len(title) * 14.5 + 20
    body = f'''
<text x="0" y="36" class="m" font-size="14" letter-spacing="2" fill="{CYAN}">{num}</text>
<text x="34" y="37" class="s" font-size="26" font-weight="700" letter-spacing="-.5" fill="{tcol}">{esc(title)}</text>
<rect x="{tx:.0f}" y="28" width="{w-tx:.0f}" height="1.5" fill="url(#ln)"/>
<clipPath id="cl"><rect x="{tx:.0f}" y="26" width="{w-tx:.0f}" height="6"/></clipPath>
<g clip-path="url(#cl)"><rect class="gl" x="0" y="28" width="120" height="1.5" fill="url(#gl)"/></g>
'''
    save(f"h-{slug}{'-light' if light else ''}.svg", svg(w, h, body, style, defs))


hero(); terminal(); status(); pipeline(); timeline(); footer()
for slug, num, title in [("about", "01", "About"), ("status", "02", "Status"), ("build", "03", "How I build"),
                         ("career", "04", "Career"), ("stack", "05", "Stack"), ("projects", "06", "Projects"),
                         ("activity", "07", "Activity")]:
    section(slug, num, title)
    section(slug, num, title, light=True)
print("ok", sorted(os.listdir(OUT)))
