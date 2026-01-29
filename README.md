# Cryst4l — Pure CSS ITCSS Framework (2026)

Cryst4l is a **pure-CSS**, **ITCSS-inspired** framework modernised for 2026:
- Native cascade control via **`@layer`**
- Design tokens via **CSS custom properties**
- Optional **fluid type + space scales**
- Optional **container query utilities** (including CQ equivalents of width fractions)
- **Structure-only core components** (`c-*`) that don't force styling

## Repo structure

```
source/css/          # Framework source (modular)
docs/                # One-page docs site (GitHub Pages ready)
```

## Quick start

Include the framework entry file:

```html
<link rel="stylesheet" href="/path/to/source/css/styles.css">
```

`styles.css` imports each module into the correct layer using `@import … layer(<name>)`.

## Layer order

```css
@layer reset, settings, base, objects, components, utilities;
```

## Docs (GitHub Pages)

This repo ships a self-contained docs site in `/docs`.

To publish it with **GitHub Pages**:
1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Under **Build and deployment**, set:
   - Source: **Deploy from a branch**
   - Branch: `main` (or `master`)
   - Folder: **/docs**
4. Save — GitHub will publish the docs site.

## Notes on breakpoints and variables

CSS custom properties **cannot** be used inside `@media` or `@container` conditions (e.g. `min-width: var(--bp-md)`).
Cryst4l keeps breakpoint values as literals in query blocks and uses tokens as documentation.

## Credits

Original Sass starter by Teo (2015–16).  
Pure CSS rewrite + modernisation: 2026-01-29.
