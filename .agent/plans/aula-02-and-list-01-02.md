# Plan: Aula 2 notes + graduate list for Aulas 1–2 (2026-10-13)

## 1. `Aula/aula-02-notes.md`
Same anatomy as `Aula/aula-01-notes.md` (front matter, Syllabus/Read lines, numbered sections,
common mistakes, exercises by number and page, sources). Content = study-guide Aula 2:
wealth effects (M&R pp. 35–36), value index $x+v(y)$ (p. 36 n. 7), value maximization
principle (pp. 36–38, Fig. 2.1, n. 10), Coase theorem (p. 38), transaction-costs view and its
limits (p. 39), threat points and the Nash split under transferable utility (stated; Varian
§30.7 says the full model is beyond its scope), preview of alternating offers (MWG 9.AA,
Aula 3). Worked examples are original (no book exercise solved).
Then: fill the placeholders in `rules/02_barganha.md`? **No** — outside the request; leave.

## 2. `Listas/lista-aulas-01-02.tex` (+ blank PDF, answer-key PDF, `-check.py`)
User choices: graduate level, heavy math, symbolic only, complete format, tangential =
alternating offers. Style: `rules/00_estilo_avaliacao.md` §8. Template: `Listas/lista-exam.tex`,
labels switched to English (global language rule), `\disciplina` set to this course.

Blocks:
- **Block 1 — Complementarities and coherent systems (Aula 1).** Objective a–d; discursive
  a–e on a quadratic two-choice system with cross effect, generalised to $n$ choices /
  general concave payoffs: proof (monotone comparative statics), characterization
  (stability $c>|b|$), limit ($|b|\to c$), quantification (gain from coordinated jump vs.
  local steps), parameter analysis; one graph (best replies).
- **Block 2 — Value maximization and Coase (Aula 2).** Objective a–d; discursive a–e: general
  $u(x,y)$ vs quasi-linear; WTP/WTA gap with log utility and property-rights dependence;
  proof of VMP; Nash split; parameter analysis; one graph (utility possibility frontier).
- **Block 3 — Integrative (Aulas 1+2+alternating offers).** Two firms with complementary
  investments split the joint value by alternating offers ($\delta_1,\delta_2$, $T$ rounds and
  infinite); hold the split fixed vs. bargain over transfers: Coase-efficiency of the joint
  choice when transfers are free, inefficiency with fixed shares, multiplier interaction.

Check script verifies with sympy: every closed form, signs at random admissible draws,
limits, distractors ≠ key. Compile blank + key twice each, `pdffonts` all Type 1,
answer key 10–15 pages.
