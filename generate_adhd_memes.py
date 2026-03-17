#!/usr/bin/env python3
"""BloomDay ADHD Meme TikTok Animations — Part 2: deeper ADHD content."""

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
# Extra bottom padding so "bloomday.app" line never gets covered
FOOTER_PAD = 120


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
  .footer {{
    position:absolute; bottom:40px; left:0; right:0;
    text-align:center; z-index:100;
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
  @keyframes slideUp {{
    from {{ opacity:0; transform:translateY(100px); }}
    to {{ opacity:1; transform:translateY(0); }}
  }}
  @keyframes crossOut {{
    from {{ text-decoration-color: transparent; }}
    to {{ text-decoration-color: currentColor; }}
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
</head><body style="position:relative">{body_html}</body></html>"""


def footer(delay, muted_color):
    """Absolute-positioned footer that never gets covered."""
    return f"""
    <div class="footer" style="opacity:0; animation: fadeIn 0.4s ease-out {delay}s forwards;">
      <div style="font-size:15px;color:{muted_color};letter-spacing:2px">
        bloomday.app · free forever</div>
    </div>"""


# ═══════════════════════════════════════════════════════
# MEME 8: "ADHD paralysis" — The freeze, then the thaw
# Shows the paralysis, then how ONE small task unlocks
# ═══════════════════════════════════════════════════════
def build_meme8_paralysis():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    snake = sv(PLANTS['Snake Plant']['svg'], 200, 225)

    freeze_lines = [
        (1.0, "can't start the project"),
        (1.8, "can't answer the email"),
        (2.6, "can't make the phone call"),
        (3.4, "can't do the dishes"),
        (4.2, "can't even get up"),
    ]

    freeze_html = ''
    for delay, text in freeze_lines:
        freeze_html += f"""
        <div style="opacity:0; animation: fadeIn 0.4s ease-out {delay}s forwards;
          font-size:28px;color:{muted};line-height:1.8;font-style:italic">
          {text}</div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 60px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
      color:#f5f0e8;line-height:1.1">the freeze.</div>
    <div style="font-size:18px;color:{muted};margin-top:12px;letter-spacing:1px">
      (you know the one)</div>
  </div>

  <!-- Paralysis lines fade in -->
  <div style="display:flex;flex-direction:column;gap:0;text-align:center">
    {freeze_html}
  </div>

  <!-- Divider beat -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 5.5s forwards;
    width:60px;height:3px;background:rgba(255,255,255,0.1)"></div>

  <!-- The unlock -->
  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:28px;
    color:#f5f0e8;line-height:1.4">
    then you open bloomday.<br>and do one tiny thing.</div>

  <!-- Task chip -->
  <div style="opacity:0; animation: bounceIn 0.6s ease-out 8.0s forwards;
    background:rgba(154,176,106,0.15);border:2px solid {accent};border-radius:20px;
    padding:16px 36px;display:inline-flex;align-items:center;gap:12px">
    <div style="width:28px;height:28px;border-radius:50%;border:2px solid {accent};
      display:flex;align-items:center;justify-content:center;
      opacity:0; animation: checkmark 0.5s ease-out 9.0s forwards;
      background:{accent}">
      <span style="color:{bg};font-size:18px;font-weight:700">✓</span>
    </div>
    <div style="font-size:24px;color:{accent}">"drink water"</div>
  </div>

  <!-- Plant grows -->
  <div style="opacity:0; animation: scaleIn 1s ease-out 9.8s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 11s infinite;">
      {snake}
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeInUp 0.6s ease-out 11.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:{accent};font-style:italic">
    the freeze thawed a little.</div>

  <div style="opacity:0; animation: fadeIn 0.3s ease-out 12.5s forwards;
    font-size:18px;color:{muted}">
    that's enough. that's the whole point.</div>
</div>
{footer(13.5, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 9: "Object permanence" — Forgot for a month
# App-doesn't-exist-if-I-can't-see-it ADHD moment
# ═══════════════════════════════════════════════════════
def build_meme9_object_permanence():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    zz = sv(PLANTS['ZZ Plant']['svg'], 240, 270)
    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 200, 225)
    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 200, 225)

    timeline = [
        (1.5, "january:", "downloaded bloomday", muted, '#f5f0e8'),
        (2.8, "february:", "forgot it existed", muted, '#f5f0e8'),
        (4.0, "march:", "still forgot", muted, '#f5f0e8'),
        (5.2, "april:", "found it on page 4 of my phone", muted, '#f5f0e8'),
        (6.5, "opened it.", "", accent, ''),
    ]

    timeline_html = ''
    for delay, label, desc, label_col, desc_col in timeline:
        timeline_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.5s ease-out {delay}s forwards;
          display:flex;gap:16px;align-items:baseline;width:100%;text-align:left;padding-left:60px">
          <div style="font-size:22px;color:{label_col};font-weight:600;min-width:140px">{label}</div>
          <div style="font-size:24px;color:{desc_col}">{desc}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 50px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-size:16px;color:{muted};letter-spacing:3px;text-transform:uppercase;
      margin-bottom:16px">adhd + bloomday</div>
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:44px;
      color:#f5f0e8;line-height:1.1">object permanence?<br>don't know her.</div>
  </div>

  <!-- Timeline -->
  <div style="display:flex;flex-direction:column;gap:12px;width:100%">
    {timeline_html}
  </div>

  <!-- The garden reveal -->
  <div style="opacity:0; animation: fadeIn 0.8s ease-out 7.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:#f5f0e8;font-style:italic">
    everything was still alive.</div>

  <!-- Plants row -->
  <div style="display:flex;gap:16px;align-items:flex-end;justify-content:center">
    <div style="opacity:0; animation: scaleIn 0.6s ease-out 9.0s forwards;">
      <div style="animation: gentleSway 3s ease-in-out 10s infinite;">{fiddle}</div>
    </div>
    <div style="opacity:0; animation: scaleIn 0.6s ease-out 9.4s forwards;">
      <div style="animation: gentleSway 2.5s ease-in-out 10.5s infinite;">{zz}</div>
    </div>
    <div style="opacity:0; animation: scaleIn 0.6s ease-out 9.8s forwards;">
      <div style="animation: gentleSway 3.5s ease-in-out 11s infinite;">{monstera}</div>
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 11.0s forwards;
    font-size:24px;color:{accent};line-height:1.5">
    no guilt. no dead plants. just "welcome back."</div>
</div>
{footer(12.0, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 10: "When the dopamine hits" — Tiny task, galaxy brain
# Complete a micro-task, euphoria ensues
# ═══════════════════════════════════════════════════════
def build_meme10_dopamine():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    sunflower = sv(PLANTS['Sunflower']['svg'], 300, 338)
    cherry = sv(PLANTS['Cherry Blossom']['svg'], 140, 157)
    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 140, 157)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 60px {FOOTER_PAD}px;
  text-align:center">

  <!-- Header -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:40px;
    color:{muted};line-height:1.2">
    the task:</div>

  <!-- Tiny task -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 1.2s forwards;
    background:rgba(255,255,255,0.05);border-radius:16px;padding:20px 40px">
    <div style="font-size:24px;color:#f5f0e8">"take out the trash"</div>
  </div>

  <!-- Check it off -->
  <div style="opacity:0; animation: bounceIn 0.5s ease-out 2.5s forwards;
    width:60px;height:60px;border-radius:50%;background:{accent};
    display:flex;align-items:center;justify-content:center">
    <span style="color:{bg};font-size:36px;font-weight:700">✓</span>
  </div>

  <!-- "when the dopamine hits" -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 3.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:48px;
    color:#f5f0e8;line-height:1.1;font-weight:700">
    when the<br>dopamine hits</div>

  <!-- HUGE sunflower celebration -->
  <div style="opacity:0; animation: scalePop 1s ease-out 5.0s forwards;">
    <div style="animation: pulseGrow 1.5s ease-in-out 6.5s infinite;">
      {sunflower}
    </div>
  </div>

  <!-- Side plants -->
  <div style="display:flex;gap:60px;align-items:center;justify-content:center">
    <div style="opacity:0; animation: slideInLeft 0.5s ease-out 6.0s forwards;">
      <div style="animation: wiggle 2s ease-in-out 7s infinite;">{cherry}</div>
    </div>
    <div style="opacity:0; animation: scalePop 0.6s ease-out 6.5s forwards;
      font-family:Georgia,'Times New Roman',serif;font-size:60px;color:{accent}">
      !!!</div>
    <div style="opacity:0; animation: slideInRight 0.5s ease-out 6.2s forwards;">
      <div style="animation: wiggle 2.5s ease-in-out 7.5s infinite;">{orchid}</div>
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 8.0s forwards;
    font-size:22px;color:{muted};font-style:italic">
    (it was literally just the trash)</div>
</div>
{footer(9.0, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 11: "Things my therapist said" — Checklist
# Advice list that bloomday actually does
# ═══════════════════════════════════════════════════════
def build_meme11_therapist():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 200, 225)

    advice = [
        (1.5, "break tasks into tiny steps"),
        (2.8, "celebrate small wins"),
        (4.0, "don't punish yourself for missing days"),
        (5.2, "find something that grows with you"),
        (6.4, "be kind to yourself"),
    ]

    advice_html = ''
    for delay, text in advice:
        advice_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.5s ease-out {delay}s forwards;
          display:flex;align-items:center;gap:16px;width:100%;text-align:left;padding-left:40px">
          <div style="opacity:0; animation: checkmark 0.4s ease-out {delay+0.6}s forwards;
            width:32px;height:32px;border-radius:50%;background:{accent};flex-shrink:0;
            display:flex;align-items:center;justify-content:center">
            <span style="color:{bg};font-size:20px;font-weight:700">✓</span>
          </div>
          <div style="font-size:26px;color:{dark};line-height:1.4">{text}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 50px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-size:16px;color:{muted};letter-spacing:3px;text-transform:uppercase;
      margin-bottom:16px">bloomday</div>
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:44px;
      color:{dark};line-height:1.1">things my therapist<br>said to do</div>
  </div>

  <!-- Advice items with checkmarks -->
  <div style="display:flex;flex-direction:column;gap:24px;width:100%">
    {advice_html}
  </div>

  <!-- Divider -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 7.5s forwards;
    width:60px;height:3px;background:{accent}"></div>

  <!-- Reveal -->
  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 8.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:{dark};line-height:1.3;font-style:italic">
    wait this is just<br>a plant app</div>

  <!-- Plant -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 9.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 10.5s infinite;">
      {monstera}
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeIn 0.5s ease-out 11.0s forwards;
    font-size:22px;color:{accent};font-weight:600">
    a really good plant app.</div>
</div>
{footer(12.0, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 12: "ADHD tax" — Things you pay for forgetting
# Each "tax" crosses out, bloomday has no tax
# ═══════════════════════════════════════════════════════
def build_meme12_adhd_tax():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']
    red = COLORS['red']
    amber = COLORS['amber']

    snake = sv(PLANTS['Snake Plant']['svg'], 220, 248)

    taxes = [
        (1.2, "$12 late fee — forgot to return the thing"),
        (2.4, "$35 overdraft — forgot to transfer"),
        (3.6, "$9.99/mo — forgot to cancel free trial"),
        (4.8, "$15 — reordered what I already had"),
        (6.0, "$49 — missed the refund window"),
    ]

    taxes_html = ''
    for delay, text in taxes:
        taxes_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.4s ease-out {delay}s forwards;
          display:flex;align-items:center;gap:12px;width:100%;text-align:left;padding:0 40px">
          <div style="font-size:22px;color:{amber};flex-shrink:0">$</div>
          <div style="font-size:22px;color:{red};line-height:1.5;position:relative">
            {text}
            <div style="position:absolute;top:50%;left:0;height:2px;background:{red};
              opacity:0.5;width:0;animation: strikethrough 0.4s ease-out {delay+0.8}s forwards"></div>
          </div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 40px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:52px;
      color:#f5f0e8;line-height:1.1">the ADHD tax</div>
    <div style="font-size:18px;color:{muted};margin-top:12px">
      (things I paid for because I forgot)</div>
  </div>

  <!-- Tax items -->
  <div style="display:flex;flex-direction:column;gap:16px;width:100%">
    {taxes_html}
  </div>

  <!-- Divider -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 7.5s forwards;
    width:60px;height:3px;background:rgba(255,255,255,0.1)"></div>

  <!-- BloomDay contrast -->
  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 8.0s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:32px;
      color:#f5f0e8;line-height:1.3">bloomday ADHD tax:</div>
  </div>

  <div style="opacity:0; animation: scalePop 0.7s ease-out 9.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:72px;
    color:{accent};font-weight:700">$0</div>

  <!-- Plant -->
  <div style="opacity:0; animation: scaleIn 0.8s ease-out 10.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 11.5s infinite;">
      {snake}
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeIn 0.5s ease-out 12.0s forwards;
    font-size:22px;color:{accent};line-height:1.5">
    free forever. nothing to forget to cancel.</div>
</div>
{footer(13.0, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 13: "My brain has 47 tabs open" — Chaos → Calm
# Chaotic text flies around, then settles into garden
# ═══════════════════════════════════════════════════════
def build_meme13_brain_tabs():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 240, 270)

    tabs = [
        (1.0, "did I lock the door", 20, 60, 180, -8),
        (1.3, "what was I doing", 22, 500, 320, 5),
        (1.6, "WHERE ARE MY KEYS", 26, 100, 450, -3),
        (1.9, "is it tuesday", 18, 600, 160, 12),
        (2.2, "forgot to eat again", 20, 150, 600, -6),
        (2.5, "wait what year is it", 19, 480, 520, 8),
        (2.8, "why did I walk in here", 22, 80, 720, -10),
        (3.1, "DID I REPLY TO THAT", 24, 400, 680, 4),
        (3.4, "need to drink water", 18, 250, 830, -5),
        (3.7, "is the stove on", 20, 550, 800, 7),
    ]

    chaos_html = ''
    for delay, text, size, x, y, rot in tabs:
        chaos_html += f"""
        <div style="position:absolute;left:{x}px;top:{y}px;
          opacity:0; animation: fadeIn 0.3s ease-out {delay}s forwards;
          font-size:{size}px;color:rgba(245,240,232,0.35);
          transform:rotate({rot}deg);white-space:nowrap">
          {text}</div>"""

    body = f"""
<div style="width:100%;height:100%;position:relative;
  display:flex;flex-direction:column;align-items:center;
  justify-content:space-between;padding:100px 60px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:42px;
    color:#f5f0e8;line-height:1.15;z-index:10">
    my brain has<br>47 tabs open</div>

  <!-- Chaotic text flying around -->
  <div style="position:absolute;top:0;left:0;width:100%;height:100%">
    {chaos_html}
  </div>

  <!-- "but this one tab" -->
  <div style="opacity:0; animation: fadeIn 0.8s ease-out 5.0s forwards;
    font-size:24px;color:{muted};z-index:10;font-style:italic">
    but this one tab...</div>

  <!-- Calm overlay fades in -->
  <div style="position:absolute;top:0;left:0;width:100%;height:100%;
    background:{bg};opacity:0;animation: fadeIn 1.5s ease-out 6.0s forwards;
    z-index:5"></div>

  <!-- Peaceful content on top -->
  <div style="z-index:10;display:flex;flex-direction:column;align-items:center;gap:30px">
    <div style="opacity:0; animation: fadeInUp 0.8s ease-out 7.5s forwards;
      font-family:Georgia,'Times New Roman',serif;font-size:48px;
      color:{accent};line-height:1.1">
      just has<br>a quiet garden.</div>

    <div style="opacity:0; animation: scaleIn 1s ease-out 9.0s forwards;">
      <div style="animation: float 3s ease-in-out 10s infinite;">
        {orchid}
      </div>
    </div>

    <div style="opacity:0; animation: fadeIn 0.5s ease-out 10.5s forwards;
      font-size:22px;color:{muted};line-height:1.5">
      no noise. no streaks. no pressure.<br>just one plant at a time.</div>
  </div>
</div>
{footer(12.0, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 14: "How I explain bloomday to neurotypical friends"
# Increasingly absurd explanations
# ═══════════════════════════════════════════════════════
def build_meme14_explain_to_friends():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    cherry = sv(PLANTS['Cherry Blossom']['svg'], 220, 248)

    attempts = [
        (1.5, "me:", "it's a productivity app", '#f5f0e8'),
        (2.5, "them:", "oh like todoist?", muted),
        (3.8, "me:", "no, you grow plants", '#f5f0e8'),
        (4.8, "them:", "...farmville?", muted),
        (6.0, "me:", "NO, you complete tasks and—", '#f5f0e8'),
        (7.0, "them:", "sounds like a game", muted),
        (8.5, "me:", "", accent),
    ]

    chat_html = ''
    for delay, speaker, text, color in attempts:
        if text:
            chat_html += f"""
            <div style="opacity:0; animation: slideInLeft 0.4s ease-out {delay}s forwards;
              display:flex;gap:12px;width:100%;text-align:left;padding:0 40px">
              <div style="font-size:20px;color:{muted};font-weight:600;min-width:70px;
                text-align:right">{speaker}</div>
              <div style="font-size:24px;color:{color};line-height:1.5">{text}</div>
            </div>"""
        else:
            chat_html += f"""
            <div style="opacity:0; animation: slideInLeft 0.4s ease-out {delay}s forwards;
              display:flex;gap:12px;width:100%;text-align:left;padding:0 40px">
              <div style="font-size:20px;color:{muted};font-weight:600;min-width:70px;
                text-align:right">{speaker}</div>
              <div style="font-size:24px;color:{color};line-height:1.5">
                ok so imagine you have ADHD and<br>
                everything feels impossible but then<br>
                you check off "drink water" and a<br>
                cherry blossom grows and suddenly<br>
                you feel like you can do anything</div>
            </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 40px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:38px;
    color:#f5f0e8;line-height:1.15">
    how I explain bloomday<br>to neurotypical friends</div>

  <!-- Chat bubbles -->
  <div style="display:flex;flex-direction:column;gap:14px;width:100%">
    {chat_html}
  </div>

  <!-- Their response -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 11.0s forwards;
    display:flex;gap:12px;width:100%;text-align:left;padding:0 40px">
    <div style="font-size:20px;color:{muted};font-weight:600;min-width:70px;
      text-align:right">them:</div>
    <div style="font-size:24px;color:{muted};line-height:1.5">...are you okay?</div>
  </div>

  <!-- Plant + final -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 12.0s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 13s infinite;">
      {cherry}
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.5s ease-out 13.5s forwards;
    font-size:24px;color:{accent};font-style:italic">
    I've never been better.</div>
</div>
{footer(14.5, muted)}"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 15: "Executive dysfunction starter pack"
# Grid of relatable ADHD moments → bloomday antidote
# ═══════════════════════════════════════════════════════
def build_meme15_starter_pack():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    strawberry = sv(PLANTS['Alpine Strawberry']['svg'], 180, 202)

    items = [
        (1.0, "13 unread texts", 0),
        (1.6, "inbox: 4,382", 1),
        (2.2, "3 half-eaten meals", 0),
        (2.8, "clean laundry still in dryer", 1),
        (3.4, "started 7 projects\nfinished 0", 0),
        (4.0, "\"I'll do it tomorrow\"\n— me, 3 weeks ago", 1),
    ]

    grid_html = ''
    for delay, text, col in items:
        x = 40 + col * 490
        grid_html += f"""
        <div style="opacity:0; animation: fadeInUp 0.4s ease-out {delay}s forwards;
          background:rgba(94,112,84,0.08);border-radius:20px;padding:24px 28px;
          width:460px;position:absolute;left:{x}px;
          top:{60 + items.index((delay,text,col)) // 2 * 160}px">
          <div style="font-size:22px;color:{dark};line-height:1.4;white-space:pre-line">{text}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:80px 40px {FOOTER_PAD}px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:44px;
      color:{dark};line-height:1.1">executive dysfunction<br>starter pack</div>
  </div>

  <!-- Grid of items -->
  <div style="position:relative;width:100%;height:540px">
    {grid_html}
  </div>

  <!-- Divider -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 5.5s forwards;
    width:60px;height:3px;background:{accent}"></div>

  <!-- The antidote -->
  <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:{dark};line-height:1.3">
    but then you open bloomday<br>and check off ONE thing</div>

  <div style="opacity:0; animation: bounceIn 0.6s ease-out 8.0s forwards;
    background:rgba(94,112,84,0.1);border:2px solid {accent};border-radius:20px;
    padding:16px 36px;display:inline-flex;align-items:center;gap:12px">
    <div style="width:28px;height:28px;border-radius:50%;background:{accent};
      display:flex;align-items:center;justify-content:center;
      opacity:0;animation:checkmark 0.5s ease-out 9.0s forwards">
      <span style="color:#f5f0e8;font-size:18px;font-weight:700">✓</span>
    </div>
    <div style="font-size:22px;color:{dark}">"brush teeth"</div>
  </div>

  <!-- Plant -->
  <div style="opacity:0; animation: scaleIn 0.8s ease-out 9.5s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 10.5s infinite;">
      {strawberry}
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.5s ease-out 11.0s forwards;
    font-size:24px;color:{accent};font-style:italic">
    and a strawberry grew.</div>
</div>
{footer(12.0, muted)}"""
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

    print("\n🧠 BloomDay ADHD Meme TikToks — Part 2\n")

    videos = [
        ('meme_adhd_paralysis',       build_meme8_paralysis,           15000),
        ('meme_adhd_object_perm',     build_meme9_object_permanence,   14000),
        ('meme_adhd_dopamine',        build_meme10_dopamine,           11000),
        ('meme_adhd_therapist',       build_meme11_therapist,          14000),
        ('meme_adhd_tax',             build_meme12_adhd_tax,           15000),
        ('meme_adhd_brain_tabs',      build_meme13_brain_tabs,         14000),
        ('meme_adhd_explain_friends', build_meme14_explain_to_friends, 16000),
        ('meme_adhd_starter_pack',    build_meme15_starter_pack,       14000),
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
            "can't start. can't answer. can't even get up. "
            "then you open bloomday and do one tiny thing. "
            "'drink water.' ✓ the freeze thawed a little.\n\n"
            "that's enough. that's the whole point.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdparalysis #adhdtiktok #executivedysfunction #bloomday #softproductivity"
        ),
        'meme_adhd_object_perm': (
            "object permanence? don't know her.\n\n"
            "january: downloaded bloomday. february: forgot it existed. "
            "march: still forgot. april: found it on page 4 of my phone. "
            "opened it. everything was still alive.\n\n"
            "no guilt. no dead plants. just 'welcome back.'\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #objectpermanence #adhdtiktok #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_dopamine': (
            "the task: 'take out the trash'\n"
            "when the dopamine hits: 🌻🌻🌻\n\n"
            "(it was literally just the trash)\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #dopamine #adhdtiktok #bloomday #adhdproductivity #adhdmemes"
        ),
        'meme_adhd_therapist': (
            "things my therapist said to do:\n"
            "✓ break tasks into tiny steps\n"
            "✓ celebrate small wins\n"
            "✓ don't punish yourself for missing days\n"
            "✓ find something that grows with you\n"
            "✓ be kind to yourself\n\n"
            "wait this is just a plant app. a really good plant app.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #therapy #adhdtiktok #bloomday #mentalhealth #softproductivity"
        ),
        'meme_adhd_tax': (
            "the ADHD tax (things I paid for because I forgot)\n\n"
            "$12 late fee. $35 overdraft. $9.99/mo forgot to cancel. "
            "$15 reordered what I already had. $49 missed the refund window.\n\n"
            "bloomday ADHD tax: $0\n"
            "free forever. nothing to forget to cancel.\n\n"
            "bloomday.app\n\n"
            "#adhd #adhdtax #adhdtiktok #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_brain_tabs': (
            "my brain has 47 tabs open\n\n"
            "did I lock the door. WHERE ARE MY KEYS. is it tuesday. "
            "forgot to eat again. why did I walk in here.\n\n"
            "but this one tab... just has a quiet garden.\n"
            "no noise. no streaks. no pressure. just one plant at a time.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #braintabs #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_adhd_explain_friends': (
            "how I explain bloomday to neurotypical friends\n\n"
            "me: it's a productivity app\n"
            "them: oh like todoist?\n"
            "me: no, you grow plants\n"
            "them: ...farmville?\n"
            "me: NO ok so imagine you have ADHD and everything feels impossible "
            "but then you check off 'drink water' and a cherry blossom grows "
            "and suddenly you feel like you can do anything\n"
            "them: ...are you okay?\n"
            "me: I've never been better.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #bloomday #neurodivergent #adhdmemes #relatable"
        ),
        'meme_adhd_starter_pack': (
            "executive dysfunction starter pack\n\n"
            "13 unread texts. inbox: 4,382. 3 half-eaten meals. "
            "clean laundry still in dryer. started 7 projects finished 0. "
            "'I'll do it tomorrow' — me, 3 weeks ago.\n\n"
            "but then you open bloomday and check off ONE thing: 'brush teeth'\n"
            "and a strawberry grew.\n\n"
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
