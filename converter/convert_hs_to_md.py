#!/usr/bin/env python3
"""Convert HSP help-source files (*.hs, Shift-JIS) into LLM-friendly Markdown.

HSP help sources are a flat list of `%tagname` blocks. A file starts with a
header section (module info: %type, %group, %ver, %date, %author, %url,
%note, %port, %portinfo, %dll) followed by one block per command, each
starting with `%index`:

    %index
    <command name>
    <one-line description>
    %group
    <group name>            (optional, overrides header group)
    %prm
    <call syntax>            e.g. "(p1)" or "p1,p2" or blank if no params
    <param> : <description>  (one line per parameter)
    %inst
    <free-form explanation, may contain ^p markers around tables/listings>
    %href / %ref
    <related command names, one per line>
    %sample
    <example code>

This script re-renders each command as a Markdown section: a fenced usage
line built from the HSP calling convention (space-separated for statements,
`name(...)` for parenthesized functions), a parameter list, the explanation
with ^p-delimited blocks turned into fenced code, and a sample code block.
"""
import glob
import os
import re

SRC_DIR = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
)

TAG_RE = re.compile(r'^%([A-Za-z_]+)$')

# Manual context that isn't derivable from the .hs source itself, keyed by
# source filename. Rendered as an extra header bullet.
EXTRA_NOTES = {
    "hgimg_common.hs": (
        "この命令群は hgimg3.as と hgimg4.as/hgimg4dx.as のどちらと組み合わせても"
        "使用できる、オブジェクト操作の共通処理です(HGIMG4専用ではありません)。"
    ),
}

HEADER_LABELS = [
    ("dll", "DLL/モジュール名"),
    ("type", "種別"),
    ("group", "グループ"),
    ("ver", "バージョン"),
    ("date", "更新日"),
    ("author", "作者"),
    ("url", "URL"),
    ("port", "対応環境"),
    ("portinfo", "動作条件"),
    ("note", "備考"),
]


def read_sjis(path):
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("cp932", errors="replace")


def split_blocks(text):
    """Split into (tag, lines) blocks. tag is None for text before the first %tag."""
    blocks = []
    tag = None
    lines = []
    for raw in text.splitlines():
        m = TAG_RE.match(raw.strip())
        if m:
            blocks.append((tag, lines))
            tag = m.group(1).lower()
            lines = []
        else:
            lines.append(raw)
    blocks.append((tag, lines))
    return blocks


def group_entries(blocks):
    """Split blocks into a header (before first %index) and a list of entries,
    each entry being the list of (tag, lines) from one %index up to the next."""
    header = []
    entries = []
    current = None
    for tag, lines in blocks:
        if tag is None:
            continue  # leading ; comment lines, not part of any tag
        if tag == "index":
            if current is not None:
                entries.append(current)
            current = []
        if current is None:
            header.append((tag, lines))
        else:
            current.append((tag, lines))
    if current is not None:
        entries.append(current)
    return header, entries


def blocks_to_dict(blocks):
    """Merge repeated tags by joining their line lists with a blank separator."""
    d = {}
    for tag, lines in blocks:
        if tag in d:
            d[tag] = d[tag] + [""] + lines
        else:
            d[tag] = lines
    return d


def strip_blank_edges(lines):
    start = 0
    end = len(lines)
    while start < end and lines[start].strip() == "":
        start += 1
    while end > start and lines[end - 1].strip() == "":
        end -= 1
    return lines[start:end]


def slugify(text):
    """Reproduce the GitHub-flavored-Markdown heading-anchor algorithm:
    lowercase, drop anything but letters/digits/spaces/hyphens/underscores,
    then turn spaces into hyphens. Needed because command names can contain
    '#' (e.g. #deffunc) or parentheses (e.g. setcolor(HGIMG3)), which GFM
    strips from the anchor even though they stay in the visible heading."""
    s = text.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s


def make_anchor_resolver():
    """Return a function that assigns each heading text the same anchor a
    Markdown renderer would, including GFM's -1/-2 suffixing of repeats."""
    seen = {}

    def resolve(text):
        base = slugify(text)
        n = seen.get(base, 0)
        seen[base] = n + 1
        return base if n == 0 else f"{base}-{n}"

    return resolve


def escape_markdown_line(line):
    # A leading '#' would otherwise be read as an ATX heading by Markdown
    # renderers; HSP preprocessor directives (#include, #deffunc, ...) show
    # up at line-start in plain explanation text.
    if line.lstrip().startswith("#"):
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        return indent + "\\" + stripped
    return line


def render_prose(lines, escape=True):
    """Render free-form HSP help text, turning ^p-delimited regions into
    fenced code blocks (they mark tables/listings in the original help)."""
    lines = strip_blank_edges(lines)
    out = []
    in_code = False
    for line in lines:
        if line.strip() == "^p":
            out.append("```")
            in_code = not in_code
            continue
        out.append(line if in_code or not escape else escape_markdown_line(line))
    if in_code:
        out.append("```")
    return "\n".join(out).strip("\n")


def parse_prm(lines):
    """Return (syntax, [(name_part, desc), ...]) from a %prm block."""
    lines = strip_blank_edges(lines)
    if not lines:
        return "", []
    syntax = lines[0].strip()
    params = []
    for line in lines[1:]:
        if not line.strip():
            continue
        m = re.match(r'^(.*?)\s*:\s*(.*)$', line.strip())
        if m:
            params.append((m.group(1).strip(), m.group(2).strip()))
        else:
            params.append((line.strip(), ""))
    return syntax, params


def build_usage(name, syntax):
    if not syntax:
        return name
    if syntax.startswith("("):
        return f"{name}{syntax}"
    return f"{name} {syntax}"


def render_header(header_dict, filename):
    title = None
    dll_lines = header_dict.get("dll")
    if dll_lines and strip_blank_edges(dll_lines):
        title = strip_blank_edges(dll_lines)[0].strip()
    if not title:
        title = os.path.splitext(filename)[0]

    out = [f"# {title}", ""]
    for tag, label in HEADER_LABELS:
        if tag == "dll":
            continue
        raw = header_dict.get(tag)
        if not raw:
            continue
        content_lines = strip_blank_edges(raw)
        if not content_lines:
            continue
        value = " / ".join(l.strip() for l in content_lines if l.strip())
        if value:
            out.append(f"- **{label}**: {value}")
    extra = EXTRA_NOTES.get(filename)
    if extra:
        out.append(f"- **補足**: {extra}")
    out.append("")
    return out


def render_entry(entry_dict):
    index_lines = strip_blank_edges(entry_dict.get("index", []))
    if not index_lines:
        return []
    name = index_lines[0].strip()
    desc_lines = strip_blank_edges(index_lines[1:])
    desc = " ".join(l.strip() for l in desc_lines if l.strip())

    out = [f"### {name}", ""]
    if desc:
        out.append(desc)
        out.append("")

    group_lines = strip_blank_edges(entry_dict.get("group", []))
    if group_lines:
        out.append(f"- **グループ**: {' '.join(l.strip() for l in group_lines if l.strip())}")
        out.append("")

    syntax, params = parse_prm(entry_dict.get("prm", []))
    out.append("**構文**")
    out.append("```")
    out.append(build_usage(name, syntax))
    out.append("```")
    out.append("")

    out.append("**パラメータ**")
    if params:
        for name_part, pdesc in params:
            if pdesc:
                out.append(f"- `{name_part}`: {pdesc}")
            else:
                out.append(f"- `{name_part}`")
    else:
        out.append("- なし")
    out.append("")

    inst_lines = entry_dict.get("inst", [])
    inst_text = render_prose(inst_lines)
    if inst_text:
        out.append("**説明**")
        out.append("")
        out.append(inst_text)
        out.append("")

    href_lines = strip_blank_edges(entry_dict.get("href", []) + entry_dict.get("ref", []))
    if href_lines:
        related = ", ".join(l.strip() for l in href_lines if l.strip())
        if related:
            out.append(f"**関連**: {related}")
            out.append("")

    sample_lines = strip_blank_edges(entry_dict.get("sample", []))
    if sample_lines:
        out.append("**サンプル**")
        out.append("```hsp")
        out.append("\n".join(sample_lines).strip("\n"))
        out.append("```")
        out.append("")

    note_lines = strip_blank_edges(entry_dict.get("note", []))
    if note_lines:
        out.append(f"**備考**: {render_prose(note_lines, escape=False)}")
        out.append("")

    portinfo_lines = strip_blank_edges(entry_dict.get("portinfo", []))
    if portinfo_lines:
        out.append(f"**動作条件**: {render_prose(portinfo_lines, escape=False)}")
        out.append("")

    out.append("---")
    out.append("")
    return out


def convert_file(path):
    filename = os.path.basename(path)
    text = read_sjis(path)
    blocks = split_blocks(text)
    header_blocks, entry_blocks = group_entries(blocks)
    header_dict = blocks_to_dict(header_blocks)
    entries = [blocks_to_dict(e) for e in entry_blocks]

    out = render_header(header_dict, filename)

    if entries:
        resolve_anchor = make_anchor_resolver()
        out.append("## 命令一覧")
        out.append("")
        out.append("| 命令 | 概要 |")
        out.append("|---|---|")
        for e in entries:
            idx = strip_blank_edges(e.get("index", []))
            if not idx:
                continue
            name = idx[0].strip()
            desc = " ".join(l.strip() for l in strip_blank_edges(idx[1:]) if l.strip())
            anchor = resolve_anchor(name)
            out.append(f"| [{name}](#{anchor}) | {desc} |")
        out.append("")
        out.append("## 命令詳細")
        out.append("")

    for e in entries:
        out.extend(render_entry(e))

    return "\n".join(out).rstrip("\n") + "\n"


def main():
    hs_files = sorted(glob.glob(os.path.join(SRC_DIR, "*.hs")))
    for path in hs_files:
        md_text = convert_file(path)
        out_path = os.path.splitext(path)[0] + ".md"
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(md_text)
        print(f"converted: {os.path.basename(path)} -> {os.path.basename(out_path)}")


if __name__ == "__main__":
    main()
