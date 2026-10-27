# Plan: Lecture 2 — notes reconcile, quizzes, NotebookLM audio, TTS, practice list

Sub-plan of `lecture-batch-01-08.md` (L02 agent). No question round; defaults from the batch plan.
Shared indexes (`Map/*`, `Notas/00-index.md`, `NotebookLM/README.md`, `README.md`) are left to the main loop.

## 0. Reconcile `Notas/L02/` with `Aula/Lecture02.pdf` (56 slides, frame numbers cited as "slide N")

Slides teach, in order: recap of L1 (DSE, Pareto, epistemic IESDS) · BoS, best response, BR correspondence, NBR,
rationalizability, Tadelis Prop. 4.4, Lessons 3–4 · NE definition, interpretations, Props. 1–2 (NE survives IESDS;
unique IESDS survivor is NE) with proofs, weak-dominance caveat, side-of-road and PD · Cournot in $q^m$/$q^{cp}$
notation, BR, NE $\tfrac23q^m$, IESDS sequence, cartel matrix, $n$ firms · Bertrand general $a,b,c$, BR
correspondence, $(c,c)$ unique (two steps), paradox, Cournot vs Bertrand · mixed strategies ($\Sigma_i$), expected
payoffs, mixed NE, principle of indifference (iff) with proof, BoS mixed $(p,q)=(\tfrac23,\tfrac13)$,
interpretations, Nash's theorem · graded mini case (monitoring remote work): method only.

Edits:
- notation $v_i\to u_i$ (slides), keep Tadelis numbering, add slide refs;
- add slide content to 01 (Lessons 3–4), 02 (Props. 1–2 proofs, interpretations, weak-dominance caveat, road game,
  PD), 03 ($q^m$ form, IESDS sequence, cartel matrix, $n$ firms), 04 (general BR correspondence, two-step
  uniqueness, paradox, Cournot vs Bertrand), 07 (slides' expected-payoff formulas, principle of indifference promoted
  from G to C with both proofs, BoS mixed as the lead example, interpretations, mini case method);
- mark not covered in class: 01 §4 beauty contest, 02 Stag Hunt, 04 cent grid / asymmetric / differentiated,
  05 commons, 06 Hotelling voting, 07 MP/RPS/§6.2.3/all-pay, 08 whole, 09 proof (theorem only taught);
- `status: taught`; map banner → reconciled; formulas §0 spec = slides; pitfalls + slide items.
- figures unchanged; rerun `make_figures.py` to confirm. No PDF compile.

## 1–4
Quizzes (3×10, validator), audio (2 prompts < 5,000 chars), TTS of the reconciled notes, practice list
(`Listas/pratica-lecture-02.md`, verbatim statements, pages verified). Exercises list delegated to a forked
agent in parallel.
