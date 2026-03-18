#!/usr/bin/env python3
"""BloomDay ADHD Meme TikTok Animations — Part 2: visual-first, less text, bigger plants."""

import os
import sys
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
    'muted_sage': '#8da880',
    'red': '#e74c3c',
    'amber': '#f39c12',
}

W, H = 1080, 1920


def base_html(bg_color, body_html):
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    width:{W}px; height:{H}px;
    background:{bg_color};
    font-family:'DM Sans',Arial,Helvetica,sans-serif;
    overflow:hidden;
  }}
  @keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
  @keyframes fadeInUp {{
    from {{ opacity:0; transform:translateY(60px); }}
    to {{ opacity:1; transform:translateY(0); }}
  }}
  @keyframes fadeInDown {{
    from {{ opacity:0; transform:translateY(-40px); }}
    to {{ opacity:1; transform:translateY(0); }}
  }}
  @keyframes scaleIn {{
    from {{ opacity:0; transform:scale(0.5); }}
    to {{ opacity:1; transform:scale(1); }}
  }}
  @keyframes scalePop {{
    0% {{ opacity:0; transform:scale(0.3); }}
    70% {{ opacity:1; transform:scale(1.15); }}
    100% {{ opacity:1; transform:scale(1); }}
  }}
  @keyframes shakeNo {{
    0%, 100% {{ transform:translateX(0); }}
    20% {{ transform:translateX(-12px); }}
    40% {{ transform:translateX(12px); }}
    60% {{ transform:translateX(-8px); }}
    80% {{ transform:translateX(8px); }}
  }}
  @keyframes gentleSway {{
    0%, 100% {{ transform:rotate(0deg); }}
    25% {{ transform:rotate(3deg); }}
    75% {{ transform:rotate(-3deg); }}
  }}
  @keyframes slideInLeft {{
    from {{ opacity:0; transform:translateX(-120px); }}
    to {{ opacity:1; transform:translateX(0); }}
  }}
  @keyframes slideInRight {{
    from {{ opacity:0; transform:translateX(120px); }}
    to {{ opacity:1; transform:translateX(0); }}
  }}
  @keyframes strikethrough {{
    from {{ width: 0; }}
    to {{ width: 100%; }}
  }}
  @keyframes dropIn {{
    0% {{ opacity:0; transform:translateY(-200px) rotate(-10deg); }}
    60% {{ opacity:1; transform:translateY(20px) rotate(2deg); }}
    80% {{ transform:translateY(-8px) rotate(-1deg); }}
    100% {{ opacity:1; transform:translateY(0) rotate(0deg); }}
  }}
  @keyframes float {{
    0%, 100% {{ transform:translateY(0); }}
    50% {{ transform:translateY(-15px); }}
  }}
  @keyframes glowPulse {{
    0%, 100% {{ text-shadow: 0 0 20px rgba(154,176,106,0.3); }}
    50% {{ text-shadow: 0 0 40px rgba(154,176,106,0.8), 0 0 80px rgba(154,176,106,0.4); }}
  }}
  @keyframes checkmark {{
    0% {{ opacity:0; transform:scale(0) rotate(-45deg); }}
    60% {{ opacity:1; transform:scale(1.3) rotate(5deg); }}
    100% {{ opacity:1; transform:scale(1) rotate(0deg); }}
  }}
  @keyframes bounceIn {{
    0% {{ opacity:0; transform:scale(0.3); }}
    50% {{ opacity:1; transform:scale(1.1); }}
    70% {{ transform:scale(0.9); }}
    100% {{ opacity:1; transform:scale(1); }}
  }}
  @keyframes pulseGrow {{
    0%, 100% {{ transform:scale(1); }}
    50% {{ transform:scale(1.05); }}
  }}
  @keyframes wiggle {{
    0%, 100% {{ transform:rotate(0); }}
    25% {{ transform:rotate(-5deg); }}
    75% {{ transform:rotate(5deg); }}
  }}
</style>
</head><body>{body_html}</body></html>"""


# ═══════════════════════════════════════════════════════
# MEME 8: "ADHD paralysis" — The freeze → one tiny task
# Big plant hero, minimal text
# ═══════════════════════════════════════════════════════
def build_meme8_paralysis():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    snake = sv(PLANTS['Snake Plant']['svg'], 400, 450)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:50px;padding:80px 60px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.8s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:80px;
    color:#f5f0e8;line-height:1.0;font-weight:700">
    the freeze.</div>

  <!-- Short freeze lines -->
  <div style="display:flex;flex-direction:column;gap:8px;text-align:center">
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 1.5s forwards;
      font-size:32px;color:{muted};font-style:italic">can't start</div>
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 2.2s forwards;
      font-size:32px;color:{muted};font-style:italic">can't move</div>
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 2.9s forwards;
      font-size:32px;color:{muted};font-style:italic">can't even get up</div>
  </div>

  <!-- Task chip pops -->
  <div style="opacity:0; animation: bounceIn 0.6s ease-out 4.5s forwards;
    background:rgba(154,176,106,0.15);border:2px solid {accent};border-radius:24px;
    padding:20px 44px;display:inline-flex;align-items:center;gap:16px">
    <div style="width:36px;height:36px;border-radius:50%;background:{accent};
      display:flex;align-items:center;justify-content:center;
      opacity:0; animation: checkmark 0.5s ease-out 5.5s forwards;">
      <span style="color:{bg};font-size:22px;font-weight:700">✓</span>
    </div>
    <div style="font-size:30px;color:{accent}">"drink water"</div>
  </div>

  <!-- BIG plant hero -->
  <div style="opacity:0; animation: scaleIn 1.2s ease-out 6.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 8s infinite;">
      {snake}
    </div>
  </div>

  <!-- Punchline - BIG -->
  <div style="opacity:0; animation: fadeInUp 0.6s ease-out 8.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:52px;
    color:{accent};font-style:italic">
    it thawed a little.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 10.0s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 9: "Object permanence" — Forgot for months
# Big plant garden reveal, minimal timeline
# ═══════════════════════════════════════════════════════
def build_meme9_object_permanence():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    zz = sv(PLANTS['ZZ Plant']['svg'], 320, 360)
    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 280, 315)
    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 280, 315)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:40px;padding:80px 50px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:64px;
      color:#f5f0e8;line-height:1.05;font-weight:700">object<br>permanence?</div>
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:48px;
      color:{muted};margin-top:10px;font-style:italic">don't know her.</div>
  </div>

  <!-- Short timeline -->
  <div style="display:flex;flex-direction:column;gap:10px;text-align:center">
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 1.8s forwards;
      font-size:28px;color:{muted}">downloaded it in january</div>
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 2.8s forwards;
      font-size:28px;color:{muted}">forgot for 3 months</div>
    <div style="opacity:0; animation: fadeIn 0.4s ease-out 3.8s forwards;
      font-size:36px;color:#f5f0e8;font-weight:600">opened it.</div>
  </div>

  <!-- BIG plant garden reveal -->
  <div style="display:flex;gap:10px;align-items:flex-end;justify-content:center">
    <div style="opacity:0; animation: scaleIn 0.8s ease-out 5.0s forwards;">
      <div style="animation: gentleSway 3s ease-in-out 6s infinite;">{fiddle}</div>
    </div>
    <div style="opacity:0; animation: scaleIn 0.8s ease-out 5.5s forwards;">
      <div style="animation: gentleSway 2.5s ease-in-out 6.5s infinite;">{zz}</div>
    </div>
    <div style="opacity:0; animation: scaleIn 0.8s ease-out 6.0s forwards;">
      <div style="animation: gentleSway 3.5s ease-in-out 7s infinite;">{monstera}</div>
    </div>
  </div>

  <!-- Punchline - BIG -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 7.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:56px;
    color:{accent};font-weight:700">
    everything<br>was still alive.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 9.5s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 10: "When the dopamine hits" — HUGE plant celebration
# Minimal text, maximum visual impact
# ═══════════════════════════════════════════════════════
def build_meme10_dopamine():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    sunflower = sv(PLANTS['Sunflower']['svg'], 480, 540)
    cherry = sv(PLANTS['Cherry Blossom']['svg'], 200, 225)
    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 200, 225)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:40px;padding:80px 60px;
  text-align:center">

  <!-- Tiny task label -->
  <div style="opacity:0; animation: fadeIn 0.5s ease-out 0.5s forwards;
    font-size:28px;color:{muted}">the task:</div>

  <div style="opacity:0; animation: fadeIn 0.5s ease-out 1.2s forwards;
    font-size:32px;color:#f5f0e8">"take out the trash"</div>

  <!-- BIG checkmark -->
  <div style="opacity:0; animation: bounceIn 0.5s ease-out 2.5s forwards;
    width:80px;height:80px;border-radius:50%;background:{accent};
    display:flex;align-items:center;justify-content:center">
    <span style="color:{bg};font-size:48px;font-weight:700">✓</span>
  </div>

  <!-- HUGE dramatic text -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 3.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:72px;
    color:#f5f0e8;line-height:1.0;font-weight:700">
    when the<br>dopamine hits</div>

  <!-- HUGE sunflower -->
  <div style="opacity:0; animation: scalePop 1s ease-out 5.0s forwards;">
    <div style="animation: pulseGrow 1.5s ease-in-out 6.5s infinite;">
      {sunflower}
    </div>
  </div>

  <!-- Side plants celebration -->
  <div style="display:flex;gap:40px;align-items:center;justify-content:center">
    <div style="opacity:0; animation: slideInLeft 0.5s ease-out 6.0s forwards;">
      <div style="animation: wiggle 2s ease-in-out 7s infinite;">{cherry}</div>
    </div>
    <div style="opacity:0; animation: slideInRight 0.5s ease-out 6.2s forwards;">
      <div style="animation: wiggle 2.5s ease-in-out 7.5s infinite;">{orchid}</div>
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 8.5s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 11: "Things my therapist said" — Visual checklist
# Bigger text, bigger plant, fewer words
# ═══════════════════════════════════════════════════════
def build_meme11_therapist():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 380, 428)

    advice = [
        (1.5, "tiny steps"),
        (2.5, "celebrate small wins"),
        (3.5, "no punishment"),
        (4.5, "grow with it"),
    ]

    advice_html = ''
    for delay, text in advice:
        advice_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.5s ease-out {delay}s forwards;
          display:flex;align-items:center;gap:20px">
          <div style="opacity:0; animation: checkmark 0.4s ease-out {delay+0.6}s forwards;
            width:40px;height:40px;border-radius:50%;background:{accent};flex-shrink:0;
            display:flex;align-items:center;justify-content:center">
            <span style="color:#f5f0e8;font-size:24px;font-weight:700">✓</span>
          </div>
          <div style="font-size:34px;color:{dark};line-height:1.3">{text}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:44px;padding:80px 60px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:56px;
    color:{dark};line-height:1.1">things my<br>therapist said</div>

  <!-- Checklist -->
  <div style="display:flex;flex-direction:column;gap:28px;text-align:left;
    padding-left:80px">
    {advice_html}
  </div>

  <!-- Big plant -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 6.0s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 7s infinite;">
      {monstera}
    </div>
  </div>

  <!-- Punchline - BIG -->
  <div style="opacity:0; animation: fadeInUp 0.6s ease-out 7.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:48px;
    color:{dark};font-style:italic;line-height:1.1">
    wait... this is just<br>a plant app</div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 9.0s forwards;
    font-size:28px;color:{accent};font-weight:600">
    a really good one.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 10.0s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 12: "ADHD tax" — Big $0 reveal, plant hero
# Less items, bigger impact
# ═══════════════════════════════════════════════════════
def build_meme12_adhd_tax():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']
    red = COLORS['red']

    snake = sv(PLANTS['Snake Plant']['svg'], 360, 405)

    taxes = [
        (1.2, "$12 late fee"),
        (2.0, "$35 overdraft"),
        (2.8, "$9.99/mo forgot to cancel"),
        (3.6, "$49 missed refund"),
    ]

    taxes_html = ''
    for delay, text in taxes:
        taxes_html += f"""
        <div style="opacity:0; animation: shakeNo 0.5s ease-out {delay}s forwards, fadeIn 0.3s ease-out {delay}s forwards;
          font-size:30px;color:{red};line-height:1.8;position:relative">
          {text}
          <div style="position:absolute;top:50%;left:0;height:3px;background:{red};
            opacity:0.6;width:0;animation: strikethrough 0.4s ease-out {delay+0.6}s forwards"></div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:40px;padding:80px 60px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:72px;
    color:#f5f0e8;line-height:1.0;font-weight:700">
    the ADHD tax</div>

  <!-- Tax items -->
  <div style="display:flex;flex-direction:column;gap:4px;text-align:center">
    {taxes_html}
  </div>

  <!-- Bloomday tax - HUGE $0 -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 5.5s forwards;
    font-size:28px;color:{muted}">bloomday:</div>

  <div style="opacity:0; animation: scalePop 0.8s ease-out 6.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:120px;
    color:{accent};font-weight:700;line-height:1">$0</div>

  <!-- Big plant -->
  <div style="opacity:0; animation: scaleIn 1s ease-out 7.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 9s infinite;">
      {snake}
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 9.5s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 13: "47 tabs open" — Chaos → calm garden
# Visual chaos, then big peaceful plant
# ═══════════════════════════════════════════════════════
def build_meme13_brain_tabs():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 400, 450)

    tabs = [
        (1.0, "did I lock the door", 24, 60, 250, -8),
        (1.3, "what was I doing", 26, 500, 400, 5),
        (1.6, "WHERE ARE MY KEYS", 30, 80, 550, -3),
        (1.9, "is it tuesday", 22, 620, 220, 12),
        (2.2, "forgot to eat", 24, 150, 700, -6),
        (2.5, "why did I walk in here", 26, 400, 650, 8),
        (2.8, "DID I REPLY", 28, 100, 850, -10),
        (3.1, "is the stove on", 24, 550, 820, 4),
    ]

    chaos_html = ''
    for delay, text, size, x, y, rot in tabs:
        chaos_html += f"""
        <div style="position:absolute;left:{x}px;top:{y}px;
          opacity:0; animation: fadeIn 0.3s ease-out {delay}s forwards;
          font-size:{size}px;color:rgba(245,240,232,0.4);
          transform:rotate({rot}deg);white-space:nowrap">
          {text}</div>"""

    body = f"""
<div style="width:100%;height:100%;position:relative">

  <!-- Title - BIG on top -->
  <div style="position:absolute;top:80px;left:0;right:0;text-align:center;z-index:10;
    opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:72px;
      color:#f5f0e8;line-height:1.0;font-weight:700">
      my brain has<br>47 tabs open</div>
  </div>

  <!-- Chaotic text scattered -->
  <div style="position:absolute;top:0;left:0;width:100%;height:100%">
    {chaos_html}
  </div>

  <!-- Dark overlay wipes chaos -->
  <div style="position:absolute;top:0;left:0;width:100%;height:100%;
    background:{bg};opacity:0;animation: fadeIn 1.5s ease-out 5.0s forwards;
    z-index:5"></div>

  <!-- Peaceful reveal on top -->
  <div style="position:absolute;top:0;left:0;width:100%;height:100%;
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    gap:40px;z-index:10;padding:80px 60px">

    <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.5s forwards;
      font-family:Georgia,'Times New Roman',serif;font-size:60px;
      color:{accent};line-height:1.05;font-weight:700">
      but this tab<br>is just a<br>quiet garden.</div>

    <div style="opacity:0; animation: scaleIn 1s ease-out 8.0s forwards;">
      <div style="animation: float 3s ease-in-out 9.5s infinite;">
        {orchid}
      </div>
    </div>

    <div style="opacity:0; animation: fadeIn 0.3s ease-out 10.0s forwards;
      font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
  </div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 14: "Explaining to neurotypical friends"
# Bigger text bubbles, big plant at end
# ═══════════════════════════════════════════════════════
def build_meme14_explain_to_friends():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    cherry = sv(PLANTS['Cherry Blossom']['svg'], 360, 405)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:36px;padding:80px 60px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:50px;
    color:#f5f0e8;line-height:1.1">
    explaining bloomday<br>to neurotypicals</div>

  <!-- Chat - bigger, simpler -->
  <div style="display:flex;flex-direction:column;gap:16px;width:100%;text-align:left;padding:0 50px">
    <div style="opacity:0; animation: slideInLeft 0.4s ease-out 1.5s forwards;
      font-size:30px;color:#f5f0e8">"it's a productivity app"</div>
    <div style="opacity:0; animation: slideInRight 0.4s ease-out 2.5s forwards;
      font-size:30px;color:{muted};text-align:right">"oh like todoist?"</div>
    <div style="opacity:0; animation: slideInLeft 0.4s ease-out 3.5s forwards;
      font-size:30px;color:#f5f0e8">"no you grow plants"</div>
    <div style="opacity:0; animation: slideInRight 0.4s ease-out 4.5s forwards;
      font-size:30px;color:{muted};text-align:right">"...farmville?"</div>
    <div style="opacity:0; animation: slideInLeft 0.4s ease-out 5.5s forwards;
      font-size:30px;color:{accent};font-weight:600">"NO ok so imagine<br>you have ADHD and—"</div>
    <div style="opacity:0; animation: slideInRight 0.4s ease-out 7.0s forwards;
      font-size:30px;color:{muted};text-align:right">"are you okay?"</div>
  </div>

  <!-- BIG plant -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 8.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 9.5s infinite;">
      {cherry}
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 10.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:52px;
    color:{accent};font-style:italic">
    never been better.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 11.5s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 15: "Executive dysfunction starter pack"
# Fewer items, bigger text, big plant payoff
# ═══════════════════════════════════════════════════════
def build_meme15_starter_pack():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    strawberry = sv(PLANTS['Alpine Strawberry']['svg'], 360, 405)

    items = [
        (1.0, "13 unread texts"),
        (1.8, "inbox: 4,382"),
        (2.6, "started 7 projects"),
        (3.4, "finished 0"),
    ]

    items_html = ''
    for delay, text in items:
        items_html += f"""
        <div style="opacity:0; animation: fadeInUp 0.4s ease-out {delay}s forwards;
          font-size:34px;color:{dark};line-height:1.7">{text}</div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:44px;padding:80px 60px;
  text-align:center">

  <!-- Title - BIG -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:56px;
    color:{dark};line-height:1.05;font-weight:700">
    executive<br>dysfunction<br>starter pack</div>

  <!-- Items - clean list -->
  <div style="display:flex;flex-direction:column;gap:0;text-align:center">
    {items_html}
  </div>

  <!-- Task chip -->
  <div style="opacity:0; animation: bounceIn 0.6s ease-out 5.0s forwards;
    background:rgba(94,112,84,0.1);border:2px solid {accent};border-radius:24px;
    padding:20px 44px;display:inline-flex;align-items:center;gap:16px">
    <div style="width:36px;height:36px;border-radius:50%;background:{accent};
      display:flex;align-items:center;justify-content:center;
      opacity:0;animation:checkmark 0.5s ease-out 6.0s forwards">
      <span style="color:#f5f0e8;font-size:22px;font-weight:700">✓</span>
    </div>
    <div style="font-size:28px;color:{dark}">"brush teeth"</div>
  </div>

  <!-- BIG plant -->
  <div style="opacity:0; animation: scaleIn 1s ease-out 7.0s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 8s infinite;">
      {strawberry}
    </div>
  </div>

  <!-- Punchline - BIG -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 8.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:48px;
    color:{accent};font-style:italic">
    a strawberry grew.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 10.0s forwards;
    font-size:16px;color:{muted};letter-spacing:2px">bloomday.app</div>
</div>"""
    return base_html(bg, body)


def save_html(name, html):
    path = os.path.join(WORK_DIR, f"{name}.html")
    with open(path, 'w') as f:
        f.write(html)
    return path


def record_video(html_path, out_name, duration_ms=10000):
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
        page.wait_for_timeout(duration_ms + 500)
        webm_path = page.video.path()
        page.close()
        context.close()
        browser.close()

    if not webm_path or not os.path.exists(webm_path):
        print(f"  ✗ Failed to record {out_name}")
        return None

    mp4_path = os.path.join(OUTPUT_DIR, f"bloomday_{out_name}.mp4")
    cmd = [
        'ffmpeg', '-y', '-i', webm_path,
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        '-vf', f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2',
        mp4_path,
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    os.remove(webm_path)
    print(f"  ✓ {out_name}.mp4 ({W}×{H})")
    return mp4_path


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n🧠 BloomDay ADHD Meme TikToks — Part 2 (visual-first)\n")

    videos = [
        ('meme_adhd_paralysis',       build_meme8_paralysis,           12000),
        ('meme_adhd_object_perm',     build_meme9_object_permanence,   11000),
        ('meme_adhd_dopamine',        build_meme10_dopamine,           10000),
        ('meme_adhd_therapist',       build_meme11_therapist,          12000),
        ('meme_adhd_tax',             build_meme12_adhd_tax,           11000),
        ('meme_adhd_brain_tabs',      build_meme13_brain_tabs,         12000),
        ('meme_adhd_explain_friends', build_meme14_explain_to_friends, 13000),
        ('meme_adhd_starter_pack',    build_meme15_starter_pack,       12000),
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

    # Write captions
    print("\nWriting captions...")
    captions = {
        'meme_adhd_paralysis': (
            "the freeze. you know the one.\n\n"
            "can't start. can't move. can't even get up. "
            "then you do one tiny thing. it thawed a little.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdparalysis #adhdtiktok #executivedysfunction #bloomday #softproductivity"
        ),
        'meme_adhd_object_perm': (
            "object permanence? don't know her.\n\n"
            "forgot bloomday existed for 3 months. "
            "opened it. everything was still alive.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #objectpermanence #adhdtiktok #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_dopamine': (
            "the task: 'take out the trash'\n"
            "when the dopamine hits: 🌻🌻🌻\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #dopamine #adhdtiktok #bloomday #adhdproductivity #adhdmemes"
        ),
        'meme_adhd_therapist': (
            "things my therapist said to do:\n"
            "✓ tiny steps ✓ celebrate wins ✓ no punishment ✓ grow with it\n\n"
            "wait... this is just a plant app. a really good one.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #therapy #adhdtiktok #bloomday #mentalhealth #softproductivity"
        ),
        'meme_adhd_tax': (
            "the ADHD tax\n\n"
            "$12 late fee. $35 overdraft. $9.99/mo forgot to cancel. $49 missed refund.\n\n"
            "bloomday: $0. free forever.\n\n"
            "bloomday.app\n\n"
            "#adhd #adhdtax #adhdtiktok #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_brain_tabs': (
            "my brain has 47 tabs open\n\n"
            "but this tab is just a quiet garden.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #braintabs #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_explain_friends': (
            "explaining bloomday to neurotypicals\n\n"
            "'it's a productivity app' 'like todoist?' 'no you grow plants' "
            "'farmville?' 'NO ok imagine you have ADHD and—' 'are you okay?'\n\n"
            "never been better.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #bloomday #neurodivergent #adhdmemes #relatable"
        ),
        'meme_adhd_starter_pack': (
            "executive dysfunction starter pack\n\n"
            "13 unread texts. inbox: 4,382. started 7 projects. finished 0.\n\n"
            "then you check off 'brush teeth' and a strawberry grew.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #executivedysfunction #adhdtiktok #bloomday #starterpack #adhdmemes"
        ),
    }

    md = "# BloomDay ADHD Meme TikToks — Part 2\n\n---\n\n"
    for name, caption in captions.items():
        md += f"### bloomday_{name}.mp4\n\n{caption}\n\n---\n\n"
    captions_path = os.path.join(OUTPUT_DIR, 'bloomday_captions_adhd_memes.md')
    with open(captions_path, 'w') as f:
        f.write(md)

    print(f"\n✅ Done! {len(results)} ADHD meme TikToks saved to {OUTPUT_DIR}")
    for p in results:
        print(f"   {os.path.basename(p)}")
    print(f"   bloomday_captions_adhd_memes.md")
    print("\nAll videos are 1080×1920 MP4, ready for TikTok upload!")
