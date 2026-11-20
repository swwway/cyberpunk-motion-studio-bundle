# Role 05: Motion QA

A probe or shot is done when the checks below pass, every axis scores ≥ 8 and the owner has watched the clip. Work in `out/cyber/qa/<shot>/` (not in git), commands from the repo root; `IN` is the render.

## 1. Short clips to the owner
Each probe (3 s) and each fix goes to the owner's Telegram as a file: `sendDocument` with `disable_content_type_detection=true`, ≤ 50 MB; bot and variables — `~/.claude/memory/telegram-video-as-file.md`; never `getUpdates` with that token. Caption in 1–2 lines: what it is, what changed, what wasn't checked. The owner watching the clip is the final motion check.

## 2. Joint-speed graphs — is it alive
Rigs are pure functions of the frame, so joints are exported exactly, not tracked.
1. Write `out/cyber/qa/<shot>/joints.mjs` (plain JS: a `.ts` file outside `src/` would land in `tsc` of `npm run lint`):
```js
import { walkFrame, WALK_FRAMES } from "../../../../src/cyber/rig/walk"; // ← the shot's pose function
import { forward, apply } from "../../../../src/cyber/rig/kinematics";
import { BONES, GROUND } from "../../../../src/cyber/rig/body";
// tips show what pivots can't: coat hem, fingers, head
const TIPS = { hemNear: ["flapNear", [206, 1090]], fingers: ["handNear", [184, 974]], forehead: ["head", [0, 60]] };
const out = {};
const put = (k, p, w) => (out[k] ??= []).push([w.root[0] + p[0] * w.scale, w.root[1] + (p[1] - GROUND) * w.scale]);
for (let f = 0; f < WALK_FRAMES; f++) {
  const w = walkFrame(f), m = forward(w.pose);
  for (const b of BONES) put(b.id, apply(m[b.id], b.pivot), w);
  for (const [k, [bone, pt]] of Object.entries(TIPS)) put(k, apply(m[bone], pt), w);
}
process.stdout.write(JSON.stringify({ fps: 30, joints: out }));
```
2. `npx esbuild out/cyber/qa/<shot>/joints.mjs --bundle --platform=node --format=esm --log-level=warning --outfile=out/cyber/qa/<shot>/joints.bundle.mjs && node out/cyber/qa/<shot>/joints.bundle.mjs > out/cyber/qa/<shot>/joints.json` (≈1 s; node alone can't load the `.tsx` imports).
3. `/root/.venvs/motion/bin/python -I .claude/skills/cyberpunk-motion-studio/tools/joint_speed.py out/cyber/qa/<shot>/joints.json out/cyber/qa/<shot>/speed.png pelvis chest forehead hemNear fingers --lag pelvis:hemNear chest:forehead` — a PNG plus per joint: max speed, dead holds, pops, lags.

Reading: a body part near 0 for ≥ 8 frames outside a planned hold is a dead hold (planted feet are meant to be 0); parent and child curves lying on each other — no overlap; the coat hem must trail the hip by 3–4 frames; spikes (`pops`) — pose jumps; flat plateaus — linear spacing; a part faster than ≈30 px/frame wants a smear. Starting thresholds; tune them on approved probes. Calibration — `CyberWalkTest`, which the owner called lifeless: the body is dead from frame 126 for 60+ frames, the hem trails by 7–8 frames.

In a tracked walk the speed lag `pelvis:hem` is noise (−12…+11 f on `KitProfileWalk`): the pelvis bobs at the step period, the flap swings with the thigh at the stride period. There, measure the angle lag thigh → flap by cross-correlating the two angle curves from the pose function (3–4 f), and keep `--lag` for single moves.

## 3. Onion skin — spacing, arcs, hidden bends
`ffmpeg -v error -y -i "$IN" -vf "trim=start_frame=A:end_frame=B,setpts=PTS-STARTPTS,tmix=frames=N" -update 1 -frames:v N out/cyber/qa/<shot>/onion_A.png`, N = B − A ≤ 9. An even fan is mechanical spacing; ghosts should crowd near the key poses. A knee or elbow hinge among the ghosts fails axis 1.

## 4. Contact sheet — composition, palette, safe zones only
`D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")`, then `ffmpeg -v error -y -i "$IN" -vf "fps=30/$D,scale=360:640,tile=6x5" -frames:v 1 out/cyber/qa/<shot>/sheet.png` — 30 tiles over the whole clip, one file. Never a motion verdict from it.

## 5. Safe zone and cover
`ffmpeg -v error -y -i "$IN" -vf "select='eq(n\,0)',drawbox=x=108:y=384:w=800:h=999:color=red@0.9:t=4" -frames:v 1 out/cyber/qa/<shot>/safe_0.png` — frame 0 and the frames of every line and the CTA: eyes, lines and the CTA inside the box; frame 0 reads as a cover.

## 6. Static checks
- `ffprobe`: 1080×1920, 30 fps, H.264/AAC; the render logs no errors.
- No outline in a colour other than the fill (same-colour seam strokes are fine); no `#000000` in shadow fills (the coat and the approved face's ink are black by design); no `Easing.linear` on characters or text; no cross-dissolves; no `Tone.Offline`.
- Facets: hero ≈80–100, interlocutor clearly fewer.

## 7. Scoring — 1–10 per axis, pass ≥ 8
1. Hidden joints and proportions: no knee or elbow in any frame; 7.8 heads measured; the clothes read as garments that sit on the body, the neck has form (jaw shadow, muscle, slope into the shoulders); the face identical to the approved one.
2. Motion life: §2–3 pass; the walk matches 100STYLE (cadence, bob).
3. Palette and facets: motivated cyan-left and coral-right rims, plum and navy shadows, facet budgets.
4. Safe zone and text: all inside; lines readable at the speaker; frame 0 works as a cover.
5. Shot grammar: the shot does its type's job (bible §5); the world stands, the characters move; parallax depth; cuts on action.
6. Sound sync: steps, snap and whistle within ±1 frame; silence before the barb; −14 LUFS.
7. Transitions: no cross-dissolve, no repeat in a row, the star wipe in and out of the dive.

Below 8 → fixes with file and line in `out/cyber/qa/<shot>/report.md`, back to the owning role. At most 3 rounds per shot; then stop and send the owner the clip, the graphs and the one bottleneck.
