---
name: cyberpunk-motion-studio
description: Production-grade 2D/2.5D Faceted Neo-Cyberpunk animation & motion-graphics studio skill for Claude Code (Remotion + Three.js + FFmpeg). Strictly scoped to animation craft, SVG rigging, 3D camera, lip-sync, audio synthesis, and visual QA.
---

# Faceted Neo-Cyberpunk Motion Studio — Master Orchestrator (`SKILL.md`)

## 1. Scope & Boundary Contract
- **Your Mission:** Execute Netflix-tier 9:16 (`1080x1920`, `30 fps`) vertical cartoon motion graphics in **100% pure code** (`Remotion` + `@remotion/three` + `FFmpeg` + Russian neural TTS/alignment).
- **Strict Separation of Concerns:** You own **animation, rigging, camera choreography, optical transitions, audio/music sync, and technical QA**. Do NOT invent marketing angles or Telegram funnel copy from scratch—consume script/CTA payloads from local HQ/Shtat workspace skills or user input and inject CTA text cleanly into `<CtaOverlaySlot />`.

## 2. Mandatory Session Boot Sequence (Parallel READs)
Before writing any code, run a parallel read of:
1. `MOTION_STUDIO_STATE.md` (if present in project root) to restore active stage and locked paths.
2. `.claude/skills/` and workspace `CLAUDE.md` to ingest active HQ/Shtat scripts or CTA payloads.
3. `specs/tokens.json` (single source of truth for HEX codes, springs, safe zones, heroic rig anchors).
4. `assets/refs/character_turnaround.png` and `assets/refs/emotion_sheet_6x.png` (multimodal visual ground truth—NEVER invent character geometry without inspecting these references).

## 3. Modular Role Architecture & Strict File Ownership
Never collapse all responsibilities into one chaotic pass. Load the specific role manual from `roles/` for each task and enforce **exclusive file ownership** when delegating to sub-agents:

| Role Manual | Reasoning Effort | Exclusive File Ownership | Primary Deliverable |
| :--- | :--- | :--- | :--- |
| `roles/01_DIRECTOR_BEAT_PLANNER.md` | **High** | `data/beat_sheet.json`, `MOTION_STUDIO_STATE.md` | Frame-timed beat grid, emotional swings, shot pruning, transition rotation |
| `roles/02_SVG_RIG_ENGINEER.md` | **High** | `src/components/HeroRig.tsx`, `src/components/MouthPhonemes.tsx`, `src/components/OpticalCheats.tsx` | Lineless faceted SVG rig (3.2x heroic shoulders, smaller head), 2 outfits, 6 emotions, 6 Russian visemes, smear wedges |
| `roles/03_CAMERA_WORLD_3D.md` | **Medium/High** | `src/scenes/*`, `src/components/CameraRig.tsx`, `src/components/Cosmos3D.tsx`, `remotion.config.ts` | 3-plane parallax, 3 locations, Three.js spiral camera, 4 transitions, captions |
| `roles/04_AUDIO_LIPSYNC_ENGINEER.md` | **Medium** | `scripts/audio/*`, `public/audio/*`, `data/phonemes.json`, `data/beats.json` | Chunked emotional Russian TTS, `rhubarb -r phonetic` / WhisperX alignment, offline Python/Chromium synth + SFX |
| `roles/05_QA_CRITIQUE_AGENT.md` | **High** | `qa/*` (read-only on `src/`, outputs scored critique reports) | `ffmpeg` contact sheets, safe-zone overlay check, 7-axis 1–10 scoring (pass >= 8/10, max 3 retries) |

## 4. 4-Stage Incremental Execution Protocol
Never jump straight to rendering a 60-second Reel before verifying prior stages:
- **Stage 1 — 3s Style & Motion Demo (90 frames):** Scaffold Remotion + `@remotion/three`, configure headless WebGL (`remotion.config.ts`), build `tokens.ts` + `MoodPanel.tsx` + Russian `KineticCaptions.tsx`. Pass Stage 1 QA.
- **Stage 2 — Character Rig & Lip-Sync Test (120 frames):** Inspect reference sheets -> build `HeroRig.tsx` (`viewBox="0 0 700 800"`, 3.2x sharp shoulders, smaller head, `OUTFIT_TECHWEAR_JACKET` + `OUTFIT_FORMAL_SUIT`, 6 emotions, 6 Russian visemes, `#prop_hand_point_pov` + `SMEAR_WEDGE`) -> render rig alignment grid + `SARCASTIC_HAPPY -> DEAD_SERIOUS_GRAVE` whip-lash test. Pass Stage 2 QA.
- **Stage 3 — World, Cosmos & Optical Transitions Assembly (180 frames):** Build `LOC_CYBER_SKYLINE`, `LOC_ARCHITECT_TERMINAL`, `LOC_AI_COSMOS`, `SHOT_SHOE_STEP`, and all 4 transitions (`TRANS_SHADOW_WHIP`, `TRANS_IMPACT_FRAME`, `TRANS_AFTERIMAGE_ECHO`, `TRANS_SHADOW_BRIDGE`). Pass Stage 3 QA.
- **Stage 4 — Full Funnel Reel Production:** Ingest script + emotional voice chunks + `phonemes.json` + `beats.json` + CTA slot -> assemble root composition -> render draft 50% preview -> pass Critique Loop (>= 8/10) -> export final `1080x1920` H.264/AAC MP4.

## 5. Context Economy & Non-Negotiable Engineering Bans
- **Parallel READs, Sequential WRITEs:** Batch all file reads and `ffprobe` calls; perform writes and renders sequentially.
- **BAN `Tone.Offline` in plain Node.js:** Synthesize offline audio/SFX via Python (`numpy`/`scipy`/`soundfile`) or headless Chromium WebAudio.
- **BAN `rhubarb` default PocketSphinx on Russian:** Always run `rhubarb -r phonetic` or `WhisperX` (`ru`).
- **BAN per-chunk `-14 LUFS` normalization:** Normalize the assembled master dialogue track to `-14 LUFS` while preserving per-beat emotional gain offsets (`whisper: -6dB` vs `energetic: +2dB`).
- **BAN `#000000` shadows, `stroke` outlines on character, `Easing.linear` on character/UI, and cross-dissolves.**
