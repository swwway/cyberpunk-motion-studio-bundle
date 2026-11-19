# 02_CHARACTER_RIG_SPEC.md — hero, hidden bends, inserts, interlocutors, the locked face

1. **Hero:** a tall guy, ≈8.5 heads (target; now ≈6.5), long black high-collar coat, curly dark-blond hair, blue eyes; an ironic mocker, hard on everyone (owner's choice). The rig is `src/cyber/rig/` in units of height 1600 (tokens `rig_body`); the v1 700×800 bust canvas and the suit outfit are not used. Acting states: `CONFIDENT`, `LOCKED_IN`, `SARCASTIC_HAPPY`, `DEAD_SERIOUS_GRAVE`, `WHISPER_CONSPIRACY`, `BREAKTHROUGH`. `assets/refs/character_turnaround.png` (coat, turn) and `assets/refs/emotion_sheet_6x.png` (expressions) are acting references, not geometry.
2. **Locked face:** the face of `CyberWalkTest` and of `public/cyber/refs/hero_flat_gemini.jpg` — `src/cyber/data/flat_hero.json`, `hero_head.json` and the drawing in `src/cyber/flat/FlatHero.tsx`. Paths, colours, feature placement and facet count don't change. Allowed: `HeroPose` (blink, brows, iris, mouth, smirk, rim flashes) and the head's transform on the body (scale, position, turn). Anything else — the owner's approval first.
3. **Hidden bends:**
   - Never in frame: knees, elbows, the full-height step (bible §2, §8).
   - Steps → boot close-up; body → profile or waist-up, hands in coat pockets; a gesture → one hand close-up; full height → a far silhouette only (small, flat fill and rims).
   - Joints overlap with a seam facet over the joint; the coat flap trails 3–4 frames; smear frames on fast moves; legs on twos, coat on ones; key poses hold 2–3 frames.
4. **Inserts:** the hand (palm, thumb, fingers with joints, cuff) and the boot (upper, sole, heel, the roll) are separate rigs with their own facets. Never scale the full rig for a close-up: its hand and boot have 2 facets each.
5. **Interlocutors:** one shared waist-up rig + per-episode parts — silhouette, hairstyle, skin tone, clothing, props. Same language, simpler than the hero (start ≈50 facets, thinner rims). A new person every episode the viewer recognises himself in: a coffee-shop owner, a freelancer, a manager, a student.
6. **Visemes (Russian):** `REST` (closed, smirk) · `AI` (А, Я, Э — jaw drop) · `E` (Е, И, Ы, С, З) · `O` (О, У, Ю, Ё — narrow hexagon) · `M` (М, Б, П — lips pressed) · `FV` (Ф, В — teeth on the lower lip).
   - Jaw drop — one number, `jaw_drop_max_px` 5 in tokens (v1 700×800 units). In code it is a share of mouth width, `SHAPES.AI.open` 0.12 in `src/cyber/faceRig.ts`; the flat hero's small mouth reads at ×1.4 (`MOUTH_GAIN`).
   - The mouth leads the sound by 2 frames (`LIP_LEAD`); shapes hold on twos.
   - Rhubarb, if it is ever installed (not on this server; run with `-r phonetic`): A→M, B→E (clenched teeth: К, С, Т, И), C→AI, D→AI, E→O, F→O, G→FV, H→E, X→REST.
7. **Rejected (bible §8) — don't propose:** many-facet 3D models («грани в случайных местах»); the full-height step and visible knees or elbows; a demo without the character.
