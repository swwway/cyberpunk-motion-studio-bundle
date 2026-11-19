# MOTION_STUDIO_STATE.md

MultStudio's anchor in the Remotion repo root: read at session start, update after every task.

- **Skill:** `cyberpunk-motion-studio` 2.0 (copy of swwway/cyberpunk-motion-studio-bundle@`<commit>`)
- **Worktree:** `/root/projects/Remotion-mult`, branch `mult`; last push to main: `<commit>`
- **Open issues:** `#…`
- **Engine:** Remotion + SVG, `1080x1920`, `30fps`; CPU-only server (WebGL: default `--gl` or `swangle`)

## Shot-type library (bible §5)

| # | Type | Composition | Probe render | Status: todo / sent dd.mm / approved dd.mm |
|---|---|---|---|---|
| 1 | boots | | | todo |
| 2 | profile walk | | | todo |
| 3 | two waist-up | | | todo |
| 4 | hand | | | todo |
| 5 | dive | | | todo |
| 6 | reaction | | | todo |
| 7 | far silhouette | | | todo |
| 8 | CTA | | | todo |

## Rig and kits

- Proportions ≈8.5 heads: `HEAD_SCALE` …, `NECK` …, arms −…% — measured on a render: … heads [ ]
- Inserts: hand [ ] · boot [ ]
- Interlocutor kit: parts … · people built: …
- World kit: parts … · places built: …
- Facets: hero … (80–100) · interlocutor …

## Motion data in use

- 100STYLE: … · caption credit line — owner's decision: …
- `out/motion-ref` curves: …
- CMU: …

## Last QA — `<shot>`, round `n/3`

- Clip to the owner: dd.mm · verdict: …
- Graphs and onion skins: `out/cyber/qa/<shot>/…`
- Scores: hidden joints & proportions `-/10` · motion life `-/10` · palette & facets `-/10` · safe zone & text `-/10` · shot grammar `-/10` · sound sync `-/10` · transitions `-/10`

## Episode

- `EP_xx` — storyboard `docs/series/boards/…` · animatic (Showrunner): …
