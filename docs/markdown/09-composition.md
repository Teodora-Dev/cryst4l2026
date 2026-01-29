Cryst4l is designed for **composition**.

A common pattern:
- `c-*` provides structure
- `u-*` provides visual decisions
- tokens provide scaling and theming

Example:

```html
<article class="c-card u-border u-p-4">
  <header class="c-cluster u-mb-3">
    <h2 class="u-fs-2">Title</h2>
    <span class="u-fs--1">Meta</span>
  </header>

  <div class="c-stack">
    <p>Paragraph one</p>
    <p>Paragraph two</p>
  </div>

  <footer class="c-cluster u-mt-4">
    <button class="c-button u-px-3 u-py-2 u-border">Action</button>
  </footer>
</article>
```
