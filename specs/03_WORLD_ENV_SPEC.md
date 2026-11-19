# 03_WORLD_ENV_SPEC.md — 3-Plane Worlds & Anti-Puppet Optical Playbook

1. **3 Depth Planes:** `BG (0.3x, 1.5–3px blur)` | `MG (0.7x, Mood Panels & frosted-glass HUDs)` | `FG (1.0x–1.2x, Hero, macro inserts, sparks, captions)`.
2. **3 Recurring Locations:**
   - `LOC_CYBER_SKYLINE`: Brutalist dark skyline + morphing Mood Block (`#F24C4E` / `#A8C0E0` / `#FFB84D`) + drifting sparks.
   - `LOC_ARCHITECT_TERMINAL`: Panoramic night window + diagonal rain + frosted-glass AI/revenue dashboards (default with `OUTFIT_FORMAL_SUIT`).
   - `LOC_AI_COSMOS`: Faceless Three.js/WebGL deep space (`#090B16`), 3D starfield, polygonal AI agent cores linked by `#00F0FF` streams (`CAM_SPIRAL_ORBIT`).
3. **Anti-Puppet Optical Cheats (Zero Fragile Limb Skeletons):**
   - `SMEAR_WEDGE`: 2-frame skewed polygonal motion-shadow wedge (`#1F1638` + `#00F0FF` leading edge, `opacity: 0.6 -> 0`) snapping into `#prop_hand_point_pov` or target pose + 3-frame spring settle.
   - `SHOT_SHOE_STEP`: 0.5–0.8s low-angle macro of faceted shoes hitting wet neon pavement (ripple + reflection) -> `TRANS_SHADOW_WHIP` into `BUST_UP_DIALOGUE`.
   - `WALK_AND_TALK_BOB`: Sinusoidal vertical bob (`Math.abs(Math.sin(f * freq)) * 10px`), sharp-shoulder counter-tilt (`±2.5deg`), 2-frame hair lag, 3-layer parallax glide.
4. **4-Variant Transition Grammar (Rotate by Beat — Never Spam One Transition):**
   - `TRANS_SHADOW_WHIP`, `TRANS_IMPACT_FRAME` (1–2 frame `#090B16` + `#00F0FF` flash hiding instant outfit/location swaps), `TRANS_AFTERIMAGE_ECHO` (2–3 trailing ghost silhouettes), `TRANS_SHADOW_BRIDGE` (2-frame dark shadow push into `LOC_AI_COSMOS`).
5. **Shot Archetype Pruning:** Mount ONLY the layers required for the active shot (`MACRO_SHOE_STEP`, `BUST_UP_DIALOGUE`, `EYE_LETTERBOX`, `POV_HAND_SMASH`, `COSMOS_3D_SPIRAL`).
