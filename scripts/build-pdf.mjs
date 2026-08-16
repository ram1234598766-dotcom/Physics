import { spawnSync } from 'node:child_process'
import { existsSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { out as htmlOut } from './build-standalone.mjs'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const pdfOut = resolve(root, 'Structure-Flow-Calculus-Docs.pdf')

const candidates = [
  process.env.EDGE_PATH,
  process.env.CHROME_PATH,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
].filter(Boolean)

const browser = candidates.find((p) => existsSync(p))
if (!browser) {
  console.error('No Chromium browser found. Install Microsoft Edge or Google Chrome, or set EDGE_PATH / CHROME_PATH.')
  process.exit(1)
}

const fileUrl = 'file:///' + htmlOut.replace(/\\/g, '/')
const res = spawnSync(
  browser,
  [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--no-pdf-header-footer',
    `--print-to-pdf=${pdfOut}`,
    fileUrl
  ],
  { encoding: 'utf8', timeout: 180000 }
)

if (res.status !== 0) {
  console.error('PDF generation failed:', res.stderr || res.stdout || res.error)
  process.exit(1)
}
console.log(`Wrote ${pdfOut}`)