#!/usr/bin/env python3
"""BloomDay 'Surprise Me' Campaign Pack #2 — visual-heavy, minimal text"""

import re
import os
import sys

sys.path.insert(0, '/home/user/claudecode')
from bloomday_plants import PLANTS, sv, HP, GD, AL, plant

from playwright.sync_api import sync_playwright

OUTPUT_DIR = '/mnt/user-data/outputs'
WORK_DIR = '/home/user/claudecode'
CHROME_PATH = '/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome'

COLORS = {
    'dark':   '#2a2520',
    'sage':   '#5e7054',
    'cream':  '#f5f0e8',
    'green':  '#9ab06a',
    'text_light': '#f5f0e8',
    'text_dark':  '#2a2520',
    'muted_dark': '#9a8f84',
    'muted_sage': '#8da880',
    'muted_cream': '#9a9088',
    'accent_dark': '#9ab06a',
    'accent_sage': '#d4e8a8',
    'accent_cream': '#5e7054',
}


def make_html(w, h, bg_color, body_html):
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    width:{w}px; height:{h}px;
    background:{bg_color};
    font-family:'DM Sans',Arial,Helvetica,sans-serif;
    overflow:hidden;
  }}
</style>
</head><body>{body_html}</body></html>"""


def save_html(name, html):
    path = os.path.join(WORK_DIR, f"{name}.html")
    with open(path, 'w') as f:
        f.write(html)
    return path


def batch_screenshot(jobs):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH)
        for html_path, out_name, w, h in jobs:
            out_path = os.path.join(OUTPUT_DIR, f"bloomday_{out_name}.png")
            page = browser.new_page(viewport={'width': w, 'height': h})
            page.goto(f'file://{html_path}', timeout=60000, wait_until='domcontentloaded')
            page.wait_for_timeout(1500)
            page.screenshot(path=out_path, clip={'x':0,'y':0,'width':w,'height':h}, timeout=60000)
            page.close()
            print(f"  ✓ {out_name}.png ({w}×{h})")
            results.append(out_path)
        browser.close()
    return results


# ═══════════════════════════════════════════════════════
# POST 1: DARK — Giant garden scene, one short phrase
# Visual: 5 large plants in a row, short text overlay
# ═══════════════════════════════════════════════════════
def build_post1_dark():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 200, 225)
    snake = sv(PLANTS['Snake Plant']['svg'], 180, 202)
    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 200, 225)
    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 180, 202)
    sunflower = sv(PLANTS['Sunflower']['svg'], 190, 214)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:60px 40px 50px;text-align:center">

  <div style="font-size:14px;color:{muted};letter-spacing:3px;text-transform:uppercase">
    bloomday</div>

  <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
    color:{accent};line-height:1.1">nothing dies here.</div>

  <div style="display:flex;gap:8px;align-items:flex-end;justify-content:center">
    {snake}
    {monstera}
    {sunflower}
    {orchid}
    {fiddle}
  </div>

  <div style="font-size:15px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# POST 2: SAGE — Visual grid of 6 plants with tiny labels
# ═══════════════════════════════════════════════════════
def build_post2_sage():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    plants_data = [
        (sv(PLANTS['Monstera Deliciosa']['svg'], 140, 158), "monstera"),
        (sv(PLANTS['Cherry Blossom']['svg'], 140, 158), "cherry blossom"),
        (sv(PLANTS['Sunflower']['svg'], 140, 158), "sunflower"),
        (sv(PLANTS['Alpine Strawberry']['svg'], 140, 158), "strawberry"),
        (sv(PLANTS['Snake Plant']['svg'], 140, 158), "snake plant"),
        (sv(PLANTS['Heirloom Tomato']['svg'], 140, 158), "tomato"),
    ]

    cards_html = ''
    for plant_svg, name in plants_data:
        cards_html += f"""
        <div style="background:rgba(0,0,0,0.10);border-radius:24px;
          display:flex;flex-direction:column;align-items:center;justify-content:center;
          gap:10px;width:300px;height:300px">
          {plant_svg}
          <div style="font-size:13px;color:{accent};letter-spacing:1px;opacity:0.7">{name}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:50px 40px;text-align:center">

  <div style="font-family:Georgia,'Times New Roman',serif;font-size:38px;
    color:#f5f0e8;line-height:1.15">131 species. all hand-drawn.</div>

  <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center">
    {cards_html}
  </div>

  <div style="font-size:14px;color:{muted};letter-spacing:2px">
    bloomday.app · free forever</div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# POST 3: CREAM — Single giant orchid, one line of text
# Minimal, gallery-style post
# ═══════════════════════════════════════════════════════
def build_post3_cream():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 420, 472)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:60px;text-align:center;gap:40px">

  {orchid}

  <div style="font-family:Georgia,'Times New Roman',serif;font-size:40px;
    color:{dark};line-height:1.2">grew this by finishing<br>one small task.</div>

  <div style="font-size:15px;color:{muted};letter-spacing:2px">
    bloomday.app</div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# TIKTOK COVER: 1080×1920 — Tall garden scene
# Big plants stacked, minimal text
# ═══════════════════════════════════════════════════════
def build_tiktok_cover():
    bg = COLORS['dark']
    light = COLORS['text_light']
    muted = COLORS['muted_dark']
    accent = COLORS['accent_dark']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 280, 315)
    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 240, 270)
    cherry = sv(PLANTS['Cherry Blossom']['svg'], 260, 293)
    snake = sv(PLANTS['Snake Plant']['svg'], 220, 248)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 60px 100px;
  text-align:center">

  <div style="font-size:14px;color:{muted};letter-spacing:3px;text-transform:uppercase">
    bloomday</div>

  <div style="font-family:Georgia,'Times New Roman',serif;font-size:64px;
    color:{accent};line-height:1.05">your<br>garden<br>grows<br>with you.</div>

  <div style="display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap;justify-content:center">
    {snake}
    {monstera}
    {cherry}
    {fiddle}
  </div>

  <div style="text-align:center">
    <div style="font-size:22px;color:{accent};font-weight:600;margin-bottom:6px">
      link in bio</div>
    <div style="font-size:15px;color:{muted};letter-spacing:2px">bloomday.app</div>
  </div>
</div>"""
    return make_html(1080, 1920, bg, body)


# ═══════════════════════════════════════════════════════
# END SCREEN: 1080×1920
# Big plant showcase, barely any text
# ═══════════════════════════════════════════════════════
def build_end_screen():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    muted = COLORS['muted_cream']
    accent = COLORS['accent_cream']

    showcase = [
        sv(PLANTS['ZZ Plant']['svg'], 160, 180),
        sv(PLANTS['Sunflower']['svg'], 160, 180),
        sv(PLANTS['Monstera Deliciosa']['svg'], 160, 180),
        sv(PLANTS['Heirloom Tomato']['svg'], 160, 180),
        sv(PLANTS['Cherry Blossom']['svg'], 160, 180),
        sv(PLANTS['Snake Plant']['svg'], 160, 180),
        sv(PLANTS['Phalaenopsis Orchid']['svg'], 160, 180),
        sv(PLANTS['Alpine Strawberry']['svg'], 160, 180),
    ]

    row1 = ''.join(f'<div>{s}</div>' for s in showcase[:4])
    row2 = ''.join(f'<div>{s}</div>' for s in showcase[4:])

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 40px 80px;
  text-align:center">

  <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
    color:{dark};line-height:1.1">your garden<br>remembers.</div>

  <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">
    {row1}
  </div>
  <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">
    {row2}
  </div>

  <div style="font-size:20px;color:{muted};font-style:italic">
    131 species · 3 themes · ambient sound</div>

  <div style="text-align:center">
    <div style="font-size:28px;color:{accent};font-weight:700;margin-bottom:6px">
      bloomday.app</div>
    <div style="font-size:16px;color:{muted};letter-spacing:2px">free forever · no ads</div>
  </div>
</div>"""
    return make_html(1080, 1920, bg, body)


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════
if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n🌿 BloomDay Campaign Pack #2 — Visual-Heavy Edition\n")

    print("Building HTML...")
    jobs = []

    p1 = save_html('grid2_01_dark_comparison', build_post1_dark())
    jobs.append((p1, 'grid2_01_dark_comparison', 1080, 1080))

    p2 = save_html('grid2_02_sage_starterpack', build_post2_sage())
    jobs.append((p2, 'grid2_02_sage_starterpack', 1080, 1080))

    p3 = save_html('grid2_03_cream_bornto', build_post3_cream())
    jobs.append((p3, 'grid2_03_cream_bornto', 1080, 1080))

    p4 = save_html('tiktok2_cover', build_tiktok_cover())
    jobs.append((p4, 'tiktok2_cover', 1080, 1920))

    p5 = save_html('end2_screen', build_end_screen())
    jobs.append((p5, 'end2_screen', 1080, 1920))

    print("\nScreenshotting...")
    paths = batch_screenshot(jobs)

    print("\nWriting captions...")
    captions = {
        'grid2_01_dark_comparison': (
            "nothing dies here. 🌿\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #neurodivergent #indieapp"
        ),
        'grid2_02_sage_starterpack': (
            "131 hand-drawn species. which one are you growing first?\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #productivity #adhdproductivity #cozygames"
        ),
        'grid2_03_cream_bornto': (
            "grew this by finishing one small task. 🌸\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #adhdproductivity #plantmom"
        ),
        'tiktok2_cover': (
            "your garden grows with you. 🌿\n\n"
            "bloomday.app — link in bio\n\n"
            "#adhd #bloomday #productivity #softproductivity #indieapp"
        ),
        'end2_screen': (
            "your garden remembers. 🌱\n\n"
            "131 species · 3 themes · ambient sound\n"
            "bloomday.app — free forever · no ads\n\n"
            "#adhd #bloomday #productivity #neurodivergent #cozygames"
        ),
    }

    md = "# BloomDay Campaign Pack #2 — Visual-Heavy Edition\n\n---\n\n"
    for name, caption in captions.items():
        md += f"### bloomday_{name}.png\n\n{caption}\n\n---\n\n"
    captions_path = os.path.join(OUTPUT_DIR, 'bloomday_captions_surprise_me_2.md')
    with open(captions_path, 'w') as f:
        f.write(md)

    print(f"\n✅ Campaign pack #2 complete! {len(paths)} images + captions saved to {OUTPUT_DIR}")
    for p in paths:
        print(f"   {os.path.basename(p)}")
    print(f"   bloomday_captions_surprise_me_2.md")
