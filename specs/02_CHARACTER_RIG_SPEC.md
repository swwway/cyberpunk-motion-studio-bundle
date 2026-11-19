# 02_CHARACTER_RIG_SPEC.md — Protagonist Rig, Heroic Proportions, Outfits & Russian Visemes

1. **Identity & Heroic Proportions (LOCKED):**
   - Stylized Senior AI Architect with **graphic-novel heroic build**: proportionally **smaller, sleek head** anchored over a **broad, imposing chest and razor-sharp angular shoulders** (**shoulder width ≈ 3.2x head width**, zero soft/sloped shoulders).
   - Elongated chiseled jawline, 2-polygon straight Greek nose, piercing blue hunter eyes (`#1D9BF0` iris, `#7DD3FC` glint), brown eyebrows (`#4E3524`), dirty-blonde angular curls (`#D4AA5A` / `#9E773B` / `#5C4128`) with front bangs slightly overlapping upper forehead.
2. **Normalized Rig Canvas:** `viewBox="0 0 700 800"` with locked anchors in `specs/tokens.json` (`head_pivot: [350, 345]`, `neck_pivot: [350, 395]`, `shoulder_left_corner: [95, 455]`, `shoulder_right_corner: [605, 455]`, `eye_center_y: 235`, `mouth_pivot: [350, 310]`).
3. **Wardrobe (`outfit_mode`):**
   - `OUTFIT_TECHWEAR_JACKET`: Matte-black high-collar techwear jacket (`#141724` / `#23283D` / `#0D0F1A`) with broad architectural angular shoulders.
   - `OUTFIT_FORMAL_SUIT`: Tailored charcoal-navy suit (`#161A26` / `#242B3D`) with broad razor-sharp padded shoulders, ice-white shirt (`#E2E8F0`), dark tie (`#0B0E17`).
4. **6 Emotional States (`emotion_state`):**
   - `CONFIDENT`, `LOCKED_IN`, `SARCASTIC_HAPPY`, `DEAD_SERIOUS_GRAVE`, `WHISPER_CONSPIRACY`, `BREAKTHROUGH`.
5. **6 Russian Visemes (`mouth_phonemes`):**
   - `REST` (closed/smirk), `AI` (А/Я/Э + jaw drops `+4px`), `E` (Е/И/Ы/С/З), `O` (О/У/Ю/Ё angular hex), `M` (М/Б/П compressed), `FV` (Ф/В teeth on lower lip).
6. **Mandatory Visual Grounding:** Before coding any `<polygon>` or `<path>` points in `HeroRig.tsx`, inspect `assets/refs/character_turnaround.png` and `assets/refs/emotion_sheet_6x.png`.
