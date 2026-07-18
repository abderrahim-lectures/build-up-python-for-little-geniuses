% magazine.cls -- the "not a textbook" layout for Build Up: Python for
% Little Geniuses.
%
% Mechanism (see the plan this book was built from for why): `multicol` for
% column layouts, plain `tcolorbox` (its ordinary box styling, NOT the
% unrelated `magazine` library, which is a page-continuation feature) for
% the colored panels, and `tikzpagenodes`/`textpos` for placing elements at
% fixed page positions. This is a stretch-goal-friendly starting point, not
% a finished art-directed design.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{magazine}[2026/07/18 Build Up magazine-style book class]

\LoadClass[11pt, twoside]{book}

\RequirePackage[a4paper, margin=2cm]{geometry}
\RequirePackage{multicol}
\RequirePackage[most]{tcolorbox}
\RequirePackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes.geometric}
\RequirePackage[absolute, overlay]{textpos}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{titlesec}
\RequirePackage{etoolbox}

% Colorblind-safe accent palette (see assets/generate_sprites.py for the
% same check on the pixel-art side). Blue/amber reads distinctly under
% deuteranopia and protanopia simulation, unlike red/green.
\definecolor{buWhole}{HTML}{4C6EF5}
\definecolor{buPart}{HTML}{FFB000}
\definecolor{buOutline}{HTML}{212121}

% hyperref last (standard practice), after buWhole exists for its link colors.
\RequirePackage[colorlinks=true, linkcolor=buWhole, urlcolor=buWhole, citecolor=buWhole]{hyperref}

% --- Chapter opener: big colored band, not a plain heading ------------------
% titlesec passes the chapter's title text automatically between the
% "before" and "after" code blocks below -- it is NOT substituted via a
% #1/##1 parameter (that syntax is for \newcommand, not \titleformat).
%
% \tableofcontents calls the unnumbered \chapter* internally, which would
% otherwise pick up this same colored-band styling and print a stale/wrong
% "Chapter N" line above "Contents". \ifbu@shownum guards against that --
% true for real chapters, switched off for the duration of \tableofcontents.
\newtoggle{bu@shownum}
\toggletrue{bu@shownum}

\titleformat{\chapter}[block]
  {\normalfont\Huge\bfseries\color{white}}
  {}
  {0pt}
  {%
    \begin{tcolorbox}[
      colback=buWhole, colframe=buWhole, arc=0pt, outer arc=0pt,
      boxrule=0pt, width=\textwidth, halign=left, valign=center,
      height=3.2cm, before skip=0pt, after skip=1cm,
    ]
    \begin{minipage}{\textwidth}
    \iftoggle{bu@shownum}{%
      \textcolor{white}{\normalfont\small\bfseries\MakeUppercase{Build Up}}\\[2pt]
      \textcolor{white}{\Large Chapter \thechapter}\\[2pt]
    }{}
  }
  [%
    \end{minipage}
    \end{tcolorbox}
  ]
\titlespacing*{\chapter}{0pt}{0pt}{0pt}

\let\bu@oldtableofcontents\tableofcontents
\renewcommand{\tableofcontents}{%
  \togglefalse{bu@shownum}%
  \bu@oldtableofcontents
  \toggletrue{bu@shownum}%
}

% This book counts chapters from 0 (matching the book/00-welcome/,
% book/01-.../ folder numbering), not LaTeX's default start at 1. Every
% \input of a NN-named chapter folder should be preceded by
% \setcounter{chapter}{NN-1} so \chapter{...} inside it steps up to the
% right number -- see build-up.tex.

% --- Custom title page, replacing plain \maketitle --------------------------
% The cover art itself (book/00-welcome/images/cover.png) is a real designed
% asset made in Canva -- not something hand-coded in tikz/textpos, since
% illustration is outside what code-only generation can do well (see the
% plan this book was built from). The cover is full-bleed and already
% carries its own title text, so it is left alone, full page, no overlay --
% author/version/brief get their own plain colophon page right after,
% instead of competing with the art for space.
%
% \bookversion and \bookbrief work like \author/\date: set them in the
% document preamble before \maketitle.
\newcommand{\bookversion}[1]{\gdef\@bookversion{#1}}
\newcommand{\bookbrief}[1]{\gdef\@bookbrief{#1}}
\bookversion{}
\bookbrief{}

% NOTE, hard-won: the standard \titlepage environment resets \c@page to 1
% and calls \cleardoublepage every time it's used, so nesting a second one
% for the colophon silently ate its content -- fixed by not using \titlepage
% at all here, just a plain \clearpage + \thispagestyle{empty} by hand.
%
% Root cause of the actual content loss, found by bisecting down to a bare
% test string: `textpos`'s `overlay`-mode content (the full-bleed cover
% image below) corrupts the page-builder state for whatever immediately
% follows it, even after the intervening \clearpage. A single non-empty
% \mbox{} placed right after it absorbs that corruption instead of losing
% real content -- see the buffer immediately below.
\renewcommand{\maketitle}{%
  \begin{textblock*}{\paperwidth}(0cm, 0cm)
    \includegraphics[width=\paperwidth]{book/00-welcome/images/cover.png}
  \end{textblock*}
  \clearpage
  \thispagestyle{empty}
  \mbox{}% buffer: textpos's overlay content otherwise corrupts the very
          % next page's typesetting (diagnosed empirically); a real,
          % non-empty box here absorbs that instead of losing real content
  \clearpage
  \thispagestyle{empty}
  \begin{center}
    \vspace*{3cm}
    {\Huge\bfseries \@title\par}
    \vspace{1.2cm}
    {\Large \@author\par}
    \vspace{4pt}
    {\large \@date%
      \ifx\@bookversion\@empty\else\ \textbullet\ v\@bookversion\fi
    \par}
    \vspace{1.5cm}
    \ifx\@bookbrief\@empty\else
      {\normalsize\itshape\begin{minipage}{0.7\textwidth}\centering\@bookbrief\end{minipage}\par}
    \fi
  \end{center}
  \clearpage
}

% --- Recurring pedagogical boxes -------------------------------------------
% One \tcolorbox environment per box type from the plan. Titles are set from
% the argument so each chapter can phrase its own heading.

\newtcolorbox{objectivesbox}[1]{
  colback=buWhole!8, colframe=buWhole, fonttitle=\bfseries,
  title={By the end of this chapter, you can...},
}

\newtcolorbox{socraticbox}[1]{
  colback=white, colframe=buOutline, fonttitle=\bfseries, title={#1},
}

\newtcolorbox{conceptbox}[1]{
  colback=buPart!10, colframe=buPart, fonttitle=\bfseries, title={#1},
}

\newtcolorbox{geogebrabox}[1]{
  colback=white, colframe=buWhole, fonttitle=\bfseries,
  title={Try it live: #1},
}

\newtcolorbox{codebox}[1]{
  colback=black!5, colframe=black, fonttitle=\bfseries\ttfamily, title={#1},
}

\newtcolorbox{buildbox}[1]{
  colback=buWhole!12, colframe=buWhole, fonttitle=\bfseries,
  title={Build Up: #1},
}

\newtcolorbox{practiceset}[1]{
  colback=buPart!8, colframe=buPart, fonttitle=\bfseries, title={#1},
}

\newtcolorbox{explainbox}[1]{
  colback=white, colframe=buOutline, fonttitle=\bfseries, title={#1},
}

\newtcolorbox{knowledgecheck}[1]{
  colback=buWhole!8, colframe=buWhole, fonttitle=\bfseries, title={#1},
}

\newtcolorbox{retrievalbox}[1]{
  colback=buPart!12, colframe=buPart, fonttitle=\bfseries, title={#1},
}

\endinput
