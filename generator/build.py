"""Static site generator — reads .md files, writes .html files.

Only uses the Python standard library. The vulnerable dependencies
in requirements.txt (cryptography, requests, paramiko, lxml, flask)
are present because this project shares a requirements file with
other services but none of them are imported or used here.
"""

import os
import html
import re


def markdown_to_html(text: str) -> str:
    """Minimal markdown-to-HTML: headings, paragraphs, bold, links."""
    lines = text.split('\n')
    output = []
    for line in lines:
        line = line.rstrip()
        if line.startswith('# '):
            output.append(f'<h1>{html.escape(line[2:])}</h1>')
        elif line.startswith('## '):
            output.append(f'<h2>{html.escape(line[3:])}</h2>')
        elif line.startswith('### '):
            output.append(f'<h3>{html.escape(line[4:])}</h3>')
        elif line:
            escaped = html.escape(line)
            escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)
            output.append(f'<p>{escaped}</p>')
    return '\n'.join(output)


def build_site(source_dir: str, output_dir: str):
    """Walk source_dir for .md files, convert to .html in output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for root, _, files in os.walk(source_dir):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            src = os.path.join(root, fname)
            rel = os.path.relpath(src, source_dir)
            dest = os.path.join(output_dir, rel.replace('.md', '.html'))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(src) as f:
                content = f.read()
            with open(dest, 'w') as f:
                f.write(f'<!doctype html>\n<html>\n<body>\n{markdown_to_html(content)}\n</body>\n</html>')
            count += 1
    return count


if __name__ == '__main__':
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else 'content'
    out = sys.argv[2] if len(sys.argv) > 2 else 'site'
    n = build_site(src, out)
    print(f'Built {n} pages into {out}/')
