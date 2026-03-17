#!/usr/bin/env python3
"""BloomDay 'Surprise Me' Full Campaign Pack Generator"""

import re
import os
import sys

# Add project root to path for bloomday_plants
sys.path.insert(0, '/home/user/claudecode')
from bloomday_plants import PLANTS, sv, HP, GD, AL, plant

from playwright.sync_api import sync_playwright

OUTPUT_DIR = '/mnt/user-data/outputs'
WORK_DIR = '/home/user/claudecode'
CHROME_PATH = '/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome'

FONT_LINK = ''

# ── Design tokens ──
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
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{FONT_LINK}
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
# POST 1: DARK — POV format
# "You missed a whole week. Your garden is still here."
# ═══════════════════════════════════════════════════════
def build_post1_dark():
    bg = COLORS['dark']
    title_col = COLORS['text_light']
    muted = COLORS['muted_dark']
    accent = COLORS['accent_dark']
    pov_bg = COLORS['cream']
    pov_text = COLORS['text_dark']

    zz = sv(PLANTS['ZZ Plant']['svg'], 240, 270)

    lines = [
        ("Nothing wilted. Nothing died.", True),
        ("No guilt notification at 9 a.m.", False),
        ("No streak counter screaming at you.", False),
        ("Just your plants. Waiting quietly.", False),
        ("Ready whenever you are. 🌿", False),
    ]
    lines_html = ''.join(
        f'<div style="font-size:28px;color:{title_col if bold else muted};'
        f'line-height:1.55;{"font-weight:600" if bold else ""}">{text}</div>'
        for text, bold in lines
    )

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:80px 72px;text-align:center">

  <div style="background:{pov_bg};color:{pov_text};font-family:'DM Sans',sans-serif;
    font-size:120px;font-weight:700;letter-spacing:-2px;padding:10px 52px 14px;
    border-radius:28px;display:inline-block;line-height:1">POV</div>

  <div style="font-family:'Playfair Display',serif;font-size:52px;color:{title_col};
    line-height:1.1;max-width:880px">You missed a whole week.<br>Your garden is still here.</div>

  <div style="display:flex;align-items:center;gap:48px;width:100%">
    <div style="flex-shrink:0">{zz}</div>
    <div style="flex:1;display:flex;flex-direction:column;gap:4px;text-align:left">{lines_html}</div>
  </div>

  <div style="font-size:17px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# POST 2: SAGE — Era format
# "in my doing one task and feeling like a CEO era"
# ═══════════════════════════════════════════════════════
def build_post2_sage():
    bg = COLORS['sage']
    title_col = COLORS['text_light']
    muted = COLORS['muted_sage']
    accent = COLORS['accent_sage']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 110, 124)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:64px 72px;text-align:center">

  <div style="color:{accent};font-size:15px;letter-spacing:3px;text-transform:uppercase">
    bloomday
  </div>

  <div style="flex:1;display:flex;flex-direction:column;align-items:center;
    justify-content:center;gap:22px">
    <div style="font-family:'Playfair Display',serif;font-size:52px;
      color:{muted};line-height:1.1">in my</div>
    <div style="font-family:'Playfair Display',serif;font-size:62px;
      color:{title_col};line-height:1.05;text-align:center;max-width:800px">
      doing one task<br>and feeling like<br>a CEO</div>
    <div style="font-family:'Playfair Display',serif;font-size:52px;
      color:{muted};line-height:1.1">era</div>
    <div style="width:80px;height:3px;background:{accent}"></div>
    {monstera}
    <div style="font-size:22px;color:{accent};font-style:italic;line-height:1.5">
      the monstera grew a new leaf. I am unstoppable.</div>
    <div style="font-size:18px;color:{muted}">
      (the task was "reply to one email")</div>
  </div>

  <div style="font-size:14px;color:{muted};letter-spacing:2px">
    bloomday.app · free forever
  </div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# POST 3: CREAM — Quote format
# "nothing dies when you miss a day"
# ═══════════════════════════════════════════════════════
def build_post3_cream():
    bg = COLORS['cream']
    title_col = COLORS['text_dark']
    muted = COLORS['muted_cream']
    accent = COLORS['accent_cream']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 100, 112)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:100px 80px;text-align:center;gap:36px">

  <div style="font-family:'Playfair Display',serif;font-size:76px;
    color:{title_col};line-height:1.0">nothing dies<br>when you<br>miss a day.</div>

  <div style="width:80px;height:3px;background:{accent}"></div>

  <div style="font-size:24px;color:{muted};font-style:italic;max-width:700px;line-height:1.5">
    not even close. your garden just waits.<br>no guilt. no punishment. just plants.</div>

  {orchid}

  <div style="font-size:15px;color:{muted};letter-spacing:2px">
    bloomday.app · free forever
  </div>
</div>"""
    return make_html(1080, 1080, bg, body)


# ═══════════════════════════════════════════════════════
# TIKTOK COVER: 1080×1920 — POV
# "the only productivity app that didn't make me quit"
# ═══════════════════════════════════════════════════════
def build_tiktok_cover():
    bg = COLORS['dark']
    title_col = COLORS['text_light']
    muted = COLORS['muted_dark']
    accent = COLORS['accent_dark']
    pov_bg = COLORS['cream']
    pov_text = COLORS['text_dark']

    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 200, 224)

    lines = [
        ("nothing dies when you miss a day.", True),
        ("not even a little bit.", False),
        ("your garden just waits.", False),
        ("no punishment. no reset. no lecture.", False),
        ("131 hand-drawn plants inside.", False),
        ("free forever. no ads.", False),
    ]
    lines_html = ''.join(
        f'<div style="font-size:28px;color:{title_col if bold else muted};'
        f'line-height:1.6;{"font-weight:600" if bold else ""}">{text}</div>'
        for text, bold in lines
    )

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:140px 80px 110px;
  text-align:center">

  <div style="background:{pov_bg};color:{pov_text};font-size:130px;font-weight:700;
    letter-spacing:-3px;padding:8px 56px 16px;border-radius:24px;
    line-height:1;display:inline-block">POV</div>

  <div style="font-family:'Playfair Display',serif;font-size:64px;
    color:{title_col};line-height:1.05;max-width:900px">the only productivity<br>app that didn't<br>make me quit</div>

  <div style="display:flex;flex-direction:column;gap:8px;width:100%">
    {lines_html}
  </div>

  {fiddle}

  <div style="text-align:center">
    <div style="font-size:24px;color:{accent};font-weight:600;margin-bottom:8px">
      link in bio</div>
    <div style="font-size:17px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
  </div>
</div>"""
    return make_html(1080, 1920, bg, body)


# ═══════════════════════════════════════════════════════
# END SCREEN: 1080×1920
# Plant collection showcase + core message
# ═══════════════════════════════════════════════════════
def build_end_screen():
    bg = COLORS['sage']
    title_col = COLORS['text_light']
    muted = COLORS['muted_sage']
    accent = COLORS['accent_sage']

    # Pick 6 diverse plants for the showcase
    showcase = [
        sv(PLANTS['Monstera Deliciosa']['svg'], 130, 146),
        sv(PLANTS['Sunflower']['svg'], 130, 146),
        sv(PLANTS['Heirloom Tomato']['svg'], 130, 146),
        sv(PLANTS['Cherry Blossom']['svg'], 130, 146),
        sv(PLANTS['Snake Plant']['svg'], 130, 146),
        sv(PLANTS['Alpine Strawberry']['svg'], 130, 146),
    ]

    plant_row1 = ''.join(f'<div>{s}</div>' for s in showcase[:3])
    plant_row2 = ''.join(f'<div>{s}</div>' for s in showcase[3:])

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 60px 100px;
  text-align:center">

  <div style="font-family:'Playfair Display',serif;font-size:72px;
    color:{title_col};line-height:1.05">nothing dies<br>when you<br>miss a day.</div>

  <div style="width:80px;height:3px;background:{accent}"></div>

  <div style="font-size:26px;color:{accent};line-height:1.6;max-width:800px">
    112 hand-drawn plant species.<br>
    3 garden themes. ambient sound.<br>
    time capsule letters to your future self.<br>
    free forever. no ads. no subscriptions.</div>

  <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">
    {plant_row1}
  </div>
  <div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">
    {plant_row2}
  </div>

  <div style="font-family:'Playfair Display',serif;font-size:36px;
    color:{title_col};font-style:italic">
    built solo with AI by a former humanitarian worker with ADHD</div>

  <div style="text-align:center">
    <div style="font-size:28px;color:{accent};font-weight:700;margin-bottom:10px">
      bloomday.app</div>
    <div style="font-size:18px;color:{muted};letter-spacing:2px">free forever</div>
  </div>
</div>"""
    return make_html(1080, 1920, bg, body)


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════
if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n🌿 BloomDay Campaign Pack — 'Surprise Me'\n")

    # Build all HTML
    print("Building HTML...")
    jobs = []

    p1 = save_html('grid_01_dark_pov', build_post1_dark())
    jobs.append((p1, 'grid_01_dark_pov', 1080, 1080))

    p2 = save_html('grid_02_sage_era', build_post2_sage())
    jobs.append((p2, 'grid_02_sage_era', 1080, 1080))

    p3 = save_html('grid_03_cream_quote', build_post3_cream())
    jobs.append((p3, 'grid_03_cream_quote', 1080, 1080))

    p4 = save_html('tiktok_cover', build_tiktok_cover())
    jobs.append((p4, 'tiktok_cover', 1080, 1920))

    p5 = save_html('end_screen', build_end_screen())
    jobs.append((p5, 'end_screen', 1080, 1920))

    # Screenshot all
    print("\nScreenshotting...")
    paths = batch_screenshot(jobs)

    # Write captions
    print("\nWriting captions...")
    captions = {
        'grid_01_dark_pov': (
            "pov: you missed a whole week and your garden didn't even flinch\n\n"
            "no notification. no broken streak. just your ZZ plant, "
            "standing there like nothing happened. because nothing did.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #adhdproductivity #indieapp"
        ),
        'grid_02_sage_era': (
            "in my doing one task and feeling like a CEO era\n\n"
            "the task was 'reply to one email.' the monstera grew a new leaf. "
            "I am peak performance.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #productivity #adhdproductivity #plantmom"
        ),
        'grid_03_cream_quote': (
            "nothing dies when you miss a day. not even close.\n\n"
            "I built this because every productivity app I tried made me feel worse. "
            "so I made one that just... waits. bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #neurodivergent #indieapp"
        ),
        'tiktok_cover': (
            "pov: the only productivity app that didn't make me quit\n\n"
            "nothing dies when you miss a day. 131 hand-drawn plants. "
            "ambient sound. letters to your future self. free forever.\n\n"
            "bloomday.app — link in bio\n\n"
            "#adhd #bloomday #productivity #adhdproductivity #cozygames"
        ),
        'end_screen': (
            "112 plants. 3 garden themes. ambient sound. time capsule letters. "
            "nothing dies when you miss a day.\n\n"
            "built solo with AI by a former humanitarian worker with ADHD. "
            "free forever. no ads. no subscriptions.\n\n"
            "bloomday.app\n\n"
            "#adhd #bloomday #productivity #softproductivity #indieapp"
        ),
    }

    md = "# BloomDay Campaign Pack — Surprise Me\n\n---\n\n"
    for name, caption in captions.items():
        md += f"### bloomday_{name}.png\n\n{caption}\n\n---\n\n"
    captions_path = os.path.join(OUTPUT_DIR, 'bloomday_captions_surprise_me.md')
    with open(captions_path, 'w') as f:
        f.write(md)

    print(f"\n✅ Campaign pack complete! {len(paths)} images + captions saved to {OUTPUT_DIR}")
    for p in paths:
        print(f"   {os.path.basename(p)}")
    print(f"   bloomday_captions_surprise_me.md")
