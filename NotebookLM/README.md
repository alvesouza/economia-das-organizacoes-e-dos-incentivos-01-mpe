# NotebookLM prompts — Economia das Organizações e dos Incentivos

**Open any prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM (slides → slide creation field; audio → Audio Overview Customize field or as Source).**

Before generating: check **Settings → Output language** in NotebookLM (English, for every type, audio included). The prompts carry no language line; the setting decides the language of everything the notebook produces.

| File | Type | Lecture/Book | Words | Chars | Paste into |
|---|---|---|---|---|---|
| `audio/aula-01-audio-part1.md` | Audio (Custom Prompt, hard) | Aula 1, part 1/2: Ford × GM × Toyota, the M&R Ch. 1 cases, coordination vs. motivation | 734 | 4,678 | Audio Overview → Customize |
| `audio/aula-01-audio-part2.md` | Audio (Custom Prompt, hard) | Aula 1, part 2/2: complementarities, the multiplier, coherent systems (M&R Fig. 4.3), the valley, NUMMI | 792 | 4,787 | Audio Overview → Customize |
| `audio/aula-02-audio-part1.md` | Audio (Custom Prompt, hard) | Aula 2, part 1/2: Bargaining under complete information: no wealth effects, value maximization, Coase, alternating offers (Varian §30.7, MWG 9.AA), commitment, ultimatum game | 739 | 4,660 | Audio Overview → Customize |
| `audio/aula-02-audio-part2.md` | Audio (Custom Prompt, hard) | Aula 2, part 2/2: Bargaining under private information: M&R Tables 5.2–5.3, incentive efficiency (B > S + 1/4), many participants, bargaining costs, De Beers | 787 | 4,791 | Audio Overview → Customize |

Slide and Audio Customize fields truncate silently at ~6,000 chars. All prompts are kept under 5,000 chars for safety.

All course materials should be uploaded as separate sources in the same NotebookLM notebook; these prompts guide how NotebookLM processes them. Upload everything in `NotebookLM/sources/`, which includes `Aula_01_notes - Does Organization Matter.md` (a copy of `Aula/aula-01-notes.md`; re-copy it if the notes change).
