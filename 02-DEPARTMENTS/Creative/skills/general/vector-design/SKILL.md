---
name: vector-design
description: Create, edit, and critique accurate, scalable SVG artwork such as logos, icons, diagrams, illustrations, and geometric graphics. Use whenever the requested deliverable is SVG or editable vector artwork. Do not use for bitmap illustration or photo editing.
---

# Purpose

Produce vector artwork that is visually intentional, distinctive, technically valid, editable, and accurate at its intended sizes.

This skill controls vector construction and verification. It does not define the brand aesthetic. Use the Core Brand Skill, Brand Kit, relevant medium-specific skill, and No Slop Skill for visual direction.

For marks, icons, mascots, and compact illustrations, require logo-grade clarity and craft rather than accepting technically correct SVG as a finished design.

# Define the Deliverable

Before drawing, establish what materially affects construction:

- intended use and target sizes
- canvas size or aspect ratio
- whether the SVG must be responsive
- whether text should remain editable
- whether strokes should scale
- required color modes or variants
- browser, print, animation, or software compatibility
- whether an existing visual must be matched

Ask only when a missing answer would change the geometry or file structure.

# Concept Before Construction

For open-ended design, define the central visual idea in one sentence before building final geometry.

Explore several materially different silhouette-level approaches when the concept is unresolved. Compare them using:

- relevance to the brief
- immediate recognizability
- distinctiveness within the category
- simplicity without genericness
- potential to work at small sizes

Do not polish the first literal solution merely because it is easy to draw.

Aim for one dominant read and, when useful, one secondary discovery. Combine familiar forms only when the relationship communicates something meaningful; avoid arbitrary visual mashups.

Do not inherit the subject, palette, or construction of a reference merely because its quality is desirable. Extract the principle behind its success.

# Plan the Geometry

Set the coordinate system before creating shapes.

- Use a deliberate `viewBox` with a predictable origin and dimensions.
- Identify the dominant silhouette, axes, alignments, proportions, and negative spaces.
- Choose a limited, coherent shape vocabulary for curves, corners, angles, and stroke behavior.
- Break complex artwork into simple geometric relationships before writing path data.
- Measure repeated gaps, radii, angles, and stroke widths rather than estimating each instance independently.
- Account for optical balance when mathematical centering looks wrong.
- Resolve the silhouette and major internal spaces before adding facial features, texture, or decoration.

For reference-based work, identify a small set of measurable landmarks and ratios. Do not rely on a general visual impression.

# Construct Deliberately

Prefer the simplest editable construction that preserves the design's distinctive character.

- Use SVG primitives for regular geometry when practical, but treat them as construction tools rather than automatically accepting their default appearance.
- Use paths for genuinely custom contours, not as a default for every shape.
- Keep path nodes purposeful and curves smooth.
- Use consistent stroke widths, caps, and joins unless variation is intentional.
- Use groups to express meaningful structure and layer order.
- Give reusable definitions and important groups clear, stable IDs.
- Use `defs`, symbols, gradients, masks, and clipping paths only when they reduce duplication or enable a required effect.
- Keep transforms understandable. Avoid deep transform stacks that make editing and debugging difficult.
- Use enough numeric precision to preserve the form without filling the file with meaningless decimals.

Build complex artwork in stages. Render and inspect the major silhouette before adding internal detail.

# Shape Language and Optical Craft

- Keep outer contours and internal cutouts visually related.
- Maintain smooth curve tension and deliberate transitions between straight and curved segments.
- Avoid accidental tangencies, narrow pinches, almost-touching shapes, and uneven negative spaces.
- Balance filled mass, stroke weight, and empty space optically rather than relying only on mathematical equality.
- Use controlled asymmetry, tilt, overlap, or scale contrast when they add energy or personality.
- Make corner radii and terminals feel like part of one system, while allowing optical exceptions where strict repetition looks wrong.
- Create personality through proportion and spatial relationships before adding extra features.

Simple does not mean raw geometry. Refine primitive shapes until the result feels authored rather than assembled.

# Quality Bar for Marks and Icons

For logos, symbols, icons, mascots, and other compact graphics:

- require a memorable silhouette that remains identifiable without color
- preserve one clear focal idea rather than distributing attention equally
- make every internal detail earn its place at the smallest intended size
- prefer meaningful negative space over added decoration
- ensure the result feels specific to the brief rather than like generic clip art
- challenge default chatbot faces, robot heads, badges, speech bubbles, sparkles, and other familiar category symbols unless the concept genuinely benefits from them

If the mark is technically clean but forgettable, return to concept and proportion. Do not try to rescue it with gradients, shadows, or additional details.

# Text and Fonts

Do not pretend text is portable when it depends on an unavailable font.

- Keep text as `<text>` when editability or accessibility matters and the font environment is controlled.
- Specify intentional fallbacks for browser-delivered SVG.
- Convert text to outlines only when fixed appearance is required and actual font-outline tooling is available.
- Do not invent glyph outlines or approximate a wordmark with guessed path data.
- Record any font dependency when delivering the SVG.

# Color, Effects, and Images

- Use explicit, consistent color values.
- Establish a strong monochrome version before depending on color.
- Prefer a limited palette with clear contrast and purposeful color relationships.
- Use color to clarify hierarchy, overlap, or personality, not to rescue an undistinguished silhouette.
- Keep opacity behavior understandable and avoid accidental stacking.
- Use gradients and filters only when required by the design.
- Keep filter regions large enough to prevent clipped shadows or blur.
- Do not embed raster images or base64 image data unless the user explicitly wants a hybrid asset.
- Do not describe an auto-traced raster as clean vector artwork without inspecting and refining its paths.

# Accuracy Rules

Do not use a giant guessed path string as a shortcut for complex artwork.

Do not hide inaccurate geometry behind texture, blur, shadows, mockups, or excessive detail.

Do not introduce accidental asymmetry, uneven spacing, inconsistent radii, or almost-aligned edges.

Do not crop artwork unintentionally with the `viewBox`, masks, clipping paths, or filter bounds.

Do not depend on external CSS, scripts, fonts, or assets unless the delivery context explicitly supports them.

Do not add invisible shapes, redundant groups, duplicate IDs, unused definitions, or editor metadata without a reason.

# SVG Structure

The final SVG should normally:

- use the SVG namespace
- include a correct `viewBox`
- have predictable width and height behavior
- use valid XML
- contain no duplicate IDs
- resolve every `url(#id)`, `href`, mask, clip, gradient, and filter reference
- keep all intended artwork within the visible bounds
- avoid embedded raster content unless approved
- remain understandable enough for another designer or agent to edit

For functional web graphics, include a concise `<title>` and, when useful, a `<desc>`. Do not add accessibility text to purely decorative SVG when the surrounding implementation will hide it from assistive technology.

# Required Verification

Never treat unrendered SVG source as a finished visual.

Before delivery:

1. Parse or open the SVG with a standards-compliant XML or SVG tool.
2. Render it to a bitmap at the intended size and at a larger inspection size.
3. Visually inspect the render for clipping, malformed paths, layer-order errors, uneven curves, alignment problems, incorrect strokes, missing fonts, and broken effects.
4. Inspect the SVG at the smallest realistic use size for legibility and unwanted detail loss.
5. For marks and icons, inspect a thumbnail grid in monochrome and on relevant light and dark backgrounds.
6. Ask whether the silhouette is immediate, specific, and balanced. If it reads as generic, return to the concept or proportions rather than adding decoration.
7. When matching a source, compare the render side by side or with an overlay and correct meaningful proportion or contour errors.
8. Re-render after every meaningful correction.

If rendering or visual inspection is unavailable, state that limitation. Do not claim visual accuracy from source-code inspection alone.

# Delivery

When the user asks for an SVG file, save and deliver an actual `.svg` file rather than only showing a code block.

Preserve useful source work and avoid overwriting approved assets without explicit permission.

Provide requested variants from the same approved geometry rather than rebuilding each one independently.

Mention any remaining font, external asset, browser, or software dependency.

# Final Vector Check

Before presenting the result, confirm:

1. Is there one clear, relevant visual idea?
2. Does the silhouette feel memorable and specific before details are considered?
3. Are proportions, negative spaces, curves, terminals, and alignment optically deliberate?
4. Does the shape language feel coherent rather than assembled from defaults?
5. Is the construction simpler than an equally accurate alternative without losing character?
6. Is the SVG valid, editable, and free of broken references?
7. Does it render correctly in monochrome, on required backgrounds, and at every required size?
8. Does it follow the brand and medium direction without generic vector decoration?
9. Was the latest saved file rendered and visually inspected?

Fix meaningful failures before delivery.
