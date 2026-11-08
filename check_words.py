"""Checks that before.html and after.html contain exactly the same words, in the same order.
Run: python3 check_words.py"""
import re, sys
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, a):
        if tag in ("style", "script", "title", "svg"): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ("style", "script", "title", "svg"): self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.parts.append(d)

def words(path):
    t = Text(); t.feed(open(path, encoding="utf-8").read())
    return re.findall(r"[\w₹']+", " ".join(t.parts))

b, a = words("before.html"), words("after.html")
print(f"before.html: {len(b)} words | after.html: {len(a)} words")
if a == b:
    print("PASS: the words match exactly, in the same order.")
else:
    import difflib
    for line in difflib.unified_diff(b, a, "before", "after", lineterm=""): print(line)
    sys.exit(1)
