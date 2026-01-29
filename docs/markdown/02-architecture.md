# Architecture

Cryst4l follows **ITCSS**, implemented natively via CSS `@layer`.

```css
@layer reset, settings, base, objects, components, utilities;
```

Each layer has:
- a single responsibility
- strict rules
- a defined place in the cascade

Result: fewer specificity hacks, fewer “where is this coming from?” moments.
