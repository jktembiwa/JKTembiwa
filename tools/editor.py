#!/usr/bin/env python3
"""Local editor for the protocols section.

Run:  python tools/editor.py   (or double-click edit-site.bat)
Opens http://localhost:8000/protocols/ with editing tools on top of the normal pages.
The tools exist only in this local copy: built pages and the live site never contain them.
Only this computer can reach the server.
"""
import argparse, ast, json, os, re, shutil, subprocess, sys, threading, webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "protocols", "src")
BUILD = os.path.join(ROOT, "tools", "build_protocols.py")
TEXTS = {"faq": "protocols/faq.txt", "intro-index": "protocols/intro-index.txt", "intro-faq": "protocols/intro-faq.txt"}
KEYS = ["title", "category", "tags", "summary", "source", "version", "status"]
REQUIRED = ["title", "category", "tags", "summary", "source", "version"]
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")
LINK_RE = re.compile(r'(?:href|src)="([^"#?]+)')
EXTERNAL_RE = re.compile(r"^(https?:|mailto:|tel:|data:|//|javascript:)")
INJECT = '<link rel="stylesheet" href="/tools/editor/editor.css">\n<script src="/tools/editor/editor.js" defer></script>\n'
LOCK = threading.Lock()  # one save/build/publish at a time

# --- tools: the build must use pandoc 3.1.3 and UTF-8 mode, or output drifts or fails
ENV = dict(os.environ, PYTHONUTF8="1", GIT_TERMINAL_PROMPT="0")
_pd = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "pandoc-3.1.3")
if os.path.isfile(os.path.join(_pd, "pandoc.exe")):
    ENV["PATH"] = _pd + os.pathsep + ENV.get("PATH", "")
GIT = shutil.which("git", path=ENV["PATH"]) or r"C:\Program Files\Git\cmd\git.exe"
PANDOC = shutil.which("pandoc", path=ENV["PATH"])

def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, env=ENV, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).rstrip()  # keep leading spaces: porcelain status columns

def git(*args):
    return run([GIT, *args])

def pandoc_version():
    if not PANDOC:
        return None
    return run([PANDOC, "--version"])[1].splitlines()[0].split()[-1]

def categories():
    m = re.search(r"^ORDER=(\[.*?\])", open(BUILD, encoding="utf-8").read(), re.M)
    return [c for c in ast.literal_eval(m.group(1)) if c != "Protocols"]

# --- sources (same format the build script parses)
def src_path(slug):
    if not SLUG_RE.match(slug or ""):
        raise ValueError("Invalid protocol name.")
    return os.path.join(SRC, slug + ".md")

def read_source(slug):
    raw = open(src_path(slug), encoding="utf-8").read()
    head, body = raw.split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body

def render_source(meta, body):
    for k, v in meta.items():
        if "\n" in v or "\r" in v:
            raise ValueError(f"'{k}' must be a single line.")
    missing = [k for k in REQUIRED if not meta.get(k, "").strip()]
    if missing:
        raise ValueError("Please fill in: " + ", ".join(missing) + ".")
    meta = dict(meta)
    if meta.get("status", "").lower() != "reviewed":
        meta.pop("status", None)  # draft is the default; no line needed
    order = KEYS + [k for k in meta if k not in KEYS]
    head = "\n".join(f"{k}: {meta[k].strip()}" for k in order if meta.get(k, "").strip())
    return head + "\n---\n" + body.replace("\r\n", "\n").rstrip("\n") + "\n"

# --- build, with rollback if the new content breaks it
def build():
    return run([sys.executable, BUILD])

def write_and_build(path, text):
    """Write text to path (None deletes it) and rebuild; restore the old file if the build fails."""
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if text is None:
        os.remove(path)
    else:
        open(path, "w", encoding="utf-8").write(text)
    code, log = build()
    if code != 0:
        if old is None:
            if os.path.exists(path):
                os.remove(path)
        else:
            open(path, "w", encoding="utf-8").write(old)
        build()
        raise ValueError("The build failed, so nothing was saved.\n\n" + log[-2000:])
    return log

def broken_links():
    bad = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in fns:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dp, fn)
            for u in LINK_RE.findall(open(p, encoding="utf-8", errors="replace").read()):
                if EXTERNAL_RE.match(u):
                    continue
                t = os.path.join(ROOT, u.lstrip("/")) if u.startswith("/") else os.path.join(dp, u)
                if not os.path.exists(os.path.normpath(t)):
                    bad.append(f"{os.path.relpath(p, ROOT)} -> {u}")
    return bad

def preview(body):
    r = subprocess.run([PANDOC, "-f", "markdown+pipe_tables+bracketed_spans", "-t", "html", "--wrap=none"],
                       input=body, env=ENV, capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else "<pre>" + r.stderr + "</pre>"

def new_slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60].rstrip("-") or "protocol"
    slug, n = s, 2
    while os.path.exists(os.path.join(SRC, slug + ".md")):
        slug, n = f"{s}-{n}", n + 1
    return slug

# --- git
def changes():
    code, out = git("status", "--porcelain", "-uall")
    files = []
    for line in out.splitlines():
        path = line[3:].strip().strip('"').split(" -> ")[-1]
        files.append({"code": line[:2].strip(), "path": path, "included": path.startswith("protocols/")})
    code, ahead = git("rev-list", "--count", "origin/main..HEAD")
    return {"files": files, "ahead": int(ahead) if code == 0 and ahead.isdigit() else 0}

def publish(message):
    log = []
    def step(label, *args):
        code, out = git(*args)
        log.append(f"$ git {' '.join(args)}\n{out}".rstrip())
        if code != 0:
            raise RuntimeError(label)
    st = changes()
    if not any(f["included"] for f in st["files"]) and not st["ahead"]:
        return ["Nothing to publish."]
    try:
        if any(f["included"] for f in st["files"]):
            step("Could not stage changes.", "add", "-A", "--", "protocols")
            step("Could not commit.", "commit", "-m", message or "Update protocols")
        try:
            step("pull", "pull", "--rebase", "--autostash", "origin", "main")
        except RuntimeError:
            git("rebase", "--abort")
            raise RuntimeError("Your edits conflict with changes made on GitHub. They are saved in a local "
                               "commit; nothing was pushed. Ask Claude to merge them.")
        code, out = build()  # pull may bring source edits made on GitHub
        log.append("$ build\n" + out)
        if code != 0:
            raise RuntimeError("The build failed after pulling from GitHub; nothing was pushed.")
        if git("status", "--porcelain", "--", "protocols")[1]:
            step("Could not stage rebuild.", "add", "-A", "--", "protocols")
            step("Could not commit rebuild.", "commit", "-m", "Rebuild protocols")
        step("Push failed. If GitHub asked you to sign in, try Publish again.", "push", "origin", "HEAD:main")
    except RuntimeError as e:
        log.append("ERROR: " + str(e))
        raise RuntimeError("\n\n".join(log))
    return log

# --- HTTP
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def log_message(self, fmt, *args):
        if self.path.startswith("/api/") and not self.path.startswith(("/api/status", "/api/preview")):
            sys.stderr.write("%s\n" % (fmt % args))

    def handle(self):
        try:
            super().handle()
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass  # the browser navigated away mid-request

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def local_request(self):
        # blocks other sites in the browser (DNS rebinding, cross-site form posts) from using the API
        host = self.headers.get("Host", "").rsplit(":", 1)[0]
        return host in ("localhost", "127.0.0.1")

    def send_json(self, obj, status=200):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self.local_request():
            return self.send_error(403)
        u = urlparse(self.path)
        if u.path.startswith("/api/"):
            return self.api(u, None)
        if u.path in ("/", "/protocols", "/protocols/"):
            self.send_response(302)
            self.send_header("Location", "/protocols/index.html")
            return self.end_headers()
        if u.path.startswith("/protocols/") and u.path.endswith(".html"):
            path = self.translate_path(u.path)
            if os.path.isfile(path):
                page = open(path, encoding="utf-8").read().replace("</body>", INJECT + "</body>", 1)
                data = page.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                return self.wfile.write(data)
        return super().do_GET()

    def do_POST(self):
        # the custom header forces a CORS preflight, which this server never approves
        if not self.local_request() or self.headers.get("X-Editor") != "1":
            return self.send_error(403)
        n = int(self.headers.get("Content-Length") or 0)
        if n > 5_000_000:
            return self.send_error(413)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return self.send_json({"error": "Bad request."}, 400)
        return self.api(urlparse(self.path), body)

    def api(self, u, data):
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if data is None:
                return self.send_json(self.api_get(u.path, q))
            with LOCK:
                return self.send_json(self.api_post(u.path, data))
        except FileNotFoundError:
            return self.send_json({"error": "That protocol has no source file."}, 404)
        except (ValueError, RuntimeError) as e:
            return self.send_json({"error": str(e)}, 400)

    def api_get(self, path, q):
        if path == "/api/info":
            return {"categories": categories(), "pandoc": pandoc_version(), "git": os.path.exists(GIT)}
        if path == "/api/protocol":
            meta, body = read_source(q.get("slug"))
            return {"slug": q["slug"], "meta": meta, "body": body}
        if path == "/api/text":
            name = q.get("name")
            if name not in TEXTS:
                raise ValueError("Unknown text file.")
            return {"name": name, "text": open(os.path.join(ROOT, TEXTS[name]), encoding="utf-8").read()}
        if path == "/api/status":
            return changes()
        raise ValueError("Unknown request.")

    def api_post(self, path, d):
        if path == "/api/preview":
            return {"html": preview(d.get("body", ""))}
        if path == "/api/save":
            slug = d.get("slug")
            meta, _ = read_source(slug)
            meta.update({k: str(v) for k, v in (d.get("meta") or {}).items()})
            log = write_and_build(src_path(slug), render_source(meta, d.get("body", "")))
            return {"ok": True, "log": log, "broken": broken_links()}
        if path == "/api/new":
            meta = {k: str(d.get(k, "")).strip() for k in ("title", "category", "tags", "summary", "source")}
            meta["version"] = "Draft 0.1"
            slug = new_slug(meta["title"])
            log = write_and_build(src_path(slug), render_source(meta, "Write the protocol here.\n"))
            return {"ok": True, "slug": slug, "log": log, "broken": broken_links()}
        if path == "/api/text":
            name = d.get("name")
            if name not in TEXTS:
                raise ValueError("Unknown text file.")
            text = d.get("text", "").replace("\r\n", "\n")
            log = write_and_build(os.path.join(ROOT, TEXTS[name]), text)
            return {"ok": True, "log": log, "broken": broken_links()}
        if path == "/api/publish":
            return {"ok": True, "log": "\n\n".join(publish(d.get("message", "").strip()))}
        raise ValueError("Unknown request.")

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args()
    v = pandoc_version()
    if v != "3.1.3":
        print(f"WARNING: pandoc {v or 'not found'}; the build needs 3.1.3 to match the published pages.")
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    url = f"http://localhost:{a.port}/protocols/index.html"
    print(f"Local editor running at {url}\nClose this window (or press Ctrl+C) to stop.")
    if not a.no_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
