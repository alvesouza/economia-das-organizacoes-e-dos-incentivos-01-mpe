# Plan: map Lectures 6-7, real-exercise lists, NotebookLM exercise prompts (2026-11-20)

## Inputs
- New slides: `Aula/Lecture06.pdf` (Nov 11, "Bargaining and Bayesian games", 40 frames) and
  `Aula/Lecture07.pdf` (Nov 17, "Bayesian games, adverse selection and signaling", 58 frames).
- New schedule (L6 slide 3): L8 Nov 24 auctions; L9 Dec 1 mechanism design (half class) +
  presentations; L10 Dec 8 final exam. Short-paper milestones per lecture.

## 1. Map
- `Map/study-guide.md`: L6 and L7 rows and sections from the slides; L8 auctions, L9 mechanism
  design; schedule-vs-estimate note; kit pointers to the new lists and prompts.
- `Map/topics-index.md`, `Map/exercises-index.md`: point the topics to the new items.
- `NotebookLM/sources/`: copy the two slide PDFs (same naming as Lectures 1-5).

## 2. Real-exercise lists (blocks 6-7, items 51-70 of a combined 01-07 list)
- Statements: `\input` the fragments `pratica-lecture-0N-solutions/stmt/item-NN.tex`, which
  `make_statements.py` generates from the practice lists (single source, already verbatim with
  source lines). No statement is retyped.
- Files: `lista-reais-lectures-01-05/preamble-06-07.tex` (pandoc support, rows, overrides),
  `block6.tex`, `block7.tex`; drivers `lista-reais-lecture-06.tex`, `-07.tex`,
  `lista-reais-lectures-01-07.tex`; `order.md` extended.
- Solutions (deepened rewrites, (a)-(f) incl. Common mistakes, slide citations):
  `lista-reais-lectures-01-05-solutions/sol-<slug>.tex`, `sol-items.tex` gets `\itemsvi`,
  `\itemsvii`; drivers `lecture-06.tex`, `lecture-07.tex`, `main-01-07.tex`; check scripts
  `check_F_L06.py`, `check_G_L07.py`. Two forks write the solutions (one per lecture).

| L# | All# | L6 item | slug | level | diff |
|---|---|---|---|---|---|
| 1 | 51 | Gibbons 3.1 | gibbons-3-1 | Found. | 1 |
| 2 | 52 | Tadelis 11.1 | tadelis-11-1 | Found. | 1 |
| 3 | 53 | Muñoz-Garcia Ch. 4 Ex. 1 | munoz-garcia-4-1 | Found. | 2 |
| 4 | 54 | Gibbons 3.4 | gibbons-3-4 | Exam | 2 |
| 5 | 55 | Muñoz-Garcia Ch. 7 Ex. 1 | munoz-garcia-7-1 | Exam | 3 |
| 6 | 56 | Tadelis 11.2 | tadelis-11-2 | Exam | 3 |
| 7 | 57 | Tadelis 12.3 | tadelis-12-3 | Exam | 3 |
| 8 | 58 | Tadelis 12.2 | tadelis-12-2 | Exam | 4 |
| 9 | 59 | Tadelis 12.9 | tadelis-12-9 | Adv. | 4 |
| 10 | 60 | Tadelis 11.7 | tadelis-11-7 | Adv. | 5 |

| L# | All# | L7 item | slug | level | diff |
|---|---|---|---|---|---|
| 1 | 61 | Tadelis 15.1 | tadelis-15-1 | Found. | 1 |
| 2 | 62 | Muñoz-Garcia Ch. 9 Ex. 1 | munoz-garcia-9-1 | Found. | 2 |
| 3 | 63 | Tadelis 15.3 | tadelis-15-3 | Found. | 2 |
| 4 | 64 | Tadelis 12.5 | tadelis-12-5 | Exam | 3 |
| 5 | 65 | Muñoz-Garcia Ch. 9 Ex. 2 | munoz-garcia-9-2 | Exam | 3 |
| 6 | 66 | Tadelis 12.6 | tadelis-12-6 | Exam | 3 |
| 7 | 67 | Tadelis 15.5 | tadelis-15-5 | Exam | 4 |
| 8 | 68 | Tadelis 16.4 | tadelis-16-4 | Exam | 4 |
| 9 | 69 | MWG 13.C.5 | mwg-13-c-5 | Adv. | 4 |
| 10 | 70 | Tadelis 16.8 | tadelis-16-8 | Adv. | 5 |

Tit-for-tat and the folk theorem (L6 part 1) are drilled by block 5 (items 43-44); no new item.

## 3. NotebookLM prompts, 3 per lecture
`NotebookLM/audio/lecture-0N-exercises-part{1,2,3}.md`: problems and solutions in detail plus
the traps; each prompt under ~5,000 characters, no language line; sources = the list PDF, its
solutions PDF and the slides.

## 4. Verify
Compile every driver twice; `pdffonts` all Type 1 with uni = yes; run both check scripts;
prompt lengths counted.
