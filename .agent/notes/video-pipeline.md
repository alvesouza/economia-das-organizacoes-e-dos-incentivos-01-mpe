# Video pipeline findings (2026-10-09, Aula 1)

- **Kit bug, small text loses its spaces.** Manim `Text` below about font_size 30 drops word
  spacing ("assembly hours per car" → "assembly hoursper car"). Confirmed on a still: the same
  string at 40 or 60 and scaled down is correct. It hits the kit's `table()` (cells at 18–24)
  and `axes_panel()` labels (20). Titles (30) and notes (24) looked fine. Local workaround in
  `Videos/aula-01-does-organization-matter/scenes.py`: `small()`, `grid()`, `panel()` build at
  2× and scale by ½. **Upstream fix belongs in `../Video explainer/src/video_explainer/manim_kit.py`**
  (same trick inside `table()`, `axes_panel()`, `note()`); not applied without asking, since
  other projects' videos import it.
- **Speechify credits ran out** (HTTP 402) on the first `--check` of 2026-10-09. Durations are
  estimated at 197 wpm by `fill_durations.py` until audio exists; the 480p draft is silent.
- **The machine sleeps during long renders.** BeatScale "took" 5,927 s because the laptop slept
  between 17:51 and 19:29; nothing was wrong with the scene. Monitors expire on wall-clock time.
- `rm -rf` is denied by the project's settings; Manim's partial-movie cache is keyed by content,
  so changed scenes re-render without clearing `media/`.
- `layoutcheck` verified on a planted collision (caught at step 2) before trusting its clean run.
- **Two `.animate` steps on one mobject inside one Beat break the first.** `Beat` declares every
  step before playing any, and `mob.animate` stores its target ON the mobject at declaration, so
  the later builder overwrites the earlier one's target (labels revealed by opacity stayed
  invisible because a later recolour step had captured them at opacity 0). Use `FadeToColor` /
  `ApplyMethod` (target built at play time) for the second change. A kit-level guard would help.
- **Build overlays after `st.show()`.** `Stage.show` fits and moves a group immediately; anything
  computed from its parts' coordinates (arrows, paths) must be built after that call.
- `beatcheck --rendered` reports a "gap" equal to the scripted pauses (n × 2.5 s): expected with
  the PAUSE_S design, not drift.
