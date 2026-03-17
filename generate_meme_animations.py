#!/usr/bin/env python3
"""BloomDay Meme TikTok Animations — viral meme formats as MP4 videos."""

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
    'red_dark': '#c0392b',
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
  @keyframes typewriter {{
    from {{ clip-path: inset(0 100% 0 0); }}
    to {{ clip-path: inset(0 0% 0 0); }}
  }}
  @keyframes glowPulse {{
    0%, 100% {{ text-shadow: 0 0 20px rgba(154,176,106,0.3); }}
    50% {{ text-shadow: 0 0 40px rgba(154,176,106,0.8), 0 0 80px rgba(154,176,106,0.4); }}
  }}
</style>
</head><body>{body_html}</body></html>"""


# ═══════════════════════════════════════════════════════
# MEME 1: POV — "You missed a whole week"
# Text appears line by line with dramatic pauses,
# then plant drops in with a bounce
# ═══════════════════════════════════════════════════════
def build_meme1_pov_missed():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']
    cream = COLORS['cream']
    dark = COLORS['text_dark']

    zz = sv(PLANTS['ZZ Plant']['svg'], 320, 360)

    lines = [
        (1.8, "You open the app after a week.", muted, 24),
        (3.0, "No notification.", '#f5f0e8', 28),
        (4.0, "No broken streak.", '#f5f0e8', 28),
        (5.0, "No guilt trip.", '#f5f0e8', 28),
        (6.2, "Just your ZZ plant.", accent, 32),
        (7.2, "Standing there.", accent, 32),
        (8.0, "Like nothing happened.", accent, 36),
    ]

    lines_html = ''
    for delay, text, color, size in lines:
        lines_html += f"""
        <div style="opacity:0; animation: fadeInUp 0.5s ease-out {delay}s forwards;
          font-size:{size}px; color:{color}; line-height:1.6; font-weight:{'600' if color == accent else '400'}">
          {text}</div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 70px 80px;
  text-align:center">

  <!-- POV badge drops in -->
  <div style="opacity:0; animation: dropIn 0.8s ease-out 0.3s forwards;">
    <div style="background:{cream};color:{dark};font-size:110px;font-weight:700;
      letter-spacing:-2px;padding:10px 52px 18px;border-radius:28px;
      line-height:1;display:inline-block">POV</div>
  </div>

  <!-- Title -->
  <div style="opacity:0; animation: fadeIn 0.8s ease-out 1.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:52px;
    color:#f5f0e8;line-height:1.1">
    you missed a<br>whole week.</div>

  <!-- Lines appear one by one -->
  <div style="display:flex;flex-direction:column;gap:6px;text-align:left;
    width:100%;padding:0 20px">
    {lines_html}
  </div>

  <!-- Plant drops in at the end -->
  <div style="opacity:0; animation: dropIn 1s cubic-bezier(0.34, 1.56, 0.64, 1) 9.0s forwards;">
    <div style="animation: gentleSway 3s ease-in-out 10s infinite;">
      {zz}
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.5s ease-out 10.5s forwards;
    font-size:20px;color:{accent};letter-spacing:1px">
    because nothing happened.</div>

  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 11.5s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 2: "In my ___ era" — CEO energy
# Dramatic era reveal, then comedic punchline
# ═══════════════════════════════════════════════════════
def build_meme2_ceo_era():
    bg = COLORS['sage']
    accent = COLORS['accent_sage']
    muted = COLORS['muted_sage']

    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 300, 338)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 60px 80px;
  text-align:center">

  <!-- "in my" - small, muted -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 0.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:48px;
    color:{muted};line-height:1.1">in my</div>

  <!-- Main era text - BIG dramatic reveal -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 1.5s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:72px;
      color:#f5f0e8;line-height:1.05;font-weight:700">
      doing one task<br>and feeling like<br>a CEO</div>
  </div>

  <!-- "era" -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 3.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:48px;
    color:{muted};line-height:1.1">era</div>

  <!-- Divider -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 3.8s forwards;
    width:80px;height:3px;background:{accent}"></div>

  <!-- Plant pops in -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 4.2s forwards;">
    <div style="animation: float 3s ease-in-out 5s infinite;">
      {monstera}
    </div>
  </div>

  <!-- Punchline 1 -->
  <div style="opacity:0; animation: fadeInUp 0.6s ease-out 5.5s forwards;
    font-size:26px;color:{accent};font-style:italic;line-height:1.5">
    the monstera grew a new leaf.<br>I am unstoppable.</div>

  <!-- Punchline 2 - the joke -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 7.0s forwards;
    font-size:20px;color:{muted};line-height:1.5">
    (the task was "reply to one email")</div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 8.5s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">
    bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 3: Other Apps vs BloomDay — Side comparison
# Left side gets struck through, right side glows
# ═══════════════════════════════════════════════════════
def build_meme3_other_apps_vs():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']
    red = COLORS['red']

    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 220, 248)
    snake = sv(PLANTS['Snake Plant']['svg'], 200, 225)

    other_apps = [
        (1.5, "missed a day?"),
        (2.2, "STREAK LOST"),
        (3.0, "here's a guilt notification"),
        (3.8, "your plants are DYING"),
        (4.6, "pay $9.99 to recover"),
    ]

    bloomday_lines = [
        (6.5, "missed a week?"),
        (7.2, "that's okay."),
        (7.9, "your garden waited."),
        (8.6, "nothing died."),
        (9.3, "welcome back."),
    ]

    left_html = ''
    for delay, text in other_apps:
        left_html += f"""
        <div style="opacity:0; animation: shakeNo 0.5s ease-out {delay}s forwards, fadeIn 0.3s ease-out {delay}s forwards;
          position:relative; font-size:24px; color:{red}; line-height:2.0">
          {text}
          <div style="position:absolute;top:50%;left:0;height:3px;background:{red};
            width:0; animation: strikethrough 0.4s ease-out {delay+0.8}s forwards;"></div>
        </div>"""

    right_html = ''
    for delay, text in bloomday_lines:
        right_html += f"""
        <div style="opacity:0; animation: fadeInUp 0.5s ease-out {delay}s forwards;
          font-size:24px; color:{accent}; line-height:2.0">
          {text}</div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:80px 50px 80px;
  text-align:center">

  <!-- Title -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:42px;
    color:#f5f0e8;line-height:1.15">
    every productivity app<br>I've ever tried</div>

  <!-- VS comparison -->
  <div style="display:flex;width:100%;gap:30px;align-items:flex-start">

    <!-- Left: Other apps -->
    <div style="flex:1;text-align:center">
      <div style="opacity:0; animation: fadeIn 0.4s ease-out 1.0s forwards;
        font-size:18px;color:{red};letter-spacing:2px;text-transform:uppercase;
        margin-bottom:20px">other apps</div>
      <div style="display:flex;flex-direction:column;gap:0;text-align:left;padding-left:20px">
        {left_html}
      </div>
    </div>

    <!-- Divider -->
    <div style="opacity:0; animation: fadeIn 0.3s ease-out 0.8s forwards;
      width:2px;background:rgba(255,255,255,0.1);min-height:350px;align-self:stretch"></div>

    <!-- Right: BloomDay -->
    <div style="flex:1;text-align:center">
      <div style="opacity:0; animation: fadeIn 0.4s ease-out 6.0s forwards;
        font-size:18px;color:{accent};letter-spacing:2px;text-transform:uppercase;
        margin-bottom:20px">bloomday</div>
      <div style="display:flex;flex-direction:column;gap:0;text-align:left;padding-left:20px">
        {right_html}
      </div>
    </div>
  </div>

  <!-- Plants appear at the bottom -->
  <div style="display:flex;gap:20px;align-items:flex-end;justify-content:center">
    <div style="opacity:0; animation: fadeInUp 0.8s ease-out 10.0s forwards;">
      <div style="animation: gentleSway 3s ease-in-out 11s infinite;">{snake}</div>
    </div>
    <div style="opacity:0; animation: fadeInUp 0.8s ease-out 10.4s forwards;">
      <div style="animation: gentleSway 3.5s ease-in-out 11.5s infinite;">{fiddle}</div>
    </div>
  </div>

  <!-- Final line -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 11.5s forwards;">
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:36px;
      color:{accent};animation: glowPulse 2s ease-in-out 12s infinite;
      margin-bottom:10px">nothing dies here.</div>
    <div style="font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
  </div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 4: "Tell me you have ADHD without telling me"
# Tasks appear, plant grows after each one
# ═══════════════════════════════════════════════════════
def build_meme4_tell_me_adhd():
    bg = COLORS['cream']
    dark = COLORS['text_dark']
    accent = COLORS['accent_cream']
    muted = COLORS['muted_cream']

    tasks = [
        (2.0, "opened the app at 11pm", "sunflower_small"),
        (4.0, "did one task: 'drink water'", "orchid_small"),
        (6.0, "grew a whole sunflower", "monstera_small"),
        (8.0, "wrote a letter to future me at 2am", "cherry_small"),
        (10.0, "forgot about it for 3 weeks", "zz_small"),
        (12.0, "came back. nothing died.", "snake_small"),
    ]

    plant_svgs = {
        'sunflower_small': sv(PLANTS['Sunflower']['svg'], 80, 90),
        'orchid_small': sv(PLANTS['Phalaenopsis Orchid']['svg'], 80, 90),
        'monstera_small': sv(PLANTS['Monstera Deliciosa']['svg'], 80, 90),
        'cherry_small': sv(PLANTS['Cherry Blossom']['svg'], 80, 90),
        'zz_small': sv(PLANTS['ZZ Plant']['svg'], 80, 90),
        'snake_small': sv(PLANTS['Snake Plant']['svg'], 80, 90),
    }

    tasks_html = ''
    for delay, text, plant_key in tasks:
        tasks_html += f"""
        <div style="opacity:0; animation: slideInLeft 0.5s ease-out {delay}s forwards;
          display:flex;align-items:center;gap:20px;width:100%">
          <div style="opacity:0; animation: scalePop 0.4s ease-out {delay+0.6}s forwards;
            flex-shrink:0">
            {plant_svgs[plant_key]}
          </div>
          <div style="font-size:26px;color:{dark};line-height:1.4;text-align:left">
            {text}</div>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 60px 80px;
  text-align:center">

  <!-- Header -->
  <div style="opacity:0; animation: fadeInDown 0.6s ease-out 0.3s forwards;">
    <div style="font-size:16px;color:{muted};letter-spacing:3px;text-transform:uppercase;
      margin-bottom:16px">bloomday</div>
    <div style="font-family:Georgia,'Times New Roman',serif;font-size:44px;
      color:{dark};line-height:1.1">tell me you have ADHD<br>without telling me<br>you have ADHD</div>
  </div>

  <!-- Divider -->
  <div style="opacity:0; animation: fadeIn 0.3s ease-out 1.5s forwards;
    width:60px;height:3px;background:{accent}"></div>

  <!-- Tasks appear one by one with plant icons -->
  <div style="display:flex;flex-direction:column;gap:20px;width:100%;padding:0 40px">
    {tasks_html}
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 14.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:36px;
    color:{accent};font-style:italic">
    peak performance.</div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 15.0s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 5: "The task was..." — Dramatic buildup
# Giant dramatic text, tiny punchline task, then
# HUGE plant celebration
# ═══════════════════════════════════════════════════════
def build_meme5_the_task_was():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    sunflower = sv(PLANTS['Sunflower']['svg'], 380, 428)
    monstera = sv(PLANTS['Monstera Deliciosa']['svg'], 200, 225)
    cherry = sv(PLANTS['Cherry Blossom']['svg'], 180, 202)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 60px 80px;
  text-align:center">

  <!-- "I just..." -->
  <div style="opacity:0; animation: fadeIn 0.6s ease-out 0.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:40px;
    color:{muted}">I just</div>

  <!-- "GREW A WHOLE SUNFLOWER" - huge, dramatic -->
  <div style="opacity:0; animation: scalePop 1s ease-out 1.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:76px;
    color:{accent};line-height:1.0;font-weight:700;
    animation: scalePop 1s ease-out 1.5s forwards, glowPulse 2s ease-in-out 3s infinite;">
    GREW A<br>WHOLE<br>SUNFLOWER</div>

  <!-- Sunflower pops in huge -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 3.0s forwards;">
    <div style="animation: float 2.5s ease-in-out 4s infinite;">
      {sunflower}
    </div>
  </div>

  <!-- Beat... -->
  <div style="opacity:0; animation: fadeIn 0.8s ease-out 5.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:{muted};font-style:italic">the task was...</div>

  <!-- Tiny punchline -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 6.5s forwards;
    background:rgba(255,255,255,0.05);border-radius:16px;padding:20px 40px;">
    <div style="font-size:22px;color:#f5f0e8;letter-spacing:1px">
      "reply to one email"</div>
  </div>

  <!-- Side plants celebrate -->
  <div style="display:flex;gap:30px;align-items:flex-end;justify-content:center">
    <div style="opacity:0; animation: slideInLeft 0.6s ease-out 7.5s forwards;">
      <div style="animation: gentleSway 2.5s ease-in-out 8s infinite;">{cherry}</div>
    </div>
    <div style="opacity:0; animation: fadeInUp 0.5s ease-out 8.0s forwards;
      font-family:Georgia,'Times New Roman',serif;font-size:28px;
      color:{accent};font-style:italic;padding:0 20px">
      peak<br>performance.</div>
    <div style="opacity:0; animation: slideInRight 0.6s ease-out 7.8s forwards;">
      <div style="animation: gentleSway 3s ease-in-out 8.5s infinite;">{monstera}</div>
    </div>
  </div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 9.5s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 6: "Nobody:" format — ADHD at 2am
# Classic nobody meme with plant gardening twist
# ═══════════════════════════════════════════════════════
def build_meme6_nobody():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']

    orchid = sv(PLANTS['Phalaenopsis Orchid']['svg'], 260, 293)
    strawberry = sv(PLANTS['Alpine Strawberry']['svg'], 200, 225)

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:120px 60px 80px;
  text-align:center">

  <div style="opacity:0; animation: fadeIn 0.5s ease-out 0.3s forwards;
    font-size:16px;color:{muted};letter-spacing:4px;text-transform:uppercase">
    bloomday</div>

  <!-- Nobody: -->
  <div style="opacity:0; animation: fadeIn 0.4s ease-out 1.0s forwards;
    font-size:32px;color:{muted};text-align:left;width:100%;padding-left:60px">
    nobody:</div>

  <!-- Absolutely nobody: -->
  <div style="opacity:0; animation: fadeIn 0.4s ease-out 2.0s forwards;
    font-size:32px;color:{muted};text-align:left;width:100%;padding-left:60px">
    absolutely nobody:</div>

  <!-- Me at 2am: -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 3.2s forwards;
    font-size:38px;color:#f5f0e8;text-align:left;width:100%;padding-left:60px;
    font-weight:600">
    me at 2am:</div>

  <!-- The action - dramatic -->
  <div style="opacity:0; animation: scalePop 0.8s ease-out 4.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:44px;
    color:{accent};line-height:1.2;max-width:800px">
    writing a time capsule<br>letter to future me<br>while growing an orchid</div>

  <!-- Plants appear -->
  <div style="display:flex;gap:40px;align-items:flex-end;justify-content:center">
    <div style="opacity:0; animation: fadeInUp 0.8s ease-out 6.0s forwards;">
      <div style="animation: float 3s ease-in-out 7s infinite;">{strawberry}</div>
    </div>
    <div style="opacity:0; animation: scalePop 1s ease-out 6.5s forwards;">
      <div style="animation: float 2.5s ease-in-out 7.5s infinite;">{orchid}</div>
    </div>
  </div>

  <!-- Punchline -->
  <div style="opacity:0; animation: fadeInUp 0.5s ease-out 8.5s forwards;
    font-size:22px;color:{muted};font-style:italic;line-height:1.5">
    the task was "take my meds"<br>but we don't talk about that</div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 10.0s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
</div>"""
    return base_html(bg, body)


# ═══════════════════════════════════════════════════════
# MEME 7: "POV: the only app that didn't gaslight you"
# Dark humor about toxic productivity apps
# ═══════════════════════════════════════════════════════
def build_meme7_pov_gaslight():
    bg = COLORS['dark']
    accent = COLORS['accent_dark']
    muted = COLORS['muted_dark']
    cream = COLORS['cream']
    dark = COLORS['text_dark']
    red = COLORS['red']

    fiddle = sv(PLANTS['Fiddle Leaf Fig']['svg'], 280, 315)

    # Fake notifications that shake and get dismissed
    notifs = [
        (1.5, "You haven't logged in for 3 days!", red),
        (2.8, "Your streak is about to expire!", red),
        (4.0, "Your friends completed 47 tasks!", red),
        (5.2, "Upgrade to Premium to recover!", red),
    ]

    notifs_html = ''
    for delay, text, color in notifs:
        notifs_html += f"""
        <div style="opacity:0;
          animation: shakeNo 0.6s ease-out {delay}s forwards, fadeIn 0.3s ease-out {delay}s forwards;
          background:rgba(231,76,60,0.15);border:2px solid {color};border-radius:16px;
          padding:16px 24px;width:100%;max-width:800px;
          font-size:22px;color:{color};text-align:left">
          {text}
          <span style="opacity:0; animation: fadeIn 0.2s ease-out {delay+0.8}s forwards;
            position:relative;float:right;font-size:28px;color:{muted}">
            ×</span>
        </div>"""

    body = f"""
<div style="width:100%;height:100%;display:flex;flex-direction:column;
  align-items:center;justify-content:space-between;padding:100px 60px 80px;
  text-align:center">

  <!-- POV badge -->
  <div style="opacity:0; animation: dropIn 0.8s ease-out 0.3s forwards;">
    <div style="background:{cream};color:{dark};font-size:100px;font-weight:700;
      letter-spacing:-2px;padding:8px 48px 14px;border-radius:24px;
      line-height:1;display:inline-block">POV</div>
  </div>

  <!-- Title -->
  <div style="opacity:0; animation: fadeIn 0.8s ease-out 0.8s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:42px;
    color:#f5f0e8;line-height:1.15">
    the only productivity app<br>that didn't gaslight you</div>

  <!-- Fake notifications appear and shake -->
  <div style="display:flex;flex-direction:column;gap:12px;width:100%;
    align-items:center;padding:0 20px">
    {notifs_html}
  </div>

  <!-- "then you found bloomday" -->
  <div style="opacity:0; animation: fadeIn 1s ease-out 7.0s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:32px;
    color:{muted};font-style:italic">
    then you found bloomday.</div>

  <!-- Plant grows peacefully -->
  <div style="opacity:0; animation: scaleIn 1.2s ease-out 8.5s forwards;">
    <div style="animation: float 3s ease-in-out 10s infinite;">
      {fiddle}
    </div>
  </div>

  <!-- Peaceful message -->
  <div style="opacity:0; animation: fadeInUp 0.6s ease-out 10.5s forwards;
    font-family:Georgia,'Times New Roman',serif;font-size:36px;
    color:{accent};animation: fadeInUp 0.6s ease-out 10.5s forwards, glowPulse 2s ease-in-out 11.5s infinite">
    nothing dies here.</div>

  <div style="opacity:0; animation: fadeIn 0.4s ease-out 12.0s forwards;
    font-size:15px;color:{muted};letter-spacing:2px">bloomday.app · free forever</div>
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

    print("\n🎬 BloomDay Meme TikTok Animations\n")

    videos = [
        ('meme_pov_missed_week',    build_meme1_pov_missed,     13000),
        ('meme_ceo_era',            build_meme2_ceo_era,        10000),
        ('meme_other_apps_vs',      build_meme3_other_apps_vs,  14000),
        ('meme_tell_me_adhd',       build_meme4_tell_me_adhd,   16000),
        ('meme_the_task_was',       build_meme5_the_task_was,   11000),
        ('meme_nobody_2am',         build_meme6_nobody,         11500),
        ('meme_pov_gaslight',       build_meme7_pov_gaslight,   14000),
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
        'meme_pov_missed_week': (
            "pov: you missed a whole week and your garden didn't even flinch\n\n"
            "no notification. no broken streak. just your ZZ plant, "
            "standing there like nothing happened. because nothing did.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #adhdproductivity #indieapp #adhdtiktok"
        ),
        'meme_ceo_era': (
            "in my doing one task and feeling like a CEO era\n\n"
            "the task was 'reply to one email.' the monstera grew a new leaf. "
            "I am peak performance.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #productivity #adhdproductivity #inmyera #ceoera"
        ),
        'meme_other_apps_vs': (
            "every productivity app I've ever tried vs bloomday\n\n"
            "one side: guilt, broken streaks, dying plants, pay to recover\n"
            "other side: nothing dies. ever.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #productivityapps #softproductivity #neurodivergent"
        ),
        'meme_tell_me_adhd': (
            "tell me you have ADHD without telling me you have ADHD\n\n"
            "opened the app at 11pm. did one task: 'drink water.' "
            "grew a whole sunflower. wrote a letter to future me at 2am. "
            "forgot about it for 3 weeks. came back. nothing died. peak performance.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #bloomday #neurodivergent #adhdmemes"
        ),
        'meme_the_task_was': (
            "I just GREW A WHOLE SUNFLOWER\n\n"
            "the task was \"reply to one email\"\n\n"
            "peak performance.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #softproductivity #adhdproductivity #adhdmemes"
        ),
        'meme_nobody_2am': (
            "nobody:\nabsolutely nobody:\nme at 2am: writing a time capsule letter to future me "
            "while growing an orchid\n\n"
            "the task was 'take my meds' but we don't talk about that\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #adhdtiktok #bloomday #nobody #2am #neurodivergent"
        ),
        'meme_pov_gaslight': (
            "pov: the only productivity app that didn't gaslight you\n\n"
            "no guilt notifications. no dying plants. no streak pressure. "
            "just a garden that waits.\n\n"
            "bloomday.app — free forever\n\n"
            "#adhd #bloomday #productivityapps #gaslighting #softproductivity #indieapp"
        ),
    }

    md = "# BloomDay Meme TikTok Animations\n\n---\n\n"
    for name, caption in captions.items():
        md += f"### bloomday_{name}.mp4\n\n{caption}\n\n---\n\n"
    captions_path = os.path.join(OUTPUT_DIR, 'bloomday_captions_meme_tiktoks.md')
    with open(captions_path, 'w') as f:
        f.write(md)

    print(f"\n✅ Done! {len(results)} meme TikTok animations saved to {OUTPUT_DIR}")
    for p in results:
        print(f"   {os.path.basename(p)}")
    print(f"   bloomday_captions_meme_tiktoks.md")
    print("\nAll videos are 1080×1920 MP4, ready for TikTok upload!")
