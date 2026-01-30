# Tabs (CSS-only)

Cryst4l includes a **CSS-only tabs** component built with **radio inputs + labels**.
This gives you tab switching without JavaScript.

> Note: CSS-only tabs can't dynamically update `aria-selected`. If you need strict ARIA, add a tiny JS enhancement.

## Markup (horizontal)

```html
<div class="c-tabs" style="--tabs-active-bg: var(--surface, transparent);">
  <input class="c-tabs__radio" type="radio" name="example" id="tab-1" checked>
  <input class="c-tabs__radio" type="radio" name="example" id="tab-2">
  <input class="c-tabs__radio" type="radio" name="example" id="tab-3">

  <div class="c-tabs__list" role="tablist" aria-label="Example tabs">
    <label class="c-tabs__tab" for="tab-1" role="tab">Overview</label>
    <label class="c-tabs__tab" for="tab-2" role="tab">Details</label>
    <label class="c-tabs__tab" for="tab-3" role="tab">Files</label>
  </div>

  <div class="c-tabs__panels">
    <section class="c-tabs__panel" role="tabpanel"><div class="c-box u-p-4 u-border">Panel 1</div></section>
    <section class="c-tabs__panel" role="tabpanel"><div class="c-box u-p-4 u-border">Panel 2</div></section>
    <section class="c-tabs__panel" role="tabpanel"><div class="c-box u-p-4 u-border">Panel 3</div></section>
  </div>
</div>
```

## Vertical tabs

```html
<div class="c-tabs c-tabs--vertical">…</div>
```

## Tokens you can override

- `--tabs-gap`
- `--tabs-pad-y`, `--tabs-pad-x`
- `--tabs-border`
- `--tabs-radius`
- `--tabs-active-bg`, `--tabs-active-fg`
