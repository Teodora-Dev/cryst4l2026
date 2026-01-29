# Media & Container Queries

## Media queries

Use literal values:

```css
@media (min-width: 720px){ … }
```

CSS custom properties **cannot** be used inside media query conditions.

## Container queries (recommended)

Container queries let components respond to their container, not the viewport.

Enable containers with:

```html
<div class="u-container">…</div>
```

Then use CQ utilities like:

```html
<div class="u-container o-grid">
  <div class="o-grid__item u-cq-1/2@md-up">…</div>
  <div class="o-grid__item u-cq-1/2@md-up">…</div>
</div>
```

Cryst4l’s CQ utilities mirror the `@*-up` suffix convention.
