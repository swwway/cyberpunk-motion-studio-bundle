# Role 03: Camera, 3-Plane Worlds & Three.js Engineer (Medium/High Reasoning)

## Exclusive File Ownership
- `remotion.config.ts`
- `src/components/CameraRig.tsx`
- `src/components/Cosmos3D.tsx`
- `src/components/Transitions.tsx`
- `src/components/KineticCaptions.tsx`
- `src/components/CtaOverlaySlot.tsx`
- `src/scenes/*`

## Responsibilities
1. **Headless WebGL Stability (`remotion.config.ts`):**
   - Configure `Config.setChromiumOpenGlRenderer('angle')` (with `'swiftshader'` fallback for headless Linux/CI).
   - **Strict Mounting Rule:** Only mount `<ThreeCanvas>` during `COSMOS_3D_SPIRAL` (`LOC_AI_COSMOS`) shots. Unmount completely on pure 2D SVG shots to guarantee fast renders and zero WebGL context loss.
2. **3-Plane Parallax Architecture:**
   - Every scene separates `BG (0.3x, filter: blur(2px))`, `MG (0.7x, MoodPanel + FrostedGlassHUD)`, and `FG (1.0x–1.2x, HeroRig + sparks + captions)`.
   - Maintain continuous subtle camera drift (`0.5%–1.5%` scale/translate push) on >65% of dialogue frames.
3. **Signature Camera Moves (`CameraRig.tsx`):**
   - `CAM_SPIRAL_ORBIT`: Parametric 3D spiral curve in `Cosmos3D.tsx` orbiting glowing polygonal AI cores (`#00F0FF`) before whipping into the protagonist.
   - `CAM_EYE_LETTERBOX`: Spring punch-in (`scale: 2.2x`, centered on `eye_center_y: 235`) while top/bottom `#090B16` `clip-path` bars narrow frame to 21:9.
   - `CAM_FOURTH_WALL`: Hero scales `1.0 -> 1.35` with Z-tilt and drop shadow cast *over* MG HUD cards.
   - `CAM_POV_CLOSE`: `scale: 1.28` intimate framing with subtle vignette for `[whisper]` beats.
4. **4-Variant Transition Primitives (`Transitions.tsx`):**
   - Implement `TRANS_SHADOW_WHIP`, `TRANS_IMPACT_FRAME` (1–2 frames `#090B16` + `#00F0FF`), `TRANS_AFTERIMAGE_ECHO` (2–3 trailing ghost silhouettes), and `TRANS_SHADOW_BRIDGE`. Zero cross-dissolves.
5. **Russian Kinetic Captions & Safe-Zone Lock:**
   - Render `Unbounded` (800/900) 1–3 words per beat inside `X: 108–907px`, `Y: 384–1382px`.
   - `slide-up + clip-path` reveal synced to word-level timestamps; highlight active word in `#00F0FF` or `#FFB84D`.
