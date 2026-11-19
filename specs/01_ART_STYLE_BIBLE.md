# 01_ART_STYLE_BIBLE.md — style, palette, facets, technical contract

1. **Look:** flat faceted neo-cyberpunk vector, as the approved hero (`public/cyber/refs/hero_flat_gemini.jpg`): large flat planes, hard two-tone shading, a cyan rim on the left, a coral rim on the right, a night city in plum and navy. Facets fewer but in their places (owner): a cheek is 1 facet, the upper lip 4, the lower lip 2, the nose a few, the eyes a little more.
2. **Palette:**
   - Roles: cyan rim left, coral rim right, shadows plum or navy — never `#000000`; 3 values per material (light, mid, shadow).
   - Hex: series work uses `colors.flat` in tokens.json — the approved hero's set (rims `#30FBFD` / `#FD805B`, navy `#0E142F`, plum `#2E2057`). The v1 groups (`#00F0FF` / `#FF6B5B`, `#1F1638`) stay for the stage-1 components that import them. Don't mix the two rim pairs in one frame.
   - Black is a material, not a shadow: the coat and the face's ink (lashes, lines) are black in the approved art; shadow planes never are.
   - Inside the head: format 2's saturated gradients and format 1's lime `#C8FF2E` (`colors.head_world`). Outside the head the active word takes the rim cyan of the set in use or amber `#FFB84D`; keeping lime for the head makes the dive read at once.
3. **Facets:** hero ≈80–100 (now 81: body 40, head 41). Interlocutors: the same language, simpler, so the hero leads the frame. Inserts and world parts have their own budgets. No slivers under 4 px at 1080 wide; limb facets split along the limb, not across it.
4. **Edges:** no outlines — edges are colour boundaries. A same-colour stroke closes anti-alias seams: 0.8 px on rig parts (`HeroBody.tsx`), 1.5–2 px on masks over neighbouring patches.
5. **Gradients:** none on characters and kit parts; sky, haze, light pools, glow and the inside of the head may use them.
6. **Safe zone (1080×1920):** eyes, lines and the CTA inside X 108–907, Y 384–1382 (10–84 %, 20–72 %) — stricter than `src/kit/safe-zone.ts`. Frame 0 is the cover: its key text is readable.
7. **Type:** `Unbounded` 800/900 (fallback `Montserrat` Black), 1–3 words per beat, lines in format-1 kinetics (`src/formats/explainer/kit.tsx`); `Inter` Bold for HUD.
8. **Motion craft:**
   - No `Easing.linear` on characters or text — springs from tokens.json; no cross-dissolves.
   - No dead frame on screen: a push, a breath or the coat keeps living (push 1.00 → 1.06–1.10 over 3–4 s).
   - `stepped_character_fps` 15: legs, boot steps and drawn swaps (mouth, eyelids, hand shapes) hold each pose 2 frames and start on even frames; coat, hair, camera, parallax, effects and text move every frame at 30 fps. Key poses hold 2–3 frames; the coat flap trails 3–4 frames.
9. **Render on this server (no GPU):** WebGL — the default `--gl` or `swangle`; `angle` only on a GPU machine; `remotion.config.ts` stays. Drafts `--scale=0.5`. Blur filters are slow (a 50 s explainer took 8 min). Telegram ≤ 50 MB: grainy clips at crf 26.
