# Project 17 · Same Page, New Design

**Section D · Video, skills and design** — GenAI Internship, Week 2, Bharat Space Education Research Centre

One plain web page for an imaginary Bengaluru breakfast café, **The Tiffin Room**, built twice with exactly the same words:

| File | How it was made |
|---|---|
| `before.html` | Step 1 — built with **no design skill**. Plain HTML, browser default styles. |
| `after.html` | Step 3 — redesigned using the **frontend-design** skill (from skills.sh). |

## How to open it
Double-click `before.html` or `after.html`. No internet, no install, no login needed — the fonts are stored in the `fonts/` folder, so the redesign looks the same with Wi-Fi off.

## Done when — checklist

- [x] **Both before.html and after.html exist.**
- [x] **The words in both files match.** Run `python3 check_words.py`. It pulls the visible text out of both files and compares them word by word.
  Result: `before.html: 197 words | after.html: 197 words — PASS`.
- [x] **The redesign works on a phone.** Tested at 390 px wide (iPhone 12–15 size): no sideways scrolling, menu turns into a stacked list, buttons are at least 48 px tall for thumbs. See `screenshots/after-phone.png`.
- [x] **3 design changes and why each one helps** — below.

## 3 design changes and why each one helps

### 1. Colours taken from the café's own world
Before: blue links on white, nothing that says "breakfast" or "Bengaluru".
After: banana-leaf green for the top, red-oxide (the red floor of old Malleswaram houses) for the menu, turmeric yellow for the main button and prices, steel grey for the tumbler drawing.
**Why it helps:** the page feels like *this* café, not any café. Strong colour bands also split the page into clear parts, so you always know whether you're reading about the café, the menu or the address.

### 2. Two fonts with clear jobs, and a real type scale
Before: Times New Roman everywhere, every heading similar size.
After: **Rozha One** (big, signboard-like serif) for the name, headings, dish names and prices; **Mukta** (clean sans-serif) for everything you read in sentences. Both are from Indian Type Foundry, which fits a South Indian café.
**Why it helps:** your eye jumps straight to the dish name and price, then reads the description only if it wants to. The huge café name in the hero is remembered.

### 3. A menu you can scan, laid out for each screen
Before: a table with grey borders — hard to read, and squashed on a phone.
After: on a laptop, three clean columns with dotted lines between dishes (like a printed menu card). On a phone, each dish becomes a block: name and price on one line, description under it.
**Why it helps:** the most important question on a café page is "what can I eat and how much is it?" — this now takes one glance on any screen.

**Smaller changes:** buttons that look like buttons ("See today's menu" is the main action, so it's yellow); the phone number is now a tap-to-call button; a hand-drawn steel tumbler and davara with rising steam in the header (the only animation, and it stops if your phone has "reduce motion" on); visible yellow focus ring when using the keyboard.

## Folder contents
```
before.html          Step 1 — no design skill
after.html           Step 3 — with the frontend-design skill
fonts/               Rozha One + Mukta (.woff2) and their open-font licences (OFL)
check_words.py       proves the words match
screenshots/         before/after at laptop (1280px) and phone (390px) widths
prompts.md           every prompt used, in order
```

## Credits
Fonts: Rozha One and Mukta by Indian Type Foundry, SIL Open Font License (files in `fonts/`). Café, people and phone number are made up.
