#!/usr/bin/env python3
"""Build protocol pages from protocols/src/*.md. Run from the repo root."""
import glob, html, os, re, subprocess
BASE="https://jktembiwa.github.io/JKTembiwa/"
NAV='''<a href="../index.html">About</a>
<a href="../research.html">Research</a>
<a href="../methods.html">Methods</a>
<a href="../publications.html">Publications</a>
<a href="../news.html">News</a>
<a href="../contact.html">Contact</a>'''
def head(title,desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(desc,quote=True)}">
<meta name="robots" content="noindex">
<title>{html.escape(title)} | Microbial Mosaic</title>
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<link rel="stylesheet" href="../assets/style.css">
<link rel="stylesheet" href="../assets/protocols.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
<div class="container nav-wrap">
<a class="brand" href="../index.html"><span class="brand-mark"><img src="../assets/brand-mark.png" alt="" width="42" height="42"></span><span>Microbial Mosaic</span></a>
<nav class="nav" aria-label="Main navigation">
{NAV}
</nav>
</div>
</header>
<main id="main">
'''
FOOT='''</main>
<footer class="site-footer"><div class="container footer-row"><span>© 2026 Karen Tembiwa · Microbial Mosaic</span><a href="../contact.html">Contact</a></div></footer>
</body>
</html>
'''
def md(text):
    return subprocess.run(["pandoc","-f","markdown+pipe_tables+bracketed_spans","-t","html","--wrap=none"],input=text,capture_output=True,text=True,check=True).stdout
def parse(path):
    raw=open(path,encoding="utf-8").read()
    meta,body=raw.split("\n---\n",1)
    d={}
    for line in meta.splitlines():
        k,v=line.split(":",1); d[k.strip()]=v.strip()
    d["tags"]=[t.strip() for t in d["tags"].split(",")]
    d.setdefault("category","Protocols")
    d["slug"]=os.path.splitext(os.path.basename(path))[0]
    d["body"]=body
    return d
pages=[parse(p) for p in sorted(glob.glob("protocols/src/*.md"))]
os.makedirs("protocols",exist_ok=True)
STATUS='<span class="status draft">Draft: not yet reviewed by the author</span>'
LEGEND='<p class="tbc-legend"><span class="tbc">Highlighted</span> values are awaiting confirmation. Do not rely on them without checking.</p>'
for p in pages:
    out=head(p["title"],p["summary"])+f'''<section class="page-hero"><div class="container">
<div class="eyebrow"><a href="index.html">Protocols</a></div>
<h1 class="proto-title">{html.escape(p["title"])}</h1>
<p class="lede">{html.escape(p["summary"])}</p>
<p class="proto-meta">{STATUS} <span class="meta">{html.escape(p["version"])}</span></p>
</div></section>
<section class="section"><div class="container prose">
{LEGEND}
{md(p["body"])}
<hr>
<p class="meta"><strong>Source / credit:</strong> {html.escape(p["source"])}</p>
<p class="tag-row">{''.join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"])}</p>
<p><a href="index.html">← All protocols</a> · <a href="faq.html">Troubleshooting FAQ</a></p>
</div></section>
'''+FOOT
    open(f"protocols/{p['slug']}.html","w",encoding="utf-8").write(out)
# index
ORDER=["Media and reagents","Cloning","Transformation","Mycobacterial genetics","Imaging and analysis","Reference","Protocols"]
from collections import Counter
_c=Counter(t.lower() for p in pages for t in p['tags'])
alltags=sorted({t for p in pages for t in p['tags'] if _c[t.lower()]>=2})
def card(p):
    return f'''<article class="card proto-card" data-tags="{html.escape('|'.join(p['tags']).lower(),quote=True)}" data-text="{html.escape((p['title']+' '+p['summary']+' '+' '.join(p['tags'])).lower(),quote=True)}">
<h3><a href="{p['slug']}.html">{html.escape(p['title'])}</a></h3>
<p>{html.escape(p['summary'])}</p>
<p class="meta">{STATUS}</p>
</article>
'''
cards=""
cats=[c for c in ORDER if any(p["category"]==c for p in pages)]+sorted({p["category"] for p in pages}-set(ORDER))
for c in cats:
    cards+=f'<section class="proto-group"><h2 class="group-title">{html.escape(c)}</h2><div class="grid-2">\n'+"".join(card(p) for p in pages if p["category"]==c)+"</div></section>\n"
buttons=''.join(f'<button type="button" class="chip" data-tag="{html.escape(t.lower(),quote=True)}">{html.escape(t)}</button>' for t in alltags)
idx=head("Protocols","Common molecular microbiology protocols and troubleshooting notes.")+f'''<section class="page-hero"><div class="container">
<div class="eyebrow">Protocols</div>
<h1>Common protocols and troubleshooting.</h1>
<p class="lede">Practical protocols for everyday molecular microbiology, with notes on where they usually go wrong. Pages marked <em>Draft</em> have not yet been fully reviewed.</p>
<p class="meta">These pages draw on the Boutte Lab Beginner&rsquo;s Manual and the work of past lab members; individual credits appear on each page where relevant.</p>
<p><a class="button secondary" href="faq.html">Troubleshooting FAQ</a></p>
</div></section>
<section class="section"><div class="container">
<label class="sr-only" for="q">Search protocols</label>
<input id="q" class="search" type="search" placeholder="Search protocols (e.g. PCR, conjugation, plates)">
<div class="chips" role="group" aria-label="Filter by tag">{buttons}</div>
<p id="empty" class="meta" hidden>No protocols match.</p>
<div id="list">
{cards}</div>
</div></section>
<script src="../assets/protocols.js"></script>
'''+FOOT
open("protocols/index.html","w",encoding="utf-8").write(idx)
# FAQ
faq=[l.strip() for l in open("protocols/faq.txt",encoding="utf-8").read().split("\n===\n") if l.strip()]
items=""
for block in faq:
    lines=block.split("\n")
    q=lines[0]; link=lines[1]; ans="\n".join(lines[2:])
    slug,label=link.split("|")
    items+=f'<details class="faq"><summary>{html.escape(q)}</summary>{md(ans)}<p class="meta">Related: <a href="{slug}.html">{html.escape(label)}</a> · {STATUS}</p></details>\n'
f=head("Troubleshooting FAQ","Common failure points in molecular microbiology protocols.")+f'''<section class="page-hero"><div class="container">
<div class="eyebrow"><a href="index.html">Protocols</a></div>
<h1>Troubleshooting FAQ.</h1>
<p class="lede">Common failure points and what usually fixes them. Entries come from lab experience and are marked as drafts until reviewed.</p>
</div></section>
<section class="section"><div class="container prose">
{LEGEND}
{items}
<p><a href="index.html">← All protocols</a></p>
</div></section>
'''+FOOT
open("protocols/faq.html","w",encoding="utf-8").write(f)
print("built",len(pages),"protocols,",len(faq),"faq entries")
