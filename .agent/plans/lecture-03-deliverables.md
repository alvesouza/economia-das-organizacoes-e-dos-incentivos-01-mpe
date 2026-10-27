# Plan: Lecture 3 deliverables (quizzes, NotebookLM audio, TTS, practice list)

Child of `.agent/plans/lecture-batch-01-08.md` (step 1, L03 agent). No slides: everything follows
`Notas/L03/` (estimated) and Tadelis Ch. 7–8; each file says so in its header.

| # | Deliverable | File | Check |
|---|---|---|---|
| 1 | 3 quizzes × 10, by cluster: (1) extensive form, strategies, normal form and paths; (2) backward induction and subgame perfection; (3) credibility, commitment, Stackelberg, time inconsistency | `Simulados/quiz-lecture03-{1,2,3}-<slug>-2026-10-25.md` | `python .claude/quiz-validate.py` → PASS |
| 2 | 2 audio Custom Prompts: (1) describing dynamic games and the refinement (Ch. 7, §8.1–8.2); (2) applications (MAD, entry/commitment, Stackelberg, time inconsistency) | `NotebookLM/audio/lecture-03-audio-part{1,2}.md` | `wc -c` < 5,000; no language line |
| 3 | TTS narration of `Notas/L03/` 00–11, math in words | `Leituras/lecture-03-notes-narrated.txt` | speechify Step 6 script: no hostile symbols |
| 4 | Practice list, ~22 book exercises verbatim, 3 tiers | `Listas/pratica-lecture-03.md`, figures in `Listas/figures/` | every row has a statement block; pages checked in PDF |

Exercise candidates: Tadelis 7.1–7.10 (pp. 147–150), 8.1–8.16 (pp. 170–174); Muñoz-Garcia Ch. 4
(pp. 153–214) except Ex. 1, 16–18 (Lecture 4, bargaining/multistage) and 21 (moral hazard, out);
Gibbons Ch. 2 problems 2.1–2.3 style (Stackelberg, backward induction) and MWG 9.B where in scope.

No shared index edits. No solutions file.
