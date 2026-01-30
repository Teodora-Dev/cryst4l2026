# Popup (unstyled modal shell)

Cryst4l includes an **unstyled popup** component (`c-popup`) that provides structural CSS for a modal:
- full-screen overlay container
- backdrop element
- dialog container with scroll handling
- header/body/footer hooks
- close hooks for your JS

Your JavaScript should handle:
- toggling open/close
- focus trap
- ESC handling
- closing on click of `[data-popup-close]`

## Markup

```html
<div class="c-popup" data-popup data-open="false" aria-hidden="true">
  <div class="c-popup__backdrop" data-popup-close></div>

  <div class="c-popup__dialog"
       role="dialog"
       aria-modal="true"
       aria-labelledby="popup-title">

    <header class="c-popup__header">
      <h2 id="popup-title" class="c-popup__title">Popup title</h2>
      <button class="c-popup__close c-button" type="button" data-popup-close aria-label="Close">
        ×
      </button>
    </header>

    <div class="c-popup__body">
      <div class="c-box u-p-4 u-border">Your content here…</div>
    </div>

    <footer class="c-popup__footer">
      <button class="c-button u-px-3 u-py-2 u-border" type="button" data-popup-close>Close</button>
    </footer>
  </div>
</div>
```

## Toggle (what JS should do)

- set `data-open="true"` (and `aria-hidden="false"`) to show
- set `data-open="false"` (and `aria-hidden="true"`) to hide

## Tokens you can override

- `--popup-z`
- `--popup-width`
- `--popup-backdrop`
- `--popup-surface`
- `--popup-gap`
- `--popup-body-gap`
