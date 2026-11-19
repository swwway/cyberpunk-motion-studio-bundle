# Role 04: Emotional Audio, Lip-Sync & Procedural Synth Engineer (Medium Reasoning)

## Exclusive File Ownership
- `scripts/audio/*`
- `public/audio/*`
- `data/phonemes.json`
- `data/beats.json`
- Updates exact `start_frame`/`end_frame` in `data/beat_sheet.json` after audio synthesis.

## Responsibilities
1. **Chunked Emotional Russian Voiceover (Zero Flat TTS):**
   - NEVER synthesize an entire Reel in one flat TTS call.
   - Iterate through `data/beat_sheet.json` and generate each beat via **Fish Audio S2.1 Pro MCP**, **ElevenLabs**, or local **F5-TTS/XTTS-v2** using each beat's `voice_tag` (`[whisper]`, `[energetic]`, `[sarcastic/chuckle]`, `[dead serious/grave]`).
   - Trim dead silence (`> 120ms` leading/trailing) via `ffmpeg silenceremove` to preserve punchy Reels pacing (~3.8 words/sec).
2. **Russian Lip-Sync Alignment (Fixing the Rhubarb English Trap):**
   - **Option A (Fast & Local):** Run `rhubarb -r phonetic -f json beat.wav -o beat_rhubarb.json` (MANDATORY `-r phonetic` flag so PocketSphinx English bias is bypassed) and map Rhubarb shapes (`A->M`, `B/C/D->AI`, `E/F->O`, `G->FV`, `H->E`, `X->REST`).
   - **Option B (Highest Russian Precision):** Run `WhisperX` (`--language ru`) for word/char timestamps and map Cyrillic vowels/consonants directly to `REST | AI | E | O | M | FV`.
   - Export unified frame-indexed `data/phonemes.json` (`{ "frame": 42, "viseme": "AI", "word": "агент" }`).
3. **Pure-Code Cyberpunk Music & Procedural SFX (Fixing the Node `Tone.Offline` Trap):**
   - **NEVER run `Tone.Offline` inside plain Node.js** (crashes without browser `OfflineAudioContext`).
   - Synthesize 120 BPM cyberpunk synth basslines, arpeggios, sub-bass booms, whip-pan whooshes, and UI clicks using a **deterministic Python DSP script** (`scripts/audio/synth_score.py` using `numpy` + `scipy` + `soundfile`) OR a Playwright headless-Chromium WebAudio script.
   - Export `data/beats.json` with exact frame indices of every kick/snare/bar transition.
4. **Dynamic Master Mixing (Preserving Emotional Swings):**
   - Apply relative per-beat gain offsets from `tokens.json` (`WHISPER_CONSPIRACY: -6dB`, `CONFIDENT: 0dB`, `BREAKTHROUGH: +2dB`) BEFORE assembling `dialogue_master.wav`.
   - Normalize the **assembled** `dialogue_master.wav` as a whole to `-14 LUFS` (`true peak -1 dBTP`) via `ffmpeg loudnorm`.
   - Duck music `-12 dB` under speech, and **hard-mute music (`volume=0`) for 140ms + drop a 55Hz sub-bass hit** on every `SARCASTIC_HAPPY -> DEAD_SERIOUS_GRAVE` transition.
