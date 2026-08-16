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
    }
  },
  themeConfig: {
    nav: [
      { text: 'Overview', link: '/' },
      { text: 'The Stream', link: '/overview' },
      { text: 'Papers', link: '/papers/00-capstone' },
      { text: 'Verification', link: '/verification' },
      { text: 'Roadmap', link: '/roadmap' },
      { text: 'Demos', link: '/demos' },
      { text: 'Paper 12', link: '/papers/12-quantum-information' },
      { text: 'PDF', link: 'https://github.com/ram1234598766-dotcom/Physics/releases/latest' }
    ],
    sidebar: [
      { text: 'Overview', link: '/' },
      { text: 'The Stream', link: '/overview' },
      { text: 'Verification', link: '/verification' },
      { text: 'Roadmap', link: '/roadmap' },
      { text: 'Demos', link: '/demos' },
      {
        text: 'Research Papers',
        items: [
          { text: '00 — Capstone', link: '/papers/00-capstone' },
          { text: '00 — Comprehensive Treatise', link: '/papers/00-treatise' },
          { text: '01 — Foundations', link: '/papers/01-foundations' },
          { text: '02 — Structure Spectral Theory', link: '/papers/02-structure-spectral-theory' },
          { text: '03 — Causal Network Spectral Theory', link: '/papers/03-causal-network-spectral-theory' },
          { text: '04 — Variational & Conservation', link: '/papers/04-variational-conservation' },
          { text: '05 — Graded Media Engineering', link: '/papers/05-graded-media-engineering' },
          { text: '06 — Power Networks & Synchronization', link: '/papers/06-power-networks-synchronization' },
          { text: '07 — Epidemiology on Adaptive Networks', link: '/papers/07-epidemiology-adaptive-networks' },
          { text: '08 — Numerical Methods', link: '/papers/08-numerical-methods' },
          { text: '09 — Higher-Dimensional Structure-Flow', link: '/papers/09-higher-dimensional-structure-flow' },
          { text: '10 — Causal Graph-Time Signal Processing', link: '/papers/10-causal-graph-time-signal-processing' },
          { text: '11 — Novelty & Literature', link: '/papers/11-novelty-and-literature' },
          { text: '12 — Quantum & Information', link: '/papers/12-quantum-information' }
        ]
      }
    ],
    footer: {
      message: 'Structure-Flow Calculus Working Group',
      copyright: 'Every theorem proved, every central claim verified numerically.'
    }
  },
  server: {
    allowedHosts: ['.monkeycode-ai.live']
  }
})
