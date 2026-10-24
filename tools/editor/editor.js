// Local protocol editor. Loaded only by tools/editor.py; never part of the built or live pages.
(function () {
  "use strict";
  const page = location.pathname.match(/^\/protocols\/([a-z0-9-]+)\.html$/);
  const slug = page ? page[1] : null;
  const kind = slug === "index" ? "index" : slug === "faq" ? "faq" : slug ? "protocol" : null;
  if (!kind) return;
  const TBC = /\[([^\]]*)\]\{\.tbc\}/g;
  let info = { categories: [] };
  let dirty = false;

  // ---------- helpers
  function el(tag, attrs, ...kids) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (k === "class") n.className = v;
      else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
      else if (v === true) n.setAttribute(k, "");
      else if (v !== false && v != null) n.setAttribute(k, v);
    }
    for (const c of kids.flat()) if (c != null) n.append(c);
    return n;
  }
  async function api(path, body) {
    const opts = body === undefined ? {} : {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-Editor": "1" },
      body: JSON.stringify(body),
    };
    const r = await fetch("/api/" + path, opts);
    const j = await r.json().catch(() => ({ error: "No response from the editor. Is it still running?" }));
    if (!r.ok || j.error) throw new Error(j.error || "Request failed.");
    return j;
  }
  function field(label, input, hint) {
    return el("label", { class: "ed-field" }, el("span", {}, label), input, hint ? el("small", {}, hint) : null);
  }
  function setMsg(box, text, type) {
    box.textContent = text;
    box.className = "ed-msg" + (type ? " ed-" + type : "");
  }
  function afterSave(res, box, go) {
    if (res.broken && res.broken.length) {
      setMsg(box, "Saved, but some links are broken:\n" + res.broken.join("\n"), "warn");
      box.append(el("button", { type: "button", class: "ed-btn", onclick: go }, "Continue"));
    } else {
      setMsg(box, "Saved and rebuilt.", "ok");
      go();
    }
  }
  function insertText(ta, start, end, text) {
    ta.focus();
    ta.setSelectionRange(start, end);
    // execCommand keeps the browser's undo history; fall back if unsupported
    if (!document.execCommand("insertText", false, text)) ta.setRangeText(text, start, end, "end");
    ta.dispatchEvent(new Event("input"));
  }

  // ---------- drawer
  const drawer = el("aside", { class: "ed-drawer", hidden: true, "aria-label": "Editor" });
  function openDrawer(title, ...content) {
    drawer.replaceChildren(
      el("header", { class: "ed-head" },
        el("h2", {}, title),
        el("button", { type: "button", class: "ed-x", "aria-label": "Close editor", onclick: closeDrawer }, "×")),
      ...content);
    drawer.hidden = false;
    document.body.classList.add("ed-open");
  }
  function closeDrawer() {
    if (dirty && !confirm("Discard unsaved changes?")) return;
    dirty = false;
    drawer.hidden = true;
    document.body.classList.remove("ed-open");
  }
  addEventListener("beforeunload", (e) => { if (dirty) { e.preventDefault(); e.returnValue = ""; } });

  // ---------- protocol editor
  async function editProtocol() {
    let p;
    try { p = await api("protocol?slug=" + slug); } catch (e) { return alert(e.message); }
    const m = p.meta;
    const reviewed = (m.status || "").toLowerCase() === "reviewed";
    const f = {
      title: el("input", { type: "text", value: m.title || "" }),
      category: el("select", {}, info.categories.map((c) => el("option", { value: c, selected: c === m.category }, c))),
      tags: el("input", { type: "text", value: m.tags || "" }),
      summary: el("input", { type: "text", value: m.summary || "" }),
      source: el("input", { type: "text", value: m.source || "" }),
      version: el("input", { type: "text", value: m.version || "" }),
    };
    if (m.category && !info.categories.includes(m.category)) f.category.append(el("option", { value: m.category, selected: true }, m.category));
    const draftR = el("input", { type: "radio", name: "ed-status", value: "draft", checked: !reviewed });
    const revR = el("input", { type: "radio", name: "ed-status", value: "reviewed", checked: reviewed });
    const statusNote = el("small", {});
    revR.addEventListener("change", () => {
      if (/^draft/i.test(f.version.value)) {
        f.version.value = "Version 1.0";
        statusNote.textContent = "Version changed to “Version 1.0”. Edit it if you prefer another label.";
      }
    });
    const status = el("div", { class: "ed-field" }, el("span", {}, "Status"),
      el("div", { class: "ed-seg" },
        el("label", {}, draftR, " Draft"),
        el("label", {}, revR, " Reviewed")), statusNote);

    const ta = el("textarea", { class: "ed-body", spellcheck: "true" });
    ta.value = p.body;
    const prev = el("div", { class: "prose ed-preview", hidden: true });
    const count = el("span", { class: "ed-count" });
    const updateCount = () => {
      const n = (ta.value.match(TBC) || []).length;
      count.textContent = n ? `${n} highlight${n > 1 ? "s" : ""}` : "No highlights";
    };
    updateCount();
    let timer;
    const refreshPreview = async () => {
      try { prev.innerHTML = (await api("preview", { body: ta.value })).html; } catch (e) { prev.textContent = e.message; }
    };
    ta.addEventListener("input", () => {
      updateCount();
      if (!prev.hidden) { clearTimeout(timer); timer = setTimeout(refreshPreview, 500); }
    });
    const tabMd = el("button", { type: "button", class: "ed-tab on" }, "Markdown");
    const tabPv = el("button", { type: "button", class: "ed-tab" }, "Preview");
    tabMd.onclick = () => { prev.hidden = true; ta.hidden = false; tabMd.classList.add("on"); tabPv.classList.remove("on"); };
    tabPv.onclick = () => { prev.hidden = false; ta.hidden = true; tabPv.classList.add("on"); tabMd.classList.remove("on"); refreshPreview(); };

    const markTbc = () => {
      const [s, e] = [ta.selectionStart, ta.selectionEnd];
      if (s === e) return setMsg(msg, "Select the text to highlight first.", "warn");
      insertText(ta, s, e, "[" + ta.value.slice(s, e) + "]{.tbc}");
    };
    const clearTbc = () => {
      const [s, e] = [ta.selectionStart, ta.selectionEnd];
      const hits = [...ta.value.matchAll(TBC)].filter((x) => x.index <= e && x.index + x[0].length >= s);
      if (!hits.length) return setMsg(msg, "Put the cursor inside a highlight, or select text containing highlights.", "warn");
      const a = hits[0].index, b = hits[hits.length - 1].index + hits[hits.length - 1][0].length;
      insertText(ta, a, b, ta.value.slice(a, b).replace(TBC, "$1"));
    };

    const msg = el("div", { class: "ed-msg" });
    const save = el("button", { type: "button", class: "ed-btn primary" }, "Save");
    const doSave = async () => {
      save.disabled = true;
      setMsg(msg, "Saving and rebuilding…");
      const meta = Object.fromEntries(Object.entries(f).map(([k, v]) => [k, v.value]));
      meta.status = revR.checked ? "reviewed" : "draft";
      try {
        const res = await api("save", { slug, meta, body: ta.value });
        dirty = false;
        afterSave(res, msg, () => location.replace(location.pathname));
        refreshStatus();
      } catch (e) { setMsg(msg, e.message, "err"); }
      save.disabled = false;
    };
    save.onclick = doSave;

    const form = el("div", { class: "ed-form" },
      el("div", { class: "ed-grid" },
        field("Title", f.title), field("Category", f.category),
        field("Summary", f.summary), field("Tags", f.tags, "Comma-separated"),
        field("Source / credit", f.source), field("Version", f.version), status),
      el("div", { class: "ed-toolbar" }, tabMd, tabPv,
        el("span", { class: "ed-sp" }),
        el("button", { type: "button", class: "ed-btn", onclick: markTbc, title: "Wrap the selected text in a yellow highlight" }, "Mark TBC"),
        el("button", { type: "button", class: "ed-btn", onclick: clearTbc, title: "Remove the highlight around the cursor or selection" }, "Clear highlight"),
        count),
      ta, prev,
      el("p", { class: "ed-help" }, "Markdown: 1. numbered steps, - bullets, **bold**, *italic*, [link text](page.html), | pipe | tables |. Highlights look like [text]{.tbc}. Ctrl+S saves."));
    form.addEventListener("input", () => { dirty = true; });
    form.addEventListener("change", () => { dirty = true; });
    form.addEventListener("keydown", (e) => { if ((e.ctrlKey || e.metaKey) && e.key === "s") { e.preventDefault(); doSave(); } });
    openDrawer("Edit protocol", form,
      el("footer", { class: "ed-foot" }, msg, el("button", { type: "button", class: "ed-btn", onclick: closeDrawer }, "Cancel"), save));
    f.title.focus();
  }

  // ---------- new protocol
  function newProtocol() {
    const f = {
      title: el("input", { type: "text", required: true }),
      category: el("select", {}, info.categories.map((c) => el("option", { value: c }, c))),
      summary: el("input", { type: "text", required: true }),
      tags: el("input", { type: "text", required: true }),
      source: el("input", { type: "text", required: true }),
    };
    const msg = el("div", { class: "ed-msg" });
    const create = el("button", { type: "button", class: "ed-btn primary" }, "Create");
    create.onclick = async () => {
      create.disabled = true;
      setMsg(msg, "Creating and rebuilding…");
      try {
        const res = await api("new", Object.fromEntries(Object.entries(f).map(([k, v]) => [k, v.value])));
        dirty = false;
        afterSave(res, msg, () => location.assign(res.slug + ".html?edit=1"));
        refreshStatus();
      } catch (e) { setMsg(msg, e.message, "err"); create.disabled = false; }
    };
    const form = el("div", { class: "ed-form" },
      el("p", { class: "ed-help" }, "Creates a new source file in protocols/src, marked Draft 0.1. You can write the steps on the next screen."),
      el("div", { class: "ed-grid" },
        field("Title", f.title), field("Category", f.category),
        field("Summary", f.summary, "One sentence for the index card"),
        field("Tags", f.tags, "Comma-separated, e.g. PCR, cloning, E. coli"),
        field("Source / credit", f.source, "Where the protocol comes from")));
    form.addEventListener("input", () => { dirty = true; });
    openDrawer("New protocol", form,
      el("footer", { class: "ed-foot" }, msg, el("button", { type: "button", class: "ed-btn", onclick: closeDrawer }, "Cancel"), create));
    f.title.focus();
  }

  // ---------- plain text files (FAQ, intros)
  const TEXT_HELP = {
    faq: "Each entry is: the question on line 1, then slug|link label on line 2 (the related protocol), then the answer (markdown). Separate entries with a line containing only ===.",
    "intro-index": "One item per line as key: value (heading, lede, note). Inline HTML such as <em>word</em> is allowed. Lines starting with # are comments.",
    "intro-faq": "One item per line as key: value (heading, lede). Inline HTML such as <em>word</em> is allowed. Lines starting with # are comments.",
  };
  async function editText(name, title) {
    let t;
    try { t = await api("text?name=" + name); } catch (e) { return alert(e.message); }
    const ta = el("textarea", { class: "ed-body", spellcheck: "true" });
    ta.value = t.text;
    const msg = el("div", { class: "ed-msg" });
    const save = el("button", { type: "button", class: "ed-btn primary" }, "Save");
    const doSave = async () => {
      save.disabled = true;
      setMsg(msg, "Saving and rebuilding…");
      try {
        const res = await api("text", { name, text: ta.value });
        dirty = false;
        afterSave(res, msg, () => location.replace(location.pathname));
        refreshStatus();
      } catch (e) { setMsg(msg, e.message, "err"); }
      save.disabled = false;
    };
    save.onclick = doSave;
    ta.addEventListener("input", () => { dirty = true; });
    ta.addEventListener("keydown", (e) => { if ((e.ctrlKey || e.metaKey) && e.key === "s") { e.preventDefault(); doSave(); } });
    openDrawer(title, el("div", { class: "ed-form" }, el("p", { class: "ed-help" }, TEXT_HELP[name]), ta),
      el("footer", { class: "ed-foot" }, msg, el("button", { type: "button", class: "ed-btn", onclick: closeDrawer }, "Cancel"), save));
    ta.focus();
  }

  // ---------- publish
  const pubBtn = el("button", { type: "button", class: "ed-btn primary", onclick: () => openPublish() }, "Publish");
  async function refreshStatus() {
    try {
      const s = await api("status");
      const n = s.files.filter((f) => f.included).length;
      pubBtn.textContent = n || s.ahead ? `Publish (${n + s.ahead})` : "Publish";
      return s;
    } catch (e) { pubBtn.textContent = "Publish"; return null; }
  }
  async function openPublish() {
    const s = await refreshStatus();
    if (!s) return alert("Could not read the git status.");
    const inc = s.files.filter((f) => f.included), other = s.files.filter((f) => !f.included);
    const list = (files) => el("ul", { class: "ed-files" }, files.map((f) => el("li", {}, el("code", {}, f.code), " " + f.path)));
    const message = el("input", { type: "text", value: "Update protocols" });
    const msg = el("div", { class: "ed-msg" });
    const log = el("pre", { class: "ed-log", hidden: true });
    const go = el("button", { type: "button", class: "ed-btn primary", disabled: !inc.length && !s.ahead }, "Publish to the live site");
    go.onclick = async () => {
      go.disabled = true;
      setMsg(msg, "Publishing… If a GitHub sign-in window appears, sign in there.");
      try {
        const r = await api("publish", { message: message.value });
        setMsg(msg, "Published. The live site updates within a minute or two.", "ok");
        log.textContent = r.log; log.hidden = false;
      } catch (e) {
        setMsg(msg, "Not published. See the details below.", "err");
        log.textContent = e.message; log.hidden = false;
        go.disabled = false;
      }
      refreshStatus();
    };
    openDrawer("Publish",
      el("div", { class: "ed-form" },
        inc.length ? [el("p", {}, "These changes will be published:"), list(inc)]
          : el("p", {}, s.ahead ? `${s.ahead} saved commit(s) waiting to be pushed.` : "Nothing to publish yet."),
        s.ahead && inc.length ? el("p", {}, `Plus ${s.ahead} commit(s) already saved locally.`) : null,
        other.length ? [el("p", { class: "ed-help" }, "Changed outside protocols/ (not included):"), list(other)] : null,
        field("Description of the change", message),
        log),
      el("footer", { class: "ed-foot" }, msg, el("button", { type: "button", class: "ed-btn", onclick: closeDrawer }, "Close"), go));
  }

  // ---------- floating bar
  const bar = el("div", { class: "ed-bar", role: "toolbar", "aria-label": "Local editor" }, el("span", { class: "ed-badge" }, "Local editor"));
  if (kind === "protocol") bar.append(el("button", { type: "button", class: "ed-btn", onclick: editProtocol }, "Edit this protocol"));
  if (kind === "index") bar.append(
    el("button", { type: "button", class: "ed-btn", onclick: newProtocol }, "New protocol"),
    el("button", { type: "button", class: "ed-btn", onclick: () => editText("intro-index", "Edit index intro") }, "Edit intro"));
  if (kind === "faq") bar.append(
    el("button", { type: "button", class: "ed-btn", onclick: () => editText("faq", "Edit FAQ") }, "Edit FAQ"),
    el("button", { type: "button", class: "ed-btn", onclick: () => editText("intro-faq", "Edit FAQ intro") }, "Edit intro"));
  bar.append(pubBtn);
  document.body.append(bar, drawer);

  api("info").then((i) => {
    info = i;
    if (i.pandoc !== "3.1.3") bar.append(el("span", { class: "ed-warn" }, `pandoc ${i.pandoc || "missing"}: needs 3.1.3`));
    if (kind === "protocol" && new URLSearchParams(location.search).has("edit")) editProtocol();
  }).catch(() => {});
  refreshStatus();
})();
