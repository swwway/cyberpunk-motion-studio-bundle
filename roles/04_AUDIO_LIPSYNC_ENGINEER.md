# Role 04: Sound — line timing, action track, future voice

Episode assembly and the final mix are Showrunner's (bible §6–7). MultStudio gives every probe its own cues — the owner judges motion with sound — and hands the cue frames over with the shot.

## 1. Pilot — no voice
- Lines are text at the speaker in format-1 kinetics, timed for the future voice (role 01).
- The action track (bible §1): a hit on the snap, a whistle on the dive, silence before the barb, steps on contacts. No foreign songs in the render; the owner adds Instagram music when publishing.
- Cue frames come from the data (contact frames, the snap frame), not by ear; ±1 frame.
- Silence before the barb: music hard-muted for at least `whiplash_music_mute_ms` (140 ms), the barb lands inside it; a 55 Hz hit may mark the turn (`synth_score.py` does both).

## 2. Tools
- Python DSP in `/root/.venvs/audio` (never `Tone.Offline` in Node): `scripts/cyber/audio/walk_sfx.py` (steps on contact frames + city hum; its contact frames copy `walk.ts` — update them with the shot), `synth_score.py` (120 BPM synth, the mute and the 55 Hz hit), `scripts/formats/make_symbols_score.py` (pad, shimmer, a whoosh on every star wipe). CC0 packs: `public/sfx/kenney-*`.
- Loudness after the render: −14 LUFS, −1 dBTP (`ffmpeg loudnorm`).

## 3. Future voice
- Where: credits of the Higgsfield web account (`text2speech_v2`, ElevenLabs variant) or `ELEVENLABS_API_KEY`. Now: 0 credits, no key. Money — owner's yes. Fish Audio is paid and untested.
- Closed: Piper («very bad»); non-commercial licences — F5-TTS, XTTS-v2, Silero, Piper ruslan; Gemini TTS (server region); the Higgsfield API has no voice.
- One generation per line with its emotion tag; trim silence over 120 ms; apply `beat_relative_gain_db`; normalise the assembled dialogue once to −14 LUFS — never per chunk; duck music −12 dB under speech.
- Word stamps: whisper.cpp medium, ru — `npm run subs -- public/<dir or file>` (`sub.mjs`, `whisper-config.mjs`) writes word-level JSON next to each video file (.mp4/.mov/.webm/.mkv; wrap a .wav into .mp4 first; no argument = all of `public/`). Run it in `/root/projects/Remotion`: `whisper.cpp/` with the 1.5 GB model is not in git, and in the worktree the script would install it again. No rhubarb or WhisperX on the server.
- Visemes from the words: spec 02 §6; the mouth leads the sound by 2 frames.
