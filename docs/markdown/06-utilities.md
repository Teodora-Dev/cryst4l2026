Utilities are **explicit overrides**: local, single-purpose, and predictable.

Cryst4l supports two tiers.

## Tier 1 — Classic responsive utilities
Viewport-based helpers (ported from the original Sass system).

Examples:
- `u-1/2@md-up`
- `u-margin-bottom@lg-up`
- `u-push-1/3@sm-up`

Use when:
- layout must respond to the viewport
- you need precise breakpoint control

## Tier 2 — Token utilities
Modern, small, token-backed shortcuts (2026 upgrade).

Examples:
- `u-p-4`, `u-mb-3`, `u-gap-2`
- `u-fs-2`, `u-lh-tight`, `u-flow`

Use when:
- you want fast spacing/type tweaks
- you want fluid scaling “for free”

You can use either tier or both.
