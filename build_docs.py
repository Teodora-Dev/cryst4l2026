#!/usr/bin/env python3
"""
Build docs/index.html from docs/markdown/*.md

Usage:
  python3 build_docs.py
"""
from __future__ import annotations

import re, html, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
MD = DOCS / "markdown"
OUT = DOCS / "index.html"

ORDER = [
  "01-introduction.md",
  "02-architecture.md",
  "03-layers.md",
  "04-objects.md",
  "05-components.md",
  "06-utilities.md",
  "07-tokens-and-theming.md",
  "08-queries.md",
  "09-composition.md",
  "10-lean-builds.md",
  "11-philosophy.md",
]

def md_to_html(md: str) -> str:
  lines = md.splitlines()
  out = []
  in_code = False
  para = []
  ul_open = False

  def flush_para():
    nonlocal para
    if para:
      text = " ".join([p.strip() for p in para]).strip()
      if text:
        text = re.sub(r'`([^`]+)`', lambda m: f"<code>{html.escape(m.group(1))}</code>", text)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        out.append(f"<p>{text}</p>")
      para = []

  def close_ul():
    nonlocal ul_open
    if ul_open:
      out.append("</ul>")
      ul_open = False

  for line in lines:
    if line.strip().startswith("```"):
      if not in_code:
        flush_para(); close_ul()
        in_code = True
        out.append("<pre><code>")
      else:
        in_code = False
        out.append("</code></pre>")
      continue

    if in_code:
      out.append(html.escape(line))
      continue

    if not line.strip():
      flush_para(); close_ul()
      continue

    m = re.match(r'^(#{1,3})\s+(.*)$', line)
    if m:
      flush_para(); close_ul()
      level = len(m.group(1))
      out.append(f"<h{level}>{html.escape(m.group(2).strip())}</h{level}>")
      continue

    m = re.match(r'^\-\s+(.*)$', line)
    if m:
      flush_para()
      if not ul_open:
        out.append("<ul>"); ul_open = True
      item = m.group(1).strip()
      item = re.sub(r'`([^`]+)`', lambda mm: f"<code>{html.escape(mm.group(1))}</code>", item)
      item = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', item)
      out.append(f"<li>{item}</li>")
      continue

    if line.strip().startswith(">"):
      flush_para(); close_ul()
      bq = html.escape(line.strip()[1:].strip())
      bq = re.sub(r'`([^`]+)`', lambda mm: f"<code>{html.escape(mm.group(1))}</code>", bq)
      out.append(f"<blockquote><p>{bq}</p></blockquote>")
      continue

    para.append(line)

  flush_para(); close_ul()
  return "\n".join(out)

def slug(title: str) -> str:
  s = title.lower()
  s = re.sub(r'[^a-z0-9\s\-]', '', s)
  s = re.sub(r'\s+', '-', s).strip('-')
  return s

def main():
  sections = []
  nav = []

  for fname in ORDER:
    path = MD / fname
    md = path.read_text(encoding="utf-8")
    m = re.search(r'^#\s+(.+)$', md, flags=re.MULTILINE)
    title = m.group(1).strip() if m else fname
    sid = slug(title)
    body_html = md_to_html(md)
    sections.append((sid, title, body_html))
    nav.append((sid, title))

  today = datetime.date.today().isoformat()

  html_out = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Cryst4l — Documentation</title>
  <link rel="stylesheet" href="./css/styles.css" />
  <link rel="stylesheet" href="./docs.css" />
  <style>
    html{{ scroll-behavior: smooth; }}
    :target{{ scroll-margin-top: 90px; }}
    blockquote{{ border-left: 3px solid color-mix(in oklab, currentColor 20%, transparent); padding-left: 1rem; margin-left: 0; }}
  </style>
</head>
<body>
  <header class="docs-topbar">
    <div class="docs-topbar-inner">
      <div class="docs-brand">
        <strong>Cryst4l</strong>
        <span>Documentation • built from Markdown</span>
      </div>
      <nav class="docs-nav" aria-label="Docs navigation">
        {''.join([f'<a href="#{sid}">{html.escape(title)}</a>' for sid,title in nav])}
      </nav>
    </div>
  </header>

  <main class="docs-shell">
    <section class="docs-hero" id="start">
      <div>
        <h1>Cryst4l Documentation</h1>
        <div class="docs-pillrow">
          <span class="docs-pill">Pure CSS</span>
          <span class="docs-pill">ITCSS via <code>@layer</code></span>
          <span class="docs-pill">Tokens</span>
          <span class="docs-pill">Utilities</span>
          <span class="docs-pill">Optional container queries</span>
        </div>
      </div>
      <aside class="docs-card">
        <h3>Build</h3>
        <pre><code>python3 build_docs.py</code></pre>
        <p style="margin-top:0.75rem;">Last built: {today}</p>
      </aside>
    </section>

    {''.join([f'<section id="{sid}">{body}</section>' for sid,title,body in sections])}

    <footer class="docs-footer">
      <p>Built from Markdown on {today}.</p>
    </footer>
  </main>
</body>
</html>
"""
  OUT.write_text(html_out, encoding="utf-8")
  print(f"Wrote {OUT}")

if __name__ == "__main__":
  main()
