# Role 02: Rig — waist-up hero, inserts, interlocutor kit

Rules: spec 02. Numbers: tokens.json (`rig_body`, `stepping`, `motion`). New code goes to `src/series/kit/`; take pieces from `src/cyber/` instead of rewriting them.

## 1. What exists
- `src/cyber/rig/body.ts` — bones and facets in character units: height 1600, sole at y 1600, x 0 = pelvis axis; 3/4 view facing left (his far side is on the left). `NECK [0, 231]`, `HEAD_SCALE 0.38`, `FOOT` heel and toe for the roll.
- `kinematics.ts` — FK `forward(pose)`, two-bone leg IK `legIK`, SVG matrices. `walk.ts` — the full-height walk and stop as a pure function of the frame: shot 7 only; its heel→toe roll (`ankleAbout`) serves the boot insert. Its 17-frame step was a guess; 100STYLE measured 20.
- `HeroBody.tsx` — parts by z, a same-colour 0.8 px stroke closes anti-alias seams; the head is `FlatHeroArt` in `head` mode.
- Face: `src/cyber/flat/FlatHero.tsx` + `src/cyber/data/flat_hero.json` (49 paths, 768×1376) + `hero_head.json` (crop, pivot, `exclude`; from `scripts/cyber/hero_parts.py`). Locked — spec 02.
- Facets: 81 (body 40, head 41) of the ≈80–100 budget; none of the rest goes to the face.

## 2. Proportions (issue #8)
- `HEAD_SCALE` 0.38 → ≈0.295 for ≈8.5 heads; arms −8–10 % along the bone (upper arm, forearm, hand pivots and facets); shoulder width unchanged (≈1.9 heads after the change).
- Then refit for the new head: `NECK`, the collar and the upper chest — the `chest` polygon from `[-80, 276]` to `[62, 272]` and its collar facets were traced to the reference collar at 0.38. The head mask runs `EXT` = 40 art px below the collar line (`hero_parts.py`): 15 units at 0.38, ≈12 at 0.295; the rig collar must still cover it at every head turn.
- The numbers are Proko/Loomis, unchecked: draw a debug overlay (crown, chin, shoulder line, sole), measure in px, send a before/after sheet.

## 3. Waist-up hero (shots 2, 3, 8)
- Same skeleton, frame cut at the waist, legs out. Hands in coat pockets: the sleeve reads as one shape from shoulder to pocket; any bend lives under a fold facet that overlaps both segments.
- Profile walk: body motion from the 100STYLE curves (§6), the world scrolls behind (role 03 §2). In profile the bob, head pitch and shoulder rise read; sway and roll read only in 3/4 or front.
- Holds are moving holds: breath every 105–135 frames (`walk.ts`: 120, chest ×1.006), the coat answers every stop late.
- Over mocap (`src/series/kit/hero/sideWalk.ts`, shot 2): a hard 2-frame hold at contacts makes pops when it releases — ease the body time inside each step instead (speed 50 % at the contact, 150 % mid-step; 30 % was a snap). Chest trails the pelvis 2 f, head 3 f. Hands in pockets: put the wrist on the shoulder → pocket ray at the fixed reach of an 8° elbow, so the bend never breathes and the slack goes into pocket depth under the clip; drop the drawn rim strips of the sleeve, or the chest edge shows behind the forearm as a second coral line.
- Acting: `HeroPose` — `blink`, `browL/browR`, `iris`, `mouth`, `smirk`, `rimCyan/rimCoral`. Blink every 75–120 frames plus a forced one on each emotion switch, starting on even frames (`blinkAt` in `src/cyber/faceRig.ts`).

## 4. Inserts (issue #11) — separate rigs, own facets
- Hand: palm, thumb and fingers with their own joints, the cuff over the wrist. The snap follows the MediaPipe hand curves; a smear on the slide, the hit on the slide frame, the end pose held 2–3 frames.
- Boot: upper, sole, heel, a seam or lace; heel strike → flat → toe-off with the sole flexing at the ball. Steps on twos; the wet-asphalt reflection and ripple (world kit) on ones.
- Facets are free here: detail until the insert holds a full frame.

## 5. Interlocutor kit (issue #13)
- One shared waist-up rig (the hero's bones and pose functions) + per-episode parts: silhouette (shoulder and torso widths, height), hairstyle, skin tone, clothing, props (phone).
- Simpler than the hero: start at ≈50 facets, the same two rims but thinner; the hero stays the most detailed figure in frame.
- Face: blink, brows, wide eyes, jaw, mouth (visemes for the future voice); reactions (shot 6) from MediaPipe blendshapes.
- First one: a tired person with a phone.
- Option, not a rule: a flat reference image can be vectorised with vtracer (recipe — `scripts/cyber/flat_hero.py`, `prep_refs.py`) and cut down to the budget. Generating the reference costs credits — owner's yes.

## 6. Motion data → rig
- **100STYLE:** `data/motion/100style/HandsInPockets_FW_gait.json` → `perframe` (60 fps, detrended, 3.47 s): `root_height_pct`, `lateral_pct`, `head_pitch_deg`, `head_roll_deg`, `shoulder_roll_deg`. Take every second sample for 30 fps, loop on whole strides (40 frames), scale % by the hero's height in px. Keep the asymmetry — it is what reads as alive.
- **New BVH (CMU):** `/root/.venvs/motion/bin/python -I scripts/series/bvh_analyze.py <in.bvh> <out.json>` (≈1 s). It expects 100STYLE joint names (`Head`, `LeftShoulder`, `RightShoulder`, `LeftAnkle`, `RightAnkle`, `LeftToe`): rename CMU joints (`LeftFoot`, `LeftToeBase`…) first.
- **Video curves:** `/root/projects/Remotion/out/motion-ref/README.md` lists clips, curve files, scripts and model paths — use those. New analysis: venv `/root/.venvs/motion` (mediapipe 1.2.3, OpenCV, matplotlib), Tasks API only — `mediapipe.tasks.python.vision` `PoseLandmarker`, `HandLandmarker`, `FaceLandmarker`; `BaseOptions(model_asset_path=…, delegate=BaseOptions.Delegate.CPU)`; `RunningMode.VIDEO` + `detect_for_video(image, timestamp_ms)` with rising timestamps. Pose 33 points, hand 21, face 478 + 52 blendshapes. CPU: pose 22–25 fps, face 39–42 fps. Needs the system `libegl1`.
- **Retarget:** 2D angles from landmark triplets (e.g. wrist–knuckle–tip per finger), light smoothing that keeps accents, resample to 30 fps, then quantise the stepped parts to twos and hold key poses 2–3 frames. Blendshapes → controls: `eyeBlink*` → blink, `browInnerUp`/`browOuterUp*` → brows, `jawOpen` → mouth open, `mouthSmile*` → smirk, `eyeWide*` → wide eyes.

## 7. Mouth (future voice)
Viseme map and jaw — spec 02 §6; `visemeAt` with `LIP_LEAD` 2 frames in `faceRig.ts`; the flat hero's small mouth reads at ×1.4 (`MOUTH_GAIN` in `src/cyber/flat/FlatTest.tsx`). Default without a voice: the speaker's mouth moves on its line, visemes from the text at 3.8 words/s, so the real voice only re-times it — confirm with the owner on the first shot-3 probe.
