# Plan: refresh Map/ for Lectures 1–8 (2026-11-03)

`/study-map` re-run. Current state: `Map/study-guide.md` is current (game theory, 8 lectures);
`Map/books-index.md` maps Tadelis/Gibbons/Muñoz-Garcia/MWG sections with pages but has no
section-level links to the material built since 2026-10-13; `Map/topics-index.md` still holds the
9 superseded M&R topics; `Map/exercises-index.md` lists game-theory exercises only per lecture.
Books: all converted to `.md` except `Livros/Risco_Incerteza_Varian.pdf` (an excerpt; skipped).

## Canonical topics (names and tags shared by every Map file)

| # | Topic | Tag | Lectures | Complexity |
|---|---|---|---|---|
| T1 | Normal-form games and solution concepts | `#topic/normal-form` | 1 | foundational |
| T2 | Dominance and IESDS | `#topic/dominance-iesds` | 1 | foundational |
| T3 | Best responses and rationalizability | `#topic/rationalizability` | 2 | intermediate |
| T4 | Nash equilibrium | `#topic/nash-equilibrium` | 2 | intermediate |
| T5 | Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling) | `#topic/oligopoly` | 1–3, 6 | intermediate |
| T6 | Mixed strategies and existence | `#topic/mixed-strategies` | 2–3 | intermediate |
| T7 | Extensive form, strategies and information | `#topic/extensive-form` | 3 | foundational |
| T8 | Backward induction and subgame perfection | `#topic/spe` | 3 | intermediate |
| T9 | Commitment and credibility (Stackelberg, entry, time inconsistency) | `#topic/commitment` | 3–4 | intermediate |
| T10 | Multistage games (carrot and stick, one-stage deviation) | `#topic/multistage` | 4 | intermediate |
| T11 | Strategic bargaining | `#topic/bargaining` | 4 | intermediate |
| T12 | Repeated games and the folk theorem | `#topic/repeated-games` | 5 | advanced |
| T13 | Collusion and price wars | `#topic/collusion` | 6 | advanced |
| T14 | Reputation and relational contracts | `#topic/reputation` | 6 | advanced |
| T15 | Bayesian games and Bayesian Nash equilibrium | `#topic/bayesian-games` | 7 | intermediate |
| T16 | Adverse selection | `#topic/adverse-selection` | 7 | intermediate |
| T17 | Auctions | `#topic/auctions` | 7 | advanced |
| T18 | Perfect Bayesian equilibrium | `#topic/pbe` | 8 | advanced |
| T19 | Signaling and refinements | `#topic/signaling` | 8 | advanced |

The 9 M&R topics move to a final "Background and applications (superseded plan)" section of
`topics-index.md`, each pointing to the T-topic that now carries it (Bargaining → T11, Adverse
selection → T16, Moral hazard: out of scope).

## Work split

- **Agent T (topics + books):** rewrite `Map/topics-index.md` with T1–T19 in the `/study-map`
  format (complexity, prerequisites, cross-topic links, difficulty progression with wiki-links,
  cross-topic synthesis); add "Materials" link lines under the game-theory sections of
  `Map/books-index.md` (Tadelis Ch. 3–13, 15–16; Gibbons Ch. 1–4; Muñoz-Garcia; MWG 7–9, 12–13;
  Cabral Ch. 7, 9; M&R Ch. 8) and fix section/exercise ranges that the lists contradict.
- **Agent E (exercises):** add per-book tables to `Map/exercises-index.md` for Tadelis, Gibbons,
  Muñoz-Garcia and the game-theory MWG/Cabral/M&R exercises, parsed from the tier tables of
  `Listas/pratica-lecture-0{1..8}.md` (+ optional extras, marked), tagged with T-topic names,
  level, page, "Verified = yes" (pages checked against the PDF when the lists were built), and
  the list/solution that uses each.
- **Main loop:** `Map/study-guide.md` (Lecture 3 slides, mini cases, Brexit case, notes PDFs,
  narrations, audio prompts, real-exercise list); final link check.

## Material inventory (for links)

Notes `Notas/LNN/` (+ `LNN-notes.pdf`) · quizzes `Simulados/quiz-lectureNN-K-*.md` · practice lists
`Listas/pratica-lecture-NN.md` · `Listas/lista-lecture-01.tex` · `Listas/lista-reais-lectures-01-04.pdf`
(+ solutions, study pack) · NotebookLM `NotebookLM/audio/lecture-NN-audio-part{1,2}.md` · narrations
`Leituras/lecture-NN-notes-narrated.txt` · mini cases `Resolucao/mini-case-lecture-01.pdf`,
`Resolucao/mini-case-lecture-03{,-short}.pdf` · Brexit `Cases/Brexit/brexit-game.pdf` (L3–L4:
SPE, commitment, bargaining) · slides `Aula/Lecture0{1,2,3}.pdf` · rules `rules/game-theory.md`,
`rules/02_barganha.md`, `rules/07_selecao_adversa.md`.
