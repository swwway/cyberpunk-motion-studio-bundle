# Role 01: Director — storyboard & animatic

The rhythm is fixed before anything moves. Input: the approved script, `docs/series/scripts/<ep>.md` (Showrunner with the owner). Output: the storyboard. The animatic — stills held for their durations, lines, rough sound — is Showrunner's composition in `src/series/episodes/`; MultStudio supplies stills of library shots, grey silhouettes stand in for parts not built yet. Draft and stress-test the board with the agent `mult-director`.

## 30 s template → default shots
| s | Beat (bible §1) | Default shots |
|---|---|---|
| 0–3 | hook: the interlocutor's line, the problem visible at once | 3 (pilot: he walks into the hero, eyes on the phone); frame 0 is the cover |
| 3–9 | dialogue on the move, the hero doesn't slow down | 2 ↔ 3, a 1 as punctuation between lines |
| 9–21 | dive: eye or temple → symbols world → transformation → lime words and scheme → exit | 5, cut inside by star wipes |
| 21–26 | solution: hand close, snap; the world answers; the interlocutor in shock | 4 → world beat → 6 |
| 26–30 | the hero looks into the camera, CTA | 8 |

Shot 7 is optional: an establishing far silhouette for the new place. The template is a start; the animatic sets the exact timing.

## Shot types (bible §5)
| # | Shot | Frame, and how bends stay hidden | Motion from | Sound cue |
|---|---|---|---|---|
| 1 | Boots close | ankle-down, wet asphalt, reflections; boot insert | boot clip curves, 100STYLE cadence, heel→toe roll of `walk.ts` | a step on each heel strike |
| 2 | Profile walk | waist-up profile, hands in pockets, the world scrolls behind | 100STYLE per-frame curves | off-screen steps on step frames |
| 3 | Two waist-up | dialogue, lines at the speaker; arms in pockets or at rest — a gesture cuts to 4 | face rig, breath, moving holds | line pops |
| 4 | Hand close | the snap; the cuff hides the wrist; hand insert | MediaPipe hand curves | hit on the snap frame |
| 5 | Dive | eye → symbols world → exit; no body | symbols and lime kits (role 03) | whistle on entry |
| 6 | Reaction close | the interlocutor's face | MediaPipe face blendshapes | silence or a sting |
| 7 | Far silhouette | the only full height: small, flat fill and rims, knees unreadable | `walk.ts` at small scale | ambience |
| 8 | CTA | look into the camera, plate «ссылка в профиле» (not scaled by the camera) | face rig | — |

## Storyboard file
`docs/series/boards/<ep>.md` unless the task names another path. One row per shot:

| # | Frames (30 fps) | s | Type 1–8 | Size, angle | What moves | Bend hidden by | Line: who, text | Sound | Out |
|---|---|---|---|---|---|---|---|---|---|

Under the table, 2–4 lines: the rhythm in one sentence, where the silence before the barb sits, what frame 0 shows, which library parts are missing.

## Rules of the board
- Frame 0 is the cover: the key line is already readable on it, no fade-in (rule of the AspTheABlog scripts).
- The hero's barb is ≤ 6 words, lands after a silence and is held by the face and a pause. He mocks everyone hard — the owner's choice; don't soften it.
- Timing for the future voice: a line's slot = words ÷ `target_speech_wps` (3.8). Text may stay past its slot to be readable without sound; the voice will simply end earlier.
- Neighbouring shots never share a size or a transition. Cut on an action change or a gesture end, never mid-gesture; no cross-dissolves (grammar — spec 03).
- Every row names how its bends are hidden. A shot that can't name it is redesigned.
