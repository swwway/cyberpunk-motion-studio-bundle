# Cyberpunk Motion Studio Bundle — v2.0

Claude Code skill `cyberpunk-motion-studio` and agent `mult-director` for a faceless animated series: Russian-language 9:16 reels (`1080x1920`, `30 fps`) made in code with Remotion, Python and FFmpeg. The MultStudio session uses it in the Remotion repository, where the series bible `docs/series/bibliya-formata.md` is the source of truth.

**2.0 (19.11.2026):** rebuilt for the series format — a person with a routine → a dive into the hero's head → a one-gesture solution → CTA, ≈30 s — and its 8 shot types.

## Structure

```text
.
├── SKILL.md                           # router: format, pipeline, hard rules, motion sources, paths
├── MOTION_STUDIO_STATE.template.md    # MultStudio state: shot library, rig, kits, last QA
├── agents/
│   └── mult-director.md               # Fable director: storyboards, staging, fresh-eye review
├── tools/
│   └── joint_speed.py                 # joint-speed graph: dead holds, pops, lags (role 05)
├── assets/refs/                       # v1 turnaround and emotion sheet — acting references
├── specs/
│   ├── tokens.json                    # numbers; imported by Remotion src/cyber/tokens.ts
│   ├── 01_ART_STYLE_BIBLE.md          # palette, facets, safe zone, motion craft, render
│   ├── 02_CHARACTER_RIG_SPEC.md       # hero, hidden bends, inserts, interlocutors, locked face, visemes
│   └── 03_WORLD_ENV_SPEC.md           # kit worlds, parallax, the dive, transitions
└── roles/
    ├── 01_DIRECTOR_BEAT_PLANNER.md    # storyboard and animatic, 30 s template, 8 shot types
    ├── 02_SVG_RIG_ENGINEER.md         # waist-up hero, proportions, inserts, interlocutor kit, motion data
    ├── 03_CAMERA_WORLD_3D.md          # world kit, parallax, the dive, 3D variant
    ├── 04_AUDIO_LIPSYNC_ENGINEER.md   # line timing, action track, future voice, word stamps
    └── 05_QA_CRITIQUE_AGENT.md        # clips, joint-speed graphs, onion skin, sheet, safe zone, scoring
```

## Install and sync

This repository is the source; Remotion keeps a copy. Change it here, then copy into MultStudio's worktree (the main checkout `/root/projects/Remotion` is Showrunner's) and push `mult:main`:

```bash
rsync -a --delete --exclude .git --exclude .gitignore --exclude ВХОДЯЩИЕ.md ./ /root/projects/Remotion-mult/.claude/skills/cyberpunk-motion-studio/
cp agents/mult-director.md /root/projects/Remotion-mult/.claude/agents/mult-director.md
```

`specs/tokens.json` is imported by Remotion code: add keys, never rename or remove them.

## From v1 to v2

- **Kept:** palette, safe zone, transitions without cross-dissolves, viseme map, 7-axis scoring (rebuilt around motion), springs, audio-mix numbers for the future voice.
- **New:** 8 shot types and the 30 s template; waist-up rig, hand and boot inserts, interlocutor kit, world kit; motion sources (100STYLE, CMU, MediaPipe); motion QA by clips, joint-speed graphs and onion skins; agent `mult-director`.
- **Removed:** the full-height walk as a shot (only a far silhouette), the 3D cosmos as the default (now a variant), Piper and non-commercial voices, the 4-stage protocol, the 700×800 bust rig and the suit outfit, rhubarb and WhisperX as aligners.
