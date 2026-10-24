# CLAUDE.md: working in this repo

Personal academic site "Microbial Mosaic" for Karen Tembiwa (mycobacterial cell biology; PhD from the Boutte lab at UTA, now a postdoc in the Lentz lab at UiT). Act as an expert in bacterial pathogen research, basic and translational. Keep replies concise unless she asks for depth.

## Repo and publishing
- GitHub Pages from `main`, root folder. Repo `jktembiwa/JKTembiwa` (the old `jktembiwa/jktembiwa` redirects). Live site: https://jktembiwa.github.io/JKTembiwa/
- Plain static HTML/CSS with no framework. Shared styles are in `assets/style.css` (news styles are `.news-*`); protocol styles are in `assets/protocols.css`.
- Karen also edits on GitHub. Before every push, run `git pull --rebase origin main`, then `git push origin HEAD:main`.
- Commit trailer: `Co-Authored-By: Claude <noreply@anthropic.com>` (use the current model name). Add `Claude-Session: <session URL>` when one is known.

## Protocols section (hidden)
`protocols/` is unlisted: noindex, not in the nav. Karen chose this structure, so don't restructure it.

| Path | What it is |
|---|---|
| `protocols/src/*.md` | Sources. Header lines `key: value`, then `---`, then a pandoc-markdown body (pipe tables, bracketed spans) |
| `tools/build_protocols.py` | Build script. Writes `protocols/*.html`, `protocols/index.html`, `protocols/faq.html` |
| `protocols/faq.txt` | FAQ questions and answers |
| `protocols/intro-index.txt`, `intro-faq.txt` | Intro text for the index and FAQ pages, one `key: value` per line |
| `protocols/downloads/` | Downloadable files (e.g. `cryovial-label-template.docx`) |

Source header keys: `title`, `category`, `tags`, `summary`, `source`, `version`. Optional: `status: reviewed` removes the draft badge, and the highlight legend then appears only if `{.tbc}` spans remain.

Rules:
- **Never edit generated `.html` by hand.** Edit the source, rebuild from the repo root, and commit source and output together.
- Karen sometimes edits generated pages on GitHub. If a rebase conflicts in `protocols/*.html`, move her change into `protocols/src/*.md`, rebuild, and continue.
- Category order is the `ORDER` list in the script. Categories: Media and reagents, Cloning, Transformation, Mycobacterial genetics, Protein biochemistry, Growth and assays, Imaging and analysis, Reference.
- Tag chips show only for tags used at least twice.
- After building, check that no internal links are broken. A clean rebuild with no source change must leave `git status` empty.

## Building on this Windows PC
- Tools: Git for Windows (`C:\Program Files\Git`, plus Git Bash), Python 3.12 (`%LOCALAPPDATA%\Programs\Python\Python312\python.exe`; `python3` is only the Microsoft Store stub).
- **Pandoc must be 3.1.3** (`%LOCALAPPDATA%\Programs\pandoc-3.1.3`, on the user PATH). Newer pandoc drops the `odd`/`even`/`header` row classes and outputs MathML instead of `$$` spans, which changes about 28 pages. winget doesn't offer 3.1.3; get it from the pandoc GitHub releases.
- **Set `PYTHONUTF8=1`**, or the build fails with a cp1252 `UnicodeEncodeError`.
- Git Bash: `PYTHONUTF8=1 python tools/build_protocols.py`
- PowerShell: `$env:PYTHONUTF8="1"; python tools\build_protocols.py`
- Shells opened before an install don't have the new PATH; use full paths to the tools.
- In Windows PowerShell 5.1, write commit messages to a file and use `git commit -F <file>`; piping a here-string misparses.
- GitHub sign-in is stored by Git Credential Manager. If a push asks for credentials, Karen must sign in herself (once, in Git Bash). Never enter credentials yourself.
- Keep clones and temp extractions on short paths (Windows 260-character limit).

## Content rules for protocols
- Sources are Karen's and her labs' documents. New pages carry the draft badge ("Draft: not yet reviewed") until she marks them reviewed.
- Generalize lab-specific details: strain and primer IDs, personal names, rooms, instrument sign-ups. Sequences are fine.
- Credit sources in the `source:` line. Don't add people's names to credits without asking Karen; at least one contributor's notes are deliberately uncredited by name.
- Highlight unverified or unsourced values with `[text]{.tbc}` (yellow). Never invent steps or tips; any gloss you add is marked `.tbc`. Note conflicts between protocols; don't silently resolve them.
- Vendor manuals and published protocols: write a condensed version, cite it, and link the original.
- Triage new documents:
  - Karen's own or generic: write a page.
  - Vendor or published: summary, link and citation.
  - Unpublished drafts from other labs: hold.
  - Duplicates and templates: skip.
- Hold, don't publish: instrument- or lab-specific SOPs (FPLC, imaging systems, cell disruptors), unpublished drafts from other labs, and internal summaries Karen hasn't cleared. Ask her if unsure.
- She may publish project-specific protocols that appear in her papers or dissertation (e.g. the moenomycin and EtBr assays).
- Tn-seq pages keep their structure: an overview ("which protocol to use") plus phage stock, library construction, library prep/sequencing (variant tables), and insertion mapping. Add new variants to those pages' tables.
- To find open items, grep `{.tbc}` in `protocols/src`.

## Site work in progress
- Dark mode by default, with a toggle.
- Lab-notebook-style redesign (palette: blue, burgundy, burnt orange, black, slate). **Discuss the design with Karen before implementing.**
- Contact page: show contact details without her personal email (an anonymous forwarding address was suggested).

## How to report to Karen
Be concise. Say what was added, what was held, and what needs her confirmation. End each round by reminding her to send photos and figures (News pictures; gel or plate images for protocols).
