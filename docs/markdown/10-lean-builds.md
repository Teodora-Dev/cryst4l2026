Cryst4l is modular by design: ship only what you use.

## A) Lean entry file

Create `styles.build.css`:

```css
@layer reset, settings, base, objects, components, utilities;

@import url("./_3-resets/_normalize.css") layer(reset);
@import url("./_1-settings/_variables.css") layer(settings);
@import url("./_4-base/_base.css") layer(base);
@import url("./_5-objects/_wrappers.css") layer(objects);
@import url("./_5-objects/_grid.css") layer(objects);
@import url("./_6-components/_components-core.css") layer(components);

/* import only the utility helpers you use */
```

## B) Pick utilities à la carte

Instead of importing `_utilities.css`, import just helpers:

```css
@import url("./_7-utilities/helpers/_widths.css") layer(utilities);
@import url("./_7-utilities/helpers/_margins.css") layer(utilities);
@import url("./_7-utilities/helpers/_padding.css") layer(utilities);
```
