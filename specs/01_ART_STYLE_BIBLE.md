# 01_ART_STYLE_BIBLE.md — Visual, Motion & Technical Contract

1. **Aesthetic:** Faceted Neo-Cyberpunk Vector (structured polygonal facial planes + clean low-detail polygonal brutalism).
2. **Line Art:** Strictly lineless (`stroke="none"`, `0px` outline on character). Edges are defined purely by sharp flat polygon color boundaries.
3. **Shading:** Hard Dual-Tone Planar Shading (max 3–4 flat color planes per surface, zero airbrush gradients). Shadows MUST use `#1F1638` / `#2D224D` — NEVER `#000000`.
4. **Safe Zones (`1080x1920`):** All eyes, captions, and `<CtaOverlaySlot />` sit strictly inside `X: 108–907px` (`10%–84%`) and `Y: 384–1382px` (`20%–72%`).
5. **Typography (Russian):** `Unbounded` (800/900) or `Montserrat Black` for 1–3 word kinetic captions (`slide-up + clip-path`), active word in `#00F0FF` or `#FFB84D`. `Inter Bold` for HUD cards.
6. **Motion Craft:**
   - Zero `Easing.linear` on character/UI (use `specs/tokens.json` springs).
   - Zero cross-dissolves.
   - Camera never freezes: continuous `0.5%–1.5%` micro-drift on >65% of frames.
7. **Headless WebGL Lock (`remotion.config.ts`):**
   - Explicitly set `Config.setChromiumOpenGlRenderer('angle')` (fallback `'swiftshader'` on CPU-only Linux/CI) and unmount `<ThreeCanvas>` on non-3D shots to prevent WebGL context loss.
