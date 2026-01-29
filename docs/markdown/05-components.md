Components are **contracts**, not designs.

They define:
- structure
- relationships
- behaviour hooks

Core components included:
- `c-box`
- `c-stack` (+ `c-stack--tight`, `c-stack--loose`)
- `c-cluster`
- `c-card`
- `c-media`
- `c-switcher`
- `c-button`
- `c-list`
- `c-disclosure` (for `<details>`)

Example:

```html
<article class="c-card u-border u-p-4">
  <header class="c-cluster">
    <h2 class="u-fs-2">Title</h2>
    <span class="u-fs--1">Meta</span>
  </header>

  <div class="c-stack">
    <p>Paragraph one</p>
    <p>Paragraph two</p>
  </div>
</article>
```

All visual decisions live in **utilities** or **tokens**.
