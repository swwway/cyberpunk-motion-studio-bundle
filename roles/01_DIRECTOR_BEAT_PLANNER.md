# Role 01: Director & Beat Planner (High Reasoning)

## Exclusive File Ownership
- `data/beat_sheet.json`
- `MOTION_STUDIO_STATE.md`

## Responsibilities
1. **Script Ingestion:** Read the Russian script and CTA payload provided by the user or workspace HQ/Shtat skills. Never rewrite the core marketing hook or CTA promise.
2. **Emotional Rollercoaster Segmentation:** Split the script into 1–2 sentence **Emotional Beats** (`1.5s–4.5s` each). Deliberately schedule contrast swings:
   - Never keep 2 consecutive beats at the same vocal energy or camera scale.
   - Schedule at least one **Whip-lash Contrast** (`SARCASTIC_HAPPY -> DEAD_SERIOUS_GRAVE`) per 30–45s Reel.
3. **Shot Archetype Pruning & Transition Rotation:**
   - Assign each beat an explicit `shot_archetype` (`MACRO_SHOE_STEP`, `BUST_UP_DIALOGUE`, `EYE_LETTERBOX`, `POV_HAND_SMASH`, `COSMOS_3D_SPIRAL`), `location_id`, `outfit_mode`, `mood_color`, and `camera_move`.
   - Enforce **Transition Variety:** Never use the same transition type twice in a row. Use `TRANS_IMPACT_FRAME` whenever `outfit_mode` switches (`JACKET <-> SUIT`).
4. **Output Contract (`data/beat_sheet.json`):**
   Every beat object MUST contain:
   ```json
   {
     "beat_id": "B01",
     "text_ru": "...",
     "voice_tag": "[whisper]",
     "relative_gain_db": -6.0,
     "emotion_state": "WHISPER_CONSPIRACY",
     "outfit_mode": "OUTFIT_TECHWEAR_JACKET",
     "location_id": "LOC_CYBER_SKYLINE",
     "mood_color": "#F24C4E",
     "shot_archetype": "BUST_UP_DIALOGUE",
     "camera_move": "CAM_POV_CLOSE",
     "transition_in": "TRANS_SHADOW_WHIP",
     "sfx_cues": ["sub_hit", "whoosh_low"],
     "start_frame": 0,
     "end_frame": 90
   }
   ```
   *(Initial `start_frame`/`end_frame` are estimates; Role 04 updates exact frame boundaries after audio generation.)*
