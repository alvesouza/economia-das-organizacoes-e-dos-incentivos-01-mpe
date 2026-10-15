<!-- TIER-0, 900-token budget. GENERATED block: edit rules/core.md and run tools/sync_rules.py -->

# Economia das Organizações e dos Incentivos — MPE Insper

Taught as **game theory** (10 lectures, slides follow **Tadelis 2013**); M&R (1992) = applications. Books: [Livros/BOOKS.md](Livros/BOOKS.md).
Syllabus, topics, bibliography, structure: [rules/11_curso_programa.md](rules/11_curso_programa.md) · [Map/](Map/).

<!-- GENERATED:tier0:start -->
### Non-negotiable

1. Escalate retrieval in this order and stop at the first rung that answers the
   question: **graph query → symbol lookup → structural search → ripgrep → file slice
   → whole file**.

2. Do not switch the main-loop model mid-session. Delegate to a subagent instead.

3. Write the plan to `.agent/plans/<slug>.md` before implementing any non-trivial
   change, then implement against it.

4. Report only outcomes observed in tool output. Failing tests are quoted, not
   summarized away. Skipped steps are stated.

5. Never read secrets into context: `.env`, key material, credential stores, tokens.
   Reference them by name.

6. Memory-safety, point-in-time, and idempotency gates do not relax under deadline.

### Prefer

7. Persist findings to `.agent/notes/<topic>.md` rather than re-deriving them.

8. Reuse before writing. If you write new code anyway, say what you found and why it
   did not fit.

9. Match the surrounding code. `.agent/conventions.md` outranks this repo's style
   preferences; correctness rules never yield.

10. Doc comments on public functions: purpose, parameter meaning, failures, calling
    context. Inline comments state constraints the code cannot express, never narration.

### Avoid

11. Making the diff larger than the change. Refactor inside the change's own context;
    outside it, ask (`codebase-work.md`).

12. Abstractions, defensive branches for impossible states, and speculative generality.

13. Claiming completion when part of the task is unfinished. Do the rest; if truly
    blocked, state plainly what is missing and why.

14. Re-deriving facts already established in the session.

Rationale and verification commands for each rule: `rules/core.md`
<!-- GENERATED:tier0:end -->

## Scope — do not extrapolate

Only the 8 content lectures of the real schedule ([Map/study-guide.md](Map/study-guide.md)).
Core: Tadelis Ch. 3–13, 15–16; M&R for applications. Formal depth: MWG 7–9, 12.D, 13.
Out unless a lecture brings it: mechanism design (Tadelis 14, MWG 23), cheap talk, moral hazard. **Never reproduce an exercise statement**: number + page.

## Format

Output in **English**; quotes, titles and file names verbatim. LaTeX `$...$`, never a bare `$` for
currency. **Python**, no R. pdflatex needs `lmodern`+`cmap` (check `pdffonts`). NotebookLM language
is an app setting, never a prompt line. Exam style `macro-1`: `rules/00_estilo_avaliacao.md`.

## Siblings and secrets

`../Video explainer` (video kit, `pip -e`) · `../Efficient Token` (governance: packs in `rules/`,
`tools/`, `.claude/hooks/`). Keys in `.env`, gitignored; never read a secret into context.
