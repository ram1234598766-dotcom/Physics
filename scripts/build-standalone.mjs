import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import MarkdownIt from 'markdown-it'
import katexModule from '@vscode/markdown-it-katex'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const katex = katexModule.default ?? katexModule
const md = new MarkdownIt({ html: false, typographer: false })
md.use(katex, { throwOnError: false, output: 'html', strict: false })

const DOCS = [
  'docs/index.md',
  'docs/overview.md',
  'docs/papers/00-capstone.md',
  'docs/papers/00-treatise.md',
  'docs/papers/01-foundations.md',
  'docs/papers/02-structure-spectral-theory.md',
  'docs/papers/03-causal-network-spectral-theory.md',
  'docs/papers/04-variational-conservation.md',
  'docs/papers/05-graded-media-engineering.md',
  'docs/papers/06-power-networks-synchronization.md',
  'docs/papers/07-epidemiology-adaptive-networks.md',
  'docs/papers/08-numerical-methods.md',
  'docs/papers/09-higher-dimensional-structure-flow.md',
  'docs/papers/10-causal-graph-time-signal-processing.md',
  'docs/papers/11-novelty-and-literature.md',
  'docs/verification.md',
  'docs/roadmap.md',
  'docs/demos.md'
]

const stripRelativeLinks = (src) =>
  src.replace(/\[([^\]]+)\]\((?!https?:\/\/)[^)]*\)/g, '$1')

function renderDoc(file) {
  const path = resolve(root, file)
  if (!existsSync(path)) throw new Error(`missing: ${path}`)
  let src = readFileSync(path, 'utf8')
  src = stripRelativeLinks(src)
  const html = md.render(src)
  const slug = file.replace(/^docs\//, '').replace(/[^\w]+/g, '-').replace(/^-+|-+$/g, '')
  let h1 = slug
  const toc = []
  let counter = 0
  const sectioned = html.replace(/<h([1-3])([^>]*)>(.*?)<\/h\1>/g, (m, lvl, attrs, inner) => {
    counter += 1
    const id = `${slug}-s${counter}`
    const text = inner.replace(/<[^>]+>/g, '')
    if (lvl === '1') h1 = text
    if (lvl === '2') toc.push({ id, text })
    return `<h${lvl}${attrs} id="${id}">${inner}</h${lvl}>`
  })
  return { slug, h1, toc, html: sectioned }
}

const sections = DOCS.map(renderDoc)

const tocHtml = sections
  .map((s) => {
    const subs = s.toc.map((t) => `<li><a href="#${t.id}">${t.text}</a></li>`).join('')
    return `<li class="doc-item"><a href="#${s.slug}"><strong>${s.h1}</strong></a>${subs ? `<ul>${subs}</ul>` : ''}</li>`
  })
  .join('')

const bodyHtml = sections
  .map((s) => `<section id="${s.slug}" class="doc-section">${s.html}</section>`)
  .join('')

const katexDist = resolve(root, 'node_modules/katex/dist')
let katexCss = readFileSync(resolve(katexDist, 'katex.min.css'), 'utf8')
katexCss = katexCss.replace(/url\(fonts\/([^)]+\.woff2)\)/g, (m, name) => {
  const b64 = readFileSync(resolve(katexDist, 'fonts', name)).toString('base64')
  return `url(data:font/woff2;base64,${b64})`
})

const page = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Structure-Flow Calculus — Complete Documentation</title>
<style>
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 17px;
  line-height: 1.65;
  color: #1a1a1a;
  background: #fbfaf7;
}
.wrap { max-width: 820px; margin: 0 auto; padding: 0 24px 80px; }
header.hero {
  background: #17222e;
  color: #f4efe6;
  padding: 44px 24px 36px;
  text-align: center;
  border-bottom: 6px solid #c9a227;
}
header.hero h1 { margin: 0 0 8px; font-size: 30px; letter-spacing: .5px; }
header.hero p { margin: 0; font-style: italic; opacity: .85; }
.toc-box {
  background: #fff;
  border: 1px solid #ddd3c0;
  border-radius: 8px;
  padding: 18px 22px;
  margin: 28px 0 10px;
}
.toc-box h2 { margin-top: 0; font-variant: small-caps; letter-spacing: 1px; color: #7a5b12; }
.toc-box ul { margin: 0; padding-left: 20px; }
.toc-box .doc-item { margin: 6px 0; }
.toc-box ul ul { margin: 2px 0 8px; font-size: .92em; color: #444; }
a { color: #1f5c8f; text-decoration: none; }
a:hover { text-decoration: underline; }
.doc-section { padding: 26px 0 10px; }
.doc-section + .doc-section { border-top: 1px solid #e4dccb; }
h1, h2, h3, h4 { color: #17222e; line-height: 1.3; }
.doc-section h1 { font-size: 24px; border-bottom: 2px solid #c9a227; padding-bottom: 6px; }
h2 { font-size: 20px; margin-top: 28px; }
h3 { font-size: 17px; margin-top: 22px; }
em { color: #333; }
blockquote {
  margin: 14px 0; padding: 2px 16px; color: #444;
  border-left: 3px solid #c9a227; background: #f4efe3;
}
code { font-family: Consolas, Menlo, monospace; font-size: .9em; background: #efece4; padding: 1px 4px; border-radius: 3px; }
pre {
  background: #17222e; color: #eae5da; padding: 14px 16px; border-radius: 6px;
  overflow-x: auto; font-size: .9em; line-height: 1.5;
}
pre code { background: none; color: inherit; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: .95em; }
th, td { border: 1px solid #cfc5ad; padding: 7px 10px; text-align: left; vertical-align: top; }
th { background: #efe7d3; }
tr:nth-child(even) td { background: #f7f3ea; }
hr { border: none; border-top: 1px solid #ddd3c0; margin: 24px 0; }
strong { color: #0f1822; }
.katex-display { margin: 16px 0; overflow-x: auto; overflow-y: hidden; padding: 4px 0; }
footer { text-align: center; color: #888; font-size: .85em; margin-top: 30px; }
@media print {
  @page { size: A4; margin: 16mm 15mm 18mm; }
  body { background: #fff; font-size: 11pt; }
  a { color: inherit; text-decoration: none; }
  .toc-box { page-break-after: always; border: none; }
  .doc-section { page-break-before: always; }
  .katex-display { overflow: visible !important; }
  p, li { orphans: 3; widows: 3; }
}
${katexCss}
</style>
</head>
<body>
<header class="hero">
  <h1>Structure-Flow Calculus</h1>
  <p>Complete documentation — the treatise, the eleven papers, and the program reports, in one readable file.</p>
</header>
<div class="wrap">
  <nav class="toc-box">
    <h2>Contents</h2>
    <ul>${tocHtml}</ul>
  </nav>
  ${bodyHtml}
  <footer>Structure-Flow Calculus Working Group &mdash; generated by scripts/build-standalone.mjs</footer>
</div>
</body>
</html>
`

const outDir = resolve(root, 'build')
const out = resolve(outDir, 'Structure-Flow-Calculus-Docs.html')
mkdirSync(outDir, { recursive: true })
writeFileSync(out, page, 'utf8')
console.log(`Wrote ${out} (${(Buffer.byteLength(page) / 1024).toFixed(0)} KB, ${sections.length} documents, ${sections.reduce((n, s) => n + (s.html.match(/<h2 /g) || []).length, 0)} sections)`)
export { out }