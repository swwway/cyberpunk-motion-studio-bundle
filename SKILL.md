---
name: cyberpunk-motion-studio
description: "MultStudio's craft for the faceless animated series in Remotion (9:16, 30 fps, flat faceted style): hero rig and waist-up shots, hand and boot inserts, interlocutor kit, world kit, the dive into the hero's head, the 8 shot types, storyboards, motion QA. Triggers: «раскадровка», «риг», «пропорции», «кисть крупно», «ботинок», «собеседник», «место серии», «нырок», «проверь движение», «план N». Scripts, episode assembly and the final mix are Showrunner's."
---

# Cyberpunk Motion Studio 2.0

Source of truth — the series bible, Remotion `docs/series/bibliya-formata.md`. This skill adds numbers, paths, tools and checks. If they disagree, the bible wins: send the fix to the orchestrator `content`, don't edit the bible.

## Format (bible §1, §5)
- ≈30 s, 1080×1920, 30 fps, Russian: a person with a manual routine → dive into the hero's head → one-gesture solution → reaction → CTA «ссылка в профиле».
- New interlocutor and new place every episode, both from kits. No voice yet: lines are text at the speaker (hero ≤ 6 words), own sound track.
- 8 shot types: 1 boots · 2 profile walk · 3 two waist-up · 4 hand · 5 dive · 6 reaction · 7 far silhouette · 8 CTA. Each is a 3 s probe the owner approves once, then reused.

## Pipeline
script (Showrunner + owner) → storyboard (MultStudio + `mult-director`) → animatic (Showrunner, owner approves the rhythm) → library shots (MultStudio) → assembly and sound (Showrunner) → owner's Telegram as a file → publish on the owner's yes. Tasks: issues labelled `сессия:MultStudio` (`hq/runbooks/tasks.md`), report as a comment.

## Hard rules
1. Knees and elbows never in frame, no full-height step («ужасно, безжизненно»). Steps — boot close-up; body — profile or waist-up, hands in pockets; gesture — one hand close-up; full height — only a far silhouette.
2. The face is approved: paths, colours, features stay; acting only through `HeroPose` (spec 02).
3. 7.8 heads (owner 20.11; 8.5 was rejected): `HEAD_SCALE` 0.316, the turtleneck refits with the head (`fitCollar`), arms −9 %, shoulder width stays. Measure on a render.
3b. Clothes (owner 20.11, coat rejected twice): outfit C — short sand work jacket, corduroy collar, milky tee, light wide jeans, chunky sneakers, no logos (`src/cyber/rig/outfits.ts`, refs `docs/series/refs/odezhda.md`). The neck is the rig's, not the head art's: the art is cut at the jaw (`JAW_CUT`), `NECK_PARTS` add throat, sternocleidomastoid, jaw shadow and the slope into the trapezius; collars wrap the neck and lie on the shoulders («одежда как будто примонтирована к голове» — never again). Every facet names its piece of the cut; hero ≤ 100 facets.
4. No dead bends: joints overlap under a seam facet; loose cloth (the tee hem on `flapNear`) trails 3–4 frames; smears on fast moves; legs on twos, cloth on ones; key poses hold 2–3 frames.
5. Close-ups are separate inserts with many facets (hand with fingers, boot with sole and roll). Never scale the full rig: its hand and boot have 2 facets each.
6. Motion comes from data (below), not invented sine waves.
7. Judge motion by clips, joint-speed graphs and onion skins, never by contact sheets (role 05).
8. Don't bring back bible §8: many-facet 3D, Piper and non-commercial voices, the full-height step, foreign songs, the «Неоновый оператор» gags.

## Roles
| Task | File |
|---|---|
| storyboard, 30 s template, shot types (animatic — Showrunner) | `roles/01_DIRECTOR_BEAT_PLANNER.md` |
| rig, proportions, inserts, interlocutor kit, motion data | `roles/02_SVG_RIG_ENGINEER.md` |
| world kit, parallax, the dive, transitions, 3D variant | `roles/03_CAMERA_WORLD_3D.md` |
| line timing, probe sound, future voice (mix — Showrunner) | `roles/04_AUDIO_LIPSYNC_ENGINEER.md` |
| motion QA, clips to the owner, scoring | `roles/05_QA_CRITIQUE_AGENT.md` |

Rules: `specs/01` style, `02` rig, `03` world. Numbers: `specs/tokens.json` — code imports it (`src/cyber/tokens.ts`): add keys, never rename or remove. Fresh eye on a board or render — agent `mult-director` (Fable). It is registered only in sessions started in the Remotion repo or worktree; elsewhere spawn a general-purpose agent with `model: fable` told to read `.claude/agents/mult-director.md` and act as it.

## Motion sources (bible §3)
| Source | Terms |
|---|---|
| 100STYLE `HandsInPockets_FW`, `data/motion/100style/`, numbers — tokens `motion.walk_100style`: the walk of shot 2 | CC BY 4.0, caption line «Движение: 100STYLE Dataset — Ian Mason (CC BY 4.0)»; owner against it → CMU |
| CMU Mocap DB, BVH into `data/motion/cmu/`: ordinary body moves | free for all uses, no credit, don't resell the data |
| Higgsfield clips → MediaPipe curves, `/root/projects/Remotion/out/motion-ref/` + README: face, snap, reaction, steps, coat | new clips cost money — owner's yes |
| Mixamo | NOT VERIFIED (403) — don't use |

Commands and retargeting — roles/02 §6.

## Paths and traps
- v1 `src/components`, `src/scenes`, `data/` live in `src/cyber/`; new parts — `src/series/kit/`; QA — `out/cyber/qa/` (not in git); state — `MOTION_STUDIO_STATE.md` in the repo root, from the template here.
- Worktree `/root/projects/Remotion-mult`, branch `mult`, its own `npm ci`; push `mult:main` only when 0 behind. Renders and QA go to the worktree's own `out/` (git-ignored): `joints.mjs` imports `src/` relatively, so in main's `out/` it would measure main's rig, not yours. Read-only by absolute path in `/root/projects/Remotion`: `out/motion-ref/`, `whisper.cpp/`. Never write to `/root/projects/Remotion` — that checkout is Showrunner's.
- `src/Root.tsx` is shared with Showrunner: one registry file under `src/series/kit/`, imported into Root once.
- Money, credits, messages to people — only on the owner's yes in this session's window; a relayed yes doesn't count.
