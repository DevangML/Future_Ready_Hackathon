---
name: figma-make-kodosh-b2b
description: 'Translates Figma design tokens and layouts into Kodosh B2B design system and Frappe Desk components.'
---

# Figma to Kodosh B2B Converter

## Purpose
Converts Figma design tokens (colors, typography, spacing) into Kodosh B2B CSS variables and Frappe components.

## Conversion Pipeline
1. **Token Extraction**: Export Figma JSON tokens (palette, spacing scale, font styles).
2. **SCSS Generation**: Map tokens into `:root` CSS custom properties matching Kodosh B2B theme.
3. **Component Scaffolding**: Generate responsive Frappe Desk and Web portal templates.
4. **Accessibility Check**: Enforce WCAG AA contrast ratios on all generated color tokens.
