# Role 03: World, camera, the dive (3D cosmos — a variant)

Rules: spec 03. Palette: spec 01. Kit code goes to `src/series/kit/`.

## 1. World kit (issue #12)
- The world stands; characters move inside it (bible §4). The camera is locked, tracks the hero, or pushes slowly; it never orbits a flat set.
- Faceted parts: walls, windows, shop windows, signs, furniture, light, wet asphalt. A place is a layout of parts per depth layer — data, not a new drawing; a new place each episode should take hours.
- Seeds: `src/cyber/flat/FlatCity.tsx` (`FLAT`, `Skyline`, `Panel`, `Particles`), `src/cyber/scenes/WalkTest.tsx` (`Ground` perspective grid, `Signs`, the `Plane` wrapper).
- Every place shows a cyan source on the left and a coral one on the right (sign, window, screen): they motivate the rims.
- Pilot: a night street, the conversation on the move; the probe — the street scrolls behind the hero in profile.

## 2. Camera and parallax
- Layer shares of the camera move — tokens `parallax`: sky 0.05, far 0.15, mid 0.4, character 1.0, foreground 1.3–1.6; far layers blur 1.5–3 px.
- Profile walk: the character plane scrolls at 54 % of the hero's height per second (100STYLE speed), the other layers at their shares — otherwise the walk floats.
- Push 1.00 → 1.06–1.10 over 3–4 s; shake only on a parent camera group, never on background layers.
- Lines, HUD and CTA take the parallax shift only, never the camera scale: at `CAM_POV_CLOSE` (1.28) the HUD left the safe zone.
- Mount only the layers the shot needs.

## 3. The dive (shot 5, issue #14)
- Entry through the eye: spring punch-in on the eye (v1 `CAM_EYE_LETTERBOX`: ×2.2 with 21:9 bars in `#090B16`), the pupil turns into the four-point star, the star flashes to full frame — the symbols world. Through the temple is the alternative.
- Inside, format 2 (`src/formats/symbols/`): one saturated gradient world (pilot: purple), one object that transforms (pilot: a pile of chats folds into paper planes that scatter — `ScenePlanes.tsx`), glow and grain (`common.tsx`: `Glow`, `Sparkle`, `SPARK_PATH`, `Grain`, `Vignette`, `camTransform`), a slow non-linear push.
- On top, format 1 lime words and scheme: `src/formats/explainer/kit.tsx` (`Word`, `Line`, `seq`, styles `lime`, `fill`, `outline`, `strike`), colours in `theme.ts` (`C.lime` `#C8FF2E`).
- Exit: the star collapses back into the hero's pupil (reverse wipe) or a match cut on the eye. The star wipe is `WipeOverlay` in `SymbolsPilot.tsx` — local there: copy it into the kit, don't edit the format.
- A whistle on entry (role 04).

## 4. Transitions
Grammar — spec 03 §6. Built: `ShadowWhip`, `ImpactFrame` in `src/cyber/components/Transitions.tsx`; the star wipe in `SymbolsPilot.tsx`.

## 5. 3D cosmos — on request only
- `LOC_AI_COSMOS` (Three.js space, polygonal AI cores, `CAM_SPIRAL_ORBIT`) is a variant, not the default inside the head.
- This server has no GPU: `--gl=angle` fails («Error creating WebGL context»); the default `--gl` and `swangle` work; `angle` only on a GPU machine. Don't change `remotion.config.ts`.
- Mount `<ThreeCanvas>` only in 3D shots and only once textures and models are loaded (else the first frames of render tabs come out empty); `linear flat legacy` keeps the token colours (`src/cyber/three/`).
