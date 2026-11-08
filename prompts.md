# prompts.md — Project 17: Same Page, New Design

Agent used: Claude (Opus 5.5). Prompts saved in the order they were used.

---

### Prompt 1 — Step 1, without a skill
> Build one simple web page for a South Indian breakfast café in Malleswaram, Bengaluru, called "The Tiffin Room". Include: a heading and one-line tagline, two links ("See today's menu" and "Find us"), three reasons people come back, a menu table with 5 items (name, short description, price in ₹), two short quotes from regulars, and the address, opening hours and phone number. Use plain HTML only — no CSS, no design skill, no fonts. Save it as before.html.

### Prompt 2 — Step 2, add a design skill
> Load the frontend-design skill. Before writing any code, critique before.html: list its biggest design problems in order of importance.

Critique that came back (short version):
1. Nothing about it says "café" or "Bengaluru" — default blue links and Times font.
2. No hierarchy: the café name, section headings and body text all feel the same weight.
3. The menu table is the most important part but the hardest to read, and it gets squashed on a phone.
4. The two links don't look like actions, and the phone number can't be tapped.

### Prompt 3 — Step 3, redesign
> Using the skill, fix the biggest problems one at a time and save the result as after.html. Rules:
> - Keep every word exactly the same as before.html — same text, same order. Don't add or remove any copy.
> - Make the colours and fonts come from the café's world, not a generic template.
> - Store the fonts inside the project folder so it works with Wi-Fi off.
> - It must work on a phone (390px wide) with no sideways scrolling.
> - Respect "reduce motion" and show a keyboard focus ring.

### Prompt 4 — Check it
> Take screenshots of both pages at laptop and phone width and review them. Then write a small script, check_words.py, that pulls the visible text out of both files and proves the words match.

### Prompt 5 — Explain it
> Write a README listing the 3 most important design changes and why each one helps, so I can explain them myself.
