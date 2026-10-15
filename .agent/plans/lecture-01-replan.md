# Plan: re-plan the course from Lecture01.pdf + Lecture 1 lists and quizzes (2026-10-13)

## Finding

`Aula/Lecture01.pdf` (Isabela Brandão Furtado, MPE 4th term 2026) shows the real course is a
**game-theory** sequence of 10 lectures, not the 16-session M&R plan estimated from the
2024/34 syllabus record:

| L | Date | Topic |
|---|---|---|
| 1 | Oct 13 | Static games: dominance, iterated elimination |
| 2 | Oct 20 | Static games: Nash equilibrium, mixed strategies |
| 3 | Oct 27 | Dynamic games: backward induction, subgame perfection |
| 4 | Nov 3 | Multistage games and bargaining |
| 5 | Nov 6 (Fri) | Repeated games I: cooperation |
| 6 | Nov 10 | Repeated games II: collusion, relational contracts |
| 7 | Nov 17 | Bayesian games, adverse selection and auctions |
| 8 | Nov 24 | Signaling and perfect Bayesian equilibrium |
| 9 | Dec 1 | Short-paper presentations |
| 10 | Dec 8 | Final exam |

Assessment: in-class exercises 10%, short paper (groups) 35% (content 15, presentation 15,
comments 5), final exam 55%. Slide notation follows Tadelis (2013) *Game Theory: An
Introduction* (iterated-elimination equilibrium, M/F prisoner's dilemma, existence /
uniqueness / invariance).

## User choices

Replace the roadmap with the real schedule (old Aula 1–2 M&R material kept, relabelled as
supplementary background) · copy Tadelis, Gibbons (1992), Muñoz-Garcia & Toro-Gonzalez
(2nd ed.) into `Livros/` · all three list formats · quizzes 3×10, hard, file-subject, symbolic.

## Steps

1. **Books** (agent): copy + markitdown `.md`, calibrate `book-registry.json`, add to
   `Livros/BOOKS.md`, chapter/section/page map in `Map/books-index.md`; inventory of
   Lecture-1 exercises (number, printed page, answer available?).
2. **Roadmap** (me, after 1): `Map/study-guide.md` → 10 real lectures with readings;
   `rules/11_curso_programa.md` (identity, assessment, topic × lecture × books);
   `CLAUDE.md` scope line; `README.md` topics table; this rule's old 16-session estimate
   recorded as superseded with a one-paragraph estimate-vs-reality note in
   `.agent/notes/roadmap-reality.md`.
3. **Practice plan**: `Listas/pratica-lecture-01.md` (number + page only).
4. **Exam-style list** (agent): `Listas/lista-lecture-01.tex` + blank/answer-key PDFs +
   `-check.py`, MPE style (`rules/00_estilo_avaliacao.md`), graduate level, symbolic.
5. **Worked solutions**: `Listas/pratica-lecture-01-solutions.pdf` for the plan's items.
6. **Quizzes**: `Simulados/quiz-lecture01-{1,2,3}-*.md`; gate `quiz-validate.py` PASS.

Files named `lecture-01` to avoid colliding with the old M&R "Aula 1" set.
All PDFs: pdflatex with `lmodern` + `cmap`, checked with `pdffonts`.
