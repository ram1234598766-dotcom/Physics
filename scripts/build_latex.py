#!/usr/bin/env python3
"""
build_latex.py — Convert Structure-Flow Calculus markdown papers to LaTeX.

Produces:
  build/latex/*.tex        — one .tex per paper
  build/latex/sfc.tex      — combined master file
  build/latex/sfc.pdf      — compiled PDF (if pdflatex is available)

Usage:
  python scripts/build_latex.py
  python scripts/build_latex.py --paper 01-foundations
  python scripts/build_latex.py --compile
"""

import subprocess
import shutil
import os
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PAPERS_DIR = DOCS / "papers"
BUILD_LATEX = ROOT / "build" / "latex"
PANDOC = shutil.which("pandoc") or r"C:\Users\Mrityunjay\AppData\Local\Pandoc\pandoc.exe"

PAPERS = [
    ("00-capstone", "docs/papers/00-capstone.md"),
    ("00-treatise", "docs/papers/00-treatise.md"),
    ("01-foundations", "docs/papers/01-foundations.md"),
    ("02-structure-spectral-theory", "docs/papers/02-structure-spectral-theory.md"),
    ("03-causal-network-spectral-theory", "docs/papers/03-causal-network-spectral-theory.md"),
    ("04-variational-conservation", "docs/papers/04-variational-conservation.md"),
    ("05-graded-media-engineering", "docs/papers/05-graded-media-engineering.md"),
    ("06-power-networks-synchronization", "docs/papers/06-power-networks-synchronization.md"),
    ("07-epidemiology-adaptive-networks", "docs/papers/07-epidemiology-adaptive-networks.md"),
    ("08-numerical-methods", "docs/papers/08-numerical-methods.md"),
    ("09-higher-dimensional-structure-flow", "docs/papers/09-higher-dimensional-structure-flow.md"),
    ("10-causal-graph-time-signal-processing", "docs/papers/10-causal-graph-time-signal-processing.md"),
    ("11-novelty-and-literature", "docs/papers/11-novelty-and-literature.md"),
    ("12-quantum-information", "docs/papers/12-quantum-information.md"),
    ("12-open-problems", "docs/papers/12-open-problems.md"),
]

EXTRA = [
    "docs/index.md",
    "docs/overview.md",
    "docs/verification.md",
    "docs/roadmap.md",
    "docs/demos.md",
]

PREAMBLE = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{mathrsfs}
\usepackage{braket}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{mathtools}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{graphicx}
\usepackage{bm}
\usepackage{upgreek}
\usepackage{siunitx}
\usepackage{physics}
\usepackage{cleveref}
\usepackage{etoolbox}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{listings}
\usepackage{textcomp}
\usepackage{bbold}
\usepackage{mathdots}
\usepackage{stackrel}
\usepackage{nicefrac}
\usepackage{gensymb}
\usepackage{wasysym}
\usepackage{relsize}
\usepackage{scalerel}
\usepackage{stackengine}
\usepackage{calrsfs}
\usepackage{mathalpha}
\usepackage{stmaryrd}
\usepackage{dsfont}
\usepackage{ulem}
\usepackage{soul}
\usepackage{tcolorbox}
\usepackage{empheq}
\usepackage{ntheorem}
\usepackage{thmtools}
\usepackage{shadethm}
\usepackage{framed}
\usepackage{mdframed}
\usepackage{tikz-cd}
\usepackage{tensor}
\usepackage{blkarray}
\usepackage{url}
\usepackage{doi}
\usepackage{cite}
\usepackage{natbib}
\usepackage{biblatex}
\usepackage{csquotes}
\usepackage{epigraph}
\usepackage{verse}
\usepackage{academicons}
\usepackage{fontawesome5}
\usepackage{fontawesome}
\usepackage{marvosym}
\usepackage{pifont}
\usepackage{dingbat}
\usepackage{ifsym}
\usepackage{manfnt}
\usepackage{shapepar}
\usepackage{wallpaper}
\usepackage{background}
\usepackage{tikzpagenodes}
\usepackage{atbegshi}
\usepackage{everypage}
\usepackage{tikzpagelayers}
\usepackage{scrlayer-scrpage}
\usepackage{fancyhdr}
\usepackage{titleps}
\usepackage{titling}
\usepackage{authblk}
\usepackage{orcidlink}
\usepackage{bookmark}
\usepackage{nameref}
\usepackage{refcount}
\usepackage{zref}
\usepackage{varioref}
\usepackage{crossreftools}
\usepackage{showkeys}
\usepackage{refcheck}
\usepackage{latexdiff}
\usepackage{pdfcomment}
\usepackage{epstopdf}
\usepackage{preview}
\usepackage{standalone}
\usepackage{subfiles}
\usepackage{import}
\usepackage{chapterfolder}
\usepackage{docmute}
\usepackage{fixltx2e}
\usepackage{ltxcmds}
\usepackage{pgfkeys}
\usepackage{pgfmath}
\usepackage{pgffor}
\usepackage{pgfplots}
\usepackage{pgfplotstable}

\hypersetup{
  colorlinks=true,
  linkcolor=blue!60!black,
  urlcolor=blue!60!black,
  citecolor=blue!60!black,
  pdftitle={Structure-Flow Calculus},
  pdfauthor={Structure-Flow Calculus Working Group},
  pdfsubject={Mathematics, Physics, Spectral Theory},
  pdfkeywords={structure field, rho-calculus, spectral theory, variational theory, network theory}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Structure-Flow Calculus}
\fancyhead[R]{\small \today}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{note}[theorem]{Note}

\theoremstyle{remark}
\newtheorem*{proofsketch}{Proof sketch}

\newcommand{\qed}{\hfill\ensuremath{\square}}
\newcommand{\bs}[1]{\boldsymbol{#1}}
\newcommand{\dd}{\;\mathrm{d}}
\newcommand{\rho}{\varrho}
\newcommand{\Rho}{\mathrm{R}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\ud}{\,\mathrm{d}}
\newcommand{\ui}{\,\mathrm{i}}
\newcommand{\ue}{\,\mathrm{e}}
\newcommand{\iu}{\mathrm{i}}
\newcommand{\ie}{\,\mathrm{e}}
\newcommand{\Id}{\mathds{1}}
\newcommand{\Tr}{\operatorname{Tr}}
\newcommand{\sgn}{\operatorname{sgn}}
\newcommand{\supp}{\operatorname{supp}}
\newcommand{\dom}{\operatorname{dom}}
\newcommand{\ran}{\operatorname{ran}}
\newcommand{\ker}{\operatorname{ker}}
\newcommand{\rank}{\operatorname{rank}}
\newcommand{\diag}{\operatorname{diag}}
\newcommand{\dist}{\operatorname{dist}}
\newcommand{\diam}{\operatorname{diam}}
\newcommand{\Lip}{\operatorname{Lip}}
\newcommand{\BV}{\operatorname{BV}}
\newcommand{\W}{\operatorname{W}}
\newcommand{\H}{\mathscr{H}}
\newcommand{\A}{\mathscr{A}}
\newcommand{\F}{\mathscr{F}}
\newcommand{\G}{\mathscr{G}}
\newcommand{\L}{\mathscr{L}}
\newcommand{\M}{\mathscr{M}}
\newcommand{\N}{\mathscr{N}}
\newcommand{\O}{\mathscr{O}}
\newcommand{\P}{\mathscr{P}}
\newcommand{\R}{\mathscr{R}}
\newcommand{\S}{\mathscr{S}}
\newcommand{\X}{\mathscr{X}}
\newcommand{\Y}{\mathscr{Y}}
\newcommand{\Z}{\mathscr{Z}}
\newcommand{\calA}{\mathcal{A}}
\newcommand{\calB}{\mathcal{B}}
\newcommand{\calC}{\mathcal{C}}
\newcommand{\calD}{\mathcal{D}}
\newcommand{\calE}{\mathcal{E}}
\newcommand{\calF}{\mathcal{F}}
\newcommand{\calG}{\mathcal{G}}
\newcommand{\calH}{\mathcal{H}}
\newcommand{\calI}{\mathcal{I}}
\newcommand{\calJ}{\mathcal{J}}
\newcommand{\calK}{\mathcal{K}}
\newcommand{\calL}{\mathcal{L}}
\newcommand{\calM}{\mathcal{M}}
\newcommand{\calN}{\mathcal{N}}
\newcommand{\calO}{\mathcal{O}}
\newcommand{\calP}{\mathcal{P}}
\newcommand{\calQ}{\mathcal{Q}}
\newcommand{\calR}{\mathcal{R}}
\newcommand{\calS}{\mathcal{S}}
\newcommand{\calT}{\mathcal{T}}
\newcommand{\calU}{\mathcal{U}}
\newcommand{\calV}{\mathcal{V}}
\newcommand{\calW}{\mathcal{W}}
\newcommand{\calX}{\mathcal{X}}
\newcommand{\calY}{\mathcal{Y}}
\newcommand{\calZ}{\mathcal{Z}}
\newcommand{\frakA}{\mathfrak{A}}
\newcommand{\frakB}{\mathfrak{B}}
\newcommand{\frakC}{\mathfrak{C}}
\newcommand{\frakD}{\mathfrak{D}}
\newcommand{\frakE}{\mathfrak{E}}
\newcommand{\frakF}{\mathfrak{F}}
\newcommand{\frakG}{\mathfrak{G}}
\newcommand{\frakH}{\mathfrak{H}}
\newcommand{\frakI}{\mathfrak{I}}
\newcommand{\frakJ}{\mathfrak{J}}
\newcommand{\frakK}{\mathfrak{K}}
\newcommand{\frakL}{\mathfrak{L}}
\newcommand{\frakM}{\mathfrak{M}}
\newcommand{\frakN}{\mathfrak{N}}
\newcommand{\frakO}{\mathfrak{O}}
\newcommand{\frakP}{\mathfrak{P}}
\newcommand{\frakQ}{\mathfrak{Q}}
\newcommand{\frakR}{\mathfrak{R}}
\newcommand{\frakS}{\mathfrak{S}}
\newcommand{\frakT}{\mathfrak{T}}
\newcommand{\frakU}{\mathfrak{U}}
\newcommand{\frakV}{\mathfrak{V}}
\newcommand{\frakW}{\mathfrak{W}}
\newcommand{\frakX}{\mathfrak{X}}
\newcommand{\frakY}{\mathfrak{Y}}
\newcommand{\frakZ}{\mathfrak{Z}}
\newcommand{\bA}{\mathbb{A}}
\newcommand{\bB}{\mathbb{B}}
\newcommand{\bC}{\mathbb{C}}
\newcommand{\bD}{\mathbb{D}}
\newcommand{\bE}{\mathbb{E}}
\newcommand{\bF}{\mathbb{F}}
\newcommand{\bG}{\mathbb{G}}
\newcommand{\bH}{\mathbb{H}}
\newcommand{\bI}{\mathbb{I}}
\newcommand{\bJ}{\mathbb{J}}
\newcommand{\bK}{\mathbb{K}}
\newcommand{\bL}{\mathbb{L}}
\newcommand{\bM}{\mathbb{M}}
\newcommand{\bN}{\mathbb{N}}
\newcommand{\bO}{\mathbb{O}}
\newcommand{\bP}{\mathbb{P}}
\newcommand{\bQ}{\mathbb{Q}}
\newcommand{\bR}{\mathbb{R}}
\newcommand{\bS}{\mathbb{S}}
\newcommand{\bT}{\mathbb{T}}
\newcommand{\bU}{\mathbb{U}}
\newcommand{\bV}{\mathbb{V}}
\newcommand{\bW}{\mathbb{W}}
\newcommand{\bX}{\mathbb{X}}
\newcommand{\bY}{\mathbb{Y}}
\newcommand{\bZ}{\mathbb{Z}}

\begin{document}

\begin{titlepage}
\begin{center}
\vspace*{2cm}
{\LARGE\bfseries Structure-Flow Calculus}\\[0.6em]
{\large Foundations, Spectral Theory, and Applications}\\[2em]
{\large Structure-Flow Calculus Working Group}\\[1em]
{\large \today}\\[2em]
\rule{\textwidth}{1.5pt}\\[0.8em]
\begin{minipage}{0.85\textwidth}
\centering
This volume contains the complete Structure-Flow Calculus program:
thirteen research papers (00--12), the comprehensive treatise,
the capstone statement, the verification report, and the research roadmap.
Every theorem is proved; every central theorem is verified numerically.
\end{minipage}
\rule{\textwidth}{1.5pt}
\end{center}
\end{titlepage}

\tableofcontents
\newpage

"""

POSTAMBLE = r"""
\end{document}
"""


def make_latex():
    BUILD_LATEX.mkdir(parents=True, exist_ok=True)
    master = BUILD_LATEX / "sfc.tex"
    
    with open(master, "w", encoding="utf-8") as out:
        out.write(PREAMBLE)
        
        for slug, path in PAPERS:
            src = ROOT / path
            if not src.exists():
                print(f"  MISSING: {src}")
                continue
            print(f"  Converting {path} -> latex/{slug}.tex")
            cmd = [
                PANDOC, str(src),
                "-f", "markdown+tex_math_dollars",
                "-t", "latex",
                "--standalone",
                "--wrap=none",
                "-o", str(BUILD_LATEX / f"{slug}.tex"),
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"    WARNING: {res.stderr[:200]}")
            with open(BUILD_LATEX / f"{slug}.tex", "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace(r"\documentclass{article}", "")
            content = content.replace(r"\begin{document}", "")
            content = content.replace(r"\end{document}", "")
            content = content.replace(r"\maketitle", "")
            content = content.replace(r"\tableofcontents", "")
            out.write(f"\\clearpage\\section{{{slug.replace('-', ' ').title()}}}\n")
            out.write(content)
            out.write("\n")
        
        for path in EXTRA:
            src = ROOT / path
            if not src.exists():
                continue
            slug = Path(path).stem
            print(f"  Converting {path} -> latex/{slug}.tex")
            cmd = [
                PANDOC, str(src),
                "-f", "markdown+tex_math_dollars",
                "-t", "latex",
                "--standalone",
                "--wrap=none",
                "-o", str(BUILD_LATEX / f"{slug}.tex"),
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"    WARNING: {res.stderr[:200]}")
            with open(BUILD_LATEX / f"{slug}.tex", "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace(r"\documentclass{article}", "")
            content = content.replace(r"\begin{document}", "")
            content = content.replace(r"\end{document}", "")
            content = content.replace(r"\maketitle", "")
            content = content.replace(r"\tableofcontents", "")
            out.write(f"\\clearpage\\section{{{slug.replace('-', ' ').title()}}}\n")
            out.write(content)
            out.write("\n")
        
        out.write(POSTAMBLE)
    
    print(f"\nWrote {master}")
    return master


def compile_latex(master):
    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        print("pdflatex not found; skipping compilation.")
        return
    cmd = [pdflatex, "-interaction=nonstopmode", str(master)]
    for i in range(2):
        print(f"  pdflatex pass {i+1}/2...")
        res = subprocess.run(cmd, cwd=str(BUILD_LATEX), capture_output=True, text=True)
        if res.returncode != 0:
            print(f"    WARNING: pdflatex failed (pass {i+1})")
            print(res.stderr[-500:])
    
    pdf_path = BUILD_LATEX / "sfc.pdf"
    if pdf_path.exists():
        size = pdf_path.stat().st_size
        print(f"Wrote {pdf_path} ({size/1024:.1f} KB)")
    else:
        print("PDF was not produced.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build LaTeX from SFC markdown")
    parser.add_argument("--compile", action="store_true", help="Also run pdflatex")
    parser.add_argument("--paper", help="Convert only this paper slug (e.g. 01-foundations)")
    args = parser.parse_args()
    
    if args.paper:
        for slug, path in PAPERS:
            if slug == args.paper:
                BUILD_LATEX.mkdir(parents=True, exist_ok=True)
                cmd = [
                    PANDOC, str(ROOT / path),
                    "-f", "markdown+tex_math_dollars",
                    "-t", "latex",
                    "--standalone",
                    "--wrap=none",
                    "-o", str(BUILD_LATEX / f"{slug}.tex"),
                ]
                print(f"Converting {path}...")
                res = subprocess.run(cmd, capture_output=True, text=True)
                if res.returncode == 0:
                    print(f"Wrote build/latex/{slug}.tex")
                else:
                    print(f"ERROR: {res.stderr[:500]}")
                sys.exit(0)
        print(f"Paper '{args.paper}' not found.")
        sys.exit(1)
    
    master = make_latex()
    if args.compile:
        compile_latex(master)
    print("\nDone. LaTeX files are in build/latex/")
