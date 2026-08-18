import { defineConfig } from 'vitepress'
import katexModule from '@vscode/markdown-it-katex'

const katex = (katexModule as any).default ?? katexModule

export default defineConfig({
  title: 'Structure-Flow Calculus',
  description: 'A new stream in mathematics and physics',
  lastUpdated: true,
  srcExclude: ['**/superpowers/**', '**/papers/archive/**'],
  markdown: {
    config(md) {
      md.use(katex, { throwOnError: false })
    }
  },
  vite: {
    build: {
      chunkSizeWarningLimit: 2500
    },
    plugins: [
      {
        name: 'convert-math-delimiters',
        enforce: 'pre',
        transform(src, id) {
          if (!id.endsWith('.md')) return null
          console.log('PLUGIN:', id, 'contains \\(:', src.includes('\\('))
          
          // Convert \(...\) to $...$
          let result = ''
          let i = 0
          let inlineCount = 0
          while (i < src.length) {
            if (src.slice(i, i + 2) === '\\(') {
              const start = i + 2
              let j = start
              while (j < src.length) {
                if (src.slice(j, j + 2) === '\\)') {
                  break
                }
                if (src[j] === '\\') {
                  j += 2
                  continue
                }
                j++
              }
              const math = src.slice(start, j)
              if (/[a-zA-Z]/.test(math)) {
                result += '$' + math + '$'
                inlineCount++
              } else {
                result += '\\(' + math + '\\)'
              }
              i = j + 2
            } else {
              result += src[i]
              i++
            }
          }
          src = result
          
          // Convert \[...\] to $$...$$
          result = ''
          i = 0
          let blockCount = 0
          while (i < src.length) {
            if (src.slice(i, i + 2) === '\\[') {
              const start = i + 2
              let j = start
              while (j < src.length) {
                if (src.slice(j, j + 2) === '\\]') {
                  break
                }
                if (src[j] === '\\') {
                  j += 2
                  continue
                }
                j++
              }
              const math = src.slice(start, j)
              if (/[a-zA-Z]/.test(math)) {
                result += '$$' + math + '$$'
                blockCount++
              } else {
                result += '\\[' + math + '\\]'
              }
              i = j + 2
            } else {
              result += src[i]
              i++
            }
          }
          src = result
          
          if (id.includes('00-treatise')) {
            console.log('TREATISE: converted', inlineCount, 'inline,', blockCount, 'block')
          }
          
          return src
        }
      }
    ]
  },
  themeConfig: {
    nav: [
      { text: 'Overview', link: '/' },
      { text: 'Papers', link: '/papers/00-capstone' },
      { text: 'Structural Synthesis Dynamics', link: '/papers/15-structural-synthesis-dynamics' },
      { text: 'Verification', link: '/verification' },
      { text: 'Demos', link: '/demos' },
      { text: 'PDF', link: 'https://github.com/ram1234598766-dotcom/Physics/releases/latest' }
    ],
    sidebar: [
      {
        text: 'Getting Started',
        items: [
          { text: 'Overview', link: '/' },
          { text: 'The Stream', link: '/overview' },
          { text: 'Verification', link: '/verification' },
          { text: 'Demos', link: '/demos' }
        ]
      },
      {
        text: 'Core Mathematics',
        items: [
          { text: '00 — Capstone', link: '/papers/00-capstone' },
          { text: '00 — Comprehensive Treatise', link: '/papers/00-treatise' },
          { text: '01 — Foundations', link: '/papers/01-foundations' },
          { text: '02 — Structure Spectral Theory', link: '/papers/02-structure-spectral-theory' },
          { text: '08 — Numerical Methods', link: '/papers/08-numerical-methods' },
          { text: '09 — Higher-Dimensional Structure-Flow', link: '/papers/09-higher-dimensional-structure-flow' }
        ]
      },
      {
        text: 'Applications',
        items: [
          { text: '03 — Causal Network Spectral Theory', link: '/papers/03-causal-network-spectral-theory' },
          { text: '04 — Variational & Conservation', link: '/papers/04-variational-conservation' },
          { text: '05 — Graded Media Engineering', link: '/papers/05-graded-media-engineering' },
          { text: '06 — Power Networks & Synchronization', link: '/papers/06-power-networks-synchronization' },
          { text: '07 — Epidemiology on Adaptive Networks', link: '/papers/07-epidemiology-adaptive-networks' },
          { text: '10 — Causal Graph-Time Signal Processing', link: '/papers/10-causal-graph-time-signal-processing' }
        ]
      },
      {
        text: 'Extensions & New Theory',
        items: [
          { text: '11 — Novelty & Literature', link: '/papers/11-novelty-and-literature' },
          { text: '12 — Quantum & Information', link: '/papers/12-quantum-information' },
          { text: '13 — Neuroscience & Brain Networks', link: '/papers/13-neuroscience-brain-networks' },
          { text: '15 — Structural Synthesis Dynamics', link: '/papers/15-structural-synthesis-dynamics' },
          { text: 'Open Problems', link: '/papers/12-open-problems' }
        ]
      }
    ],
    footer: {
      message: 'Mrityunjay K',
      copyright: 'Every theorem proved, every central claim verified numerically. Every claim honest about what is proved and what is conjectured.'
    }
  },
  server: {
    allowedHosts: ['.monkeycode-ai.live']
  }
})