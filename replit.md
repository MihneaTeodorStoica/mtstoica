# Personal Website — Mihnea-Teodor Stoica

## Overview
A minimal, dark-mode personal portfolio website with a modular, data-driven architecture. All content is stored in `data.json` and rendered dynamically by `index.html`.

## Structure
- `data.json` — all editable content (name, tagline, about, work, experience, competitions, links, etc.)
- `index.html` — template, styles, and rendering logic (fetches data.json and builds the page)

## How to Edit Content
Edit `data.json` to change any content on the site. The JSON structure supports:
- `name` / `tagline` — header info
- `about` — array of paragraph strings (HTML allowed)
- `currently` — array of bullet point strings (HTML allowed)
- `work` — array of objects with `title`, `role` (optional), `details` array
- `experience` — array of objects with `title`, `organization`, `details` array
- `competitions.results` — array of `{ year, name, note, result }`
- `competitions.ratings` — array of `{ platform, result }`
- `links` — array of `{ label, url, text }`

## Server
- Python3 `http.server` on port 5000
- Workflow: "Start application"

## Design
- Dark mode (#0a0a0b background), Inter font with system fallbacks
- Centered column layout (max-width 640px)
- Subtle hover states and fade-in animations
- Responsive (mobile + desktop)
- Accessibility: focus-visible styles, prefers-reduced-motion support, WCAG-aware contrast
