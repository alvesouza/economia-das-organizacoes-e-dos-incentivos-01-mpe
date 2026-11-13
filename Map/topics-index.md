---
tags: [map, cross-reference]
date: 2026-11-03
---

# Topics index

Nineteen topics (T1–T19) cover the 8 content lectures of the real schedule
([[Map/study-guide|study guide]]). Names and tags are shared with
[[Map/books-index|books-index]] and [[Map/exercises-index|exercises-index]]. Pages are printed
pages; book links go to the section entries in books-index, which carry the page ranges.

**How to read a progression.** Step 1 is the book section (Tadelis first, Gibbons second, MWG
for the formal side, Muñoz-Garcia & Toro-Gonzalez for drill with worked answers); step 2 the
slides and notes; step 3 the rules and formula sheet; steps 4–5 practice-list items
(`Listas/pratica-lecture-NN.md`, linked by item number and exercise ID; "L3 #6" = Lecture 3
list, item 6); step 6 the quiz sections (tag and number of questions); step 7 the audio
prompts and narrations; step 8 cases. Slides exist for Lectures 1–5
([[Aula/Lecture01.pdf|L1]], [[Aula/Lecture02.pdf|L2]], [[Aula/Lecture03.pdf|L3]],
[[Aula/Lecture04.pdf|L4]], [[Aula/Lecture05.pdf|L5]]); the notes units L03–L08 were written
from the books before the slides ([[Notas/00-index|notes index]]).

**Where each topic is actually taught (2026-11-12).** Since 2026-11-12 the practice lists follow
the real lectures (`.agent/plans/relist-real-lectures.md`), so "L3 #6"-style references point to
the real Lecture 3 list; every list has a solutions PDF (`Listas/pratica-lecture-NN-solutions.pdf`).
The notes units `Notas/LNN/` still keep the estimated numbering, which runs about half a lecture
ahead of the real lectures:

| Topics | Real lecture | Slides | Practice list |
|---|---|---|---|
| T1 Normal form, T2 Dominance and IESDS | 1 | [[Aula/Lecture01.pdf\|L1]] | 24 items |
| T3 Rationalizability, T4 Nash equilibrium, T5 Oligopoly, T6 Mixed strategies (basics) | 2 | [[Aula/Lecture02.pdf\|L2]] | 22 items |
| T6 Mixed strategies (finished), T7 Extensive form, T8 Backward induction and SPE | 3 | [[Aula/Lecture03.pdf\|L3]] | 18 items |
| T8 SPE and subgames, T9 Commitment and credibility (Brexit case), T12 repeated games: definition | 4 | [[Aula/Lecture04.pdf\|L4]] | 12 items |
| T12 Repeated games (finite and infinite, grim trigger, tit-for-tat), T10 one-stage deviation | 5 | [[Aula/Lecture05.pdf\|L5]] | 25 items |
| T11 Bargaining (announced for L5, not in its slides), T13 Collusion, T14 Reputation | 6, estimate | — | 28 items |
| T15 Bayesian games, T16 Adverse selection, T17 Auctions | 7, estimate | — | 24 items |
| T18 PBE, T19 Signaling | 8, estimate | — | 25 items |

Shared rules for every topic: [[rules/game-theory|Game theory rules]] (specify the game
completely, name the solution concept, check existence and multiplicity, repeated ≠ one-shot,
common vs. mutual knowledge).

---

## Topic: Normal-form games and solution concepts
#topic/normal-form

**T1** · **Lectures:** 1
**Complexity:** foundational
**Prerequisites:** — (decision-theory background: [[Map/books-index#Ch. 1 — The Single-Person Decision Problem (pp. 3–13)|Tadelis Ch. 1]], [[Map/books-index#Ch. 2 — Introducing Uncertainty and Time (pp. 14–40)|Ch. 2]])
**Cross-topic links:** [[#Topic: Dominance and IESDS|T2]], [[#Topic: Nash equilibrium|T4]], [[#Topic: Extensive form, strategies and information|T7]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§3.1 — Normal-Form Games with Pure Strategies (p. 46)|Tadelis §3.1 (pp. 46–50)]] · [[Map/books-index#§3.2 — Matrix Representation: Two-Player Finite Game (p. 50)|§3.2 (pp. 50–52)]] · [[Map/books-index#§3.3 — Solution Concepts (p. 52)|§3.3 (pp. 52–57; Pareto, Def. 3.5 p. 57)]] · [[Map/books-index#§1.1 — Basic Theory: Normal-Form Games and Nash Equilibrium (p. 2)|Gibbons §1.1.A (pp. 2–4)]] · formal: [[Map/books-index#§7.D — Strategies and the Normal Form Representation of a Game (p. 228)|MWG §7.D (pp. 228–231)]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture01.pdf|Lecture 1 slides]] · notes [[Notas/L01/L01-00-map|L01 map]], [[Notas/L01/L01-01-games-normal-form|games and the normal form]], [[Notas/L01/L01-02-information-and-strategies|information and strategies]], [[Notas/L01/L01-03-solution-concepts|solution concepts]], [[Notas/L01/L01-05-pareto-social-dilemmas|Pareto and social dilemmas]] · [[Notas/L01/L01-notes.pdf|L01 notes PDF]]
3. 📝 Rules (Medium): [[rules/game-theory|Game theory rules]] (Non-negotiable 1–2) · [[Notas/L01/L01-09-formulas|L01 formula sheet]] · [[Notas/L01/L01-10-pitfalls|L01 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-01#1. Tadelis 3.2|L1 #1 Tadelis 3.2]] · [[Listas/pratica-lecture-01#2. Tadelis 3.4|L1 #2 Tadelis 3.4]] · [[Listas/pratica-lecture-01#3. Muñoz-Garcia Ex. 2|L1 #3 Muñoz-Garcia Ch. 1 Ex. 2]] · [[Listas/pratica-lecture-01#4. Muñoz-Garcia Ex. 5|L1 #4 Muñoz-Garcia Ch. 1 Ex. 5]] · [[Listas/pratica-lecture-01#9. Tadelis 3.6|L1 #9 Tadelis 3.6]] · [[Listas/pratica-lecture-01#10. Tadelis 3.7|L1 #10 Tadelis 3.7]]
5. ✏️ Integrating exercises (Hard): [[Listas/lista-lecture-01.pdf|Lecture 1 exam-style list]] Question 2 (dominance × Pareto × social dilemmas) and Question 6 (normal form × dominance and IESDS × Pareto) · [[Listas/pratica-lecture-01#13. MWG 8.B.1|L1 #13 MWG 8.B.1]]
6. 🧪 Quiz: [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#nf|L1-1 nf (3)]] · [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#strategy|strategy (1)]] · [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#ck|ck (2)]] · [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#payoffs|payoffs (4)]] · [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#pareto|L1-2 pareto (2)]] · [[Simulados/quiz-topic-T01-normal-form-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-01-audio-part1|L1 audio part 1]] · [[Leituras/lecture-01-notes-narrated.txt|L1 narration]]
8. 🗂️ Cases: [[Resolucao/mini-case-lecture-01.pdf|Mini case L1, the pharmacy]] part (a), normal form and payoff formula · [[Cases/Brexit/brexit-game.pdf|Brexit case]] sections (i)–(iv), specifying players, timing, information and payoffs

**Cross-topic synthesis (Hard):**
- With [[#Topic: Dominance and IESDS|T2]]: Pareto failure of a dominant-strategy equilibrium, [[Map/books-index#§4.1 — Dominance in Pure Strategies (p. 59)|Tadelis §4.1.3 (pp. 62–63)]]; exam-style list Question 2.
- With [[#Topic: Extensive form, strategies and information|T7]]: the normal form of a tree, [[Map/books-index#§7.2 — Strategies and Nash Equilibrium (p. 137)|Tadelis §7.2.3 (p. 143)]]; [[Listas/pratica-lecture-03#6. Tadelis 7.6|L3 #6 Tadelis 7.6]], [[Listas/pratica-lecture-03#9. Tadelis 7.9|L3 #9 Tadelis 7.9]].

## Topic: Dominance and IESDS
#topic/dominance-iesds

**T2** · **Lectures:** 1 (revisited in 2)
**Complexity:** foundational
**Prerequisites:** [[#Topic: Normal-form games and solution concepts|T1]]
**Cross-topic links:** [[#Topic: Best responses and rationalizability|T3]], [[#Topic: Nash equilibrium|T4]], [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]], [[#Topic: Auctions|T17]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§4.1 — Dominance in Pure Strategies (p. 59)|Tadelis §4.1 (pp. 59–63)]] · [[Map/books-index#§4.2 — Iterated Elimination of Strictly Dominated Pure Strategies (p. 63)|§4.2 (pp. 63–69)]] · [[Map/books-index#§1.1 — Basic Theory: Normal-Form Games and Nash Equilibrium (p. 2)|Gibbons §1.1.B (pp. 4–7)]] · formal: [[Map/books-index#§8.B — Dominant and Dominated Strategies (p. 236)|MWG §8.B (pp. 236–241)]] · drill: [[Map/books-index#Ch. 1 — Dominance Solvable Games (pp. 1–36) · Lecture 1 · Exercises 1–17|Muñoz-Garcia Ch. 1]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture01.pdf|Lecture 1 slides]] · notes [[Notas/L01/L01-04-dominance|dominance]], [[Notas/L01/L01-06-iesds|IESDS]], [[Notas/L01/L01-07-cournot-iesds|Cournot by IESDS]], [[Notas/L02/L02-08-iesds-rationalizability-revisited|IESDS revisited with mixed strategies]]
3. 📝 Rules (Medium): [[Notas/L01/L01-09-formulas|L01 formula sheet]] · [[Notas/L01/L01-10-pitfalls|L01 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-01#5. Muñoz-Garcia Ex. 13|L1 #5 Muñoz-Garcia Ch. 1 Ex. 13]] · [[Listas/pratica-lecture-01#6. Tadelis 4.5|L1 #6 Tadelis 4.5]] · [[Listas/pratica-lecture-01#7. Gibbons 1.2|L1 #7 Gibbons 1.2]] · [[Listas/pratica-lecture-01#8. Muñoz-Garcia Ex. 9|L1 #8 Muñoz-Garcia Ch. 1 Ex. 9]] · [[Listas/pratica-lecture-01#11. Tadelis 4.1|L1 #11 Tadelis 4.1]] · [[Listas/pratica-lecture-01#12. Tadelis 4.2|L1 #12 Tadelis 4.2]] · [[Listas/pratica-lecture-01#14. Muñoz-Garcia Ex. 12|L1 #14 Muñoz-Garcia Ch. 1 Ex. 12]] · [[Listas/pratica-lecture-01#15. Tadelis 4.6|L1 #15 Tadelis 4.6]] · [[Listas/pratica-lecture-01#16. Tadelis 4.7|L1 #16 Tadelis 4.7]] · real-exercise list items 1–6 ([[Listas/roteiro-lectures-01-04|roteiro]], [[Listas/lista-reais-lectures-01-04.pdf|list]], [[Listas/lista-reais-lectures-01-04-solutions.pdf|solutions]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-01#19. Muñoz-Garcia Ex. 16|L1 #19 Muñoz-Garcia Ch. 1 Ex. 16]] · [[Listas/pratica-lecture-01#20. MWG 8.B.4|L1 #20 MWG 8.B.4]] · [[Listas/pratica-lecture-01#21. MWG 8.B.5|L1 #21 MWG 8.B.5]] · [[Listas/pratica-lecture-01#22. MWG 8.B.7|L1 #22 MWG 8.B.7]] · [[Listas/lista-lecture-01.pdf|exam-style list]] Question 4 (IESDS × common knowledge of rationality)
6. 🧪 Quiz: [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#dom|L1-2 dom (2)]] · [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#partnership|partnership (4)]] · [[Simulados/quiz-lecture01-3-iesds-2026-10-13#props|L1-3 props (3)]] · [[Simulados/quiz-lecture01-3-iesds-2026-10-13#ck|ck (1)]] · [[Simulados/quiz-lecture01-3-iesds-2026-10-13#cournot|cournot (4)]] · [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#iesds|L2-1 iesds (3)]] · [[Simulados/quiz-topic-T02-dominance-iesds-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-01-audio-part1|L1 audio part 1]] (dominance) · [[NotebookLM/audio/lecture-01-audio-part2|part 2]] (IESDS) · [[Leituras/lecture-01-notes-narrated.txt|L1 narration]]
8. 🗂️ Cases: [[Resolucao/mini-case-lecture-01.pdf|Mini case L1, the pharmacy]] parts (b)–(c), block 1 dominated and the IESDS rounds · [[Listas/prep-mini-case-lecture-01|mini case prep]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]: Cournot by IESDS, [[Map/books-index#§4.2 — Iterated Elimination of Strictly Dominated Pure Strategies (p. 63)|Tadelis §4.2.2 (p. 65)]]; [[Listas/pratica-lecture-01#21. MWG 8.B.5|L1 #21 MWG 8.B.5]]; location games [[Listas/pratica-lecture-01#18. Tadelis 4.10|L1 #18 Tadelis 4.10]], mini case L1, exam-style list Questions 5–6.
- With [[#Topic: Auctions|T17]]: [[Listas/pratica-lecture-01#17. Tadelis 4.3|L1 #17 Tadelis 4.3]], [[Listas/pratica-lecture-01#23. MWG 8.B.3|L1 #23 MWG 8.B.3]], [[Listas/pratica-lecture-01#24. Tadelis 4.4|L1 #24 Tadelis 4.4]].
- With [[#Topic: Nash equilibrium|T4]]: [[Listas/pratica-lecture-02#9. Tadelis 5.1|L2 #9 Tadelis 5.1]], [[Listas/pratica-lecture-02#11. Tadelis 5.3|L2 #11 Tadelis 5.3]], [[Listas/pratica-lecture-02#17. MWG 8.D.2|L2 #17 MWG 8.D.2]].
- With [[#Topic: Mixed strategies and existence|T6]]: dominance by mixed strategies, [[Map/books-index#§6.3 — IESDS and Rationalizability Revisited (p. 114)|Tadelis §6.3]]; [[Listas/pratica-lecture-03#15. Tadelis 6.3|L3 #15 Tadelis 6.3]].

## Topic: Best responses and rationalizability
#topic/rationalizability

**T3** · **Lectures:** 2
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Dominance and IESDS|T2]]
**Cross-topic links:** [[#Topic: Nash equilibrium|T4]], [[#Topic: Mixed strategies and existence|T6]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§4.3 — Beliefs, Best Response, and Rationalizability (p. 69)|Tadelis §4.3 (pp. 69–76)]] · [[Map/books-index#§6.3 — IESDS and Rationalizability Revisited (p. 114)|§6.3 (pp. 114–117)]] · formal: [[Map/books-index#§8.C — Rationalizable Strategies (p. 242)|MWG §8.C (pp. 242–245)]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture02.pdf|Lecture 2 slides]] · notes [[Notas/L02/L02-00-map|L02 map]], [[Notas/L02/L02-01-best-response-rationalizability|best responses and rationalizability]], [[Notas/L02/L02-08-iesds-rationalizability-revisited|IESDS and rationalizability revisited]] · [[Notas/L02/L02-notes.pdf|L02 notes PDF]]
3. 📝 Rules (Medium): [[Notas/L02/L02-10-formulas|L02 formula sheet]] · [[Notas/L02/L02-11-pitfalls|L02 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-02#3. Tadelis 5.5|L2 #3 Tadelis 5.5]] · [[Listas/pratica-lecture-02#18. MWG 8.C.1|L2 #18 MWG 8.C.1]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-02#9. Tadelis 5.1|L2 #9 Tadelis 5.1]] · [[Listas/pratica-lecture-02#11. Tadelis 5.3|L2 #11 Tadelis 5.3]] · [[Listas/pratica-lecture-02#17. MWG 8.D.2|L2 #17 MWG 8.D.2]] · [[Listas/pratica-lecture-03#14. Gibbons 1.14|L3 #14 Gibbons 1.14]]
6. 🧪 Quiz: [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#br|L2-1 br (3)]] · [[Simulados/quiz-topic-T03-rationalizability-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-02-audio-part1|L2 audio part 1]] · [[Leituras/lecture-02-notes-narrated.txt|L2 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Dominance and IESDS|T2]] and [[#Topic: Nash equilibrium|T4]]: the slides' Propositions 1–2 (unique IESDS survivor or unique rationalizable profile is the unique Nash equilibrium): L2 #9, #11, #17, #18.
- With [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]: the Cournot duopoly and the p-beauty contest revisited, [[Map/books-index#§4.3 — Beliefs, Best Response, and Rationalizability (p. 69)|Tadelis §4.3.4–4.3.5 (pp. 73–76)]].

## Topic: Nash equilibrium
#topic/nash-equilibrium

**T4** · **Lectures:** 2
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Best responses and rationalizability|T3]], [[#Topic: Dominance and IESDS|T2]]
**Cross-topic links:** [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]], [[#Topic: Mixed strategies and existence|T6]], [[#Topic: Backward induction and subgame perfection|T8]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§5.1 — Nash Equilibrium in Pure Strategies (p. 80)|Tadelis §5.1 (pp. 80–83)]] · [[Map/books-index#§5.2 — Nash Equilibrium: Some Classic Applications (p. 83)|§5.2.1 (pp. 83–84)]] · [[Map/books-index#§1.1 — Basic Theory: Normal-Form Games and Nash Equilibrium (p. 2)|Gibbons §1.1.C (pp. 8–14)]] · formal: [[Map/books-index#§8.D — Nash Equilibrium (p. 246)|MWG §8.D (pp. 246–253)]] · drill: [[Map/books-index#Ch. 2 — Pure Strategy Nash Equilibrium and Simultaneous-Move Games with Complete Information (pp. 37–84) · Lecture 2 · Exercises 1–17|Muñoz-Garcia Ch. 2]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture02.pdf|Lecture 2 slides]] · notes [[Notas/L02/L02-02-nash-equilibrium|Nash equilibrium]]
3. 📝 Rules (Medium): [[rules/game-theory|Game theory rules]] (Non-negotiable 3, existence and multiplicity) · [[Notas/L02/L02-10-formulas|L02 formula sheet]] · [[Notas/L02/L02-11-pitfalls|L02 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-02#1. Muñoz-Garcia Ex. 2 (Ch. 2)|L2 #1 Muñoz-Garcia Ch. 2 Ex. 2]] · [[Listas/pratica-lecture-02#2. Tadelis 5.6|L2 #2 Tadelis 5.6]] · [[Listas/pratica-lecture-02#4. Gibbons 1.3|L2 #4 Gibbons 1.3]] · [[Listas/pratica-lecture-02#10. Tadelis 5.2|L2 #10 Tadelis 5.2]] · real-exercise list items 2 and 7 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-02#9. Tadelis 5.1|L2 #9 Tadelis 5.1]] · [[Listas/pratica-lecture-02#11. Tadelis 5.3|L2 #11 Tadelis 5.3]] · [[Listas/pratica-lecture-02#17. MWG 8.D.2|L2 #17 MWG 8.D.2]] · [[Listas/pratica-lecture-02#19. MWG 8.D.3|L2 #19 MWG 8.D.3]]
6. 🧪 Quiz: [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#ne|L2-1 ne (2)]] · [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#iesds|iesds (3)]] · [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#matrix|matrix (2)]] · [[Simulados/quiz-topic-T04-nash-equilibrium-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-02-audio-part1|L2 audio part 1]] · [[Leituras/lecture-02-notes-narrated.txt|L2 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Dominance and IESDS|T2]]: Nash vs. IESDS (L2 #9, #11, #17); weakly dominated equilibria (L2 #10).
- With [[#Topic: Backward induction and subgame perfection|T8]]: Nash equilibria of a tree that are not subgame perfect, [[Listas/pratica-lecture-03#4. Tadelis 7.2|L3 #4 Tadelis 7.2]], [[Listas/pratica-lecture-03#12. Tadelis 8.10|L3 #12 Tadelis 8.10]], [[Listas/pratica-lecture-03#13. Tadelis 8.11|L3 #13 Tadelis 8.11]]; Brexit case, "A Nash equilibrium that is not subgame perfect".

## Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)
#topic/oligopoly

**T5** · **Lectures:** 1–3, 6
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Nash equilibrium|T4]] (and [[#Topic: Dominance and IESDS|T2]] for Cournot by IESDS)
**Cross-topic links:** [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]], [[#Topic: Collusion and price wars|T13]], [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§5.2 — Nash Equilibrium: Some Classic Applications (p. 83)|Tadelis §5.2.2–5.2.5 (pp. 84–95: commons, Cournot, Bertrand, Hotelling)]] · [[Map/books-index#§1.2 — Applications (p. 14)|Gibbons §1.2 (pp. 14–29)]] · [[Map/books-index#Ch. 7 — Games and Strategies (pp. 159–183)|Cabral §7.1 (p. 161)]] · formal: [[Map/books-index#§12.C — Static Models of Oligopoly (p. 387)|MWG §12.C (p. 387)]] · drill: [[Map/books-index#Ch. 5 — Applications to Industrial Organization (pp. 215–271) · Lectures 2–3, 6 · Exercises 1–16|Muñoz-Garcia Ch. 5]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture01.pdf|Lecture 1 slides]] (spatial competition) · [[Aula/Lecture02.pdf|Lecture 2 slides]] (slides 20–40) · notes [[Notas/L01/L01-07-cournot-iesds|Cournot by IESDS]], [[Notas/L01/L01-08-spatial-competition|spatial competition]], [[Notas/L02/L02-03-cournot|Cournot]], [[Notas/L02/L02-04-bertrand|Bertrand]], [[Notas/L02/L02-05-commons|commons]], [[Notas/L02/L02-06-hotelling-voting|Hotelling voting]]
3. 📝 Rules (Medium): [[Notas/L02/L02-10-formulas|L02 formula sheet]] · [[Notas/L02/L02-11-pitfalls|L02 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-02#5. Muñoz-Garcia Ex. 7 (Ch. 2)|L2 #5 Muñoz-Garcia Ch. 2 Ex. 7]] · [[Listas/pratica-lecture-02#12. Tadelis 5.8|L2 #12 Tadelis 5.8]] · [[Listas/pratica-lecture-02#13. Gibbons 1.5|L2 #13 Gibbons 1.5]] · [[Listas/pratica-lecture-02#14. Gibbons 1.6|L2 #14 Gibbons 1.6]] · [[Listas/pratica-lecture-02#15. Gibbons 1.7|L2 #15 Gibbons 1.7]] · [[Listas/pratica-lecture-02#22. Tadelis 5.15|L2 #22 Tadelis 5.15]] (reading item) · [[Listas/pratica-lecture-01#18. Tadelis 4.10|L1 #18 Tadelis 4.10]] · real-exercise list items 9 and 11 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-02#20. Tadelis 5.12|L2 #20 Tadelis 5.12]] · [[Listas/pratica-lecture-01#21. MWG 8.B.5|L1 #21 MWG 8.B.5]] · [[Listas/pratica-lecture-04#6. Tadelis 8.6|L4 #6 Tadelis 8.6]] · [[Listas/pratica-lecture-05#13. Tadelis 9.4|L5 #13 Tadelis 9.4]] · [[Listas/pratica-lecture-07#9. Tadelis 12.2|L7 #9 Tadelis 12.2]]
6. 🧪 Quiz: [[Simulados/quiz-lecture01-3-iesds-2026-10-13#cournot|L1-3 cournot (4)]] · [[Simulados/quiz-lecture01-3-iesds-2026-10-13#space|space (2)]] · [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cournot|L2-2 cournot (3)]] · [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cartel|cartel (3)]] · [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#bertrand|bertrand (2)]] · [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#compare|compare (2)]] · [[Simulados/quiz-topic-T05-oligopoly-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-01-audio-part2|L1 audio part 2]] (spatial competition) · [[NotebookLM/audio/lecture-02-audio-part1|L2 audio part 1]] (Cournot) · [[NotebookLM/audio/lecture-02-audio-part2|part 2]] (Bertrand) · [[Leituras/lecture-02-notes-narrated.txt|L2 narration]]
8. 🗂️ Cases: [[Resolucao/mini-case-lecture-01.pdf|Mini case L1, the pharmacy]] (location on a 7-block avenue, part (d) total walking distance) · [[Listas/lista-lecture-01.pdf|exam-style list]] Questions 5–6 (stations on a highway)

**Cross-topic synthesis (Hard):**
- With [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]: Stackelberg, [[Listas/pratica-lecture-04#4. Muñoz-Garcia Ex. 11|L4 #4 Muñoz-Garcia Ch. 4 Ex. 11]], [[Listas/pratica-lecture-04#8. Muñoz-Garcia Ex. 12|L4 #8 Muñoz-Garcia Ch. 4 Ex. 12]], [[Listas/pratica-lecture-04#7. Tadelis 8.4|L4 #7 Tadelis 8.4]]; [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#stack|L3-3 stack (4)]].
- With [[#Topic: Collusion and price wars|T13]]: the cartel as a prisoner's dilemma (L2 #13), one-shot cartels [[Listas/pratica-lecture-06#1. Muñoz-Garcia Ch. 5 Ex. 4|L6 #1]], [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 5 Ex. 5 (L6 further practice / dropped, not in the tiers)]], [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 5 Ex. 8 (L6 further practice / dropped, not in the tiers)]].
- With [[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]]: a Cournot first stage, [[Listas/pratica-lecture-05#13. Tadelis 9.4|L5 #13 Tadelis 9.4]], [[Listas/pratica-lecture-05#19. Tadelis 9.6|L5 #19 Tadelis 9.6]].
- With [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]: Cournot with private costs and Bertrand with private demand, L7 #9, [[Listas/pratica-lecture-07#10. Gibbons 3.3|L7 #10 Gibbons 3.3]]; [[Map/books-index#§3.1 — Theory: Static Bayesian Games and Bayesian Nash Equilibrium (p. 144)|Gibbons §3.1.A (p. 144)]].

## Topic: Mixed strategies and existence
#topic/mixed-strategies

**T6** · **Lectures:** 2–3
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Nash equilibrium|T4]] (expected payoffs: [[Map/books-index#§2.2 — Evaluating Random Outcomes (p. 18)|Tadelis §2.2]])
**Cross-topic links:** [[#Topic: Best responses and rationalizability|T3]], [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]], [[#Topic: Auctions|T17]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§6.1 — Strategies, Beliefs, and Expected Payoffs (p. 102)|Tadelis §6.1 (pp. 102–107)]] · [[Map/books-index#§6.2 — Mixed-Strategy Nash Equilibrium (p. 107)|§6.2 (pp. 107–114)]] · [[Map/books-index#§6.4 — Nash's Existence Theorem (p. 117)|§6.4 (pp. 117–123)]] · [[Map/books-index#§1.3 — Advanced Theory: Mixed Strategies and Existence of Equilibrium (p. 29)|Gibbons §1.3 (pp. 29–48)]] · formal: [[Map/books-index#§7.E — Randomized Choices (p. 231)|MWG §7.E]], [[Map/books-index#§8.D — Nash Equilibrium (p. 246)|§8.D]], [[Map/books-index#§8.F — The Possibility of Mistakes: Trembling-Hand Perfection (p. 258) · Appendix A — Existence of Nash Equilibrium (p. 260)|App. A (p. 260)]] · drill: [[Map/books-index#Ch. 3 — Mixed Strategies, Strictly Competitive Games, and Correlated Equilibria (pp. 85–151) · Lecture 2 · Exercises 1–18|Muñoz-Garcia Ch. 3]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture02.pdf|Lecture 2 slides]] (slides 42–51) · notes [[Notas/L02/L02-07-mixed-strategies|mixed strategies]], [[Notas/L02/L02-09-existence|existence]]
3. 📝 Rules (Medium): [[Notas/L02/L02-10-formulas|L02 formula sheet]] · [[Notas/L02/L02-11-pitfalls|L02 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-02#6. Muñoz-Garcia Ex. 1 (Ch. 3)|L2 #6 Muñoz-Garcia Ch. 3 Ex. 1]] · [[Listas/pratica-lecture-02#7. Tadelis 6.1|L2 #7 Tadelis 6.1]] · [[Listas/pratica-lecture-02#8. Gibbons 1.12|L2 #8 Gibbons 1.12]] · [[Listas/pratica-lecture-03#1. Tadelis 6.5|L3 #1 Tadelis 6.5]] · [[Listas/pratica-lecture-02#16. Tadelis 6.8|L2 #16 Tadelis 6.8]] · real-exercise list items 8, 10, 12 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-03#14. Gibbons 1.14|L3 #14 Gibbons 1.14]] · [[Listas/pratica-lecture-02#21. MWG 8.D.6|L2 #21 MWG 8.D.6]] · [[Listas/pratica-lecture-03#15. Tadelis 6.3|L3 #15 Tadelis 6.3]] · [[Listas/pratica-lecture-01#22. MWG 8.B.7|L1 #22 MWG 8.B.7]]
6. 🧪 Quiz: [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#mixed|L2-3 mixed (2)]] · [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#indiff|indiff (3)]] · [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#bos|bos (3)]] · [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#exist|exist (2)]] · [[Simulados/quiz-topic-T06-mixed-strategies-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-02-audio-part2|L2 audio part 2]] · [[Leituras/lecture-02-notes-narrated.txt|L2 narration]]
8. 🗂️ Cases: [[Resolucao/mini-case-lecture-03.pdf|Mini case L3, work or shirk]] (inspection game: (a) no pure equilibrium, (b) the mixed equilibrium, (c)–(d) monitoring cost and wage) · [[Resolucao/mini-case-lecture-03-short.pdf|short version]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]: purification, [[Map/books-index#§12.5 — Mixed Strategies Revisited: Harsanyi's Interpretation (p. 264)|Tadelis §12.5]]; [[Listas/pratica-lecture-07#12. Tadelis 12.9|L7 #12 Tadelis 12.9]]; [[Notas/L07/L07-04-threshold-strategies-purification|L07 purification note]]; [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#threshold|L7-1 threshold (3)]].
- With [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]: mini case L3 part (e), "The commitment variant" (a hard-wired audit rate).
- With [[#Topic: Auctions|T17]]: mixed bids, [[Listas/pratica-lecture-07#23. Tadelis 13.5|L7 #23 Tadelis 13.5]].
- With [[#Topic: Signaling and refinements|T19]]: mixed and semi-separating PBE, [[Listas/pratica-lecture-08#9. Gibbons 4.2|L8 #9 Gibbons 4.2]], [[Listas/pratica-lecture-08#11. Muñoz-Garcia Ch. 9 Ex. 5|L8 #11 Muñoz-Garcia Ch. 9 Ex. 5]].

## Topic: Extensive form, strategies and information
#topic/extensive-form

**T7** · **Lectures:** 3
**Complexity:** foundational
**Prerequisites:** [[#Topic: Normal-form games and solution concepts|T1]]
**Cross-topic links:** [[#Topic: Backward induction and subgame perfection|T8]], [[#Topic: Perfect Bayesian equilibrium|T18]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§7.1 — The Extensive-Form Game (p. 130)|Tadelis §7.1 (pp. 130–137)]] · [[Map/books-index#§7.2 — Strategies and Nash Equilibrium (p. 137)|§7.2 (pp. 137–144)]] · [[Map/books-index#§7.3 — Nash Equilibrium and Paths of Play (p. 145)|§7.3 (pp. 145–146)]] · [[Map/books-index#§2.4 — Dynamic Games of Complete but Imperfect Information (p. 115)|Gibbons §2.4.A (pp. 115–122)]] · formal: [[Map/books-index#§7.C — The Extensive Form Representation of a Game (p. 221)|MWG §7.C (pp. 221–225)]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture03.pdf|Lecture 3 slides]] · notes [[Notas/L03/L03-00-map|L03 map]], [[Notas/L03/L03-01-extensive-form|extensive form]], [[Notas/L03/L03-02-strategies|strategies]], [[Notas/L03/L03-03-normal-form-and-paths|normal form and paths of play]] · [[Notas/L03/L03-notes.pdf|L03 notes PDF]]
3. 📝 Rules (Medium): [[rules/game-theory|Game theory rules]] (Non-negotiable 1) · [[Notas/L03/L03-09-formulas|L03 formula sheet]] · [[Notas/L03/L03-10-pitfalls|L03 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-03#2. Tadelis 7.1|L3 #2 Tadelis 7.1]] · [[Listas/pratica-lecture-03#4. Tadelis 7.2|L3 #4 Tadelis 7.2]] · [[Listas/pratica-lecture-03#6. Tadelis 7.6|L3 #6 Tadelis 7.6]] · [[Listas/pratica-lecture-03#8. Tadelis 7.4|L3 #8 Tadelis 7.4]] · [[Listas/pratica-lecture-03#9. Tadelis 7.9|L3 #9 Tadelis 7.9]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-03#10. Tadelis 7.10|L3 #10 Tadelis 7.10]] · [[Listas/pratica-lecture-03#18. MWG 9.B.5|L3 #18 MWG 9.B.5]]
6. 🧪 Quiz: [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#tree|L3-1 tree (4)]] · [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#strat|strat (3)]] · [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#nfpath|nfpath (3)]] · [[Simulados/quiz-topic-T07-extensive-form-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-03-audio-part1|L3 audio part 1]] · [[Leituras/lecture-03-notes-narrated.txt|L3 narration]]
8. 🗂️ Cases: [[Cases/Brexit/brexit-game.pdf|Brexit case]] sections (ii) timing and actions, (iii) information, (v) the game tree

**Cross-topic synthesis (Hard):**
- With [[#Topic: Normal-form games and solution concepts|T1]]: trees to matrices, [[Listas/pratica-lecture-01#3. Muñoz-Garcia Ex. 2|L1 #3]], [[Listas/pratica-lecture-01#4. Muñoz-Garcia Ex. 5|L1 #4]]; [[Map/books-index#Ch. 1 — Dominance Solvable Games (pp. 1–36) · Lecture 1 · Exercises 1–17|Muñoz-Garcia Ch. 1 Ex. 1–4]].
- With [[#Topic: Perfect Bayesian equilibrium|T18]]: information sets that are not singletons make subgames scarce, [[Map/books-index#§15.1 — The Problem with Subgame Perfection (p. 303)|Tadelis §15.1]].

## Topic: Backward induction and subgame perfection
#topic/spe

**T8** · **Lectures:** 3
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Extensive form, strategies and information|T7]], [[#Topic: Nash equilibrium|T4]]
**Cross-topic links:** [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]], [[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]], [[#Topic: Strategic bargaining|T11]], [[#Topic: Perfect Bayesian equilibrium|T18]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§8.1 — Sequential Rationality and Backward Induction (p. 152)|Tadelis §8.1 (pp. 152–153)]] · [[Map/books-index#§8.2 — Subgame-Perfect Nash Equilibrium: Concept (p. 153)|§8.2 (pp. 153–159)]] · [[Map/books-index#§8.3 — Subgame-Perfect Nash Equilibrium: Examples (p. 159)|§8.3.1 centipede (p. 159)]] · [[Map/books-index#§2.1 — Dynamic Games of Complete and Perfect Information (p. 57)|Gibbons §2.1.A (pp. 57–61)]] · [[Map/books-index#§2.2 — Two-Stage Games of Complete but Imperfect Information (p. 71)|§2.2.A (pp. 71–73)]] · [[Map/books-index#§2.4 — Dynamic Games of Complete but Imperfect Information (p. 115)|§2.4.B (pp. 122–129)]] · formal: [[Map/books-index#§9.B — Sequential Rationality, Backward Induction, and Subgame Perfection (p. 268)|MWG §9.B (pp. 268–281)]] · drill: [[Map/books-index#Ch. 4 — Sequential-Move Games with Complete Information (pp. 153–214) · Lectures 3–4 · Exercises 1–21|Muñoz-Garcia Ch. 4]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture03.pdf|Lecture 3 slides]] · notes [[Notas/L03/L03-04-sequential-rationality-backward-induction|sequential rationality and backward induction]], [[Notas/L03/L03-05-subgame-perfection|subgame perfection]]
3. 📝 Rules (Medium): [[rules/game-theory|Game theory rules]] (Non-negotiable 2) · [[Notas/L03/L03-09-formulas|L03 formula sheet]] · [[Notas/L03/L03-10-pitfalls|L03 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-03#3. Muñoz-Garcia Ex. 3|L3 #3 Muñoz-Garcia Ch. 4 Ex. 3]] · [[Listas/pratica-lecture-03#5. Muñoz-Garcia Ex. 4|L3 #5 Muñoz-Garcia Ch. 4 Ex. 4]] · [[Listas/pratica-lecture-03#7. Muñoz-Garcia Ex. 9|L3 #7 Muñoz-Garcia Ch. 4 Ex. 9]] · [[Listas/pratica-lecture-03#11. Tadelis 8.5|L3 #11 Tadelis 8.5]] · [[Listas/pratica-lecture-03#12. Tadelis 8.10|L3 #12 Tadelis 8.10]] · [[Listas/pratica-lecture-03#13. Tadelis 8.11|L3 #13 Tadelis 8.11]] · real-exercise list items 13–15, 18 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-03#16. MWG 9.B.4|L3 #16 MWG 9.B.4]] · [[Listas/pratica-lecture-03#18. MWG 9.B.5|L3 #18 MWG 9.B.5]] · [[Listas/pratica-lecture-03#17. Gibbons 2.1|L3 #17 Gibbons 2.1]] · [[Listas/pratica-lecture-06#3. Tadelis 11.1|L6 #3 Tadelis 11.1]]
6. 🧪 Quiz: [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#bi|L3-2 bi (4)]] · [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#subg|subg (2)]] · [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#spe|spe (4)]] · [[Simulados/quiz-topic-T08-backward-induction-spe-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-03-audio-part1|L3 audio part 1]] · [[Leituras/lecture-03-notes-narrated.txt|L3 narration]]
8. 🗂️ Cases: [[Cases/Brexit/brexit-game.pdf|Brexit case]] section (vi), backward induction in three steps, and "A Nash equilibrium that is not subgame perfect"; "Sensitivity" for comparative statics of the SPE

**Cross-topic synthesis (Hard):**
- With [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]: non-credible threats in entry games, [[Listas/pratica-lecture-04#1. Tadelis 8.8|L4 #1 Tadelis 8.8]], [[Listas/pratica-lecture-04#10. Tadelis 8.7|L4 #10 Tadelis 8.7]].
- With [[#Topic: Strategic bargaining|T11]]: Nash vs. SPE in bargaining, L6 #3; complete SPNE strategies vs. outcome, [[Listas/pratica-lecture-06#11. Gibbons 2.19|L6 #11 Gibbons 2.19]].
- With [[#Topic: Perfect Bayesian equilibrium|T18]]: where subgame perfection fails, [[Map/books-index#§15.1 — The Problem with Subgame Perfection (p. 303)|Tadelis §15.1]]; [[Listas/pratica-lecture-08#2. Gibbons 4.1|L8 #2 Gibbons 4.1]].

## Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)
#topic/commitment

**T9** · **Lectures:** 3–4
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Backward induction and subgame perfection|T8]]
**Cross-topic links:** [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]], [[#Topic: Strategic bargaining|T11]], [[#Topic: Signaling and refinements|T19]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§8.3 — Subgame-Perfect Nash Equilibrium: Examples (p. 159)|Tadelis §8.3.2–8.3.4 (pp. 160–169: Stackelberg, mutually assured destruction, time inconsistency)]] · [[Map/books-index#§2.1 — Dynamic Games of Complete and Perfect Information (p. 57)|Gibbons §2.1.B (pp. 61–64)]] · [[Map/books-index#Ch. 7 — Games and Strategies (pp. 159–183)|Cabral §7.2 (pp. 167–172)]] · formal: [[Map/books-index#§12.G — Strategic Precommitments to Affect Future Competition (p. 414)|MWG §12.G (p. 414)]], [[Map/books-index#Ch. 12, Appendix B — Strategic Entry Deterrence and Accommodation (p. 423)|App. B (p. 423)]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture03.pdf|Lecture 3 slides]] · notes [[Notas/L03/L03-06-credibility-entry-commitment|credibility, entry and commitment]], [[Notas/L03/L03-07-stackelberg|Stackelberg]], [[Notas/L03/L03-08-time-inconsistency|time inconsistency]]
3. 📝 Rules (Medium): [[Notas/L03/L03-09-formulas|L03 formula sheet]] · [[Notas/L03/L03-10-pitfalls|L03 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-04#1. Tadelis 8.8|L4 #1 Tadelis 8.8]] · [[Listas/pratica-lecture-04#4. Muñoz-Garcia Ex. 11|L4 #4 Muñoz-Garcia Ch. 4 Ex. 11]] · [[Listas/pratica-lecture-04#5. Tadelis 8.13|L4 #5 Tadelis 8.13]] · [[Listas/pratica-lecture-04#6. Tadelis 8.6|L4 #6 Tadelis 8.6]] · [[Listas/pratica-lecture-04#8. Muñoz-Garcia Ex. 12|L4 #8 Muñoz-Garcia Ch. 4 Ex. 12]] · [[Listas/pratica-lecture-04#9. Tadelis 8.15|L4 #9 Tadelis 8.15]] · real-exercise list items 16–17 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-04#10. Tadelis 8.7|L4 #10 Tadelis 8.7]] · [[Listas/pratica-lecture-04#11. Tadelis 8.12|L4 #11 Tadelis 8.12]] · [[Listas/pratica-lecture-04#7. Tadelis 8.4|L4 #7 Tadelis 8.4]] · [[Listas/pratica-lecture-04#12. Tadelis 8.16|L4 #12 Tadelis 8.16]] · [[Listas/pratica-lecture-04#3. Gibbons 2.6|L4 #3 Gibbons 2.6]]
6. 🧪 Quiz: [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#cred|L3-3 cred (4)]] · [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#stack|stack (4)]] · [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#timeinc|timeinc (2)]] · [[Simulados/quiz-topic-T09-commitment-credibility-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-03-audio-part2|L3 audio part 2]] · [[Leituras/lecture-03-notes-narrated.txt|L3 narration]]
8. 🗂️ Cases: [[Cases/Brexit/brexit-game.pdf|Brexit case]] (no-deal preparation as a commitment; "The unobservable variant: commitment must be seen"; "Efficiency: preparation as rent-shifting") · [[Resolucao/mini-case-lecture-03.pdf|Mini case L3]] part (e), "The commitment variant"

**Cross-topic synthesis (Hard):**
- With [[#Topic: Strategic bargaining|T11]]: holdup after a sunk investment, [[Listas/pratica-lecture-04#5. Tadelis 8.13|L4 #5 Tadelis 8.13]] and [[Listas/pratica-lecture-06#10. Tadelis 11.2|L6 #10 Tadelis 11.2]]; Brexit case (commitment that shifts the bargaining split).
- With [[#Topic: Signaling and refinements|T19]]: entry deterrence under private information (limit pricing), [[Listas/pratica-lecture-08#13. Tadelis 16.3|L8 #13 Tadelis 16.3]], [[Listas/pratica-lecture-08#14. Muñoz-Garcia Ch. 11 Ex. 5|L8 #14 Muñoz-Garcia Ch. 11 Ex. 5]].
- With [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]: Stackelberg vs. Cournot, see T5.

## Topic: Multistage games (carrot and stick, one-stage deviation)
#topic/multistage

**T10** · **Lectures:** 4
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Backward induction and subgame perfection|T8]], [[#Topic: Nash equilibrium|T4]]
**Cross-topic links:** [[#Topic: Repeated games and the folk theorem|T12]], [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§9.1 — Preliminaries (p. 176) · §9.2 — Payoffs (p. 177) · §9.3 — Strategies and Conditional Play (p. 178)|Tadelis §9.1–9.3 (pp. 176–180)]] · [[Map/books-index#§9.4 — Subgame-Perfect Equilibria (p. 180)|§9.4 (pp. 180–184)]] · [[Map/books-index#§9.5 — The One-Stage Deviation Principle (p. 184)|§9.5 (pp. 184–186)]] · [[Map/books-index#§2.2 — Two-Stage Games of Complete but Imperfect Information (p. 71)|Gibbons §2.2 (pp. 71–82: bank runs, tariffs, tournaments)]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L04/L04-00-map|L04 map]], [[Notas/L04/L04-01-multistage-games|multistage games]], [[Notas/L04/L04-02-carrot-and-stick|carrot and stick]], [[Notas/L04/L04-03-one-stage-deviation|one-stage deviation]], [[Notas/L04/L04-04-two-stage-applications|two-stage applications]] · [[Notas/L04/L04-notes.pdf|L04 notes PDF]]
3. 📝 Rules (Medium): [[Notas/L04/L04-10-formulas|L04 formula sheet]] · [[Notas/L04/L04-11-pitfalls|L04 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-05#17. Tadelis 9.1|L5 #17 Tadelis 9.1]] · [[Listas/pratica-lecture-05#8. Tadelis 9.3|L5 #8 Tadelis 9.3]] · [[Listas/pratica-lecture-05#4. Gibbons 2.22|L5 #4 Gibbons 2.22]] · [[Listas/pratica-lecture-04#3. Gibbons 2.6|L4 #3 Gibbons 2.6]] · [[Listas/pratica-lecture-05#3. Muñoz-Garcia Ex. 18|L5 #3 Muñoz-Garcia Ch. 4 Ex. 18]] · [[Listas/pratica-lecture-05#12. Tadelis 9.2|L5 #12 Tadelis 9.2]] · real-exercise list items 19–21 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-05#13. Tadelis 9.4|L5 #13 Tadelis 9.4]] · [[Listas/pratica-lecture-05#19. Tadelis 9.6|L5 #19 Tadelis 9.6]] · [[Listas/pratica-lecture-05#22. Tadelis 9.5|L5 #22 Tadelis 9.5]] · [[Listas/pratica-lecture-05#23. Gibbons 2.8|L5 #23 Gibbons 2.8]]
6. 🧪 Quiz: [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#msg|L4-1 msg (2)]] · [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#cs|cs (4)]] · [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#osd|osd (2)]] · [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#app|app (2)]] · [[Simulados/quiz-topic-T10-multistage-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-04-audio-part1|L4 audio part 1]] · [[Leituras/lecture-04-notes-narrated.txt|L4 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Repeated games and the folk theorem|T12]]: two-stage repeated games and carrot and stick, [[Map/books-index#§2.3 — Repeated Games (p. 82)|Gibbons §2.3.A (pp. 82–88)]]; [[Listas/pratica-lecture-05#11. Gibbons 2.10|L5 #11 Gibbons 2.10]], [[Listas/pratica-lecture-05#16. Gibbons 2.11|L5 #16 Gibbons 2.11]].
- With [[#Topic: Collusion and price wars|T13]]: sustaining the monopoly split in a Cournot first stage, L5 #13.

## Topic: Strategic bargaining
#topic/bargaining

**T11** · **Lectures:** 4
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Backward induction and subgame perfection|T8]] ([[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]] for the one-stage deviation check)
**Cross-topic links:** [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]], [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§11.1 — One Round of Bargaining: The Ultimatum Game (p. 222)|Tadelis §11.1 (pp. 222–224)]] · [[Map/books-index#§11.2 — Finitely Many Rounds of Bargaining (p. 224)|§11.2 (pp. 224–227)]] · [[Map/books-index#§11.3 — The Infinite-Horizon Game (p. 228)|§11.3 (pp. 228–229)]] · [[Map/books-index#§11.4 — Application: Legislative Bargaining (p. 229)|§11.4 (pp. 229–235)]] · [[Map/books-index#§2.1 — Dynamic Games of Complete and Perfect Information (p. 57)|Gibbons §2.1.D (pp. 68–71)]] · formal: [[Map/books-index#Ch. 9, Appendix A — Finite and Infinite Horizon Bilateral Bargaining (p. 296)|MWG Ch. 9 App. A (pp. 296–298)]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L04/L04-05-ultimatum-game|ultimatum game]], [[Notas/L04/L04-06-finite-alternating-offers|finite alternating offers]], [[Notas/L04/L04-07-rubinstein-infinite-horizon|Rubinstein]], [[Notas/L04/L04-08-legislative-bargaining|legislative bargaining]], [[Notas/L04/L04-09-bargaining-private-information|bargaining with private information]]
3. 📝 Rules (Medium): [[rules/02_barganha|Topic 2 — Bargaining]] (alternating offers) · [[Notas/L04/L04-10-formulas|L04 formula sheet]] · [[Notas/L04/L04-11-pitfalls|L04 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-06#3. Tadelis 11.1|L6 #3 Tadelis 11.1]] · [[Listas/pratica-lecture-06#4. Muñoz-Garcia Ex. 1|L6 #4 Muñoz-Garcia Ch. 4 Ex. 1]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ex. 16 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ex. 17 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#10. Tadelis 11.2|L6 #10 Tadelis 11.2]] · [[Listas/pratica-lecture-06#8. Tadelis 11.3|L6 #8 Tadelis 11.3]] · [[Listas/pratica-lecture-06|Tadelis 11.4 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#12. Tadelis 11.5|L6 #12 Tadelis 11.5]] · [[Listas/pratica-lecture-06#11. Gibbons 2.19|L6 #11 Gibbons 2.19]] · [[Listas/pratica-lecture-06|Tadelis 11.6 (L6 further practice / dropped, not in the tiers)]] · real-exercise list items 22–24 ([[Listas/roteiro-lectures-01-04|roteiro]])
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-06#19. Gibbons 2.20|L6 #19 Gibbons 2.20]] · [[Listas/pratica-lecture-06|MWG 9.B.12 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06|MWG 9.B.13 (with 9.B.7, which it builds on) (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 6 Ex. 8 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#24. Tadelis 11.7|L6 #24 Tadelis 11.7]]
6. 🧪 Quiz: [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#ult|L4-2 ult (3)]] · [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#fin|fin (5)]] · [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#lim|lim (2)]] · [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#rub|L4-3 rub (4)]] · [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#pat|pat (2)]] · [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#leg|leg (3)]] · [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#inf|inf (1)]] · [[Simulados/quiz-topic-T11-bargaining-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-04-audio-part2|L4 audio part 2]] · [[Leituras/lecture-04-notes-narrated.txt|L4 narration]]
8. 🗂️ Cases: [[Cases/Brexit/brexit-game.pdf|Brexit case]] (the EU's offer and the UK's present/reject decisions; "In-class decision guide"; (vii) comparing the equilibrium with your negotiation)

**Cross-topic synthesis (Hard):**
- With [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]: holdup (L4 #13, L3 #15); the Brexit case.
- With [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]] and [[#Topic: Perfect Bayesian equilibrium|T18]]: bargaining under private information, [[Map/books-index#§4.3 — Other Applications of Perfect Bayesian Equilibrium (p. 210)|Gibbons §4.3.B (p. 218)]]; [[Notas/L04/L04-09-bargaining-private-information|L04 note]]; [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#inf|L4-3 inf (1)]].

## Topic: Repeated games and the folk theorem
#topic/repeated-games

**T12** · **Lectures:** 5
**Complexity:** advanced
**Prerequisites:** [[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]] (discounting: [[Map/books-index#§2.4 — Decisions over Time (p. 26)|Tadelis §2.4.2]])
**Cross-topic links:** [[#Topic: Collusion and price wars|T13]], [[#Topic: Reputation and relational contracts|T14]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§10.1 — Finitely Repeated Games (p. 190)|Tadelis §10.1 (pp. 190–192)]] · [[Map/books-index#§10.2 — Infinitely Repeated Games (p. 192)|§10.2 (pp. 192–196)]] · [[Map/books-index#§10.3 — Subgame-Perfect Equilibria (p. 196)|§10.3 (pp. 196–201)]] · [[Map/books-index#§10.6 — The Folk Theorem: Almost Anything Goes (p. 209)|§10.6 (pp. 209–214)]] · [[Map/books-index#§2.3 — Repeated Games (p. 82)|Gibbons §2.3.A–B (pp. 82–102)]] · [[Map/books-index#Ch. 7 — Games and Strategies (pp. 159–183)|Cabral §7.3 (pp. 172–174)]] · formal: [[Map/books-index#§12.D — Repeated Interaction (p. 400)|MWG §12.D]], [[Map/books-index#Ch. 12, Appendix A — Infinitely Repeated Games and the Folk Theorem (p. 417)|Ch. 12 App. A (pp. 417–422)]] · drill: [[Map/books-index#Ch. 6 — Repeated Games and Correlated Equilibria (pp. 273–316) · Lectures 5–6 · Exercises 1–10|Muñoz-Garcia Ch. 6]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L05/L05-00-map|L05 map]], [[Notas/L05/L05-01-finite-repetition-unraveling|finite repetition]], [[Notas/L05/L05-02-two-stage-carrot-stick|two-stage carrot and stick]], [[Notas/L05/L05-03-discounting-histories-strategies|discounting and strategies]], [[Notas/L05/L05-04-grim-trigger-spe|grim trigger]], [[Notas/L05/L05-05-critical-discount-factor|critical discount factor]], [[Notas/L05/L05-06-folk-theorem|folk theorem]], [[Notas/L06/L06-01-recap-grim-trigger|L06 recap]] · [[Notas/L05/L05-notes.pdf|L05 notes PDF]]
3. 📝 Rules (Medium): [[rules/game-theory|Game theory rules]] (Non-negotiable 4) · [[Notas/L05/L05-07-formulas|L05 formula sheet]] · [[Notas/L05/L05-08-pitfalls|L05 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-04#2. Gibbons 2.12|L4 #2 Gibbons 2.12]] · [[Listas/pratica-lecture-05#2. Cabral 7.8|L5 #2 Cabral 7.8]] · [[Listas/pratica-lecture-05#1. Cabral 7.13|L5 #1 Cabral 7.13]] · [[Listas/pratica-lecture-05#5. Tadelis 10.2|L5 #5 Tadelis 10.2]] · [[Listas/pratica-lecture-05#7. Tadelis 10.9|L5 #7 Tadelis 10.9]] · [[Listas/pratica-lecture-05#6. Muñoz-Garcia Ex. 1|L5 #6 Muñoz-Garcia Ch. 6 Ex. 1]] · [[Listas/pratica-lecture-05#10. Tadelis 10.3|L5 #10 Tadelis 10.3]] · [[Listas/pratica-lecture-05#9. Cabral 7.12|L5 #9 Cabral 7.12]] · [[Listas/pratica-lecture-05#14. Muñoz-Garcia Ex. 6|L5 #14 Muñoz-Garcia Ch. 6 Ex. 6]] · [[Listas/pratica-lecture-05#18. Tadelis 10.5|L5 #18 Tadelis 10.5]] · [[Listas/pratica-lecture-05#15. Muñoz-Garcia Ex. 9|L5 #15 Muñoz-Garcia Ch. 6 Ex. 9]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-05#11. Gibbons 2.10|L5 #11 Gibbons 2.10]] · [[Listas/pratica-lecture-05#16. Gibbons 2.11|L5 #16 Gibbons 2.11]] · [[Listas/pratica-lecture-05#21. Tadelis 10.7|L5 #21 Tadelis 10.7]] · [[Listas/pratica-lecture-05#24. Gibbons 2.16|L5 #24 Gibbons 2.16]] · [[Listas/pratica-lecture-05#20. MWG 12.AA.1|L5 #20 MWG 12.AA.1]] · [[Listas/pratica-lecture-05#25. MWG 12.AA.2|L5 #25 MWG 12.AA.2]]
6. 🧪 Quiz: [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#unravel|L5-1 unravel (3)]] · [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#carrot|carrot (5)]] · [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#reneg|reneg (2)]] · [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#disc|L5-2 disc (3)]] · [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#grim|grim (4)]] · [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#crit|crit (3)]] · [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#feas|L5-3 feas (2)]] · [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#folk|folk (3)]] · [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#alt|alt (3)]] · [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#select|select (2)]] · [[Simulados/quiz-topic-T12-repeated-games-folk-theorem-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-05-audio-part1|L5 audio part 1]] · [[NotebookLM/audio/lecture-05-audio-part2|part 2]] · [[Leituras/lecture-05-notes-narrated.txt|L5 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]]: L5 #7, #8 (two-stage carrot and stick); the one-stage deviation principle in §10.3.
- With [[#Topic: Collusion and price wars|T13]]: (10.5) applied to cartels, [[Map/books-index#§10.4 — Application: Tacit Collusion (p. 201)|Tadelis §10.4]]; [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 6 Ex. 2 (L6 further practice / dropped, not in the tiers)]], [[Listas/pratica-lecture-06|Gibbons 2.13 (L6 further practice / dropped, not in the tiers)]].
- With [[#Topic: Reputation and relational contracts|T14]]: finite vs. indefinite horizon in the trust game, [[Listas/pratica-lecture-06#5. Milgrom & Roberts Mathematical Exercise 4|L6 #5]], [[Listas/pratica-lecture-06#16. Milgrom & Roberts Mathematical Exercise 5|L6 #16]].

## Topic: Collusion and price wars
#topic/collusion

**T13** · **Lectures:** 6
**Complexity:** advanced
**Prerequisites:** [[#Topic: Repeated games and the folk theorem|T12]], [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]
**Cross-topic links:** [[#Topic: Reputation and relational contracts|T14]], [[#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§10.4 — Application: Tacit Collusion (p. 201)|Tadelis §10.4 (pp. 201–204)]] · [[Map/books-index#§2.3 — Repeated Games (p. 82)|Gibbons §2.3.C (pp. 102–107)]] · [[Map/books-index#Ch. 9 — Collusion and Price Wars (pp. 217–247)|Cabral Ch. 9 §9.1–9.3 (pp. 218–231)]] · formal: [[Map/books-index#§12.D — Repeated Interaction (p. 400)|MWG §12.D (p. 400)]] · drill: [[Map/books-index#Ch. 5 — Applications to Industrial Organization (pp. 215–271) · Lectures 2–3, 6 · Exercises 1–16|Muñoz-Garcia Ch. 5 Ex. 4–5, 8]], [[Map/books-index#Ch. 6 — Repeated Games and Correlated Equilibria (pp. 273–316) · Lectures 5–6 · Exercises 1–10|Ch. 6 Ex. 2–5, 10]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L06/L06-00-map|L06 map]], [[Notas/L06/L06-02-cournot-collusion|Cournot collusion]], [[Notas/L06/L06-03-bertrand-market-structure|Bertrand and market structure]], [[Notas/L06/L06-04-punishments-price-wars|punishments and price wars]] · [[Notas/L06/L06-notes.pdf|L06 notes PDF]]
3. 📝 Rules (Medium): [[Notas/L06/L06-09-formulas|L06 formula sheet]] · [[Notas/L06/L06-10-pitfalls|L06 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-06#1. Muñoz-Garcia Ch. 5 Ex. 4|L6 #1 Muñoz-Garcia Ch. 5 Ex. 4]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 5 Ex. 5 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 6 Ex. 2 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06|Gibbons 2.13 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#2. Cabral 9.1|L6 #2 Cabral 9.1]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 5 Ex. 8 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#13. Muñoz-Garcia Ch. 6 Ex. 3|L6 #13 Muñoz-Garcia Ch. 6 Ex. 3]] · [[Listas/pratica-lecture-06|Muñoz-Garcia Ch. 6 Ex. 4 (L6 further practice / dropped, not in the tiers)]] · [[Listas/pratica-lecture-06#14. Gibbons 2.15|L6 #14 Gibbons 2.15]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-06#9. Tadelis 10.8|L6 #9 Tadelis 10.8]] · [[Listas/pratica-lecture-06#20. Muñoz-Garcia Ch. 6 Ex. 5|L6 #20 Muñoz-Garcia Ch. 6 Ex. 5]] · [[Listas/pratica-lecture-06#21. Cabral 9.15|L6 #21 Cabral 9.15]] · [[Listas/pratica-lecture-06#22. Muñoz-Garcia Ch. 6 Ex. 10|L6 #22 Muñoz-Garcia Ch. 6 Ex. 10]] · [[Listas/pratica-lecture-06#23. Gibbons 2.14|L6 #23 Gibbons 2.14]] · [[Listas/pratica-lecture-06#25. Cabral 9.19|L6 #25 Cabral 9.19]]
6. 🧪 Quiz: [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#template|L6-1 template (3)]] · [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#cournot|cournot (3)]] · [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#asym|asym (2)]] · [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#shrink|shrink (2)]] · [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#bertrand|L6-2 bertrand (3)]] · [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#factors|factors (3)]] · [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#punish|punish (2)]] · [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#wars|wars (2)]] · [[Simulados/quiz-topic-T13-collusion-price-wars-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-06-audio-part1|L6 audio part 1]] · [[Leituras/lecture-06-notes-narrated.txt|L6 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]: the one-shot cartel is not an equilibrium (L6 #1, #2, #9; L2 #13; [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cartel|L2-2 cartel (3)]]); Cournot vs. Bertrand collusion in one model, L6 #10.
- With [[#Topic: Repeated games and the folk theorem|T12]]: temporary punishments (L6 #11; [[Listas/pratica-lecture-05#6. Muñoz-Garcia Ex. 1|L5 #6]]) and imperfect monitoring (L6 #20, #22).

## Topic: Reputation and relational contracts
#topic/reputation

**T14** · **Lectures:** 6
**Complexity:** advanced
**Prerequisites:** [[#Topic: Repeated games and the folk theorem|T12]] ([[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]] for trust as a credibility problem)
**Cross-topic links:** [[#Topic: Collusion and price wars|T13]], [[#Topic: Perfect Bayesian equilibrium|T18]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§10.5 — Sequential Interaction and Reputation (p. 204)|Tadelis §10.5 (pp. 204–209)]] · [[Map/books-index#Ch. 8 — Rents and Efficiency (pp. 248–287)|M&R Ch. 8 (efficiency wages pp. 250–258; reputations pp. 259–268)]] · [[Map/books-index#§2.3 — Repeated Games (p. 82)|Gibbons §2.3.D (pp. 107–112)]] · background: [[Map/books-index#Ch. 17 — Building a Reputation (pp. 339–356) · background for Lectures 6 and 8|Tadelis Ch. 17]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L06/L06-05-reputation-trust|reputation and trust]], [[Notas/L06/L06-06-institutions-reputation|institutions]], [[Notas/L06/L06-07-efficiency-wages|efficiency wages]], [[Notas/L06/L06-08-relational-contracts|relational contracts]]
3. 📝 Rules (Medium): [[Notas/L06/L06-09-formulas|L06 formula sheet]] · [[Notas/L06/L06-10-pitfalls|L06 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-06#5. Milgrom & Roberts Mathematical Exercise 4|L6 #5 M&R Ch. 8 ME 4]] · [[Listas/pratica-lecture-06#6. Milgrom & Roberts Food for Thought 3|L6 #6 M&R Ch. 8 FFT 3]] · [[Listas/pratica-lecture-06#7. Milgrom & Roberts Food for Thought 4|L6 #7 M&R Ch. 8 FFT 4]] · [[Listas/pratica-lecture-06#15. Tadelis 10.4|L6 #15 Tadelis 10.4]] · [[Listas/pratica-lecture-06#18. Tadelis 10.6|L6 #18 Tadelis 10.6]] · [[Listas/pratica-lecture-06#16. Milgrom & Roberts Mathematical Exercise 5|L6 #16 M&R Ch. 8 ME 5]] · [[Listas/pratica-lecture-06#17. Milgrom & Roberts Mathematical Exercise 3|L6 #17 M&R Ch. 8 ME 3]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-06#26. Tadelis 10.10|L6 #26 Tadelis 10.10]] · [[Listas/pratica-lecture-06#27. Gibbons 2.17|L6 #27 Gibbons 2.17]] · [[Listas/pratica-lecture-06#28. Milgrom & Roberts Mathematical Exercise 1|L6 #28 M&R Ch. 8 ME 1]]
6. 🧪 Quiz: [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#trust|L6-3 trust (2)]] · [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#mr|mr (3)]] · [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#inst|inst (2)]] · [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#wages|wages (3)]] · [[Simulados/quiz-topic-T14-reputation-relational-contracts-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-06-audio-part2|L6 audio part 2]] · [[Leituras/lecture-06-notes-narrated.txt|L6 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Perfect Bayesian equilibrium|T18]]: reputation from incomplete information, [[Listas/pratica-lecture-08#3. Tadelis 15.3|L8 #3 Tadelis 15.3]] (trust game with nice and jerk types); [[Map/books-index#§4.3 — Other Applications of Perfect Bayesian Equilibrium (p. 210)|Gibbons §4.3.C (p. 224)]].
- With [[#Topic: Collusion and price wars|T13]]: guarantors and brand names as borrowed reputation, L6 #23; [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#inst|L6-3 inst (2)]].

## Topic: Bayesian games and Bayesian Nash equilibrium
#topic/bayesian-games

**T15** · **Lectures:** 7
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Nash equilibrium|T4]], [[#Topic: Mixed strategies and existence|T6]] (expected payoffs; Bayes' rule, [[Map/books-index#Ch. 19 — Mathematical Appendix (pp. 369–384)|Tadelis §19.4.3]])
**Cross-topic links:** [[#Topic: Adverse selection|T16]], [[#Topic: Auctions|T17]], [[#Topic: Perfect Bayesian equilibrium|T18]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§12.1 — Strategic Representation of Bayesian Games (p. 246)|Tadelis §12.1 (pp. 246–252)]] · [[Map/books-index#§12.2 — Examples (p. 252)|§12.2 (pp. 252–258)]] · [[Map/books-index#§12.5 — Mixed Strategies Revisited: Harsanyi's Interpretation (p. 264)|§12.5 (pp. 264–266)]] · [[Map/books-index#§3.1 — Theory: Static Bayesian Games and Bayesian Nash Equilibrium (p. 144)|Gibbons §3.1 (pp. 144–152)]] · formal: [[Map/books-index#§8.E — Games of Incomplete Information: Bayesian Nash Equilibrium (p. 253)|MWG §8.E (pp. 253–257)]] · drill: [[Map/books-index#Ch. 7 — Simultaneous-Move Games with Incomplete Information (pp. 317–347) · Lecture 7 · Exercises 1–7|Muñoz-Garcia Ch. 7]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L07/L07-00-map|L07 map]], [[Notas/L07/L07-01-bayesian-games-harsanyi|Bayesian games]], [[Notas/L07/L07-02-bayesian-nash-equilibrium|BNE]], [[Notas/L07/L07-03-cournot-private-costs|Cournot with private costs]], [[Notas/L07/L07-04-threshold-strategies-purification|thresholds and purification]] · [[Notas/L07/L07-notes.pdf|L07 notes PDF]]
3. 📝 Rules (Medium): [[Notas/L07/L07-10-formulas|L07 formula sheet]] · [[Notas/L07/L07-11-pitfalls|L07 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-07#1. Gibbons 3.1|L7 #1 Gibbons 3.1]] · [[Listas/pratica-lecture-07#2. Muñoz-Garcia Ch. 7 Ex. 1|L7 #2 Muñoz-Garcia Ch. 7 Ex. 1]] · [[Listas/pratica-lecture-07#3. Gibbons 3.4|L7 #3 Gibbons 3.4]] · [[Listas/pratica-lecture-07#4. Tadelis 12.1|L7 #4 Tadelis 12.1]] · [[Listas/pratica-lecture-07#11. Tadelis 12.3|L7 #11 Tadelis 12.3]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-07#9. Tadelis 12.2|L7 #9 Tadelis 12.2]] · [[Listas/pratica-lecture-07#10. Gibbons 3.3|L7 #10 Gibbons 3.3]] · [[Listas/pratica-lecture-07#12. Tadelis 12.9|L7 #12 Tadelis 12.9]]
6. 🧪 Quiz: [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#harsanyi|L7-1 harsanyi (3)]] · [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#bne|bne (2)]] · [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#cournot|cournot (2)]] · [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#threshold|threshold (3)]] · [[Simulados/quiz-topic-T15-bayesian-games-bne-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-07-audio-part1|L7 audio part 1]] · [[Leituras/lecture-07-notes-narrated.txt|L7 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]: L7 #9, #10.
- With [[#Topic: Mixed strategies and existence|T6]]: purification, L7 #12.
- With [[#Topic: Adverse selection|T16]]: threshold strategies in lemons markets, [[Listas/pratica-lecture-07#13. Tadelis 12.5|L7 #13]], [[Listas/pratica-lecture-07#21. Tadelis 12.7|L7 #21]].

## Topic: Adverse selection
#topic/adverse-selection

**T16** · **Lectures:** 7
**Complexity:** intermediate
**Prerequisites:** [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
**Cross-topic links:** [[#Topic: Auctions|T17]], [[#Topic: Signaling and refinements|T19]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§12.3 — Inefficient Trade and Adverse Selection (p. 258)|Tadelis §12.3 (pp. 258–261)]] · [[Map/books-index#§3.2 — Applications (p. 152)|Gibbons §3.2.C double auction (pp. 158–163)]] · applications: [[Map/books-index#Ch. 5 — Bounded Rationality and Private Information (pp. 126–165)|M&R Ch. 5 (adverse selection pp. 149–154)]], [[Map/books-index#Ch. 5 — Market Failure and Public Policy (pp. 93–119)|Cabral §5.2 (p. 99)]], [[Map/books-index#Ch. 38 — Asymmetric Information (pp. 740–762)|Varian §38.1–38.3]] · formal: [[Map/books-index#§13.B — Informational Asymmetries and Adverse Selection (pp. 437–449)|MWG §13.B (pp. 437–449)]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L07/L07-05-adverse-selection-lemons|adverse selection and lemons]], [[Notas/L07/L07-09-common-values-curses|common values and curses]]
3. 📝 Rules (Medium): [[rules/07_selecao_adversa|Topic 7 — Adverse selection]] · [[Notas/L07/L07-10-formulas|L07 formula sheet]] · [[Notas/L07/L07-11-pitfalls|L07 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-07#13. Tadelis 12.5|L7 #13 Tadelis 12.5]] · [[Listas/pratica-lecture-07#14. Tadelis 12.6|L7 #14 Tadelis 12.6]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-07#19. MWG 13.B.1|L7 #19 MWG 13.B.1]] · [[Listas/pratica-lecture-07#20. MWG 13.B.2|L7 #20 MWG 13.B.2]] · [[Listas/pratica-lecture-07#21. Tadelis 12.7|L7 #21 Tadelis 12.7]] · [[Listas/pratica-lecture-07#22. Gibbons 3.8|L7 #22 Gibbons 3.8]]
6. 🧪 Quiz: [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#lemons|L7-2 lemons (3)]] · [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#insurance|insurance (2)]] · [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#double|double (2)]] · [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#cv|cv (3)]] · [[Simulados/quiz-topic-T16-adverse-selection-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-07-audio-part1|L7 audio part 1]] · [[Leituras/lecture-07-notes-narrated.txt|L7 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Signaling and refinements|T19]]: MWG §13.B → [[Map/books-index#§13.C — Signaling (pp. 450–459)|§13.C]] (signaling as the response to adverse selection); L7 #19–#20 then [[Listas/pratica-lecture-08#24. MWG 13.C.2|L8 #24]], [[Listas/pratica-lecture-08#25. MWG 13.C.4|L8 #25]].
- With [[#Topic: Auctions|T17]]: common values, the swing voter's and winner's curses, [[Listas/pratica-lecture-07#18. Tadelis 12.8|L7 #18 Tadelis 12.8]], [[Listas/pratica-lecture-07#24. Tadelis 13.10|L7 #24 Tadelis 13.10]].

## Topic: Auctions
#topic/auctions

**T17** · **Lectures:** 7 (second-price auction already in Lecture 1)
**Complexity:** advanced
**Prerequisites:** [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]], [[#Topic: Dominance and IESDS|T2]]
**Cross-topic links:** [[#Topic: Adverse selection|T16]], [[#Topic: Mixed strategies and existence|T6]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§13.1 — Independent Private Values (p. 272)|Tadelis §13.1 (pp. 272–282)]] · [[Map/books-index#§13.2 — Common Values and the Winner's Curse (p. 282)|§13.2 (pp. 282–284)]] · [[Map/books-index#§12.4 — Committee Voting (p. 261)|§12.4 (pp. 261–264)]] · [[Map/books-index#§3.2 — Applications (p. 152)|Gibbons §3.2.B (pp. 155–158)]] · [[Map/books-index#Ch. 6 — Price Discrimination (pp. 121–155)|Cabral §6.4 (p. 140)]] · drill: [[Map/books-index#Ch. 8 — Auctions (pp. 349–373) · Lecture 7 · Exercises 1–8|Muñoz-Garcia Ch. 8]]
2. 🎓 Lecture (Easy→Medium): [[Aula/Lecture01.pdf|Lecture 1 slides]] (second-price auction by dominance) · notes [[Notas/L07/L07-06-second-price-english|second-price and English]], [[Notas/L07/L07-07-first-price-dutch|first-price and Dutch]], [[Notas/L07/L07-08-revenue-equivalence|revenue equivalence]], [[Notas/L07/L07-09-common-values-curses|common values]]
3. 📝 Rules (Medium): [[Notas/L07/L07-10-formulas|L07 formula sheet]] · [[Notas/L07/L07-11-pitfalls|L07 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-07#5. Tadelis 13.1|L7 #5 Tadelis 13.1]] · [[Listas/pratica-lecture-07#6. Muñoz-Garcia Ch. 8 Ex. 4|L7 #6 Muñoz-Garcia Ch. 8 Ex. 4]] · [[Listas/pratica-lecture-07#7. Muñoz-Garcia Ch. 8 Ex. 1|L7 #7 Muñoz-Garcia Ch. 8 Ex. 1]] · [[Listas/pratica-lecture-07#8. Tadelis 13.2|L7 #8 Tadelis 13.2]] · [[Listas/pratica-lecture-07#15. Gibbons 3.6|L7 #15 Gibbons 3.6]] · [[Listas/pratica-lecture-07#16. Tadelis 13.9|L7 #16 Tadelis 13.9]] · [[Listas/pratica-lecture-07#17. Tadelis 13.3|L7 #17 Tadelis 13.3]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-07#18. Tadelis 12.8|L7 #18 Tadelis 12.8]] · [[Listas/pratica-lecture-07#23. Tadelis 13.5|L7 #23 Tadelis 13.5]] · [[Listas/pratica-lecture-07#24. Tadelis 13.10|L7 #24 Tadelis 13.10]] · [[Listas/pratica-lecture-02#19. MWG 8.D.3|L2 #19 MWG 8.D.3]]
6. 🧪 Quiz: [[Simulados/quiz-lecture07-3-auctions-2026-10-25#spa|L7-3 spa (2)]] · [[Simulados/quiz-lecture07-3-auctions-2026-10-25#fpa|fpa (3)]] · [[Simulados/quiz-lecture07-3-auctions-2026-10-25#rev|rev (3)]] · [[Simulados/quiz-lecture07-3-auctions-2026-10-25#wc|wc (2)]] · [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#auction|L1-2 auction (2)]] · [[Simulados/quiz-topic-T17-auctions-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-07-audio-part2|L7 audio part 2]] · [[Leituras/lecture-07-notes-narrated.txt|L7 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Dominance and IESDS|T2]]: auctions solved by dominance in Lecture 1, [[Listas/pratica-lecture-01#17. Tadelis 4.3|L1 #17]], [[Listas/pratica-lecture-01#23. MWG 8.B.3|L1 #23]], [[Listas/pratica-lecture-01#24. Tadelis 4.4|L1 #24]].
- With [[#Topic: Mixed strategies and existence|T6]]: L7 #23; with [[#Topic: Adverse selection|T16]]: L7 #24 and [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#cv|L7-2 cv (3)]].

## Topic: Perfect Bayesian equilibrium
#topic/pbe

**T18** · **Lectures:** 8
**Complexity:** advanced
**Prerequisites:** [[#Topic: Backward induction and subgame perfection|T8]], [[#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
**Cross-topic links:** [[#Topic: Signaling and refinements|T19]], [[#Topic: Reputation and relational contracts|T14]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§15.1 — The Problem with Subgame Perfection (p. 303)|Tadelis §15.1 (pp. 303–307)]] · [[Map/books-index#§15.2 — Perfect Bayesian Equilibrium (p. 307)|§15.2 (pp. 307–312)]] · [[Map/books-index#§15.3 — Sequential Equilibrium (p. 312)|§15.3 (pp. 312–313)]] · [[Map/books-index#§4.1 — Introduction to Perfect Bayesian Equilibrium (p. 175)|Gibbons §4.1 (pp. 175–183)]] · formal: [[Map/books-index#§9.C — Beliefs and Sequential Rationality (p. 282)|MWG §9.C (pp. 282–292)]], [[Map/books-index#§9.D — Reasonable Beliefs and Forward Induction (p. 292)|§9.D]] · drill: [[Map/books-index#Ch. 9 — Perfect Bayesian Equilibrium and Signaling Games (pp. 375–451) · Lecture 8 · Exercises 1–9|Muñoz-Garcia Ch. 9]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L08/L08-00-map|L08 map]], [[Notas/L08/L08-01-subgame-perfection-fails|subgame perfection fails]], [[Notas/L08/L08-02-beliefs-and-pbe|beliefs and PBE]], [[Notas/L08/L08-03-sequential-equilibrium|sequential equilibrium]] · [[Notas/L08/L08-notes.pdf|L08 notes PDF]]
3. 📝 Rules (Medium): [[Notas/L08/L08-09-formulas|L08 formula sheet]] · [[Notas/L08/L08-10-pitfalls|L08 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-08#1. Tadelis 15.1|L8 #1 Tadelis 15.1]] · [[Listas/pratica-lecture-08#2. Gibbons 4.1|L8 #2 Gibbons 4.1]] · [[Listas/pratica-lecture-08#3. Tadelis 15.3|L8 #3 Tadelis 15.3]] · [[Listas/pratica-lecture-08#9. Gibbons 4.2|L8 #9 Gibbons 4.2]] · [[Listas/pratica-lecture-08#10. Tadelis 15.5|L8 #10 Tadelis 15.5]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-08#20. Tadelis 15.6|L8 #20 Tadelis 15.6]]
6. 🧪 Quiz: [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#sp|L8-1 sp (2)]] · [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#beliefs|beliefs (3)]] · [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#pbe|pbe (3)]] · [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#se|se (2)]] · [[Simulados/quiz-topic-T18-pbe-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-08-audio-part1|L8 audio part 1]] · [[Leituras/lecture-08-notes-narrated.txt|L8 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Backward induction and subgame perfection|T8]]: Nash vs. SPE vs. PBE on the same trees, L8 #2; entry with tough and weak entrants, L8 #10.
- With [[#Topic: Reputation and relational contracts|T14]]: L8 #3; [[Map/books-index#Ch. 17 — Building a Reputation (pp. 339–356) · background for Lectures 6 and 8|Tadelis Ch. 17]].

## Topic: Signaling and refinements
#topic/signaling

**T19** · **Lectures:** 8
**Complexity:** advanced
**Prerequisites:** [[#Topic: Perfect Bayesian equilibrium|T18]], [[#Topic: Adverse selection|T16]]
**Cross-topic links:** [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]], [[#Topic: Mixed strategies and existence|T6]]

**Difficulty progression:**
1. 📖 Isolated concept (Easy): [[Map/books-index#§16.1 — Education Signaling: The MBA Game (p. 319)|Tadelis §16.1 (pp. 319–323)]] · [[Map/books-index#§16.2 — Limit Pricing and Entry Deterrence (p. 323)|§16.2 (pp. 323–332)]] · [[Map/books-index#§16.3 — Refinements of Perfect Bayesian Equilibrium in Signaling Games (p. 332)|§16.3 (pp. 332–335)]] · [[Map/books-index#§4.2 — Signaling Games (p. 183)|Gibbons §4.2 (pp. 183–210; Spence p. 190)]] · [[Map/books-index#§4.4 — Refinements of Perfect Bayesian Equilibrium (p. 233)|§4.4 (pp. 233–244)]] · applications: [[Map/books-index#Ch. 5 — Bounded Rationality and Private Information (pp. 126–165)|M&R Ch. 5 (signalling pp. 154–156)]] · formal: [[Map/books-index#§13.C — Signaling (pp. 450–459)|MWG §13.C]], [[Map/books-index#Appendix A — Reasonable-Beliefs Refinements in Signaling Games (p. 467)|App. 13.AA (p. 467)]] · drill: [[Map/books-index#Ch. 9 — Perfect Bayesian Equilibrium and Signaling Games (pp. 375–451) · Lecture 8 · Exercises 1–9|Muñoz-Garcia Ch. 9]], [[Map/books-index#Ch. 11 — More Advanced Signaling Games (pp. 481–520) · Lecture 8 · Exercises 1–6|Ch. 11]]
2. 🎓 Lecture (Easy→Medium): no slides yet · notes [[Notas/L08/L08-04-signaling-games|signaling games]], [[Notas/L08/L08-05-mba-game|MBA game]], [[Notas/L08/L08-06-spence-job-market|Spence]], [[Notas/L08/L08-07-limit-pricing|limit pricing]], [[Notas/L08/L08-08-intuitive-criterion|intuitive criterion]]
3. 📝 Rules (Medium): [[rules/07_selecao_adversa|Topic 7]] (signaling; labour-market signaling) · [[Notas/L08/L08-09-formulas|L08 formula sheet]] · [[Notas/L08/L08-10-pitfalls|L08 pitfalls]]
4. ✏️ Direct exercises (Medium): [[Listas/pratica-lecture-08#4. Muñoz-Garcia Ch. 9 Ex. 1|L8 #4 Muñoz-Garcia Ch. 9 Ex. 1]] · [[Listas/pratica-lecture-08#5. Gibbons 4.3|L8 #5 Gibbons 4.3]] · [[Listas/pratica-lecture-08#6. Gibbons 4.4|L8 #6 Gibbons 4.4]] · [[Listas/pratica-lecture-08#7. Tadelis 16.5|L8 #7 Tadelis 16.5]] · [[Listas/pratica-lecture-08#8. Muñoz-Garcia Ch. 9 Ex. 2|L8 #8 Muñoz-Garcia Ch. 9 Ex. 2]] · [[Listas/pratica-lecture-08#11. Muñoz-Garcia Ch. 9 Ex. 5|L8 #11 Muñoz-Garcia Ch. 9 Ex. 5]] · [[Listas/pratica-lecture-08#12. Tadelis 16.4|L8 #12 Tadelis 16.4]] · [[Listas/pratica-lecture-08#13. Tadelis 16.3|L8 #13 Tadelis 16.3]] · [[Listas/pratica-lecture-08#14. Muñoz-Garcia Ch. 11 Ex. 5|L8 #14 Muñoz-Garcia Ch. 11 Ex. 5]] · [[Listas/pratica-lecture-08#15. Tadelis 16.6|L8 #15 Tadelis 16.6]] · [[Listas/pratica-lecture-08#16. Tadelis 16.8|L8 #16 Tadelis 16.8]] · [[Listas/pratica-lecture-08#17. Gibbons 4.16|L8 #17 Gibbons 4.16]]
5. ✏️ Integrating exercises (Hard): [[Listas/pratica-lecture-08#22. Tadelis 16.7|L8 #22 Tadelis 16.7]] · [[Listas/pratica-lecture-08#21. Gibbons 4.7|L8 #21 Gibbons 4.7]] · [[Listas/pratica-lecture-08#23. Muñoz-Garcia Ch. 11 Ex. 4|L8 #23 Muñoz-Garcia Ch. 11 Ex. 4]] · [[Listas/pratica-lecture-08#18. MWG 13.C.1|L8 #18 MWG 13.C.1]] · [[Listas/pratica-lecture-08#19. MWG 13.C.5|L8 #19 MWG 13.C.5]] · [[Listas/pratica-lecture-08#24. MWG 13.C.2|L8 #24 MWG 13.C.2]] · [[Listas/pratica-lecture-08#25. MWG 13.C.4|L8 #25 MWG 13.C.4]]
6. 🧪 Quiz: [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#sig|L8-2 sig (3)]] · [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#mba|mba (3)]] · [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#spence|spence (4)]] · [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#lp|L8-3 lp (3)]] · [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ic|ic (4)]] · [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ref|ref (3)]] · [[Simulados/quiz-topic-T19-signaling-refinements-hard-2026-11-13|hard conceptual quiz (10)]]
7. 🎧 Audio and narration: [[NotebookLM/audio/lecture-08-audio-part1|L8 audio part 1]] (first signaling game) · [[NotebookLM/audio/lecture-08-audio-part2|part 2]] · [[Leituras/lecture-08-notes-narrated.txt|L8 narration]]

**Cross-topic synthesis (Hard):**
- With [[#Topic: Adverse selection|T16]]: Spence as the market response to adverse selection (MWG §13.B → §13.C; L8 #24, #25).
- With [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]: limit pricing revisits entry deterrence, L8 #13, #14, #19.
- With [[#Topic: Mixed strategies and existence|T6]]: semi-separating equilibria, L8 #9, #11, #20.

---

## Integrating materials across topics

- [[Cases/Brexit/brexit-game.pdf|Brexit case as a game]] (Lectures 3–4): T1, T7, T8, T9, T11 in one tree; plan in `.agent/plans/cases-lecture-03-brexit.md`.
- [[Resolucao/mini-case-lecture-01.pdf|Mini case L1, the pharmacy]]: T1, T2, T5 (and Pareto, part (d)).
- [[Resolucao/mini-case-lecture-03.pdf|Mini case L3, work or shirk]] ([[Resolucao/mini-case-lecture-03-short.pdf|short]]): T6 with T9 (commitment variant).
- [[Listas/lista-reais-lectures-01-04.pdf|Real-exercise list, Lectures 1–4]] (24 items, 6 per lecture; [[Listas/roteiro-lectures-01-04|roteiro]], [[Listas/lista-reais-lectures-01-04-solutions.pdf|solutions]], [[Listas/study-pack-roteiro-lectures-01-04.pdf|study pack]]): items 1–6 T2, 7–12 T4–T6, 13–18 T8–T9, 19–24 T10–T11.
- [[Listas/lista-lecture-01.pdf|Exam-style list, Lecture 1]] ([[Listas/lista-lecture-01-gabarito.pdf|answers]]): T1, T2, T5; Question 6 is the integrative one.
- [[Listas/pratica-lecture-01-solutions.pdf|Worked solutions, Lecture 1 practice list]].

---

## Background and applications (superseded plan)

The 16-session draft built from the 2024/34 syllabus record organised the course in 9 Milgrom &
Roberts topics. Their rules files, early notes and quizzes stay in the project as application
material; each now points to the T-topic that carries it.

| Old topic | Rules | Now carried by | Status |
|---|---|---|---|
| Does organization matter? | [[rules/01_organizacoes_importam\|Topic 1]] | [[#Topic: Nash equilibrium\|T4]] (complementarities as coordination games with several equilibria, M&R Ch. 4 p. 111) | background (Aula 1 history) |
| Bargaining | [[rules/02_barganha\|Topic 2]] | [[#Topic: Strategic bargaining\|T11]] | in scope |
| Efficiency and economic organization | [[rules/03_eficiencia_organizacao\|Topic 3]] | [[#Topic: Normal-form games and solution concepts\|T1]] (Pareto optimality, Tadelis §3.3.3) and [[#Topic: Strategic bargaining\|T11]] (Coase, value maximization) | background |
| Coordination through the market | [[rules/04_coordenacao_mercado\|Topic 4]] | [[#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)\|T5]] (strategic market interaction) | background |
| Coordination through management | [[rules/05_coordenacao_management\|Topic 5]] | [[#Topic: Nash equilibrium\|T4]] (coordination failure, multiple equilibria) | background |
| Bounded rationality, information and contracts | [[rules/06_racionalidade_limitada_contratos\|Topic 6]] | [[#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)\|T9]] (holdup: L3 #15, L4 #13) | background |
| Adverse selection | [[rules/07_selecao_adversa\|Topic 7]] | [[#Topic: Adverse selection\|T16]], [[#Topic: Signaling and refinements\|T19]] | in scope |
| Moral hazard | [[rules/08_risco_moral\|Topic 8]] | — (closest: [[#Topic: Mixed strategies and existence\|T6]], mini case L3 inspection game) | out of scope |
| Managing moral hazard | [[rules/09_gestao_risco_moral\|Topic 9]] | — (closest: [[#Topic: Reputation and relational contracts\|T14]], efficiency wages; Gibbons §2.2.D tournaments, [[#Topic: Multistage games (carrot and stick, one-stage deviation)\|T10]]) | out of scope |

Early material from that plan: [[Aula/aula-01-notes|Aula 1 notes]], [[Aula/aula-02-notes|Aula 2 notes]],
[[Listas/lista-aulas-01-02.pdf|list for Aulas 1–2]], [[Listas/pratica-aula-01-02|practice plan Aulas 1–2]],
quizzes `Simulados/quiz-aula01-*` and `Simulados/quiz-aula02-*`. Book pages for every old topic
remain in [[Map/books-index|books-index]] (M&R, Varian, Cabral, Giambiagi & Garcia, MWG Ch. 13–14, 16).
