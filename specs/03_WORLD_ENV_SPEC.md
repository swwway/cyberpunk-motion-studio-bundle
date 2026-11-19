# 03_WORLD_ENV_SPEC.md — kit worlds, the dive, transitions

1. **Still world:** the world stands, characters move inside it (bible §4). Each episode gets a new place built from the faceted kit — walls, windows, shop windows, signs, furniture, light, wet asphalt — not drawn from scratch. The v1 recurring locations (`LOC_CYBER_SKYLINE`, `LOC_ARCHITECT_TERMINAL`) are gone; their skylines survive as kit seeds (`src/cyber/components/CyberSkyline.tsx`, `src/cyber/flat/FlatCity.tsx`).
2. **Light motivates the rims:** every place shows a cyan source on the left and a coral one on the right; the hero's rims never appear without them.
3. **Depth layers:** shares of the camera move — sky 0.05 · far 0.15 · mid 0.4 · character 1.0 · foreground 1.3–1.6 (tokens `parallax`); far layers blur 1.5–3 px. In a tracked walk the character plane scrolls at the walking speed.
4. **Lines, HUD, CTA:** the parallax shift only, never the camera scale.
5. **Inside the head (formats 2 + 1):** a saturated gradient world per idea (format 2 palettes: blue-turquoise, red, purple, indigo, olive), one object that transforms, glow, grain, a slow non-linear push; lime words and a scheme on top (format 1). Entry through the eye or the temple, exit back through the eye. Pilot: purple, chats → paper planes.
6. **Transition grammar** — never a cross-dissolve, never the same transition twice in a row:
   - `TRANS_SHADOW_WHIP` — a dark whip across the cut;
   - `TRANS_IMPACT_FRAME` — 1–2 frames of `#090B16` with a cyan flash, hides an instant change of place or size;
   - `TRANS_AFTERIMAGE_ECHO` — 2–3 trailing ghost silhouettes;
   - `TRANS_SHADOW_BRIDGE` — a 2-frame dark push into another world;
   - `STAR_WIPE` — format 2's four-point star: a full-frame flash or a match by shape; the way in and out of the head.
7. **Optical cheats:** `SMEAR_WEDGE` — a 2-frame skewed facet wedge in the shadow colour of the set in use with a cyan leading edge (v1: `#1F1638` + `#00F0FF`), opacity 0.6 → 0, into the target pose, then a 3-frame spring settle (`smear_settle`); `SHOT_SHOE_STEP` is now shot type 1, the boot insert.
8. **Prune:** mount only the layers the shot needs; `<ThreeCanvas>` only in 3D shots.
9. **3D cosmos** (`LOC_AI_COSMOS`, `CAM_SPIRAL_ORBIT`): a variant on request, not the default inside the head (role 03 §5).
