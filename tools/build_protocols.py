#!/usr/bin/env python3
"""Build protocol pages from protocols/src/*.md. Run from the repo root."""
import glob, html, json, os, re, subprocess
BASE="https://jktembiwa.github.io/JKTembiwa/"
NAV='''<a href="../index.html">About</a>
<a href="../research.html">Research</a>
<a href="../methods.html">Methods</a>
<a href="../publications.html">Publications</a>
<a href="../news.html">News</a>
<a href="../contact.html">Contact</a>'''
def head(title,desc,bar=''):
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
<link rel="stylesheet" href="../assets/notebook.css?v=11">
</head>
<body class="ruled">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
<div class="container nav-wrap">
<a class="brand" href="../index.html"><span class="brand-mark"><img src="../assets/brand-mark.png" alt="Microbial Mosaic logo" width="42" height="42"></span><span class="brand-text"><small class="brand-kicker">Notebook of Karen Tembiwa · Vol. 1</small><span>Microbial Mosaic</span></span></a>
<nav class="nav" aria-label="Main navigation">
{NAV}
</nav>
</div>
</header>
<main id="main">
'''+(f'<div class="container entry-bar"><span>{html.escape(bar[0])}</span><span class="entry-date"></span><span>{html.escape(bar[1])}</span></div>\n' if bar else '')
FOOT='''</main>
<footer class="site-footer"><div class="container footer-row"><span>© 2026 Karen Tembiwa · Microbial Mosaic</span><a href="../contact.html">Contact</a></div></footer>
<script src="../assets/notebook.js?v=11"></script></body>
</html>
'''
def intro(path):
    d={}
    for l in open(path,encoding="utf-8"):
        if l.startswith("#") or ":" not in l: continue
        k,v=l.split(":",1); d[k.strip()]=v.strip()
    return d
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
STUDY='<span class="status draft study">Study notes: not yet run by the author</span>'
def badge(p):
    st=p.get("status","").lower()
    return "" if st=="reviewed" else (STUDY if st=="study" else STATUS)
LEGEND='<p class="tbc-legend"><span class="tbc">Highlighted</span> values are awaiting confirmation. Do not rely on them without checking.</p>'
INLINE=r"</?(?:a|b|i|em|strong|span|sub|sup|code|abbr|small)\b[^>]*>"
def plain(h):
    """Rendered body as plain text for full-text search."""
    h=re.sub(r"(?is)<(script|style)\b.*?</\1>"," ",h)
    h=re.sub(INLINE,"",h)  # keep OD<sub>600</sub> as one word
    return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",h))).strip()
TITLES={p["slug"]:p["title"] for p in pages}
def which(p):
    """'Which version should I use?' box from the optional 'related' header: slug | note || slug | note"""
    if not p.get("related"): return ""
    li=""
    for item in p["related"].split("||"):
        slug,note=[x.strip() for x in item.split("|",1)]
        if slug not in TITLES: raise SystemExit(f"{p['slug']}: related page not found: {slug}")
        li+=f'<li><a href="{slug}.html">{html.escape(TITLES[slug])}</a>: {html.escape(note)}</li>\n'
    return f'<aside class="which-box"><h2>Which one should I use?</h2><p>Other pages cover related versions or steps:</p><ul>\n{li}</ul></aside>\n'
for p in pages:
    p["html"]=md(p["body"])
    # "status: reviewed" in a source header drops the draft badge; the legend then appears only if .tbc spans remain
    reviewed=p.get("status","").lower()=="reviewed"
    status=(badge(p)+" ") if badge(p) else ""
    legend=LEGEND if not reviewed or "{.tbc}" in p["body"] else ""
    out=head(p["title"],p["summary"],("Protocol · "+p["category"],p["version"]))+f'''<section class="page-hero"><div class="container">
<div class="eyebrow"><a href="index.html">Protocols</a></div>
<h1 class="proto-title">{html.escape(p["title"])}</h1>
<p class="lede">{html.escape(p["summary"])}</p>
<p class="proto-meta">{status}<span class="meta">{html.escape(p["version"])}</span></p>
</div></section>
<section class="section"><div class="container prose">
{which(p)}{legend}
{p["html"]}
<hr>
<p class="meta"><strong>Source / credit:</strong> {html.escape(p["source"])}</p>
<p class="tag-row">{''.join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"])}</p>
<p class="proto-foot"><a href="index.html">← All protocols</a><a href="faq.html">Troubleshooting FAQ</a></p>
</div></section>
'''+FOOT
    open(f"protocols/{p['slug']}.html","w",encoding="utf-8").write(out)
# index
ORDER=["Media and reagents","Cloning","Transformation","Mycobacterial genetics","Protein biochemistry","Growth and assays","Imaging","Flow cytometry","Analysis","Computational analysis","Organism quick-starts","Reference","Protocols"]
from collections import Counter
_c=Counter(t.lower() for p in pages for t in p['tags'])
alltags=sorted({t for p in pages for t in p['tags'] if _c[t.lower()]>=2})
def card(p):
    return f'''<article class="card proto-card" data-tags="{html.escape('|'.join(p['tags']).lower(),quote=True)}" data-text="{html.escape((p['title']+' '+p['summary']+' '+' '.join(p['tags'])).lower(),quote=True)}">
<h3><a href="{p['slug']}.html">{html.escape(p['title'])}</a></h3>
<p>{html.escape(p['summary'])}</p>
<p class="meta">{badge(p)}</p>
</article>
'''
cards=""
cats=[c for c in ORDER if any(p["category"]==c for p in pages)]+sorted({p["category"] for p in pages}-set(ORDER))
for c in cats:
    cards+=f'<section class="proto-group"><h2 class="group-title">{html.escape(c)}</h2><div class="grid-2">\n'+"".join(card(p) for p in pages if p["category"]==c)+"</div></section>\n"
II=intro("protocols/intro-index.txt")
FI=intro("protocols/intro-faq.txt")
buttons=''.join(f'<button type="button" class="chip" data-tag="{html.escape(t.lower(),quote=True)}">{html.escape(t)}</button>' for t in alltags)
idx=head("Protocols","Common molecular microbiology protocols and troubleshooting notes.",("Protocols · Index","All protocols"))+f'''<section class="page-hero"><div class="container">
<div class="eyebrow">Protocols</div>
<h1>{II["heading"]}</h1>
<p class="lede">{II["lede"]}</p>
<p class="meta">{II["note"]}</p>
<p><a class="button secondary" href="faq.html">Troubleshooting FAQ</a></p>
</div></section>
<section class="section"><div class="container">
<label class="sr-only" for="q">Search protocols</label>
<input id="q" class="search" type="search" placeholder="Search all protocol text (e.g. glycerol wash, hygromycin, OD600)">
<div class="chips" role="group" aria-label="Filter by tag">{buttons}</div>
<p id="empty" class="meta" hidden>No protocols match.</p>
<div id="list">
{cards}</div>
</div></section>
<script src="../assets/protocols.js"></script>
'''+FOOT
open("protocols/index.html","w",encoding="utf-8").write(idx)
# full-text search data, loaded by assets/protocols.js
json.dump([{"slug":p["slug"],"text":plain(p["html"])} for p in pages],open("protocols/search.json","w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
# FAQ
faq=[l.strip() for l in open("protocols/faq.txt",encoding="utf-8").read().split("\n===\n") if l.strip()]
groups={}; order=[]; cat="General"; nfaq=0
for block in faq:
    lines=block.split("\n")
    if lines[0].startswith("@ "):
        cat=lines[0][2:].strip(); lines=lines[1:]
    q=lines[0]; link=lines[1]; ans="\n".join(lines[2:])
    slug,label=link.split("|")
    if cat not in groups: groups[cat]=""; order.append(cat)
    groups[cat]+=f'<details class="faq"><summary>{html.escape(q)}</summary>{md(ans)}<p class="meta">Related: <a href="{slug}.html">{html.escape(label)}</a> · {STATUS}</p></details>\n'
    nfaq+=1
def cid(c): return "cat-"+re.sub(r"[^a-z0-9]+","-",c.lower()).strip("-")
jump=''.join(f'<a class="chip" href="#{cid(c)}">{html.escape(c)}</a> ' for c in order)
items=''.join(f'<section class="faq-group" id="{cid(c)}"><h2 class="faq-cat">{html.escape(c)}</h2>\n{groups[c]}</section>\n' for c in order)
items=f'<input id="fq" class="search" type="search" placeholder="Search the FAQ (e.g. smear, precipitate, lawn, Tween)" aria-label="Search the FAQ">\n<p class="faq-jump">{jump}</p>\n<p id="fempty" class="meta" hidden>No questions match.</p>\n'+items
FAQJS='''<script>
(function(){var q=document.getElementById("fq");if(!q)return;var items=[].slice.call(document.querySelectorAll("details.faq")),groups=[].slice.call(document.querySelectorAll(".faq-group")),empty=document.getElementById("fempty");
function run(){var t=q.value.trim().toLowerCase(),n=0;items.forEach(function(d){var m=!t||d.textContent.toLowerCase().indexOf(t)>-1;d.hidden=!m;if(t)d.open=m;else d.open=false;if(m)n++});
groups.forEach(function(g){g.hidden=!g.querySelector("details.faq:not([hidden])")});empty.hidden=n>0}
q.addEventListener("input",run)})();
</script>'''
f=head("Troubleshooting FAQ","Common failure points in molecular microbiology protocols.",("Protocols · FAQ","Troubleshooting"))+f'''<section class="page-hero"><div class="container">
<div class="eyebrow"><a href="index.html">Protocols</a></div>
<h1>{FI["heading"]}</h1>
<p class="lede">{FI["lede"]}</p>
</div></section>
<section class="section"><div class="container prose">
{LEGEND}
{items}
<p class="proto-foot"><a href="index.html">← All protocols</a><a href="faq.html">Troubleshooting FAQ</a></p>
</div></section>
'''+FAQJS+FOOT
open("protocols/faq.html","w",encoding="utf-8").write(f)
print("built",len(pages),"protocols,",nfaq,"faq entries")
