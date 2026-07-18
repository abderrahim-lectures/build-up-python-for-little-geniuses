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
\RequirePackage{hyperref}

% Colorblind-safe accent palette (see assets/generate_sprites.py for the
% same check on the pixel-art side). Blue/amber reads distinctly under
% deuteranopia and protanopia simulation, unlike red/green.
\definecolor{buWhole}{HTML}{4C6EF5}
\definecolor{buPart}{HTML}{FFB000}
\definecolor{buOutline}{HTML}{212121}

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
