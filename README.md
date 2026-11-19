# Faceted Neo-Cyberpunk Motion Studio Bundle

Production-ready Claude Code skill & multi-role animation studio bundle for 9:16 vertical Russian-language Instagram Reels (`1080x1920`, `30 fps`) built in **100% pure code** (`Remotion` + `@remotion/three` + `FFmpeg` + Python DSP + Russian neural TTS/lip-sync).

## Repository Structure

```text
.
├── SKILL.md                           # Master Orchestrator & 4-Stage Execution Protocol
├── MOTION_STUDIO_STATE.template.md    # Zero-Drag session state anchor template
├── assets/
│   └── refs/
│       ├── character_turnaround.png   # Heroic proportions (3.2x sharp shoulders, Jacket + Suit + Close-Up)
│       └── emotion_sheet_6x.png       # 6-emotion expression reference grid
├── specs/
│   ├── tokens.json                    # Machine-readable SSOT (HEX, safe zones, springs, rig anchors, audio mix)
│   ├── 01_ART_STYLE_BIBLE.md          # Lineless faceted Neo-Cyberpunk style & motion laws
│   ├── 02_CHARACTER_RIG_SPEC.md       # Heroic SVG rig (700x800), 2 outfits, 6 Russian visemes
│   └── 03_WORLD_ENV_SPEC.md           # 3-plane worlds & Anti-Puppet optical cheats
└── roles/
    ├── 01_DIRECTOR_BEAT_PLANNER.md    # Emotional beat grid & transition rotation (High)
    ├── 02_SVG_RIG_ENGINEER.md         # HeroRig, MouthPhonemes, SmearWedge, ShotShoeStep (High)
    ├── 03_CAMERA_WORLD_3D.md          # Parallax, Cosmos3D spiral camera, captions, CTA slot (Med/High)
    ├── 04_AUDIO_LIPSYNC_ENGINEER.md   # Chunked emotional Russian TTS, Rhubarb/WhisperX, Python synth (Med)
    └── 05_QA_CRITIQUE_AGENT.md        # FFmpeg contact sheets, safe-zone check, 7-axis >=8/10 rubric (High)
```

## Quick Install into Claude Code

Clone directly into your project's `.claude/skills/` directory:

```bash
git clone https://github.com/swwway/cyberpunk-motion-studio-bundle.git .claude/skills/cyberpunk-motion-studio
```

Then copy the reference images into your working Remotion project (or keep them linked from the skill path) and start Stage 1 in Claude Code:

```text
Activate skill cyberpunk-motion-studio. Read SKILL.md, specs/tokens.json, and assets/refs/*, then execute Stage 1 (3s Style & Motion Demo) and run Role 05 QA.
```

## Core Engineering Guardrails
- **Strictly Lineless Faceted SVG (`stroke="none"`)** — zero `#000000` shadows (plum-indigo `#1F1638` core + `#00F0FF` / `#FF6B5B` rim lights).
- **Heroic Proportions (`viewBox="0 0 700 800"`)** — proportionally smaller head over broad razor-sharp angular shoulders (`3.2x` width ratio).
- **Anti-Puppet Optical Cheats** — `SMEAR_WEDGE`, `SHOT_SHOE_STEP`, and 4 rotating transitions (`SHADOW_WHIP`, `IMPACT_FRAME`, `AFTERIMAGE_ECHO`, `SHADOW_BRIDGE`).
- **Russian Lip-Sync & Emotional Swings** — `rhubarb -r phonetic` or `WhisperX --language ru` + per-beat gain offsets (`whisper: -6dB` vs `energetic: +2dB`) before master `-14 LUFS` normalization + 140ms hard music mute on `DEAD_SERIOUS_GRAVE` snaps.
