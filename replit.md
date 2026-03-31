# Personal Website — Mihnea-Teodor Stoica

## Overview
A minimal, dark-mode personal website built with a single HTML file (no frameworks, no JS). Served via Python's built-in HTTP server.

## Structure
- `index.html` — the entire site (HTML + embedded CSS)

## Server
- Python3 `http.server` on port 5000
- Workflow: "Start application"

## Design
- Dark mode (#0a0a0b background), Inter font with system fallbacks
- Centered column layout (max-width 640px)
- Text-focused with subtle interaction polish (hover states, fade-in animations)
- Work items styled with left border indicators
- Timeline section with vertical line and dot markers
- Competitions displayed in a structured grid layout
- Links section with arrow indicators and hover effects
- Responsive (mobile + desktop)
- Accessibility: focus-visible styles, prefers-reduced-motion support, WCAG-aware contrast
