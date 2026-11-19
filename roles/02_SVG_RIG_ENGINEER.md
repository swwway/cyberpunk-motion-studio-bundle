# Role 02: Faceted SVG Rig & Lip-Sync Engineer (High Reasoning)

## Exclusive File Ownership
- `src/components/HeroRig.tsx`
- `src/components/MouthPhonemes.tsx`
- `src/components/OpticalCheats.tsx`

## Responsibilities
1. **Visual Reference Grounding (Mandatory First Step):**
   - Inspect `assets/refs/character_turnaround.png` and `assets/refs/emotion_sheet_6x.png` before drafting SVG coordinates.
   - **Proportion Lock:** Strictly reproduce the **heroic silhouette** — proportionally smaller head centered over broad, razor-sharp angular shoulders (`shoulder_width ≈ 3.2x head_width`, sharp polygonal corners at `[95, 455]` and `[605, 455]`). Never draw sloped or narrow shoulders.
   - Match the exact faceted polygonal planes, front curls overlapping the upper forehead, 2-polygon Greek nose, and dual-tone rim slices (`#00F0FF` left, `#FF6B5B` right).
2. **Strict Coordinate Discipline:**
   - Build `HeroRig.tsx` inside a normalized `viewBox="0 0 700 800"` using anchor constants imported from `specs/tokens.json`.
   - Maintain exact semantic `<g id="...">` IDs: `#hero_root`, `#rim_light_layer`, `#torso_outfit`, `#neck_shadow`, `#head_group`, `#hair_back`, `#face_base_facets`, `#nose_facet`, `#eyes_group`, `#eyes_sclera_iris`, `#eyes_eyelids`, `#brows_emotion`, `#mouth_phonemes`, `#hair_front_bangs`, `#prop_hand_point_pov`.
3. **Zero-Outline & Non-Black Shadow Rule:**
   - Every `<polygon>` and `<path>` MUST have `stroke="none"`.
   - Never use `#000000`. Use `#1F1638` / `#2D224D` / `#4A3359` from `tokens.json`.
4. **Netflix-Tier Micro-Life (Deterministic `useCurrentFrame()`):**
   - **Blinking:** 3-frame closed-lid blink every 75–120 frames (deterministic pseudo-random seed per beat) + forced 2-frame blink on every `emotion_state` switch.
   - **Secondary Motion:** `#hair_back` and `#hair_front_bangs` lag `#head_group` rotation/translation by `2 frames` for natural follow-through.
   - **Jaw Coupling:** When `MouthPhonemes.tsx` renders `AI` or `O`, shift the lower jaw polygon in `#face_base_facets` down by `+4px` (interpolated via 2-frame spring).
   - **Eye Dart (`LOCKED_IN`):** Snap `#eyes_sclera_iris` `translateX` (`-6px -> +6px -> 0px`) over 3-frame snaps during `CAM_EYE_LETTERBOX`.
5. **Optical Cheats (`OpticalCheats.tsx`):**
   - Implement `SmearWedge` (2-frame polygonal motion-shadow arc `#1F1638` + `#00F0FF` edge) preceding `#prop_hand_point_pov` punch-in (`spring(stiffness: 260, damping: 16)`).
   - Implement `ShotShoeStep` (low-angle faceted sneaker/dress-shoe macro + wet asphalt neon ripple).
6. **Stage 2 Alignment Grid Mode:**
   - Support a `debugAnchors={true}` prop that draws crosshairs on `eye_center_y`, `mouth_pivot`, `head_pivot`, and both shoulder corners so Role 05 can verify exact 3.2x heroic proportions.
