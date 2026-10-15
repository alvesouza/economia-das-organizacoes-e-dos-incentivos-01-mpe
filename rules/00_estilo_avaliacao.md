# Assessment style (MPE): rules for lists, mock exams and grading

Style specification for **Economia das Organizações e dos Incentivos (MPE Insper)**, adapted
from the `macro-1` style (Macroeconomia I, MPE). It is the single source of truth for
`/exam-gen` (generate list + answer key) and `/exam-grade` (grade the student's resolution).
Paired with the template `Listas/lista-exam.tex`.

## 1. Document structure

- Organized in **thematic blocks** (1 to 4). Each block maps to a set of topics and carries a
  point total (full mock exam: 4 blocks × 25 = 100 pts; a thematic list uses 1–2 blocks).
- Each block has, typically, **two questions**:
  - **Objective question** (10 pts): items **a) and b)** multiple choice (3 pts each, 4–5
    options, no penalty for errors) + items **c) and d)** **True/False** (2 pts each).
  - **Discursive question** (15 pts): one contextualized parent statement + sub-items **a), b),
    c)** (5 pts each), with a "Resolution:" space.
- In an **exercise list** the length is flexible (the student picks the scope); keep the same
  question anatomy.

### True/False rule (always on the cover/instructions)
T/F score $=\max\{0,\ \text{correct}-\text{wrong}/2\}\times$ item value. Blank items do not
count as wrong.

### Natural blocks in this course

| Block | Topics (`rules/`) | Theme | M&R |
|---|---|---|---|
| I | 01–03 (Aulas 1–5) | Organization, bargaining and efficiency (+ NEPKE) | Ch. 1–2 (+ Ch. 4 pp. 106–113, Ch. 5 pp. 140–149) |
| II | 04–05 (Aulas 6–8) | Coordination: market vs. management (+ Sears) | Ch. 3–4 (+ Ch. 6 pp. 192–194) |
| III | 06–07 (Aulas 9–12) | Bounded rationality, private information, adverse selection and signaling | Ch. 5 |
| IV | 08–09 (Aulas 13–16) | Moral hazard and incentive contracts (+ S&L crisis) | Ch. 6–7 |

Aula numbers follow the draft class plan (`Map/study-guide.md`); update them when the real schedule arrives.

## 2. Question taxonomy

- **Multiple choice (a, b):** direct application of a result or identification of a concept.
  4–5 options. Plausible distractors of the **same length** as the key (anti-guessing),
  reflecting common mistakes in organizational economics:
  - confusing **adverse selection × moral hazard** (hidden information before vs. hidden
    action after the contract);
  - confusing **signaling × screening** (who moves first: the informed or the uninformed party);
  - reading the **Coase theorem** without its conditions (zero bargaining costs, full
    information, no wealth effects);
  - confusing **Pareto efficiency × value maximization × fairness**;
  - claiming that **stronger incentives are always better**, ignoring the risk premium the
    agent demands;
  - treating **pooling** as separating, or believing a signal must be productive to work;
  - assuming market coordination is efficient **outside** the First Welfare Theorem's
    assumptions.
- **True/False (c, d):** test **false converses** and conceptual traps (e.g. "education
  raises wages in a signaling equilibrium" is T; "education raises productivity in a
  signaling equilibrium" is F in the pure Spence model; "full insurance is optimal under
  moral hazard" needs observable effort). One claim per item, no ambiguity.
- **Discursive (a, b, c):** increasing progression: set up the problem (agents,
  information, timing, contract space) → solve/derive (participation and incentive
  constraints, equilibrium, optimal contract) → interpret (efficiency, organizational design,
  policy). Each sub-item tests a distinct aspect of the same scenario.

## 3. Contextualization (hallmark of the style)

- **Every** question is anchored in a **plausible, current Brazilian scenario**: a real
  institution, indicator or episode, such as executive compensation at listed companies (CVM
  disclosures), bank regulation and deposit insurance (Banco Central, FGC), health plans and
  ANS, used-car and insurance markets (SUSEP), public procurement and concessions,
  franchising, platform work, organ donation (SNT), public-sector career design, or the 2008
  crisis as read in Giambiagi & Garcia. The context is the shell; the core is the course's
  model.
- Numeric parameters **chosen to give clean closed answers** (CARA utility, normal noise,
  quadratic effort cost, two types). Declare "illustrative values" when convenient.
- Do not confuse institutional realism with theoretical extrapolation: **course models only**
  (see `CLAUDE.md`, "Scope — do not extrapolate").

## 4. Solution format (answer key)

- **Objective:** `Answer: X` + 1–3 lines of justification (calculation or concept).
- **Discursive:** numbered sequence **"Step — title. text."** (setup → derivation → result →
  check). Include:
  - **Economic intuition.** A short paragraph with the "why".
  - **Ref:** bibliographic anchor (chapter + section, and page when `Map/` has it).
  - **Grading rubric.** Points per step, with:
    - **Caps for conceptual errors** (e.g. "omits the participation constraint → max. 2 pts
      on the sub-item"; "treats effort as observable in a moral-hazard question → max. 1 pt";
      "separating equilibrium without checking the low type's incentive constraint → max.
      half").
    - **Light penalties** for arithmetic slips with the correct method ($-1$ pt).
    - **Non-cumulativity:** conceptual caps override light penalties (they do not add up).
  - **Residual risk** (optional): a common trap / ambiguity in the statement to avoid.
- **Graphs.** Much of the course reads graphically (indifference curves in the signaling
  diagram, the Edgeworth box, the bargaining frontier, the incentive–insurance trade-off). The
  rubric scores **labelled axes, named curves and the equilibrium point** separately from the
  verbal conclusion.

## 5. Use of the bibliography (mandatory)

Anchor content and references in the course books, through `Map/` and `rules/` when they exist:

- **Milgrom & Roberts (1992)**: the **floor** (chapter/section in every question).
  In `Livros/` (sections and printed pages: `Map/books-index.md`). Cite `Ref: M&R Ch. N,
  "<section>", p. NNN`; never invent a section number. Its *Food for Thought* items are the
  model for discursive questions (cite by number and page, never reproduce).
- **Mas-Colell, Whinston & Green (1995)**: formal depth: 9.AA (bargaining), 13.B–D (adverse
  selection, signaling, screening), 14.B–D (principal–agent), 16.C (First Welfare Theorem).
- **Varian, *Intermediate Microeconomics with Calculus* (2014)**: intuition and intermediate-level
  exposition (Ch. 12, 30, 32, 33, 35, 38). The syllabus cites the 8th ed. of the non-calculus
  book: cite the local edition and say which it is.
- **Cabral (2017, 2nd ed.)**: firm boundaries and agency (§3.3–3.5), market failure (Ch. 5),
  vertical relations (Ch. 13).
- **Giambiagi & Garcia (2010)**: Brazilian and 2008-crisis context: Cap. 7 (incentives),
  Quadro 8.1 (S&L), Cap. 16 (Sadia). Essays only, no exercises.

Write **original** questions from the concepts; never copy or paraphrase a book exercise.
Use `Map/` for topic weights and for pages in the `Ref:` lines.

## 6. LaTeX conventions

- Template: `Listas/lista-exam.tex`. A single `.tex` with `\ifsolucoes`:
  - `\solucoesfalse` → **blank list** (space to solve).
  - `\solucoestrue` → **answer key + rubric** (same file).
- Macros: `\bloco`, `\questao`, `\alternativas`, `\gabarito`, `\resolespaco`, `\passo`,
  `\intuicao`, `\refbib`, `\rubrica`; solution blocks inside the `sol` environment (excluded
  from the blank list via the `comment` package).
- **Global copyable-PDF rule:** the preamble already has `\usepackage{lmodern}` and
  `\usepackage{cmap}` after `fontenc`. Compile with `pdflatex` (2×) and check `pdffonts`
  (all **Type 1**, never Type 3).
- Math in `$...$`/`$$...$$`. Never a bare `$` for currency (write "120 reais").
- Graphs in **TikZ/pgfplots** (signaling diagram, bargaining frontier, Edgeworth box), never
  a raster image.

## 7. Anti-patterns

- Do not extrapolate beyond the course (check `CLAUDE.md`). In particular: no general
  mechanism design (MWG 23), no M&R Parts V–VII unless a lecture brings them, no IO models
  beyond what coordination needs.
- **Formatting anti-guessing:** the key cannot systematically be the longest, nor the only
  one with parentheses/formula/example. Write distractors at the same level of detail and in
  the same style as the key (parentheses, hedges, symbols, units), sometimes longer,
  sometimes shorter. The only thing that distinguishes the key is being true, never its
  format. Vary the key's position (do not fix A).
- **Majority-vote guessing.** If every distractor changes exactly one feature of the key, the
  key is the feature-by-feature majority of the options and can be found without the
  content: at least one distractor per item combines two named mistakes. Check the correct
  letters across the whole list too (every letter used, no repeating pattern), above all
  when different blocks were written separately.
- T/F without a trap = weak question; prefer converses and assumptions that "break".
- A solution without a rubric and without intuition is incomplete.
- A contracting question that does not state **what is observable and verifiable** (effort,
  output, type) and **the timing** (who offers, who moves first) is ambiguous. Always state both.

## 8. Graduate level (opt-in for lists and mock exams)

Chosen in `/exam-gen` Step 3 (*Graduate level* depth, *Graduate* math complexity). The
anatomy of §1–§4 stays (blocks, objective + discursive, rubric, intuition, `Ref:`); the bar
moves.

**Scope.** The syllabus does not grow: the exclusions of §7 and `CLAUDE.md` hold. What rises is
the mathematics applied to the course's own models. In this mode MWG 9.AA, 13 and 14 are the
main source of ideas. *Why:* a harder list that changes the topics trains for an exam the
student will not sit.

**Symbolic by default.** Graduate lists and mock exams are posed and solved in parameters
(risk aversion $r$, noise variance $\sigma^2$, discount factors $\delta_i$, type productivities
$\theta_L<\theta_H$, with their admissible ranges), without calibrated numbers: answers are
closed forms, conditions, signs, orderings and limits; multiple-choice options are
expressions or conditions; a result with no closed form is characterized (existence,
uniqueness, monotonicity, bounds) and proved. The Brazilian context stays as narrative.
`/exam-gen` asks whether to include numbers; only on an explicit yes do items add calibrated
values, numeric sensitivity tables and numbered axes.

**Questions.**
- Every discursive question starts from **primitives** (preferences and risk attitudes,
  technology, information structure, timing, contract space). The student derives what an
  intermediate list would hand over (participation and incentive constraints, the optimal
  contract, the separating condition, the subgame-perfect split) and then uses it.
- General forms come before special cases: general $u(w)$ before CARA, general cost $c(e)$
  before quadratic, $n$ rounds before the infinite horizon. Distractors and traps come from
  applying the special case where it fails.
- Each block contains at least one item of each kind: a **proof** ("show that", existence,
  uniqueness, the sign of a derivative); a **characterization** (which constraints bind,
  the set of separating equilibria, the Intuitive Criterion selection); a **limit or
  knife-edge case** ($r\to0$, $\sigma^2\to0$, $\delta\to1$, $\theta_H\to\theta_L$); a
  **quantification** in closed form (agency cost, information rent, welfare loss from
  signaling; calibrated numbers only when opted in).
- Objective items need three or more derivation steps or a trap only the general case
  reveals; none is answerable by plugging into a memorized formula.
- **Cross-topic questions.** Every discursive question chains at least two course topics
  inside one model (adverse selection × moral hazard, bargaining × efficiency, market vs.
  management × incentive design, moral hazard × deposit insurance). Name the topics in the
  question's heading. At least two objective items per block also cross topics.
- **Integrative questions.** Each graduate list has an integrative block, and each block of a
  graduate mock exam has at least one integrative question: one model in which three or more
  topics from at least two blocks cross. Name the topics in the heading.
- **No answer in the statement.** Ask to find, characterize or determine; do not print the
  formula to be proven, except when the result has a name the student should recognize.
- **Parameter analysis in every discursive question**: (i) the sign of each comparative
  static, proved; (ii) a table of those signs (results × parameters); (iii) limiting and
  knife-edge values; (iv) the economic reading of each change.
- **Graphs where the model is read graphically, not in every question.** Each block has at
  least one sub-item that asks the student to draw, and at most half of the sub-items do. The
  answer key draws it in TikZ/pgfplots from the model's own equations.
- Discursive questions have four or five sub-items **a)–e)**: set up → derive → characterize
  → quantify → parameter analysis.

**Solutions.**
- Rebuild each model from its primitives every time: state the problem, the constraints, the
  Lagrangian or the substitution used, every FOC (with what the multiplier means), then solve.
  No step is "it can be shown".
- Each step says what it uses ("from the incentive constraint (2) and participation (3)").
- An independent script (`Listas/<list>-check.py`) verifies every result and aborts on a
  mismatch (sympy closed forms; signs, limits and orderings at many random admissible
  parameter draws; every distractor differs from the key).
- **Length: 10 to 15 pages of answer key per list.** Below 10, add questions (integrative ones
  first), never pad the prose; above 15, cut questions, never steps.

**Rubric.** Score the setup and each derivation step separately. Caps: a special-case result
used in the general case (max. half the item); a result the item asks to derive that is
quoted instead (max. a third); a binding-constraint, sign or limit claim without proof (0 for
that line); a parameter analysis that lists signs without proving them or reading them
economically (max. half the item); a cross-topic question answered inside one model only
(max. half the item). A requested graph is scored on its own lines: axes and labels, each
curve, the equilibrium point, and the reading off it; a graph contradicting the student's
algebra loses the graph points.

## 9. Study-roadmap PDF and practice-plan solutions (every exercise list)

- After building any exercise list, ask the user whether to split its study roadmap into a
  PDF. This covers `/exam-gen` lists and mock exams, and `/exercise-plan` practice plans built
  from existing book exercises. Ask once, at the end, after the list exists; it is never a
  silent default in either direction.
  *Why:* the roadmap lists reading pages and exercise pages scattered across several book
  PDFs; without the extracted PDF the student re-finds each page by hand, and generating it
  unasked costs a build the student may not want.
  *Check:* the final report of every list ends with this question (AskUserQuestion), and a
  "yes" produces `/study-pack <roadmap file>`.
- On "yes", run `/study-pack` on the file that carries the roadmap tables (an `/exercise-plan`
  file already does; for an `/exam-gen` list, first write the reading and roadmap tables of the
  `/exercise-plan` format to `Listas/roteiro-<topic>.md`).
- After building an `/exercise-plan` practice plan, also ask whether to write the solutions of
  its exercises as a PDF, in the same AskUserQuestion call as the roadmap question.
  *Why:* a practice plan points to book exercises whose answers are not in M&R, Cabral or MWG,
  so without solutions the student cannot check the work; writing 30 solutions unasked is a
  long build the student may not want. (`/exam-gen` lists already ship their answer key.)
  *Check:* the plan's final question offers both PDFs; a "yes" produces
  `Listas/pratica-<topic>-solutions.pdf`.
- On "yes", solve every exercise of the plan with `/solution` in plan order, cite each one by
  number and page without restating it, and compile one pdflatex PDF (lmodern + cmap) from
  `Listas/pratica-<topic>-solutions.tex`, with a check script for every computed number.
