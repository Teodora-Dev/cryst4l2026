Tokens live in:

- `source/css/_1-settings/_variables.css` (framework source)
- `docs/css/_1-settings/_variables.css` (docs copy)

They define:
- spacing (`--space-*`)
- typography (`--fs-*`)
- optional container breakpoint values (`--cq-*`, documented)
- any brand/theme tokens you add (e.g. `--surface-bg`)

## Theming

Theme Cryst4l by overriding tokens — not by rewriting components:

```css
[data-theme="dark"]{
  --surface-bg: #111;
  --text-color: #eee;
}
```

This keeps your components portable and your CSS small.
