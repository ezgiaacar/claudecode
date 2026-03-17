#!/usr/bin/env python3
"""BloomDay TikTok Animations — generates MP4 videos for TikTok upload."""

import os
import sys
import time
import subprocess

sys.path.insert(0, '/home/user/claudecode')
from bloomday_plants import PLANTS, sv

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
    'accent_dark': '#9ab06a',
    'accent_sage': '#d4e8a8',
    'accent_cream': '#5e7054',
    'muted_cream': '#9a9088',
}

# TikTok dimensions
W, H = 1080, 1920


def make_animated_html(bg_color, body_html, duration_s=8):
    """Create an HTML page with CSS animations, sized for TikTok."""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    width:{W}px; height:{H}px;
    background:{bg_color};
    font-family:'DM Sans',Arial,Helvetica,sans-serif;
    overflow:hidden;
  }}
  @keyframes fadeInUp {{
    from {{ opacity:0; transform:translateY(60px); }}
    to {{ opacity:1; transform:translateY(0); }}
  }}
  @keyframes fadeIn {{
    from {{ opacity:0; }}
    to {{ opacity:1; }}
  }}
  @keyframes scaleIn {{
    from {{ opacity:0; transform:scale(0.7); }}
    to {{ opacity:1; transform:scale(1); }}
  }}
  @keyframes slideInLeft {{
    from {{ opacity:0; transform:translateX(-80px); }}
    to {{ opacity:1; transform:translateX(0); }}
  }}
  @keyframes slideInRight {{
    from {{ opacity:0; transform:translateX(80px); }}
    to {{ opacity:1; transform:translateX(0); }}
  }}
  @keyframes gentlePulse {{
    0%, 100% {{ transform:scale(1); }}
    50% {{ transform:scale(1.05); }}
  }}
  @keyframes gentleSway {{
    0%, 100% {{ transform:rotate(0deg); }}
    25% {{ transform:rotate(2deg); }}
    75% {{ transform:rotate(-2deg); }}
  }}
  @keyframes growUp {{
    from {{ opacity:0; transform:scaleY(0) translateY(50px); transform-origin: bottom center; }}
    to {{ opacity:1; transform:scaleY(1) translateY(0); transform-origin: bottom center; }}
  }}
  @keyframes typeIn {{
    from {{ clip-path: inset(0 100% 0 0); }}
    to {{ clip-path: inset(0 0 0 0); }}
  }}
</style>
</head><body>{body_html}</body></html>"""


# ═══════════════════════════════════════════════════════
# VIDEO 1: "Your Garden Grows With You" — Plant reveal
# Plants appear one by one, then tagline fades in
# ═══════════════════════════════════════════════════════
def build_video1_garden_grows():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    plants = [
        ('Snake Plant', 220, 248),
        ('Monstera Deliciosa', 280, 315),
        ('Sunflower', 260, 293),
        ('Phalaenopsis Orchid', 260, 293),
        ('Fiddle Leaf Fig', 240, 270),
    ]

    plants_html = ''
    for i, (name, w, h) in enumerate(plants):
        delay = 0.8 + i * 0.6
        plant_svg = sv(PLANTS[name]['svg'], w, h)
        plants_html += f"""
        <div style="opacity:0; animation: scaleIn 0.8s ease-out {delay}s forwards;
          display:flex;align-items:flex-end;">
          <div style="animation: gentleSway 3s ease-in-out {delay+1}s infinite;">
            {plant_svg}
          </div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:140px 60px 120px;
  text-align:center">

  <div style="opacity:0; animation: fadeIn 1s ease-out 0.3s forwards;
    font-size:16px;color:{muted};letter-spacing:4px;text-transform:uppercase">
    bloomday</div>

  <div style="opacity:0; animation: fadeInUp 1.2s ease-out 4.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:68px;
    color:{accent};line-height:1.05">
    your<br>garden<br>grows<br>with you.</div>

  <div style="display:flex;gap:10px;align-items:flex-end;justify-content:center;
    flex-wrap:wrap">
    {plants_html}
  </div>

  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.5s forwards;text-align:center">
    <div style="font-size:24px;color:{accent};font-weight:600;margin-bottom:8px">
      link in bio</div>
    <div style="font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
  </div>
</div>"""
    return make_animated_html(bg, body, 8)


# ═══════════════════════════════════════════════════════
# VIDEO 2: "Nothing Dies Here" — Dark moody reveal
# Plants grow up from the bottom, text appears
# ═══════════════════════════════════════════════════════
def build_video2_nothing_dies():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    plants = [
        ('Snake Plant', 200, 225),
        ('ZZ Plant', 200, 225),
        ('Monstera Deliciosa', 240, 270),
        ('Fiddle Leaf Fig', 200, 225),
        ('Snake Plant', 200, 225),
    ]

    row_html = ''
    for i, (name, w, h) in enumerate(plants):
        delay = 1.0 + i * 0.5
        plant_svg = sv(PLANTS[name]['svg'], w, h)
        row_html += f"""
        <div style="opacity:0; transform-origin:bottom center;
          animation: fadeInUp 1s ease-out {delay}s forwards;">
          <div style="animation: gentleSway 4s ease-in-out {delay+1.2}s infinite;">
            {plant_svg}
          </div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:160px 40px 100px;
  text-align:center">

  <div style="opacity:0; animation: fadeIn 1.2s ease-out 0.3s forwards;
    font-size:16px;color:{muted};letter-spacing:4px;text-transform:uppercase">
    bloomday</div>

  <div style="opacity:0; animation: fadeIn 1.5s ease-out 4.0s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:72px;
      color:{accent};line-height:1.05;margin-bottom:20px">
      nothing<br>dies here.</div>
    <div style="font-size:18px;color:{muted};letter-spacing:1px">
      a garden that grows when you do.</div>
  </div>

  <div style="display:flex;gap:6px;align-items:flex-end;justify-content:center">
    {row_html}
  </div>

  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.0s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">
    bloomday.app · free forever</div>
</div>"""
    return make_animated_html(bg, body, 8)


# ═══════════════════════════════════════════════════════
# VIDEO 3: "131 Species" — Grid reveal on sage
# Plant cards appear in a staggered grid
# ═══════════════════════════════════════════════════════
def build_video3_species_grid():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = '#8da880'

    plants_data = [
        ('Monstera Deliciosa', 'monstera'),
        ('Cherry Blossom', 'cherry blossom'),
        ('Sunflower', 'sunflower'),
        ('Alpine Strawberry', 'strawberry'),
        ('Snake Plant', 'snake plant'),
        ('Heirloom Tomato', 'tomato'),
        ('Phalaenopsis Orchid', 'orchid'),
        ('Fiddle Leaf Fig', 'fiddle leaf'),
        ('ZZ Plant', 'zz plant'),
    ]

    cards_html = ''
    for i, (name, label) in enumerate(plants_data):
        delay = 1.2 + i * 0.3
        plant_svg = sv(PLANTS[name]['svg'], 120, 135)
        cards_html += f"""
        <div style="opacity:0; animation: scaleIn 0.6s ease-out {delay}s forwards;
          background:rgba(0,0,0,0.12);border-radius:24px;
          display:flex;flex-direction:column;align-items:center;justify-content:center;
          gap:8px;width:300px;height:280px">
          <div style="animation: gentlePulse 3s ease-in-out {delay+0.8}s infinite;">
            {plant_svg}
          </div>
          <div style="font-size:14px;color:{accent};letter-spacing:1px;opacity:0.8">{label}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:80px 40px 60px;
  text-align:center">

  <div style="opacity:0; animation: fadeInUp 1s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
      color:#f5f0e8;line-height:1.1;margin-bottom:12px">
      131 species.</div>
    <div style="font-size:20px;color:{accent};letter-spacing:1px;opacity:0.8">
      all hand-drawn.</div>
  </div>

  <div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;
    max-width:960px">
    {cards_html}
  </div>

  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 5.5s forwards;
    font-size:16px;color:{accent};letter-spacing:2px;opacity:0.7">
    bloomday.app · free forever</div>
</div>"""
    return make_animated_html(bg, body, 7)


# ═══════════════════════════════════════════════════════
# VIDEO 4: "Grew This" — Single plant spotlight on cream
# One plant scales up dramatically, then text appears
# ═══════════════════════════════════════════════════════
def build_video4_grew_this():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 480, 540)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:80px 60px;
  text-align:center;gap:50px">

  <div style="opacity:0; animation: fadeIn 0.8s ease-out 0.2s forwards;
    font-size:14px;color:{muted};letter-spacing:4px;text-transform:uppercase">
    bloomday</div>

  <div style="opacity:0; animation: scaleIn 1.5s ease-out 0.8s forwards;">
    <div style="animation: gentleSway 4s ease-in-out 2.5s infinite;">
      {orchid}
    </div>
  </div>

  <div style="opacity:0; animation: fadeInUp 1.2s ease-out 3.0s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
      color:{dark};line-height:1.15;margin-bottom:16px">
      grew this by finishing<br>one small task.</div>
  </div>

  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 4.8s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">
    bloomday.app</div>
</div>"""
    return make_animated_html(bg, body, 7)


# ═══════════════════════════════════════════════════════
# VIDEO 5: "Your Garden Remembers" — End screen / showcase
# Plants appear from sides, then center text
# ═══════════════════════════════════════════════════════
def build_video5_garden_remembers():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    left_plants = [
        ('Snake Plant', 180, 202),
        ('Monstera Deliciosa', 200, 225),
        ('Cherry Blossom', 180, 202),
    ]
    right_plants = [
        ('Sunflower', 180, 202),
        ('Phalaenopsis Orchid', 200, 225),
        ('Fiddle Leaf Fig', 180, 202),
    ]

    left_html = ''
    for i, (name, w, h) in enumerate(left_plants):
        delay = 0.8 + i * 0.4
        plant_svg = sv(PLANTS[name]['svg'], w, h)
        left_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.8s ease-out {delay}s forwards;">
          <div style="animation: gentleSway 3.5s ease-in-out {delay+1}s infinite;">
            {plant_svg}
          </div>
        </div>"""

    right_html = ''
    for i, (name, w, h) in enumerate(right_plants):
        delay = 1.0 + i * 0.4
        plant_svg = sv(PLANTS[name]['svg'], w, h)
        right_html += f"""
        <div style="opacity:0; animation: slideInRight 0.8s ease-out {delay}s forwards;">
          <div style="animation: gentleSway 3.5s ease-in-out {delay+1}s infinite;">
            {plant_svg}
          </div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 30px 100px;
  text-align:center">

  <div style="opacity:0; animation: fadeIn 1s ease-out 0.3s forwards;
    font-size:16px;color:{muted};letter-spacing:4px;text-transform:uppercase">
    bloomday</div>

  <div style="display:flex;align-items:center;justify-content:center;gap:30px;
    width:100%">
    <div style="display:flex;flex-direction:column;gap:10px;align-items:center">
      {left_html}
    </div>

    <div style="opacity:0; animation: fadeIn 1.5s ease-out 3.0s forwards;
      min-width:320px">
      <div style="font-family:Georgia,'Times New Roman',serif;font-size:56px;
        color:{accent};line-height:1.1;margin-bottom:20px">
        your<br>garden<br>remembers.</div>
      <div style="font-size:18px;color:{muted};font-style:italic">
        131 species · 3 themes<br>ambient sound</div>
    </div>

    <div style="display:flex;flex-direction:column;gap:10px;align-items:center">
      {right_html}
    </div>
  </div>

  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 5.0s forwards;text-align:center">
    <div style="font-size:28px;color:{accent};font-weight:700;margin-bottom:8px">
      bloomday.app</div>
    <div style="font-size:16px;color:{muted};letter-spacing:2px">free forever · no ads</div>
  </div>
</div>"""
    return make_animated_html(bg, body, 8)


def save_html(name, html):
    path = os.path.join(WORK_DIR, f"{name}.html")
    with open(path, 'w') as f:
        f.write(html)
    return path


def record_video(html_path, out_name, duration_ms=8000):
    """Use Playwright to record a video of the animated HTML page."""
    webm_path = None
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH)
        context = browser.new_context(
            viewport={'width': W, 'height': H},
            record_video_dir=OUTPUT_DIR,
            record_video_size={'width': W, 'height': H},
        )
        page = context.new_page()
        page.goto(f'file://{html_path}', timeout=60000, wait_until='domcontentloaded')
        # Wait for the full animation duration
        page.wait_for_timeout(duration_ms + 500)
        # Get the video path before closing
        webm_path = page.video.path()
        page.close()
        context.close()
        browser.close()

    if not webm_path or not os.path.exists(webm_path):
        print(f"  ✗ Failed to record {out_name}")
        return None

    # Convert webm to mp4 with TikTok-friendly settings
    mp4_path = os.path.join(OUTPUT_DIR, f"bloomday_{out_name}.mp4")
    cmd = [
        'ffmpeg', '-y',
        '-i', webm_path,
        '-c:v', 'libx264',
        '-preset', 'medium',
        '-crf', '18',
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
        '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2',
        mp4_path,
    ]
    subprocess.run(cmd, capture_output=True, check=True)

    # Clean up webm
    os.remove(webm_path)

    print(f"  ✓ {out_name}.mp4 ({W}×{H})")
    return mp4_path


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n🎬 BloomDay TikTok Animations\n")

    videos = [
        ('tiktok_anim_garden_grows',    build_video1_garden_grows,    8000),
        ('tiktok_anim_nothing_dies',    build_video2_nothing_dies,    8000),
        ('tiktok_anim_species_grid',    build_video3_species_grid,    7000),
        ('tiktok_anim_grew_this',       build_video4_grew_this,       7000),
        ('tiktok_anim_garden_remembers', build_video5_garden_remembers, 8000),
    ]

    results = []
    for name, builder, duration in videos:
        print(f"\n📹 Recording: {name}")
        print("  Building HTML...")
        html = builder()
        html_path = save_html(name, html)
        print("  Recording & converting...")
        mp4 = record_video(html_path, name, duration)
        if mp4:
            results.append(mp4)

    print(f"\n✅ Done! {len(results)} TikTok animations saved to {OUTPUT_DIR}")
    for p in results:
        print(f"   {os.path.basename(p)}")
    print("\nAll videos are 1080×1920 MP4, ready for TikTok upload!")
