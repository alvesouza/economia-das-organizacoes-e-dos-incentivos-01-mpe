---
tags: [map, cross-reference]
date: 2026-11-03
---

# Books index

Only the chapters inside the course scope are mapped (see `CLAUDE.md`). Pages are **printed**
pages. Sources: MWG, Cabral, Varian (2014) and Giambiagi & Garcia and M&R from their text
layers (TOC + chapter body, verified against running heads). PDF page conversions: `Livros/book-registry.json`.

**Since 2026-10-13 the course is a game-theory sequence (Lecture 1) and Tadelis is the main
reference**; Tadelis, Gibbons and Muñoz-Garcia & Toro-Gonzalez are mapped at the end of this file
(TOC checked against the chapter bodies and folios). Lectures: L1 static games, dominance, IESDS ·
L2 Nash, mixed strategies · L3 backward induction, SPE · L4 multistage games, bargaining · L5
repeated games I · L6 repeated games II, collusion, relational contracts · L7 Bayesian games,
adverse selection, auctions · L8 signaling, PBE.

**Since 2026-11-03** every game-theory section (Tadelis Ch. 3–13, 15–16; Gibbons Ch. 1–4;
Muñoz-Garcia; MWG Ch. 7–9, 12–13; Cabral Ch. 7 and 9; M&R Ch. 8) carries a **Topics:** line with
the canonical topic tags T1–T19 of [[Map/topics-index|topics-index]] and a **Materials:** line
linking the notes (`Notas/LNN/`), the practice-list items (`Listas/pratica-lecture-NN.md`, "L3 #6"
= Lecture 3 list, item 6), the real-exercise list for Lectures 1–4
([[Listas/roteiro-lectures-01-04|roteiro]], "real #N"), the quiz sections (`Simulados/`) and the
cases that use it. Exercise ranges were re-checked against the PDFs (offsets in
`Livros/book-registry.json`) where the lists cite exercises outside the old ranges.

---

# Milgrom & Roberts, *Economics, Organization, and Management* (1992)

#book/mr

In `Livros/` since 2026-10-09 (PDF with an OCR text layer, 635 pages; `.md` by markitdown).
Sections and printed pages read from the book's TOC (PDF 6–11) and checked against chapter
openings and running heads. PDF page = printed + offset, and the offset **changes by part**
(the scan drops part-divider versos): Ch. 1–2 **+17**, Ch. 3–6 **+16**, Ch. 7–15 **+15**,
Ch. 16–17 **+14**. Each chapter ends with *Food for Thought* (discursive) and, from Ch. 2 on,
*Quantitative Exercises*: see [[Map/exercises-index|exercises-index]].

The catalogue TOC used before the book arrived had the chapter titles right; the section
structure below replaces the "to confirm" guesses.

## Part I — The Problem of Economic Organization

## Ch. 1 — Does Organization Matter? (pp. 2–18)
**Subtopics:**
- Business Organization (p. 2) — *Crisis and Change at General Motors* (p. 2): the Model T at 55% of the US market in 1921 against 11% for all GM brands; Sloan's segmented-market strategy and the coordination it demanded (p. 3); the multidivisional structure (p. 3); Henry Ford's "great big chart" quote and GM's 45% vs. Ford's 16% share by 1940 (p. 4). *Toyota* (p. 4): just-in-time/kanban instead of buffer inventories; operators repair their own machines (p. 5); flexible equipment vs. GM's shared specialised components; redesigns twice as often as GM (p. 5); outside suppliers and long-term relations (pp. 5–6). *The Hudson's Bay Company* (p. 6) and *The Northwest Company* (p. 7): London control and flat salaries vs. wintering partners with profit shares; NWC at ~80% of the trade by c. 1810 despite double the import cost (p. 8); HBC's 1809 reorganisation by imitation (pp. 8–9).
- Organizational Strategies of Modern Firms (p. 9) — *Salomon Brothers* (p. 9): near piece-rate bonuses that discourage cooperation across departments (pp. 10–11); the 1990 stock-in-trust reform and its market test, +7–10% firm value (pp. 11–12).
- The Changing Economies of Eastern Europe (p. 12) — Recent History (p. 12); Building Socialism (p. 13; central planning, the nail story and the **ratchet effect**, p. 14); The Collapse of Communism (p. 15; interdependent reforms, "only the trucks changed sides", p. 16).
- Patterns of Organizational Success and Failure (p. 16) — organization and strategy can matter as much as technology, cost and demand; incentives (p. 16); authority placed with those who hold information (p. 17); **"incentives and delegated authority are complements"** and the fit of structure with strategy at GM and Toyota (p. 17); the book's plan: coordination and motivation (p. 17).
**Exercises:** Food for Thought 1–3 (p. 18). No quantitative exercises.
**Linked materials:** Rules: [[rules/01_organizacoes_importam|Topic 1]] · Notes: `Aula/aula-01-notes.md` · Video: `Videos/aula-01-does-organization-matter/`

## Ch. 2 — Economic Organization and Efficiency (pp. 19–54)
**Subtopics:**
- Economic Organizations: A Perspective (p. 19) — formal organizations (p. 20); transactions and individuals as the level of analysis (p. 21).
- Efficiency (p. 22) — the concept (p. 22); efficiency of allocations (p. 23) and of organizations (p. 23); **efficiency as a positive principle** (p. 24).
- The Tasks of Coordination and Motivation (p. 25) — specialization (p. 25); the need for information (p. 26); organizational methods for coordination (p. 26).
- Transactions Costs Analysis (p. 28) — types of transaction costs (p. 29); dimensions of transactions (p. 30); limits of the approach (p. 33).
- Wealth Effects, Value Maximization and the Coase Theorem (p. 35) — **value maximization principle** (p. 35); **Coase theorem** (p. 38); the transaction-costs approach vs. alternative views (p. 39).
- Organizational Objectives (p. 39) — profit maximization (p. 40); other goals and stakeholders (p. 41).
- Modelling Human Motivation and Behavior (p. 42) — rationality-based theories (p. 42).
- Case Study: Coordination, Motivation, and Efficiency in the Market for Medical Interns (p. 43) — matching problems and failed solutions (p. 43); the National Intern Matching Program (p. 44); evolution and persistence of organizational forms (p. 48). **The book's matching case: the anchor for the NEPKE session.**
**Exercises:** Food for Thought 1–5 (p. 52) · Quantitative 1–4 (p. 53; Q3 proves the value maximization principle, Q4 characterises utility without wealth effects).
**Linked materials:** Rules: [[rules/02_barganha|Topic 2]] · [[rules/03_eficiencia_organizacao|Topic 3]]

## Part II — Coordination: Markets and Management

## Ch. 3 — Using Prices for Coordination and Motivation (pp. 56–87)
**Subtopics:**
- Prices and Coordination (p. 57) — one objective and a single scarce resource (p. 58); market-clearing interpretation (p. 60); extensions and difficulties (p. 61).
- The Fundamental Theorem of Welfare Economics (p. 62) — the neoclassical private-ownership model (p. 62); its scope (p. 68).
- Incentives and Information Transfer Under Market Institutions (p. 71) — incentives in markets (p. 71); informational efficiency (p. 72).
- The Neoclassical Model and Theories of Organization (p. 73) — market failures (p. 73) and organization (p. 77).
- Using the Price System within Organizations (p. 78) — patterns of internal organization (p. 78); **transfer pricing in multidivisional firms** (p. 79; Figure 3.3). Anchor for the Sears session (Ch. 1 n. 2, p. 4, also names Sears among the early multidivisional firms).
**Exercises:** Food for Thought 1–4 (pp. 86–87) · Quantitative 1–3 (p. 87; Q1 on the transfer-pricing figure).
**Linked materials:** Rules: [[rules/04_coordenacao_mercado|Topic 4]] · [[rules/05_coordenacao_management|Topic 5]] (Sears)

## Ch. 4 — Coordinating Plans and Actions (pp. 88–124)
**Subtopics:**
- The Variety of Coordination Problems and Solutions (p. 90) — **design attributes** (p. 91); innovation attributes (p. 92); comparing coordination schemes (p. 93).
- Prices versus Quantities: Assessing Brittleness (p. 94) — examples (p. 94); a mathematical formulation (p. 96); constant and increasing returns (p. 99).
- Economizing on Information and Communication (p. 100) — informational requirements of production planning (p. 100); judging informational efficiency (p. 101); planning with design attributes (p. 103).
- Coordination and Business Strategy (p. 106) — scale, scope and core competencies (p. 106); **Complementarities and Design Decisions** (p. 108; the definition, and footnote 8: $\partial^2\pi/\partial x_i\partial x_j \ge 0$ with the feedback rounds; box "Modern Manufacturing Strategy" pp. 109–110; Ford's "equally coherent" strategy p. 109); **Complementarities, Innovation Attributes, and Coordination Failure** (p. 111; **Figure 4.3**, product variety × batch size, several coherent intersections, Ford's and the niche strategy as two of them, p. 112; footnote 9, the profit surface as "a mountain with three peaks", p. 112; local adjustment cannot find the global shift, p. 113).
- Management, Decentralization, and the Means of Coordination (p. 113) — centralization and decentralization (p. 114); the role of management in coordination (p. 114; choosing among coherent patterns must be centralised, p. 115).
**Exercises:** Food for Thought 1–3 (p. 119) · Quantitative 1–3 (p. 120).
**Linked materials:** Rules: [[rules/01_organizacoes_importam|Topic 1]] (complementarities) · [[rules/05_coordenacao_management|Topic 5]]

## Part III — Motivation: Contracts, Information, and Incentives

## Ch. 5 — Bounded Rationality and Private Information (pp. 126–165)
**Subtopics:**
- Perfect, Complete Contracts (p. 127) — the requirements of complete contracting (p. 127); problems of actual contracting (p. 128).
- Bounded Rationality and Contractual Incompleteness (p. 129) — bounded rationality (p. 129); contractual responses (p. 131); effects of incompleteness (p. 133); **investments and specific assets** (p. 134); achieving commitment (p. 139).
- Private Information and Precontractual Opportunism (p. 140) — **bargaining over a sale** (p. 140); incentive efficiency (p. 143); many participants (p. 145); bargaining costs (p. 147).
- Measurement Costs and Investments in Bargaining Position (p. 147) — the De Beers diamond monopoly (p. 148); investing in bargaining advantages (p. 149).
- **Adverse Selection** (p. 149) — the closing of markets (p. 150); rationing (p. 153).
- **Signalling, Screening and Self-Selection** (p. 154) — signaling (p. 154); screening (p. 156).
- Implications (p. 159).
**Exercises:** Food for Thought 1–3 (pp. 163–164) · Quantitative 1–6 (pp. 164–165; Q2 extends the text's Spence example, Q4–Q5 bargaining with private information, Q6 an intermediate-good supply relation).
**Linked materials:** Rules: [[rules/02_barganha|Topic 2]] (bargaining over a sale) · [[rules/06_racionalidade_limitada_contratos|Topic 6]] · [[rules/07_selecao_adversa|Topic 7]]

## Ch. 6 — Moral Hazard and Performance Incentives (pp. 166–204)
**Subtopics:**
- The Concept of Moral Hazard (p. 167) — insurance and misbehavior (p. 167); efficiency effects (p. 168); incidence (p. 168).
- **Case Study: The U.S. Savings and Loan Crisis** (p. 170) — the industry (p. 170); deposit insurance and risk taking, an example (p. 171); incentives for risk taking with borrowed funds (p. 173); the perverse effect of competition (p. 175); fraud (p. 176); who's to blame (p. 176).
- Public versus Private Insurance (p. 176) — other US guarantee programs (p. 177); private or public (p. 178); life insurance (p. 178).
- Moral Hazard in Organizations (p. 179) — employee shirking (p. 179); managerial misbehavior (p. 181); financial contracts (p. 183).
- **Controlling Moral Hazard** (p. 185) — monitoring (p. 186); explicit incentive contracts (p. 187); bonding (p. 189); do-it-yourself, ownership changes and organizational redesign (p. 190).
- Influence Activities and Unified Ownership (p. 192) — selective intervention (p. 192); influencing interventions (p. 193); influence costs and failed mergers (p. 193).
**Exercises:** Food for Thought 1–7 (pp. 197–198; FFT 1–2 on the S&Ls) · Quantitative 1–5 (pp. 198–199).
**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]] · [[rules/09_gestao_risco_moral|Topic 9]]

## Part IV — Efficient Incentives: Contracts and Ownership

## Ch. 7 — Risk Sharing and Incentive Contracts (pp. 206–247)
**Subtopics:**
- Incentive Contracts as a Response to Moral Hazard (p. 206) — sources of randomness (p. 207); balancing risks and incentives (p. 208).
- Decisions Under Uncertainty and the Evaluation of Financial Risks (p. 209) — means and variances (p. 209); **certainty equivalents and risk premia** (p. 210); risk premia and value maximization (p. 211).
- Risk Sharing and Insurance (p. 211) — how insurance reduces the cost of risk (p. 211); efficient risk sharing, a mathematical example (p. 212); optimal sharing ignoring incentives (p. 213).
- **Principles of Incentive Pay** (p. 214) — basing pay on measured performance (p. 214); **a model of incentive compensation** (p. 215); the **Informativeness** (p. 219), **Incentive Intensity** (p. 221), **Monitoring Intensity** (p. 226) and **Equal Compensation** (p. 228) principles; intertemporal incentives, the ratchet effect (p. 232).
- Moral Hazard with Risk-Neutral Agents (p. 236) — problems with that scenario (p. 237).
**Exercises:** Food for Thought 1–6 (pp. 243–244) · Quantitative 1–5 (pp. 244–245).
**Linked materials:** Rules: [[rules/09_gestao_risco_moral|Topic 9]]

## Ch. 8 — Rents and Efficiency (pp. 248–287)
**Topics:** T14 Reputation and relational contracts #topic/reputation · T12 Repeated games and the folk theorem #topic/repeated-games
Brought into scope by Lecture 6. Sections from the TOC, exercise pages checked in the PDF (offset 15 for a 1-based viewer page, registry entry `MR Ch. 7-15`).
**Subtopics:**
- When Distribution Affects Efficiency (p. 248).
- **Efficiency Wages for Employment Incentives** (p. 250) — the Shapiro–Stiglitz model (p. 250); a mathematical example, comparative statics for efficiency wages (p. 254); a Marxian view (p. 256); additional aspects and applications (p. 257). Efficiency wages also explain Ford's $\$5$ day (Aula 1, history only).
- **Reputations as Contract Enforcers** (p. 259) — the elementary theory, reputations in repeated transactions and the trust game (p. 259); ambiguity, complexity and limits of reputations (p. 264); the advanced theory, reputations aided by institutions (p. 266).
- Rent Seeking: Influence Costs and Efficient Decision Routines (p. 269) — rents and quasi-rents (p. 269); rent seeking in the public and private sectors (p. 270); organizational design (p. 273); influence costs and the legal system (p. 277); participatory management (p. 279). Not used by the lectures.
**Exercises:** Food for Thought 1–8 (pp. 284–285) · Mathematical Exercises 1–7 (pp. 285–287; the book's heading here is "Mathematical Exercises").
**Materials:** notes [[Notas/L06/L06-05-reputation-trust|L06 reputation and trust]], [[Notas/L06/L06-06-institutions-reputation|L06 institutions]], [[Notas/L06/L06-07-efficiency-wages|L06 efficiency wages]], [[Notas/L06/L06-08-relational-contracts|L06 relational contracts]] · items [[Listas/pratica-lecture-06#6. Milgrom & Roberts Mathematical Exercise 4|L6 #6 (ME 4)]], [[Listas/pratica-lecture-06#7. Milgrom & Roberts Food for Thought 3|L6 #7 (FFT 3)]], [[Listas/pratica-lecture-06#8. Milgrom & Roberts Food for Thought 4|L6 #8 (FFT 4)]], [[Listas/pratica-lecture-06#16. Milgrom & Roberts Mathematical Exercise 5|L6 #16 (ME 5)]], [[Listas/pratica-lecture-06#17. Milgrom & Roberts Mathematical Exercise 3|L6 #17 (ME 3)]], [[Listas/pratica-lecture-06#25. Milgrom & Roberts Mathematical Exercise 1|L6 #25 (ME 1)]] · quiz [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#mr|L6-3 mr]], [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#wages|wages]] · audio [[NotebookLM/audio/lecture-06-audio-part2|L6 part 2]]

## Beyond the core (in scope only if a lecture brings them)
- Ch. 8 Rents and Efficiency: now mapped above (Lecture 6).
- Ch. 9 Ownership and Property Rights (p. 288): residual control and returns (p. 289); the Coase theorem reconsidered (p. 293); asset specificity and the hold-up problem (p. 307), which supports Topic 6.
- Ch. 10–17 (Parts V–VII: employment, compensation, executive pay, finance, corporate control, organizational design and dynamics): outside the syllabus.

---

# Mas-Colell, Whinston & Green, *Microeconomic Theory* (1995)

#book/mwg

Part Two (Game Theory, Ch. 7–9) and Ch. 12 added 2026-11-03 for the game-theory lectures:
section titles and pages from the TOC (`.md` lines 96–175), section ranges as the practice lists
use them (pages checked when the lists were built). Subtopics beyond the TOC titles and the
lists' descriptions are **to confirm**. 2-up scan: PDF page = (printed + 20) // 2.

## Ch. 7 — Basic Elements of Noncooperative Games (pp. 219–234)
**Topics:** T1 Normal-form games #topic/normal-form · T7 Extensive form #topic/extensive-form · T6 Mixed strategies #topic/mixed-strategies
### §7.A — Introduction (p. 219) · §7.B — What Is a Game? (p. 219)
### §7.C — The Extensive Form Representation of a Game (p. 221)
- Game trees, information sets, perfect and imperfect information (lists: pp. 221–225).
**Materials:** notes [[Notas/L03/L03-01-extensive-form|L03 extensive form]] · quiz [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#tree|L3-1 tree]] · [[Map/topics-index#Topic: Extensive form, strategies and information|T7]]
### §7.D — Strategies and the Normal Form Representation of a Game (p. 228)
- Strategies as complete contingent plans; the normal form of an extensive game (lists: pp. 228–231).
**Materials:** notes [[Notas/L01/L01-01-games-normal-form|L01 normal form]], [[Notas/L03/L03-03-normal-form-and-paths|L03 normal form and paths]] · quiz [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#strategy|L1-1 strategy]] · [[Map/topics-index#Topic: Normal-form games and solution concepts|T1]]
### §7.E — Randomized Choices (p. 231)
- Mixed and behavior strategies (to confirm). Exercises p. 233.
**Materials:** notes [[Notas/L02/L02-07-mixed-strategies|L02 mixed strategies]], [[Notas/L03/L03-02-strategies|L03 strategies]] · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]

## Ch. 8 — Simultaneous-Move Games (pp. 235–266)
**Topics:** T2 Dominance and IESDS #topic/dominance-iesds · T3 Rationalizability #topic/rationalizability · T4 Nash equilibrium #topic/nash-equilibrium · T6 Mixed strategies #topic/mixed-strategies · T15 Bayesian games #topic/bayesian-games
Exercises pp. 262–266.
### §8.A — Introduction (p. 235)
### §8.B — Dominant and Dominated Strategies (p. 236)
- Strictly and weakly dominant and dominated strategies; iterated deletion (lists: pp. 236–241).
**Materials:** notes [[Notas/L01/L01-04-dominance|L01 dominance]], [[Notas/L01/L01-06-iesds|L01 IESDS]] · items [[Listas/pratica-lecture-01#13. MWG 8.B.1|L1 #13 (8.B.1)]], [[Listas/pratica-lecture-01#23. MWG 8.B.3|L1 #23 (8.B.3)]], [[Listas/pratica-lecture-01#20. MWG 8.B.4|L1 #20 (8.B.4)]], [[Listas/pratica-lecture-01#21. MWG 8.B.5|L1 #21 (8.B.5)]], [[Listas/pratica-lecture-01#22. MWG 8.B.7|L1 #22 (8.B.7)]] · real #6 (8.B.5) · [[Map/topics-index#Topic: Dominance and IESDS|T2]]
### §8.C — Rationalizable Strategies (p. 242)
- Rationalizability and its relation to iterated strict dominance (lists: pp. 242–245).
**Materials:** notes [[Notas/L02/L02-01-best-response-rationalizability|L02 best responses and rationalizability]] · item [[Listas/pratica-lecture-02#19. MWG 8.C.1|L2 #19 (8.C.1)]] · [[Map/topics-index#Topic: Best responses and rationalizability|T3]]
### §8.D — Nash Equilibrium (p. 246)
- Pure and mixed Nash equilibrium; existence (lists: pp. 246–253).
**Materials:** notes [[Notas/L02/L02-02-nash-equilibrium|L02 Nash equilibrium]], [[Notas/L02/L02-09-existence|L02 existence]] · items [[Listas/pratica-lecture-02#18. MWG 8.D.2|L2 #18 (8.D.2)]], [[Listas/pratica-lecture-02#21. MWG 8.D.3|L2 #21 (8.D.3)]], [[Listas/pratica-lecture-02#23. MWG 8.D.6|L2 #23 (8.D.6)]] · real #12 (8.D.6) · [[Map/topics-index#Topic: Nash equilibrium|T4]], [[Map/topics-index#Topic: Mixed strategies and existence|T6]]
### §8.E — Games of Incomplete Information: Bayesian Nash Equilibrium (p. 253)
- Bayesian games and BNE, the formal side of Lecture 7 (lists: pp. 253–257).
**Materials:** notes [[Notas/L07/L07-01-bayesian-games-harsanyi|L07 Bayesian games]], [[Notas/L07/L07-02-bayesian-nash-equilibrium|L07 BNE]] · [[Map/topics-index#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
### §8.F — The Possibility of Mistakes: Trembling-Hand Perfection (p. 258) · Appendix A — Existence of Nash Equilibrium (p. 260)
- Trembling-hand perfection: not used by the lectures. Appendix A: the existence proof behind Nash's theorem.
**Materials:** notes [[Notas/L02/L02-09-existence|L02 existence]] · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]

## Ch. 9 — Dynamic Games (pp. 267–306)
**Topics:** T8 Subgame perfection #topic/spe · T9 Commitment #topic/commitment · T11 Bargaining #topic/bargaining · T18 PBE #topic/pbe
Exercises pp. 301–306.
### §9.A — Introduction (p. 267)
### §9.B — Sequential Rationality, Backward Induction, and Subgame Perfection (p. 268)
- Backward induction, subgames, SPNE; Example 9.B.1 (entry, pp. 268–269) on credibility (lists: pp. 267–281).
**Materials:** notes [[Notas/L03/L03-04-sequential-rationality-backward-induction|L03 backward induction]], [[Notas/L03/L03-05-subgame-perfection|L03 subgame perfection]] · items [[Listas/pratica-lecture-03#19. MWG 9.B.4|L3 #19 (9.B.4)]], [[Listas/pratica-lecture-03#20. MWG 9.B.5|L3 #20 (9.B.5)]] · quiz [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#spe|L3-2 spe]], [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#cred|L3-3 cred]] · [[Map/topics-index#Topic: Backward induction and subgame perfection|T8]]
### §9.C — Beliefs and Sequential Rationality (p. 282)
- Systems of beliefs, weak PBE, sequential equilibrium (lists: pp. 282–292).
**Materials:** notes [[Notas/L08/L08-02-beliefs-and-pbe|L08 beliefs and PBE]], [[Notas/L08/L08-03-sequential-equilibrium|L08 sequential equilibrium]] · quiz [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#se|L8-1 se]] · [[Map/topics-index#Topic: Perfect Bayesian equilibrium|T18]]
### §9.D — Reasonable Beliefs and Forward Induction (p. 292)
- Restrictions on off-path beliefs (to confirm); background for the intuitive criterion.
**Materials:** notes [[Notas/L08/L08-08-intuitive-criterion|L08 intuitive criterion]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]

## Ch. 9, Appendix A — Finite and Infinite Horizon Bilateral Bargaining (p. 296)
**Subtopics:**
- Example 9.AA.1 — finite-horizon alternating offers solved by backward induction; the split depends on who moves last.
- Example 9.AA.2 — infinite-horizon alternating offers; unique SPNE split driven by discount factors (Rubinstein).

**Linked materials:**
- Rules: [[rules/02_barganha|Topic 2 — Bargaining]]
- Exercises: [[Map/exercises-index|9.B.7, 9.B.12, 9.B.13]]

**Materials:** notes [[Notas/L04/L04-06-finite-alternating-offers|L04 finite alternating offers]], [[Notas/L04/L04-07-rubinstein-infinite-horizon|L04 Rubinstein]] · items [[Listas/pratica-lecture-04#22. MWG 9.B.12|L4 #22 (9.B.12)]], [[Listas/pratica-lecture-04#23. MWG 9.B.13 (with 9.B.7, which it builds on)|L4 #23 (9.B.13 with 9.B.7)]] · quiz [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#rub|L4-3 rub]] · [[Map/topics-index#Topic: Strategic bargaining|T11]]

## Ch. 12 — Market Power (pp. 383–435)
**Topics:** T5 Oligopoly #topic/oligopoly · T9 Commitment #topic/commitment · T12 Repeated games #topic/repeated-games · T13 Collusion #topic/collusion
Exercises pp. 428–435. §12.A Introduction (p. 383) and §12.B Monopoly Pricing (p. 384) are background.
### §12.C — Static Models of Oligopoly (p. 387)
- Bertrand and Cournot models (to confirm: subsection pages).
**Materials:** notes [[Notas/L02/L02-03-cournot|L02 Cournot]], [[Notas/L02/L02-04-bertrand|L02 Bertrand]] · [[Map/topics-index#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]
### §12.D — Repeated Interaction (p. 400)
- Finitely repeated Bertrand unravels (lists: pp. 400–401); infinitely repeated price competition and collusion.
**Materials:** notes [[Notas/L05/L05-01-finite-repetition-unraveling|L05 unraveling]], [[Notas/L06/L06-03-bertrand-market-structure|L06 Bertrand and market structure]] · quiz [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#bertrand|L6-2 bertrand]] · [[Map/topics-index#Topic: Collusion and price wars|T13]]
### §12.E — Entry (p. 405) · §12.F — The Competitive Limit (p. 411)
### §12.G — Strategic Precommitments to Affect Future Competition (p. 414)
- Two-stage games in which a first-stage choice changes later competition (to confirm).
**Materials:** notes [[Notas/L03/L03-06-credibility-entry-commitment|L03 credibility and commitment]] · [[Map/topics-index#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]
### Ch. 12, Appendix A — Infinitely Repeated Games and the Folk Theorem (p. 417)
- Nash reversion, minimax payoffs, the folk theorem (lists: pp. 417–422); in-text Exercise 12.AA.1 (p. 420), end-of-chapter Exercise 12.AA.2 (p. 435).
**Materials:** notes [[Notas/L05/L05-06-folk-theorem|L05 folk theorem]] · items [[Listas/pratica-lecture-05#16. MWG 12.AA.1|L5 #16 (12.AA.1)]], [[Listas/pratica-lecture-05#17. MWG 12.AA.2|L5 #17 (12.AA.2)]] · quiz [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#folk|L5-3 folk]] · [[Map/topics-index#Topic: Repeated games and the folk theorem|T12]]
### Ch. 12, Appendix B — Strategic Entry Deterrence and Accommodation (p. 423)
**Materials:** notes [[Notas/L03/L03-06-credibility-entry-commitment|L03 credibility, entry and commitment]], [[Notas/L08/L08-07-limit-pricing|L08 limit pricing]] · [[Map/topics-index#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]

## Ch. 13 — Adverse Selection, Signaling, and Screening (pp. 436–476)
**Topics:** T16 Adverse selection #topic/adverse-selection · T19 Signaling and refinements #topic/signaling

### §13.A — Introduction (p. 436)
- Asymmetric information at the time of contracting; overview of the three responses.

### §13.B — Informational Asymmetries and Adverse Selection (pp. 437–449)
**Subtopics:**
- Labour-market adverse selection: workers' types unobservable, wage reflects average quality of those who accept.
- Akerlof's lemons logic: unraveling of the market.
- Competitive equilibrium vs. Pareto optimality; multiple equilibria; game-theoretic (wage-offer) foundation.
- Constrained Pareto optimality and market interventions.

**Linked materials:** Rules: [[rules/07_selecao_adversa|Topic 7]] · Exercises: [[Map/exercises-index|13.B.1–13.B.10]]
**Materials:** notes [[Notas/L07/L07-05-adverse-selection-lemons|L07 adverse selection and lemons]] · items [[Listas/pratica-lecture-07#19. MWG 13.B.1|L7 #19 (13.B.1)]], [[Listas/pratica-lecture-07#20. MWG 13.B.2|L7 #20 (13.B.2)]] · quiz [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#lemons|L7-2 lemons]] · [[Map/topics-index#Topic: Adverse selection|T16]]

### §13.C — Signaling (pp. 450–459)
**Subtopics:**
- Spence education signaling: unproductive education as a costly signal.
- Separating and pooling perfect Bayesian equilibria; single-crossing.
- Welfare effects of signaling.

**Linked materials:** Rules: [[rules/07_selecao_adversa|Topic 7 — labour-market signaling application]] · Exercises: [[Map/exercises-index|13.C.1–13.C.6]]
**Materials:** notes [[Notas/L08/L08-06-spence-job-market|L08 Spence]] · items [[Listas/pratica-lecture-08#22. MWG 13.C.1|L8 #22 (13.C.1)]], [[Listas/pratica-lecture-08#24. MWG 13.C.2|L8 #24 (13.C.2)]], [[Listas/pratica-lecture-08#25. MWG 13.C.4|L8 #25 (13.C.4)]], [[Listas/pratica-lecture-08#23. MWG 13.C.5|L8 #23 (13.C.5)]] · quiz [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#spence|L8-2 spence]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]

### §13.D — Screening (pp. 460–466)
**Subtopics:**
- Uninformed party moves first, offering a menu (contracts, tasks).
- Equilibrium existence problems (Rothschild–Stiglitz-type logic); separating contracts.

**Linked materials:** Rules: [[rules/07_selecao_adversa|Topic 7]] · Exercises: [[Map/exercises-index|13.D.1–13.D.3]]

### Appendix A — Reasonable-Beliefs Refinements in Signaling Games (p. 467)
- Equilibrium domination; the Intuitive Criterion (Cho–Kreps) selects the best separating equilibrium with two types.
- Exercises: [[Map/exercises-index|13.AA.1]]
- **Materials:** notes [[Notas/L08/L08-08-intuitive-criterion|L08 intuitive criterion]] · quiz [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ic|L8-3 ic]], [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ref|ref]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]

## Ch. 14 — The Principal-Agent Problem (pp. 477–510)

### §14.A — Introduction (p. 477)
- Asymmetries that arise **after** contracting: hidden actions and hidden information.

### §14.B — Hidden Actions (Moral Hazard) (pp. 478–487)
**Subtopics:**
- Owner–manager model; first best with observable effort.
- Risk-neutral manager: selling the firm restores the first best.
- Risk-averse manager: the incentives-vs-insurance trade-off; FOC of the optimal compensation scheme.
- Two effort levels; role of informative signals.

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]] · [[rules/09_gestao_risco_moral|Topic 9]] · Exercises: [[Map/exercises-index|14.B.1–14.B.8]]

### §14.C — Hidden Information (and Monopolistic Screening) (pp. 488–500)
**Subtopics:**
- Manager privately observes a state; optimal contract under full observability vs. hidden state.
- Monopolistic screening (price discrimination menus).

**Linked materials:** Rules: [[rules/06_racionalidade_limitada_contratos|Topic 6]] · [[rules/07_selecao_adversa|Topic 7]] · Exercises: [[Map/exercises-index|14.C.1–14.C.8]]

### §14.D — Hidden Actions and Hidden Information: Hybrid Models (p. 501)
- Combined models.

### Appendix A — Multiple Effort Levels in the Hidden Action Model (p. 502)
### Appendix B — A Formal Solution of the Principal-Agent Problem with Hidden Information (p. 504)

## Ch. 16 — Equilibrium and Its Basic Welfare Properties (pp. 545–)

### §16.A — Introduction (p. 545) · §16.B — The Basic Model and Definitions (p. 546)

### §16.C — The First Fundamental Theorem of Welfare Economics (p. 549)
**Subtopics:**
- Proposition 16.C.1 (First Welfare Theorem): with locally nonsatiated preferences, a price equilibrium is Pareto optimal.
- Role of complete markets and price-taking; what the theorem does not say.

**Linked materials:** Rules: [[rules/03_eficiencia_organizacao|Topic 3]] · [[rules/04_coordenacao_mercado|Topic 4]] · Exercises: [[Map/exercises-index|16.C.2–16.C.4]]

Ch. 23 (Incentives and Mechanism Design, p. 857): out of scope unless a lecture brings it.

---

# Varian, *Intermediate Microeconomics with Calculus*, 1st ed. (2014)

#book/varian

⚠️ **Edition divergence:** the syllabus cites *Intermediate Microeconomics*, 8th ed. (2010). The
local book is the calculus version: same chapter titles and order, but cite it as "Varian
(2014, with Calculus)" with these page numbers. The scanned Ch. 11–13 excerpt
(`Risco_Incerteza_Varian.pdf`) is superseded.

## Ch. 12 — Uncertainty (pp. 219–238)
**Subtopics:**
- §12.1 Contingent consumption (p. 219): consumption in each state of nature as a separate good; the insurance budget line.
- Expected utility (p. 225) and why it is reasonable (p. 226): utility additive across states, weighted by probabilities.
- §12.5 Risk aversion (p. 228): concave utility; expected value vs. expected utility; Example: the demand for insurance.
- §12.6 Diversification · §12.7 Risk spreading (p. 235): pooling independent risks; role of the stock market (p. 236).

**Linked materials:** Rules: [[rules/09_gestao_risco_moral|Topic 9 — risk aversion and risk sharing]] · Exercises: [[Map/exercises-index|Varian 12 RQ 1–6]]

## Ch. 30 — Game Applications (pp. 557–585)
**Subtopics:**
- Games of commitment (p. 572): the value of tying one's hands (the frog and the scorpion, the kindly kidnapper).
- **Hold Up** (p. 579): specific investment followed by renegotiation; the investor anticipates expropriation and under-invests.
- **§30.7 Bargaining** (p. 581): Rubinstein alternating offers; the split depends on patience.
- **The Ultimatum Game** (p. 582): theory vs. experimental evidence.

**Linked materials:** Rules: [[rules/02_barganha|Topic 2 — Bargaining]] · [[rules/06_racionalidade_limitada_contratos|Topic 6 — incomplete contracts and hold-up]] · Exercises: [[Map/exercises-index|Varian 30 RQ 5]]

## Ch. 32 — Exchange (pp. 601–628)
**Subtopics:**
- Edgeworth box (p. 602); trade (p. 604).
- §32.3 Pareto efficient allocations (p. 605): the contract curve.
- Market trade (p. 609); Walras' law (p. 613).
- §32.11 Efficiency and equilibrium (p. 621); **§32.12 Implications of the First Welfare Theorem** (p. 623): what the theorem implies for designing ways to allocate resources, and its implicit assumptions (no consumption externalities, price-taking); Second Welfare Theorem (p. 624).

**Linked materials:** Rules: [[rules/03_eficiencia_organizacao|Topic 3]] · [[rules/04_coordenacao_mercado|Topic 4]] · Exercises: [[Map/exercises-index|Varian 32 RQ 1–5]]

## Ch. 33 — Production (pp. 629–651)
**Subtopics:**
- Robinson Crusoe economy (p. 629); Crusoe, Inc. (p. 631): separating consumption and production decisions through prices.
- Production and the welfare theorems (pp. 637–638); comparative advantage (p. 640).
- **§33.14 Decentralized resource allocation** (p. 648): prices coordinate separate decision-makers without central knowledge, which is the market side of the market-vs-management comparison.

**Linked materials:** Rules: [[rules/04_coordenacao_mercado|Topic 4 — prices as coordination]] · Exercises: [[Map/exercises-index|Varian 33 RQ 1–5]]

## Ch. 35 — Externalities (pp. 666–688)
**Subtopics:**
- **§35.2 Quasilinear preferences and the Coase theorem** (p. 670): with quasilinear utility the efficient level does not depend on the assignment of property rights; bargaining reaches it.
- Production externalities (p. 672); market signals (p. 680); tragedy of the commons (p. 681).

**Linked materials:** Rules: [[rules/02_barganha|Topic 2 — Coase]] · [[rules/03_eficiencia_organizacao|Topic 3]] · Exercises: [[Map/exercises-index|Varian 35 RQ 1–4]]

## Ch. 38 — Asymmetric Information (pp. 740–762)
**Subtopics:**
- §38.1 The market for lemons (p. 741): Akerlof unraveling.
- §38.2 Quality choice (p. 742): endogenous quality when buyers cannot observe it.
- §38.3 Adverse selection (p. 744): insurance example.
- §38.4 Moral hazard (p. 746): insurance against theft reduces care.
- §38.5 Moral hazard and adverse selection (p. 747): hidden action vs. hidden information.
- §38.6 Signaling (p. 748): Spence education model; Example: the sheepskin effect.
- §38.7 Incentives (p. 752): principal–agent incentive schemes (rent, wage labour, sharecropping, take-it-or-leave-it); Examples: voting rights in the corporation, Chinese economic reforms.
- §38.8 Asymmetric information (p. 757): once effort is unobservable, the incentive schemes of §38.7 must also share risk, which is why sharecropping survives although renting dominates with observable effort; Examples: monitoring costs, the Grameen Bank.

**Linked materials:** Rules: [[rules/07_selecao_adversa|Topic 7]] · [[rules/08_risco_moral|Topic 8]] · [[rules/09_gestao_risco_moral|Topic 9]] · Exercises: [[Map/exercises-index|Varian 38 RQ 1–5]]

Out of scope: Ch. 1–11, 13–29, 31, 34, 36, 37 (VCG mechanism = mechanism design).

---

# Cabral, *Introduction to Industrial Organization*, 2nd ed. (2017)

#book/cabral

Syllabus edition. Cabral is a complementary source for the market side (Topics 3–4), the
boundaries of the firm (Topic 5), and an intermediate-level treatment of information (Topics 7–9).
In the game-theory sequence it supplies Ch. 7 (games, commitment, repeated games; Lectures 3 and 5)
and Ch. 9 (collusion and price wars; Lecture 6).

## Ch. 3 — Firms (pp. 35–65)

### §3.3 — Do firms maximize profits? (pp. 52–54)
**Subtopics:**
- Separation of ownership and control: managers' objectives differ from shareholders'.
- Internal discipline (p. 52): incentive contracts; dispersed shareholders have little incentive to monitor.
- Labour-market discipline (p. 53): managers care about their reputation in the managerial labour market; product-market discipline (competition); capital-market discipline (takeovers, the "raider").

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]] · [[rules/09_gestao_risco_moral|Topic 9]]

### §3.4 — What determines a firm's boundaries? (pp. 54–56)
**Subtopics:**
- Horizontal extension vs. vertical integration (p. 54).
- The vertical boundaries of the firm (p. 55): make or buy; specific assets and the hold-up problem; tapered integration; franchising; investment incentives vs. performance incentives.

**Linked materials:** Rules: [[rules/05_coordenacao_management|Topic 5 — market vs. management]] · [[rules/06_racionalidade_limitada_contratos|Topic 6 — incomplete contracts]]

### §3.5 — Why are firms different? (pp. 56–59)
**Subtopics:**
- Sustained competitive advantage: impediments to imitation, causal ambiguity, strategy, culture, history, the learning curve.
- **Toyota's procurement system** (p. 57) as a hard-to-imitate organizational advantage.
- Management practices field experiment with Indian textile firms (p. 58).

**Linked materials:** Rules: [[rules/01_organizacoes_importam|Topic 1 — Ford × GM × Toyota]]

## Ch. 4 — Competition, Equilibrium, and Efficiency (pp. 67–91)
- §4.1 Perfect competition (p. 67); §4.2 Competitive selection (p. 74).
- **§4.4 Efficiency** (p. 81): allocative and productive efficiency of competitive markets; total surplus.

**Linked materials:** Rules: [[rules/03_eficiencia_organizacao|Topic 3]] · [[rules/04_coordenacao_mercado|Topic 4]]

## Ch. 5 — Market Failure and Public Policy (pp. 93–119)
- §5.1 Externalities and market failure (p. 93): Pigou tax, property rights; **the Coase Theorem** (p. 96).
- **§5.2 Imperfect information** (p. 99): used-car lemons unraveling; adverse selection in health insurance (p. 100); advantageous selection (p. 101); link to moral hazard (p. 102).
- §5.4 Regulation (p. 107): context for financial regulation.

**Linked materials:** Rules: [[rules/02_barganha|Topic 2 — Coase]] · [[rules/03_eficiencia_organizacao|Topic 3]] · [[rules/07_selecao_adversa|Topic 7]]

## Ch. 6 — Price Discrimination (pp. 121–155)
- §6.2 Self selection (p. 130): menus that make consumers reveal their type, i.e. screening.
- §6.3 Non-linear pricing (p. 135).
- §6.4 Auctions and negotiations (p. 140): **Negotiations** (p. 143) as bilateral price formation by offers and counter-offers.

**Linked materials:** Rules: [[rules/07_selecao_adversa|Topic 7 — screening]] · [[rules/02_barganha|Topic 2]]

## Ch. 7 — Games and Strategies (pp. 159–183)
**Topics:** T5 Oligopoly #topic/oligopoly · T8 Subgame perfection #topic/spe · T9 Commitment #topic/commitment · T12 Repeated games #topic/repeated-games
- §7.1 Nash equilibrium (p. 161): dominance and Nash equilibrium in IO examples (study guide: pp. 161–163, Lecture 1 application).
- §7.2 Sequential games (p. 167): backward induction, commitment; the value of credible commitment (pp. 169–170, Figs. 7.7–7.8, per quiz L3-3).
- §7.3 Repeated games (p. 172): the indefinitely repeated prisoner's dilemma (lists: pp. 172–174).
- **§7.4 Information** (p. 174): health-insurance pricing game with privately informed patients; standard games with asymmetric information (p. 176).
- Exercises used by the lists: 7.8 (p. 180), 7.12 (p. 181), 7.13 (p. 182).

**Linked materials:** Rules: [[rules/02_barganha|Topic 2]] · [[rules/07_selecao_adversa|Topic 7]]
**Materials:** notes [[Notas/L03/L03-06-credibility-entry-commitment|L03 credibility, entry and commitment]], [[Notas/L05/L05-01-finite-repetition-unraveling|L05 finite repetition]] · items [[Listas/pratica-lecture-05#2. Cabral 7.8|L5 #2 (7.8)]], [[Listas/pratica-lecture-05#10. Cabral 7.12|L5 #10 (7.12)]], [[Listas/pratica-lecture-05#3. Cabral 7.13|L5 #3 (7.13)]] · quiz [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#cred|L3-3 cred]] · [[Map/topics-index#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]], [[Map/topics-index#Topic: Repeated games and the folk theorem|T12]]

## Ch. 9 — Collusion and Price Wars (pp. 217–247)
**Topics:** T13 Collusion and price wars #topic/collusion · T12 Repeated games #topic/repeated-games
Brought into scope by Lecture 6. Sections and pages from the TOC; chapter opener (p. 217), §9.1 (p. 218) and the exercise pages checked in the PDF (offset 12 for a 1-based viewer page; registry entry `Cabral`).
- §9.1 Stability of collusive agreements (p. 218): grim strategies in repeated Bertrand; the discount-factor condition (9.5) (lists: pp. 218–222).
- §9.2 Price wars (p. 222) (lists: pp. 222–227).
- §9.3 Factors that facilitate collusion (p. 227): frequency of interaction, few and similar firms, multimarket contact (lists: pp. 227–231).
- §9.4 Empirical analysis of cartels and collusion (p. 232) · §9.5 Public policy (p. 234).
- Exercises: review and practice from p. 242 (9.1 p. 242, 9.15 p. 244); challenging exercises from p. 245 (9.19).

**Materials:** notes [[Notas/L06/L06-03-bertrand-market-structure|L06 Bertrand and market structure]], [[Notas/L06/L06-04-punishments-price-wars|L06 punishments and price wars]] · items [[Listas/pratica-lecture-06#5. Cabral 9.1|L6 #5 (9.1)]], [[Listas/pratica-lecture-06#19. Cabral 9.15|L6 #19 (9.15)]], [[Listas/pratica-lecture-06#22. Cabral 9.19|L6 #22 (9.19)]] · quiz [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#factors|L6-2 factors]], [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#wars|wars]] · [[Map/topics-index#Topic: Collusion and price wars|T13]]

## Ch. 13 — Vertical Relations (pp. 333–347)
- **§13.1 Vertical integration** (p. 334): double marginalization; downstream competition (p. 337); **investment incentives** (p. 338), i.e. specific investments and hold-up.
- §13.2 Vertical restraints (p. 340): franchise fees, resale price maintenance, exclusive territories.

**Linked materials:** Rules: [[rules/05_coordenacao_management|Topic 5]] · [[rules/06_racionalidade_limitada_contratos|Topic 6]]

Out of scope: Ch. 2, 8, 10–12, 14–16 (oligopoly, entry, mergers, differentiation, innovation, networks), except §14.2 (Hotelling's linear city, pp. 354, 358–360), used as a Lecture 1 application. Ch. 9 is mapped above for Lecture 6.

---

# Giambiagi & Garcia (orgs.), *Risco e Regulação* (2010)

#book/giambiagi-garcia

Edited volume in Portuguese (18 chapters, different authors). Titles are cited verbatim. It is the
context source for Topics 8–9 (incentives, moral hazard and regulation in the 2008 crisis); it has no
exercises.

## Cap. 1 — "Origens da Crise" (Mailson da Nóbrega, pp. 3–18)
- "Incentivos incorretos" (p. 12): misaligned incentives along the mortgage chain.

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]]

## Cap. 7 — "Incentivos e Crise" (Vinicius Carrasco, pp. 99–110) ★ most relevant chapter
- "Aspectos básicos da teoria econômica de incentivos" (p. 100): principal–agent model; incentives based on inputs (monitoring) vs. output (pay for performance).
- "Incentivos para executivos do setor financeiro" (p. 102): executive pay and performance measures before the crisis.
- "A crise e alguns aspectos do desenho de incentivos em bancos" (p. 105): short-term debt + equity-based pay → excessive risk-taking.
- "Regulação ou supervisão de pagamentos: por que pode fazer sentido?" (p. 108).

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]] · [[rules/09_gestao_risco_moral|Topic 9]]

## Cap. 8 — "Estrutura, Concorrência e Estabilidade" (João Manoel Pinho de Mello, pp. 111–123)
- "Risco excessivo e crises bancárias" (p. 111); "Tradeoff eficiência-estabilidade" (p. 112).
- **Quadro 8.1 "Competição Bancária e a Crise do Savings and Loans"** (p. 115): deregulated deposit rates plus FSLIC deposit insurance removed depositors' incentive to monitor; cost to taxpayers ≈ US$150 billion. This is the syllabus application for Topic 8.
- "Estrutura e estabilidade" (p. 117).

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8 — S&L crisis application]]

## Cap. 11 — "A Crise Bancária Norte-americana: algumas Lições da Experiência Brasileira" (Gustavo Franco & Luiz Alberto Rosman, pp. 157–169)
- Lei 6.024/74 (p. 160): bank intervention and liability of controllers as a moral-hazard brake; "Operações PROER e 'Maiden Lane'" (p. 163).

**Linked materials:** Rules: [[rules/08_risco_moral|Topic 8]]

## Cap. 16 — "Derivativos e Governança Corporativa: O Caso Sadia" (Ana Novaes, pp. 239–257)
- Enron and Sarbanes-Oxley (p. 240); Sadia's 2008 derivative losses (p. 243); "O caso Sadia — governança corporativa" (p. 248).

**Linked materials:** Rules: [[rules/09_gestao_risco_moral|Topic 9 — governance as moral-hazard control]]

Other chapters (2–6, 9–10, 12–15, 17–18: systemic risk, regulation, risk models, macro, central
bank, credit risk, pension funds, derivatives) are background only.

---

# Tadelis, *Game Theory: An Introduction* (2013)

#book/tadelis

**Main reference since 2026-10-13**: the Lecture 1 slides follow its notation and examples. Publisher
e-book with a clean text layer; PDF index = printed + 18 throughout (registry entry `Tadelis`).
Sections and pages from the TOC (PDF 7–12), each one found in the chapter body at the stated page.
Every chapter ends with exercises; **the book prints no answers** (the preface, p. xiii, says about
half have solutions on the publisher's web page and the rest are instructor-only).

## Part I — Rational Decision Making

## Ch. 1 — The Single-Person Decision Problem (pp. 3–13)
### §1.1 — Actions, Outcomes, and Preferences (p. 4)
- 1.1.1 Preference Relations (p. 5); 1.1.2 Payoff Functions (p. 7).
### §1.2 — The Rational Choice Paradigm (p. 9)
### §1.3 — Summary (p. 11) · §1.4 — Exercises 1.1–1.7 (pp. 11–13)

## Ch. 2 — Introducing Uncertainty and Time (pp. 14–40)
### §2.1 — Risk, Nature, and Random Outcomes (p. 14)
- 2.1.1 Finite Outcomes and Simple Lotteries (p. 15); 2.1.2 Simple versus Compound Lotteries (p. 16); 2.1.3 Lotteries over Continuous Outcomes (p. 17).
### §2.2 — Evaluating Random Outcomes (p. 18)
- 2.2.1 Expected Payoff: The Finite Case (p. 19); 2.2.2 The Continuous Case (p. 20); 2.2.3 Caveat: It's Not Just the Order Anymore (p. 21); 2.2.4 Risk Attitudes (p. 22); 2.2.5 The St. Petersburg Paradox (p. 23).
### §2.3 — Rational Decision Making with Uncertainty (p. 24)
- 2.3.1 Rationality Revisited (p. 24); 2.3.2 Maximizing Expected Payoffs (p. 24).
### §2.4 — Decisions over Time (p. 26)
- 2.4.1 Backward Induction (p. 26); 2.4.2 Discounting Future Payoffs (p. 28).
### §2.5 — Applications (p. 29)
- 2.5.1 The Value of Information (p. 29); 2.5.2 Discounted Future Consumption (p. 31).
### §2.6 — Theory versus Practice (p. 32) · §2.7 — Summary (p. 33) · §2.8 — Exercises 2.1–2.13 (pp. 33–40)

## Part II — Static Games of Complete Information

## Ch. 3 — Preliminaries (pp. 43–58) · Lecture 1
**Topics:** T1 Normal-form games and solution concepts #topic/normal-form
- Chapter opening (pp. 43–45): static games; games of complete information; **Definition 3.1, common knowledge** (p. 45).
### §3.1 — Normal-Form Games with Pure Strategies (p. 46)
- Definition 3.2 pure strategy (p. 46); **Definition 3.3 normal-form game** (p. 47).
- 3.1.1 Example: The Prisoner's Dilemma (p. 48; mum/fink, payoffs −2, −4, −5, −1); 3.1.2 Example: Cournot Duopoly (p. 49); 3.1.3 Example: Voting on a New Agenda (p. 49).
**Materials:** slides [[Aula/Lecture01.pdf|Lecture 1]] · notes [[Notas/L01/L01-01-games-normal-form|L01 games and the normal form]], [[Notas/L01/L01-02-information-and-strategies|L01 information and strategies]] · quiz [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#nf|L1-1 nf]], [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#strategy|strategy]], [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#ck|ck]] · [[Map/topics-index#Topic: Normal-form games and solution concepts|T1]]
### §3.2 — Matrix Representation: Two-Player Finite Game (p. 50)
- Definition 3.4 finite game (p. 51); 3.2.1 Example: The Prisoner's Dilemma (p. 51; the matrix is on p. 52); 3.2.2 Example: Rock-Paper-Scissors (p. 52).
**Materials:** notes [[Notas/L01/L01-01-games-normal-form|L01 games and the normal form]] · quiz [[Simulados/quiz-lecture01-1-normal-form-2026-10-13#payoffs|L1-1 payoffs]] · mini case [[Resolucao/mini-case-lecture-01.pdf|L1 pharmacy]] part (a)
### §3.3 — Solution Concepts (p. 52)
- Altruistic Prisoner's Dilemma (p. 53); Battle of the Sexes (pp. 53–54); solution concept and equilibrium (p. 54).
- 3.3.1 Assumptions and Setup (p. 54; rationality, intelligence, common knowledge, self-enforcement p. 55).
- 3.3.2 Evaluating Solution Concepts (p. 55): **existence** (p. 55), **uniqueness** (pp. 55–56), **invariance** (p. 56).
- 3.3.3 Evaluating Outcomes (p. 56): **Definition 3.5, Pareto dominance and Pareto optimality** (p. 57).
**Materials:** notes [[Notas/L01/L01-03-solution-concepts|L01 solution concepts]], [[Notas/L01/L01-05-pareto-social-dilemmas|L01 Pareto and social dilemmas]] · quiz [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#pareto|L1-2 pareto]] · [[Listas/lista-lecture-01.pdf|exam-style list L1]] Question 2
### §3.4 — Summary (p. 57) · §3.5 — Exercises 3.1–3.7 (p. 58)
**Materials:** items [[Listas/pratica-lecture-01#1. Tadelis 3.2|L1 #1 (3.2)]], [[Listas/pratica-lecture-01#2. Tadelis 3.4|L1 #2 (3.4)]], [[Listas/pratica-lecture-01#9. Tadelis 3.6|L1 #9 (3.6)]], [[Listas/pratica-lecture-01#10. Tadelis 3.7|L1 #10 (3.7)]]

## Ch. 4 — Rationality and Common Knowledge (pp. 59–78) · Lectures 1–2
**Topics:** T2 Dominance and IESDS #topic/dominance-iesds · T3 Best responses and rationalizability #topic/rationalizability · T5 Oligopoly (Cournot by IESDS) #topic/oligopoly
### §4.1 — Dominance in Pure Strategies (p. 59)
- 4.1.1 Dominated Strategies (p. 59): Definition 4.1 strict dominance, Claim 4.1 (p. 60); advertising L/M/H game (p. 60).
- 4.1.2 Dominant Strategy Equilibrium (p. 61): Definitions 4.2–4.3, Proposition 4.1 (uniqueness) (p. 61).
- 4.1.3 Evaluating Dominant Strategy Equilibrium (p. 62): existence fails (Battle of the Sexes), invariance holds, Pareto failure; "mafia-modified" Prisoner's Dilemma (pp. 62–63); weak dominance remark (p. 63).
**Materials:** notes [[Notas/L01/L01-04-dominance|L01 dominance]] · quiz [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#dom|L1-2 dom]], [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#partnership|partnership]], [[Simulados/quiz-lecture01-2-dominance-pareto-2026-10-13#auction|auction]] · [[Map/topics-index#Topic: Dominance and IESDS|T2]]
### §4.2 — Iterated Elimination of Strictly Dominated Pure Strategies (p. 63)
- 4.2.1 Iterated Elimination and Common Knowledge of Rationality (p. 63): **the 3×3 game (4.1)** (p. 64); the IESDS algorithm and Definition 4.4 (p. 65).
- 4.2.2 Example: Cournot Duopoly (p. 65; convergence to $q_i = 30$, Figure 4.1 p. 67).
- 4.2.3 Evaluating IESDS (p. 67): existence yes, uniqueness no, Pareto (p. 68); Proposition 4.2 (p. 68).
**Materials:** notes [[Notas/L01/L01-06-iesds|L01 IESDS]], [[Notas/L01/L01-07-cournot-iesds|L01 Cournot by IESDS]], [[Notas/L01/L01-08-spatial-competition|L01 spatial competition]] · quiz [[Simulados/quiz-lecture01-3-iesds-2026-10-13#props|L1-3 props]], [[Simulados/quiz-lecture01-3-iesds-2026-10-13#ck|ck]], [[Simulados/quiz-lecture01-3-iesds-2026-10-13#cournot|cournot]], [[Simulados/quiz-lecture01-3-iesds-2026-10-13#space|space]] · mini case [[Resolucao/mini-case-lecture-01.pdf|L1 pharmacy]] parts (b)–(c) · [[Listas/lista-lecture-01.pdf|exam-style list L1]] Questions 4 and 6 · [[Map/topics-index#Topic: Dominance and IESDS|T2]]
### §4.3 — Beliefs, Best Response, and Rationalizability (p. 69)
- 4.3.1 The Best Response (p. 69); 4.3.2 Beliefs and Best-Response Correspondences (p. 71); 4.3.3 Rationalizability (p. 73); 4.3.4 The Cournot Duopoly Revisited (p. 73); 4.3.5 The "p-Beauty Contest" (p. 74); 4.3.6 Evaluating Rationalizability (p. 76).
**Materials:** notes [[Notas/L02/L02-01-best-response-rationalizability|L02 best responses and rationalizability]] · quiz [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#br|L2-1 br]] · [[Map/topics-index#Topic: Best responses and rationalizability|T3]]
### §4.4 — Summary (p. 76) · §4.5 — Exercises 4.1–4.10 (pp. 76–78; 4.10 *Popsicle Stands* is a discrete location game, p. 78)
**Materials:** items [[Listas/pratica-lecture-01#11. Tadelis 4.1|L1 #11 (4.1)]], [[Listas/pratica-lecture-01#12. Tadelis 4.2|L1 #12 (4.2)]], [[Listas/pratica-lecture-01#17. Tadelis 4.3|L1 #17 (4.3)]], [[Listas/pratica-lecture-01#24. Tadelis 4.4|L1 #24 (4.4)]], [[Listas/pratica-lecture-01#6. Tadelis 4.5|L1 #6 (4.5)]], [[Listas/pratica-lecture-01#15. Tadelis 4.6|L1 #15 (4.6)]], [[Listas/pratica-lecture-01#16. Tadelis 4.7|L1 #16 (4.7)]], [[Listas/pratica-lecture-01#18. Tadelis 4.10|L1 #18 (4.10)]] · real #1 (4.5), #3 (4.6), #4 (4.7)

## Ch. 5 — Pinning Down Beliefs: Nash Equilibrium (pp. 79–100) · Lecture 2
**Topics:** T4 Nash equilibrium #topic/nash-equilibrium · T5 Oligopoly and continuous games #topic/oligopoly
### §5.1 — Nash Equilibrium in Pure Strategies (p. 80)
- 5.1.1 Pure-Strategy Nash Equilibrium in a Matrix (p. 81); 5.1.2 Evaluating the Nash Equilibria Solution (p. 83).
**Materials:** slides [[Aula/Lecture02.pdf|Lecture 2]] · notes [[Notas/L02/L02-02-nash-equilibrium|L02 Nash equilibrium]] · quiz [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#ne|L2-1 ne]], [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#iesds|iesds]], [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#matrix|matrix]] · [[Map/topics-index#Topic: Nash equilibrium|T4]]
### §5.2 — Nash Equilibrium: Some Classic Applications (p. 83)
- 5.2.1 Two Kinds of Societies (p. 83); 5.2.2 The Tragedy of the Commons (p. 84); 5.2.3 Cournot Duopoly (p. 87); 5.2.4 Bertrand Duopoly (p. 88); 5.2.5 Political Ideology and Electoral Competition (p. 93; the **Hotelling** voting model, figure p. 94).
**Materials:** notes [[Notas/L02/L02-05-commons|L02 commons]], [[Notas/L02/L02-03-cournot|L02 Cournot]], [[Notas/L02/L02-04-bertrand|L02 Bertrand]], [[Notas/L02/L02-06-hotelling-voting|L02 Hotelling voting]] · quiz [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cournot|L2-2 cournot]], [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cartel|cartel]], [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#bertrand|bertrand]], [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#compare|compare]] · [[Map/topics-index#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]
### §5.3 — Summary (p. 95) · §5.4 — Exercises 5.1–5.18 (pp. 95–100; 5.15–5.16 Hotelling, p. 99)
**Materials:** items [[Listas/pratica-lecture-02#9. Tadelis 5.1|L2 #9 (5.1)]], [[Listas/pratica-lecture-02#10. Tadelis 5.2|L2 #10 (5.2)]], [[Listas/pratica-lecture-02#11. Tadelis 5.3|L2 #11 (5.3)]], [[Listas/pratica-lecture-02#3. Tadelis 5.5|L2 #3 (5.5)]], [[Listas/pratica-lecture-02#2. Tadelis 5.6|L2 #2 (5.6)]], [[Listas/pratica-lecture-02#12. Tadelis 5.8|L2 #12 (5.8)]], [[Listas/pratica-lecture-02#22. Tadelis 5.12|L2 #22 (5.12)]], [[Listas/pratica-lecture-02#25. Tadelis 5.15|L2 #25 (5.15)]] · real #7 (5.6), #9 (5.8)

## Ch. 6 — Mixed Strategies (pp. 101–126) · Lecture 2
**Topics:** T6 Mixed strategies and existence #topic/mixed-strategies · T2/T3 revisited (§6.3)
### §6.1 — Strategies, Beliefs, and Expected Payoffs (p. 102)
- 6.1.1 Finite Strategy Sets (p. 102); 6.1.2 Continuous Strategy Sets (p. 104); 6.1.3 Beliefs and Mixed Strategies (p. 105); 6.1.4 Expected Payoffs (p. 105).
**Materials:** notes [[Notas/L02/L02-07-mixed-strategies|L02 mixed strategies]] · quiz [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#mixed|L2-3 mixed]] · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]
### §6.2 — Mixed-Strategy Nash Equilibrium (p. 107)
- 6.2.1 Example: Matching Pennies (p. 108); 6.2.2 Example: Rock-Paper-Scissors (p. 111); 6.2.3 Multiple Equilibria: Pure and Mixed (p. 113).
**Materials:** notes [[Notas/L02/L02-07-mixed-strategies|L02 mixed strategies]] · quiz [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#indiff|L2-3 indiff]], [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#bos|bos]] · mini case [[Resolucao/mini-case-lecture-03.pdf|L3 work or shirk]] parts (a)–(d) ([[Resolucao/mini-case-lecture-03-short.pdf|short]])
### §6.3 — IESDS and Rationalizability Revisited (p. 114)
**Materials:** notes [[Notas/L02/L02-08-iesds-rationalizability-revisited|L02 IESDS and rationalizability revisited]] · item [[Listas/pratica-lecture-02#24. Tadelis 6.3|L2 #24 (6.3, reading)]] · [[Map/topics-index#Topic: Best responses and rationalizability|T3]]
### §6.4 — Nash's Existence Theorem (p. 117)
**Materials:** notes [[Notas/L02/L02-09-existence|L02 existence]] · quiz [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#exist|L2-3 exist]]
### §6.5 — Summary (p. 123) · §6.6 — Exercises 6.1–6.12 (pp. 123–126)
**Materials:** items [[Listas/pratica-lecture-02#7. Tadelis 6.1|L2 #7 (6.1)]], [[Listas/pratica-lecture-02#24. Tadelis 6.3|L2 #24 (6.3)]], [[Listas/pratica-lecture-02#16. Tadelis 6.5|L2 #16 (6.5)]], [[Listas/pratica-lecture-02#17. Tadelis 6.8|L2 #17 (6.8)]] · real #10 (6.8)

## Part III — Dynamic Games of Complete Information

## Ch. 7 — Preliminaries (pp. 129–150) · Lecture 3
**Topics:** T7 Extensive form, strategies and information #topic/extensive-form
### §7.1 — The Extensive-Form Game (p. 130)
- 7.1.1 Game Trees (p. 132); 7.1.2 Imperfect versus Perfect Information (p. 136).
**Materials:** slides [[Aula/Lecture03.pdf|Lecture 3]] · notes [[Notas/L03/L03-01-extensive-form|L03 extensive form]] · quiz [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#tree|L3-1 tree]] · case [[Cases/Brexit/brexit-game.pdf|Brexit]] sections (ii), (iii), (v) · [[Map/topics-index#Topic: Extensive form, strategies and information|T7]]
### §7.2 — Strategies and Nash Equilibrium (p. 137)
- 7.2.1 Pure Strategies (p. 137); 7.2.2 Mixed versus Behavioral Strategies (p. 139); 7.2.3 Normal-Form Representation of Extensive-Form Games (p. 143).
**Materials:** notes [[Notas/L03/L03-02-strategies|L03 strategies]], [[Notas/L03/L03-03-normal-form-and-paths|L03 normal form and paths]] · quiz [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#strat|L3-1 strat]]
### §7.3 — Nash Equilibrium and Paths of Play (p. 145)
**Materials:** notes [[Notas/L03/L03-03-normal-form-and-paths|L03 normal form and paths]] · quiz [[Simulados/quiz-lecture03-1-extensive-form-2026-10-25#nfpath|L3-1 nfpath]]
### §7.4 — Summary (p. 147) · §7.5 — Exercises 7.1–7.10 (pp. 147–150)
**Materials:** items [[Listas/pratica-lecture-03#1. Tadelis 7.1|L3 #1 (7.1)]], [[Listas/pratica-lecture-03#2. Tadelis 7.2|L3 #2 (7.2)]], [[Listas/pratica-lecture-03#9. Tadelis 7.4|L3 #9 (7.4)]], [[Listas/pratica-lecture-03#5. Tadelis 7.6|L3 #5 (7.6)]], [[Listas/pratica-lecture-03#10. Tadelis 7.9|L3 #10 (7.9)]], [[Listas/pratica-lecture-03#11. Tadelis 7.10|L3 #11 (7.10)]]

## Ch. 8 — Credibility and Sequential Rationality (pp. 151–174) · Lecture 3
**Topics:** T8 Backward induction and subgame perfection #topic/spe · T9 Commitment and credibility #topic/commitment · T5 (Stackelberg) #topic/oligopoly
### §8.1 — Sequential Rationality and Backward Induction (p. 152)
**Materials:** notes [[Notas/L03/L03-04-sequential-rationality-backward-induction|L03 sequential rationality and backward induction]] · quiz [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#bi|L3-2 bi]] · [[Map/topics-index#Topic: Backward induction and subgame perfection|T8]]
### §8.2 — Subgame-Perfect Nash Equilibrium: Concept (p. 153)
**Materials:** notes [[Notas/L03/L03-05-subgame-perfection|L03 subgame perfection]] · quiz [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#subg|L3-2 subg]], [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#spe|spe]] · case [[Cases/Brexit/brexit-game.pdf|Brexit]] section (vi) and "A Nash equilibrium that is not subgame perfect"
### §8.3 — Subgame-Perfect Nash Equilibrium: Examples (p. 159)
- 8.3.1 The Centipede Game (p. 159); 8.3.2 Stackelberg Competition (p. 160); 8.3.3 Mutually Assured Destruction (p. 163); 8.3.4 Time-Inconsistent Preferences (p. 166).
**Materials:** notes [[Notas/L03/L03-06-credibility-entry-commitment|L03 credibility, entry and commitment]], [[Notas/L03/L03-07-stackelberg|L03 Stackelberg]], [[Notas/L03/L03-08-time-inconsistency|L03 time inconsistency]] · quiz [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#cred|L3-3 cred]], [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#stack|stack]], [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#timeinc|timeinc]] · cases [[Cases/Brexit/brexit-game.pdf|Brexit]] ("The unobservable variant: commitment must be seen"), [[Resolucao/mini-case-lecture-03.pdf|mini case L3]] part (e) · [[Map/topics-index#Topic: Commitment and credibility (Stackelberg, entry, time inconsistency)|T9]]
### §8.4 — Summary (p. 169) · §8.5 — Exercises 8.1–8.16 (pp. 170–174)
**Materials:** items [[Listas/pratica-lecture-03#23. Tadelis 8.4|L3 #23 (8.4)]], [[Listas/pratica-lecture-03#12. Tadelis 8.5|L3 #12 (8.5)]], [[Listas/pratica-lecture-03#16. Tadelis 8.6|L3 #16 (8.6)]], [[Listas/pratica-lecture-03#21. Tadelis 8.7|L3 #21 (8.7)]], [[Listas/pratica-lecture-03#6. Tadelis 8.8|L3 #6 (8.8)]], [[Listas/pratica-lecture-03#13. Tadelis 8.10|L3 #13 (8.10)]], [[Listas/pratica-lecture-03#14. Tadelis 8.11|L3 #14 (8.11)]], [[Listas/pratica-lecture-03#22. Tadelis 8.12|L3 #22 (8.12)]], [[Listas/pratica-lecture-03#15. Tadelis 8.13|L3 #15 (8.13)]], [[Listas/pratica-lecture-03#18. Tadelis 8.15|L3 #18 (8.15)]], [[Listas/pratica-lecture-03#25. Tadelis 8.16|L3 #25 (8.16)]] · real #13 (8.8), #15 (8.10), #16 (8.13)

## Ch. 9 — Multistage Games (pp. 175–189) · Lecture 4
**Topics:** T10 Multistage games #topic/multistage
### §9.1 — Preliminaries (p. 176) · §9.2 — Payoffs (p. 177) · §9.3 — Strategies and Conditional Play (p. 178)
**Materials:** notes [[Notas/L04/L04-01-multistage-games|L04 multistage games]] · quiz [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#msg|L4-1 msg]] · [[Map/topics-index#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]]
### §9.4 — Subgame-Perfect Equilibria (p. 180)
**Materials:** notes [[Notas/L04/L04-02-carrot-and-stick|L04 carrot and stick]], [[Notas/L04/L04-04-two-stage-applications|L04 two-stage applications]] · quiz [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#cs|L4-1 cs]], [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#app|app]]
### §9.5 — The One-Stage Deviation Principle (p. 184)
**Materials:** notes [[Notas/L04/L04-03-one-stage-deviation|L04 one-stage deviation]] · quiz [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#osd|L4-1 osd]]
### §9.6 — Summary (p. 186) · §9.7 — Exercises 9.1–9.6 (pp. 186–189)
**Materials:** items [[Listas/pratica-lecture-04#1. Tadelis 9.1|L4 #1 (9.1)]], [[Listas/pratica-lecture-04#10. Tadelis 9.2|L4 #10 (9.2)]], [[Listas/pratica-lecture-04#2. Tadelis 9.3|L4 #2 (9.3)]], [[Listas/pratica-lecture-04#11. Tadelis 9.4|L4 #11 (9.4)]], [[Listas/pratica-lecture-04#19. Tadelis 9.5|L4 #19 (9.5)]], [[Listas/pratica-lecture-04#12. Tadelis 9.6|L4 #12 (9.6)]] · real #19 (9.1), #21 (9.4)

## Ch. 10 — Repeated Games (pp. 190–219) · Lectures 5–6
**Topics:** T12 Repeated games and the folk theorem #topic/repeated-games · T13 Collusion and price wars #topic/collusion · T14 Reputation and relational contracts #topic/reputation
### §10.1 — Finitely Repeated Games (p. 190)
**Materials:** notes [[Notas/L05/L05-01-finite-repetition-unraveling|L05 finite repetition]], [[Notas/L05/L05-02-two-stage-carrot-stick|L05 two-stage carrot and stick]] · quiz [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#unravel|L5-1 unravel]], [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#carrot|carrot]], [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#reneg|reneg]] · [[Map/topics-index#Topic: Repeated games and the folk theorem|T12]]
### §10.2 — Infinitely Repeated Games (p. 192)
- 10.2.1 Payoffs (p. 193); 10.2.2 Strategies (p. 195).
**Materials:** notes [[Notas/L05/L05-03-discounting-histories-strategies|L05 discounting, histories, strategies]] · quiz [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#disc|L5-2 disc]]
### §10.3 — Subgame-Perfect Equilibria (p. 196)
**Materials:** notes [[Notas/L05/L05-04-grim-trigger-spe|L05 grim trigger]], [[Notas/L05/L05-05-critical-discount-factor|L05 critical discount factor]], [[Notas/L06/L06-01-recap-grim-trigger|L06 recap]] · quiz [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#grim|L5-2 grim]], [[Simulados/quiz-lecture05-2-grim-trigger-2026-10-25#crit|crit]]
### §10.4 — Application: Tacit Collusion (p. 201)
**Materials:** notes [[Notas/L06/L06-02-cournot-collusion|L06 Cournot collusion]], [[Notas/L06/L06-04-punishments-price-wars|L06 punishments and price wars]] · quiz [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#template|L6-1 template]], [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#cournot|cournot]], [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#asym|asym]], [[Simulados/quiz-lecture06-1-cournot-collusion-2026-10-25#shrink|shrink]] · [[Map/topics-index#Topic: Collusion and price wars|T13]]
### §10.5 — Sequential Interaction and Reputation (p. 204)
- 10.5.1 Cooperation as Reputation (p. 204); 10.5.2 Third-Party Institutions as Reputation Mechanisms (p. 205); 10.5.3 Reputation Transfers without Third Parties (p. 207).
**Materials:** notes [[Notas/L06/L06-05-reputation-trust|L06 reputation and trust]], [[Notas/L06/L06-06-institutions-reputation|L06 institutions]] · quiz [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#trust|L6-3 trust]], [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#inst|inst]] · [[Map/topics-index#Topic: Reputation and relational contracts|T14]]
### §10.6 — The Folk Theorem: Almost Anything Goes (p. 209)
**Materials:** notes [[Notas/L05/L05-06-folk-theorem|L05 folk theorem]] · quiz [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#feas|L5-3 feas]], [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#folk|folk]], [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#alt|alt]], [[Simulados/quiz-lecture05-3-folk-theorem-2026-10-25#select|select]]
### §10.7 — Summary (p. 214) · §10.8 — Exercises 10.1–10.12 (pp. 215–219)
- Range corrected 2026-11-03 (was "10.1–10.9"): 10.10 Law Merchants Revisited, 10.11 Trading Brand Names and 10.12 Folk Theorem Revisited are on p. 219 (PDF viewer page 238).
**Materials:** items [[Listas/pratica-lecture-05#4. Tadelis 10.2|L5 #4 (10.2)]], [[Listas/pratica-lecture-05#9. Tadelis 10.3|L5 #9 (10.3)]], [[Listas/pratica-lecture-06#14. Tadelis 10.4|L6 #14 (10.4)]], [[Listas/pratica-lecture-05#12. Tadelis 10.5|L5 #12 (10.5)]], [[Listas/pratica-lecture-06#15. Tadelis 10.6|L6 #15 (10.6)]], [[Listas/pratica-lecture-05#14. Tadelis 10.7|L5 #14 (10.7)]], [[Listas/pratica-lecture-06#10. Tadelis 10.8|L6 #10 (10.8)]], [[Listas/pratica-lecture-05#5. Tadelis 10.9|L5 #5 (10.9)]], [[Listas/pratica-lecture-06#23. Tadelis 10.10|L6 #23 (10.10)]] · 10.12: optional extra of [[Listas/pratica-lecture-05|list L5]]

## Ch. 11 — Strategic Bargaining (pp. 220–237) · Lecture 4
**Topics:** T11 Strategic bargaining #topic/bargaining
### §11.1 — One Round of Bargaining: The Ultimatum Game (p. 222)
**Materials:** notes [[Notas/L04/L04-05-ultimatum-game|L04 ultimatum game]] · quiz [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#ult|L4-2 ult]] · rules [[rules/02_barganha|Topic 2]] · case [[Cases/Brexit/brexit-game.pdf|Brexit]] (the EU's offer, the UK's present/reject decisions) · [[Map/topics-index#Topic: Strategic bargaining|T11]]
### §11.2 — Finitely Many Rounds of Bargaining (p. 224)
**Materials:** notes [[Notas/L04/L04-06-finite-alternating-offers|L04 finite alternating offers]] · quiz [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#fin|L4-2 fin]], [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#lim|lim]]
### §11.3 — The Infinite-Horizon Game (p. 228)
**Materials:** notes [[Notas/L04/L04-07-rubinstein-infinite-horizon|L04 Rubinstein]] · quiz [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#rub|L4-3 rub]], [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#pat|pat]]
### §11.4 — Application: Legislative Bargaining (p. 229)
- 11.4.1 Closed-Rule Bargaining (p. 230); 11.4.2 Open-Rule Bargaining (p. 232).
**Materials:** notes [[Notas/L04/L04-08-legislative-bargaining|L04 legislative bargaining]] · quiz [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#leg|L4-3 leg]]
### §11.5 — Summary (p. 235) · §11.6 — Exercises 11.1–11.7 (pp. 236–237)
**Materials:** items [[Listas/pratica-lecture-04#6. Tadelis 11.1|L4 #6 (11.1)]], [[Listas/pratica-lecture-04#13. Tadelis 11.2|L4 #13 (11.2)]], [[Listas/pratica-lecture-04#14. Tadelis 11.3|L4 #14 (11.3)]], [[Listas/pratica-lecture-04#15. Tadelis 11.4|L4 #15 (11.4)]], [[Listas/pratica-lecture-04#16. Tadelis 11.5|L4 #16 (11.5)]], [[Listas/pratica-lecture-04#18. Tadelis 11.6|L4 #18 (11.6)]], [[Listas/pratica-lecture-04#25. Tadelis 11.7|L4 #25 (11.7)]] · real #22 (11.2), #23 (11.5)

## Part IV — Static Games of Incomplete Information

## Ch. 12 — Bayesian Games (pp. 241–269) · Lecture 7
**Topics:** T15 Bayesian games and BNE #topic/bayesian-games · T16 Adverse selection #topic/adverse-selection · T17 Auctions (§12.4 common values) #topic/auctions · T6 (§12.5 purification) #topic/mixed-strategies
### §12.1 — Strategic Representation of Bayesian Games (p. 246)
- 12.1.1 Players, Actions, Information, and Preferences (p. 246); 12.1.2 Deriving Posteriors from a Common Prior: A Player's Beliefs (p. 247); 12.1.3 Strategies and Bayesian Nash Equilibrium (p. 249).
**Materials:** notes [[Notas/L07/L07-01-bayesian-games-harsanyi|L07 Bayesian games]], [[Notas/L07/L07-02-bayesian-nash-equilibrium|L07 BNE]] · quiz [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#harsanyi|L7-1 harsanyi]], [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#bne|bne]] · [[Map/topics-index#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
### §12.2 — Examples (p. 252)
- 12.2.1 Teenagers and the Game of Chicken (p. 252); 12.2.2 Study Groups (p. 255).
**Materials:** notes [[Notas/L07/L07-04-threshold-strategies-purification|L07 thresholds and purification]] · quiz [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#threshold|L7-1 threshold]]
### §12.3 — Inefficient Trade and Adverse Selection (p. 258)
**Materials:** notes [[Notas/L07/L07-05-adverse-selection-lemons|L07 adverse selection and lemons]] · quiz [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#lemons|L7-2 lemons]], [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#insurance|insurance]] · rules [[rules/07_selecao_adversa|Topic 7]] · [[Map/topics-index#Topic: Adverse selection|T16]]
### §12.4 — Committee Voting (p. 261)
**Materials:** notes [[Notas/L07/L07-09-common-values-curses|L07 common values and curses]] · quiz [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#cv|L7-2 cv]]
### §12.5 — Mixed Strategies Revisited: Harsanyi's Interpretation (p. 264)
**Materials:** notes [[Notas/L07/L07-04-threshold-strategies-purification|L07 thresholds and purification]] · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]
### §12.6 — Summary (p. 266) · §12.7 — Exercises 12.1–12.10 (pp. 266–269)
- Range corrected 2026-11-03 (was "12.1–12.9"): 12.10 Purification is on p. 269 (PDF viewer page 288), after 12.9 Grab the Dollar.
**Materials:** items [[Listas/pratica-lecture-07#4. Tadelis 12.1|L7 #4 (12.1)]], [[Listas/pratica-lecture-07#9. Tadelis 12.2|L7 #9 (12.2)]], [[Listas/pratica-lecture-07#11. Tadelis 12.3|L7 #11 (12.3)]], [[Listas/pratica-lecture-07#13. Tadelis 12.5|L7 #13 (12.5)]], [[Listas/pratica-lecture-07#14. Tadelis 12.6|L7 #14 (12.6)]], [[Listas/pratica-lecture-07#21. Tadelis 12.7|L7 #21 (12.7)]], [[Listas/pratica-lecture-07#18. Tadelis 12.8|L7 #18 (12.8)]], [[Listas/pratica-lecture-07#12. Tadelis 12.9|L7 #12 (12.9)]] · 12.10: optional extra of [[Listas/pratica-lecture-07|list L7]]

## Ch. 13 — Auctions and Competitive Bidding (pp. 270–287) · Lecture 7
**Topics:** T17 Auctions #topic/auctions
### §13.1 — Independent Private Values (p. 272)
- 13.1.1 Second-Price Sealed-Bid Auctions (p. 272); 13.1.2 English Auctions (p. 275); 13.1.3 First-Price Sealed-Bid and Dutch Auctions (p. 276); 13.1.4 Revenue Equivalence (p. 279).
**Materials:** notes [[Notas/L07/L07-06-second-price-english|L07 second-price and English]], [[Notas/L07/L07-07-first-price-dutch|L07 first-price and Dutch]], [[Notas/L07/L07-08-revenue-equivalence|L07 revenue equivalence]] · quiz [[Simulados/quiz-lecture07-3-auctions-2026-10-25#spa|L7-3 spa]], [[Simulados/quiz-lecture07-3-auctions-2026-10-25#fpa|fpa]], [[Simulados/quiz-lecture07-3-auctions-2026-10-25#rev|rev]] · [[Map/topics-index#Topic: Auctions|T17]]
### §13.2 — Common Values and the Winner's Curse (p. 282)
**Materials:** notes [[Notas/L07/L07-09-common-values-curses|L07 common values and curses]] · quiz [[Simulados/quiz-lecture07-3-auctions-2026-10-25#wc|L7-3 wc]]
### §13.3 — Summary (p. 285) · §13.4 — Exercises 13.1–13.10 (pp. 285–287)
- Range corrected 2026-11-03 (was "13.1–13.9"): 13.10 Common Values Linear Bidding is on p. 287 (PDF viewer page 306).
**Materials:** items [[Listas/pratica-lecture-07#5. Tadelis 13.1|L7 #5 (13.1)]], [[Listas/pratica-lecture-07#8. Tadelis 13.2|L7 #8 (13.2)]], [[Listas/pratica-lecture-07#17. Tadelis 13.3|L7 #17 (13.3)]], [[Listas/pratica-lecture-07#23. Tadelis 13.5|L7 #23 (13.5)]], [[Listas/pratica-lecture-07#16. Tadelis 13.9|L7 #16 (13.9)]], [[Listas/pratica-lecture-07#24. Tadelis 13.10|L7 #24 (13.10)]]

## Ch. 14 — Mechanism Design (pp. 288–299) · out of scope unless a lecture brings it
### §14.1 — Setup: Mechanisms as Bayesian Games (p. 288)
- 14.1.1 The Players (p. 288); 14.1.2 The Mechanism Designer (p. 289); 14.1.3 The Mechanism Game (p. 290).
### §14.2 — The Revelation Principle (p. 292)
### §14.3 — Dominant Strategies and Vickrey-Clarke-Groves Mechanisms (p. 295)
- 14.3.1 Dominant Strategy Implementation (p. 295); 14.3.2 Vickrey-Clarke-Groves Mechanisms (p. 295).
### §14.4 — Summary (p. 299) · §14.5 — Exercise 14.1 (p. 299)

## Part V — Dynamic Games of Incomplete Information

## Ch. 15 — Sequential Rationality with Incomplete Information (pp. 303–317) · Lecture 8
**Topics:** T18 Perfect Bayesian equilibrium #topic/pbe
### §15.1 — The Problem with Subgame Perfection (p. 303)
**Materials:** notes [[Notas/L08/L08-01-subgame-perfection-fails|L08 subgame perfection fails]] · quiz [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#sp|L8-1 sp]] · [[Map/topics-index#Topic: Perfect Bayesian equilibrium|T18]]
### §15.2 — Perfect Bayesian Equilibrium (p. 307)
**Materials:** notes [[Notas/L08/L08-02-beliefs-and-pbe|L08 beliefs and PBE]] · quiz [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#beliefs|L8-1 beliefs]], [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#pbe|pbe]]
### §15.3 — Sequential Equilibrium (p. 312)
**Materials:** notes [[Notas/L08/L08-03-sequential-equilibrium|L08 sequential equilibrium]] · quiz [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#se|L8-1 se]]
### §15.4 — Summary (p. 314) · §15.5 — Exercises 15.1–15.6 (pp. 314–317)
**Materials:** items [[Listas/pratica-lecture-08#1. Tadelis 15.1|L8 #1 (15.1)]], [[Listas/pratica-lecture-08#3. Tadelis 15.3|L8 #3 (15.3)]], [[Listas/pratica-lecture-08#10. Tadelis 15.5|L8 #10 (15.5)]], [[Listas/pratica-lecture-08#18. Tadelis 15.6|L8 #18 (15.6)]]

## Ch. 16 — Signaling Games (pp. 318–338) · Lecture 8
**Topics:** T19 Signaling and refinements #topic/signaling · T9 (limit pricing as entry deterrence) #topic/commitment
### §16.1 — Education Signaling: The MBA Game (p. 319)
**Materials:** notes [[Notas/L08/L08-04-signaling-games|L08 signaling games]], [[Notas/L08/L08-05-mba-game|L08 MBA game]] · quiz [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#sig|L8-2 sig]], [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#mba|mba]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]
### §16.2 — Limit Pricing and Entry Deterrence (p. 323)
- 16.2.1 Separating Equilibria (p. 324); 16.2.2 Pooling Equilibria (p. 330).
**Materials:** notes [[Notas/L08/L08-07-limit-pricing|L08 limit pricing]] · quiz [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#lp|L8-3 lp]]
### §16.3 — Refinements of Perfect Bayesian Equilibrium in Signaling Games (p. 332)
**Materials:** notes [[Notas/L08/L08-08-intuitive-criterion|L08 intuitive criterion]] · quiz [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ic|L8-3 ic]], [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ref|ref]]
### §16.4 — Summary (p. 335) · §16.5 — Exercises 16.1–16.8 (pp. 335–338)
**Materials:** items [[Listas/pratica-lecture-08#13. Tadelis 16.3|L8 #13 (16.3)]], [[Listas/pratica-lecture-08#12. Tadelis 16.4|L8 #12 (16.4)]], [[Listas/pratica-lecture-08#7. Tadelis 16.5|L8 #7 (16.5)]], [[Listas/pratica-lecture-08#15. Tadelis 16.6|L8 #15 (16.6)]], [[Listas/pratica-lecture-08#19. Tadelis 16.7|L8 #19 (16.7)]], [[Listas/pratica-lecture-08#16. Tadelis 16.8|L8 #16 (16.8)]]

## Ch. 17 — Building a Reputation (pp. 339–356) · background for Lectures 6 and 8
### §17.1 — Cooperation in a Finitely Repeated Prisoner's Dilemma (p. 339)
### §17.2 — Driving a Tough Bargain (p. 342)
### §17.3 — A Reputation for Being "Nice" (p. 349)
### §17.4 — Summary (p. 354) · §17.5 — Exercises 17.1–17.3 (pp. 354–356)

## Ch. 18 — Information Transmission and Cheap Talk (pp. 357–368)
### §18.1 — Information Transmission: A Finite Example (p. 358)
### §18.2 — Information Transmission: The Continuous Case (p. 361)
### §18.3 — Application: Information and Legislative Organization (p. 365)
### §18.4 — Summary (p. 367) · §18.5 — Exercises 18.1–18.4 (pp. 367–368)

## Ch. 19 — Mathematical Appendix (pp. 369–384)
### §19.1 — Sets and Sequences (p. 369) · §19.2 — Functions (p. 371) · §19.3 — Calculus and Optimization (p. 373) · §19.4 — Probability and Random Variables (p. 378)
- 19.4.3 Independence, Conditional Probability, and Bayes' Rule (p. 380); 19.4.4 Expected Values (p. 382).

References (p. 385) · Index (p. 389).

---

# Gibbons, *Game Theory for Applied Economists* (1992)

#book/gibbons

Added 2026-10-13. OCR scan; the PDF offset changes by chapter (registry entries `Gibbons Ch. 1`,
`Gibbons Ch. 2`, `Gibbons Ch. 3-4`). Sections and pages from the TOC (PDF 1–3), each found in the
body at the stated page. Problems at the end of each chapter, grouped by section. Answers: only the
external, unofficial and unfinished manual described in `Livros/BOOKS.md` (Problems 1.1–1.14,
2.1–2.23, 3.1–3.8, 4.1–4.6).

## Ch. 1 — Static Games of Complete Information (pp. 1–53) · Lectures 1–2
**Topics:** T1 Normal-form games #topic/normal-form · T2 Dominance and IESDS #topic/dominance-iesds · T4 Nash equilibrium #topic/nash-equilibrium · T5 Oligopoly #topic/oligopoly · T6 Mixed strategies #topic/mixed-strategies
### §1.1 — Basic Theory: Normal-Form Games and Nash Equilibrium (p. 2)
- 1.1.A Normal-Form Representation of Games (p. 2; Prisoners' Dilemma with Mum/Fink, payoffs −1, −9, 0, −6, p. 3).
- 1.1.B Iterated Elimination of Strictly Dominated Strategies (p. 4; Figures 1.1.1–1.1.3, pp. 6–7; common knowledge of rationality and the two drawbacks, p. 7).
- 1.1.C Motivation and Definition of Nash Equilibrium (p. 8).
**Materials:** notes [[Notas/L01/L01-01-games-normal-form|L01 normal form]], [[Notas/L01/L01-06-iesds|L01 IESDS]], [[Notas/L02/L02-02-nash-equilibrium|L02 Nash equilibrium]] · quiz [[Simulados/quiz-lecture01-3-iesds-2026-10-13#ck|L1-3 ck]], [[Simulados/quiz-lecture02-1-nash-equilibrium-2026-10-25#ne|L2-1 ne]] · [[Map/topics-index#Topic: Dominance and IESDS|T2]], [[Map/topics-index#Topic: Nash equilibrium|T4]]
### §1.2 — Applications (p. 14)
- 1.2.A Cournot Model of Duopoly (p. 14); 1.2.B Bertrand Model of Duopoly (p. 21); 1.2.C Final-Offer Arbitration (p. 22); 1.2.D The Problem of the Commons (p. 27).
**Materials:** notes [[Notas/L02/L02-03-cournot|L02 Cournot]], [[Notas/L02/L02-04-bertrand|L02 Bertrand]], [[Notas/L02/L02-05-commons|L02 commons]] · quiz [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#cournot|L2-2 cournot]], [[Simulados/quiz-lecture02-2-cournot-bertrand-2026-10-25#bertrand|bertrand]] · [[Map/topics-index#Topic: Oligopoly and continuous games (Cournot, Bertrand, commons, Hotelling)|T5]]
### §1.3 — Advanced Theory: Mixed Strategies and Existence of Equilibrium (p. 29)
- 1.3.A Mixed Strategies (p. 29); 1.3.B Existence of Nash Equilibrium (p. 33).
**Materials:** notes [[Notas/L02/L02-07-mixed-strategies|L02 mixed strategies]], [[Notas/L02/L02-09-existence|L02 existence]] · quiz [[Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25#exist|L2-3 exist]] · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]
### §1.4 — Further Reading (p. 48) · §1.5 — Problems 1.1–1.14 (pp. 48–51; Section 1.1: 1.1–1.3; 1.8 is the Hotelling voting problem, p. 50) · §1.6 — References (p. 51)
**Materials:** items [[Listas/pratica-lecture-01#7. Gibbons 1.2|L1 #7 (1.2)]], [[Listas/pratica-lecture-02#4. Gibbons 1.3|L2 #4 (1.3)]], [[Listas/pratica-lecture-02#13. Gibbons 1.5|L2 #13 (1.5)]], [[Listas/pratica-lecture-02#14. Gibbons 1.6|L2 #14 (1.6)]], [[Listas/pratica-lecture-02#15. Gibbons 1.7|L2 #15 (1.7)]], [[Listas/pratica-lecture-02#8. Gibbons 1.12|L2 #8 (1.12)]], [[Listas/pratica-lecture-02#20. Gibbons 1.14|L2 #20 (1.14)]] · real #2 (1.2), #11 (1.6)

## Ch. 2 — Dynamic Games of Complete Information (pp. 55–141) · Lectures 3–6
**Topics:** T7 Extensive form #topic/extensive-form · T8 Subgame perfection #topic/spe · T9 Commitment #topic/commitment · T10 Multistage games #topic/multistage · T11 Bargaining #topic/bargaining · T12 Repeated games #topic/repeated-games · T13 Collusion #topic/collusion · T14 Reputation and relational contracts #topic/reputation
### §2.1 — Dynamic Games of Complete and Perfect Information (p. 57)
- 2.1.A Theory: Backwards Induction (p. 57); 2.1.B Stackelberg Model of Duopoly (p. 61); 2.1.C Wages and Employment in a Unionized Firm (p. 64); 2.1.D Sequential Bargaining (p. 68).
**Materials:** notes [[Notas/L03/L03-04-sequential-rationality-backward-induction|L03 backward induction]], [[Notas/L03/L03-07-stackelberg|L03 Stackelberg]], [[Notas/L04/L04-06-finite-alternating-offers|L04 finite alternating offers]] · quiz [[Simulados/quiz-lecture03-3-commitment-stackelberg-2026-10-25#stack|L3-3 stack]], [[Simulados/quiz-lecture04-2-ultimatum-finite-offers-2026-10-25#fin|L4-2 fin]] · [[Map/topics-index#Topic: Backward induction and subgame perfection|T8]], [[Map/topics-index#Topic: Strategic bargaining|T11]]
### §2.2 — Two-Stage Games of Complete but Imperfect Information (p. 71)
- 2.2.A Theory: Subgame Perfection (p. 71); 2.2.B Bank Runs (p. 73); 2.2.C Tariffs and Imperfect International Competition (p. 75); 2.2.D Tournaments (p. 79).
**Materials:** notes [[Notas/L04/L04-04-two-stage-applications|L04 two-stage applications]] · quiz [[Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25#app|L4-1 app]] · [[Map/topics-index#Topic: Multistage games (carrot and stick, one-stage deviation)|T10]]
### §2.3 — Repeated Games (p. 82)
- 2.3.A Theory: Two-Stage Repeated Games (p. 82); 2.3.B Theory: Infinitely Repeated Games (p. 88); 2.3.C Collusion between Cournot Duopolists (p. 102); 2.3.D Efficiency Wages (p. 107); 2.3.E Time-Consistent Monetary Policy (p. 112).
**Materials:** notes [[Notas/L05/L05-02-two-stage-carrot-stick|L05 two-stage carrot and stick]], [[Notas/L05/L05-04-grim-trigger-spe|L05 grim trigger]], [[Notas/L06/L06-02-cournot-collusion|L06 Cournot collusion]], [[Notas/L06/L06-04-punishments-price-wars|L06 price wars]], [[Notas/L06/L06-07-efficiency-wages|L06 efficiency wages]] · quiz [[Simulados/quiz-lecture05-1-finite-horizon-2026-10-25#carrot|L5-1 carrot]], [[Simulados/quiz-lecture06-2-bertrand-price-wars-2026-10-25#wars|L6-2 wars]], [[Simulados/quiz-lecture06-3-reputation-wages-2026-10-25#wages|L6-3 wages]] · [[Map/topics-index#Topic: Repeated games and the folk theorem|T12]], [[Map/topics-index#Topic: Collusion and price wars|T13]], [[Map/topics-index#Topic: Reputation and relational contracts|T14]]
### §2.4 — Dynamic Games of Complete but Imperfect Information (p. 115)
- 2.4.A Extensive-Form Representation of Games (p. 115); 2.4.B Subgame-Perfect Nash Equilibrium (p. 122).
**Materials:** notes [[Notas/L03/L03-01-extensive-form|L03 extensive form]], [[Notas/L03/L03-05-subgame-perfection|L03 subgame perfection]] · quiz [[Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25#subg|L3-2 subg]] · [[Map/topics-index#Topic: Extensive form, strategies and information|T7]]
### §2.5 — Further Reading (p. 129) · §2.6 — Problems 2.1–2.23 (pp. 130–138) · §2.7 — References (p. 138)
**Materials:** items [[Listas/pratica-lecture-03#24. Gibbons 2.1|L3 #24 (2.1)]], [[Listas/pratica-lecture-04#4. Gibbons 2.6|L4 #4 (2.6)]], [[Listas/pratica-lecture-04#20. Gibbons 2.8|L4 #20 (2.8)]], [[Listas/pratica-lecture-05#7. Gibbons 2.10|L5 #7 (2.10)]], [[Listas/pratica-lecture-05#8. Gibbons 2.11|L5 #8 (2.11)]], [[Listas/pratica-lecture-05#1. Gibbons 2.12|L5 #1 (2.12)]], [[Listas/pratica-lecture-06#4. Gibbons 2.13|L6 #4 (2.13)]], [[Listas/pratica-lecture-06#21. Gibbons 2.14|L6 #21 (2.14)]], [[Listas/pratica-lecture-06#13. Gibbons 2.15|L6 #13 (2.15)]], [[Listas/pratica-lecture-05#15. Gibbons 2.16|L5 #15 (2.16)]], [[Listas/pratica-lecture-06#24. Gibbons 2.17|L6 #24 (2.17)]], [[Listas/pratica-lecture-04#17. Gibbons 2.19|L4 #17 (2.19)]], [[Listas/pratica-lecture-04#21. Gibbons 2.20|L4 #21 (2.20)]], [[Listas/pratica-lecture-04#3. Gibbons 2.22|L4 #3 (2.22)]] · real #18 (2.1), #20 (2.6)

## Ch. 3 — Static Games of Incomplete Information (pp. 143–172) · Lecture 7
**Topics:** T15 Bayesian games #topic/bayesian-games · T16 Adverse selection #topic/adverse-selection · T17 Auctions #topic/auctions
### §3.1 — Theory: Static Bayesian Games and Bayesian Nash Equilibrium (p. 144)
- 3.1.A An Example: Cournot Competition under Asymmetric Information (p. 144); 3.1.B Normal-Form Representation of Static Bayesian Games (p. 146); 3.1.C Definition of Bayesian Nash Equilibrium (p. 149).
**Materials:** notes [[Notas/L07/L07-01-bayesian-games-harsanyi|L07 Bayesian games]], [[Notas/L07/L07-03-cournot-private-costs|L07 Cournot with private costs]] · quiz [[Simulados/quiz-lecture07-1-bayesian-nash-2026-10-25#cournot|L7-1 cournot]] · [[Map/topics-index#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
### §3.2 — Applications (p. 152)
- 3.2.A Mixed Strategies Revisited (p. 152); 3.2.B An Auction (p. 155); 3.2.C A Double Auction (p. 158).
**Materials:** notes [[Notas/L07/L07-04-threshold-strategies-purification|L07 purification]], [[Notas/L07/L07-07-first-price-dutch|L07 first-price]], [[Notas/L07/L07-05-adverse-selection-lemons|L07 adverse selection]] · quiz [[Simulados/quiz-lecture07-2-adverse-selection-2026-10-25#double|L7-2 double]] · [[Map/topics-index#Topic: Auctions|T17]], [[Map/topics-index#Topic: Adverse selection|T16]]
### §3.3 — The Revelation Principle (p. 164)
- Mechanism design: out of scope unless a lecture brings it.
### §3.4 — Further Reading (p. 168) · §3.5 — Problems 3.1–3.8 (pp. 169–171) · §3.6 — References (p. 172)
**Materials:** items [[Listas/pratica-lecture-07#1. Gibbons 3.1|L7 #1 (3.1)]], [[Listas/pratica-lecture-07#10. Gibbons 3.3|L7 #10 (3.3)]], [[Listas/pratica-lecture-07#3. Gibbons 3.4|L7 #3 (3.4)]], [[Listas/pratica-lecture-07#15. Gibbons 3.6|L7 #15 (3.6)]], [[Listas/pratica-lecture-07#22. Gibbons 3.8|L7 #22 (3.8)]]

## Ch. 4 — Dynamic Games of Incomplete Information (pp. 173–255) · Lecture 8
**Topics:** T18 PBE #topic/pbe · T19 Signaling and refinements #topic/signaling · T11/T14 (§4.3.B–C) #topic/bargaining #topic/reputation
### §4.1 — Introduction to Perfect Bayesian Equilibrium (p. 175)
**Materials:** notes [[Notas/L08/L08-02-beliefs-and-pbe|L08 beliefs and PBE]] · quiz [[Simulados/quiz-lecture08-1-pbe-beliefs-2026-10-25#pbe|L8-1 pbe]] · [[Map/topics-index#Topic: Perfect Bayesian equilibrium|T18]]
### §4.2 — Signaling Games (p. 183)
- 4.2.A Perfect Bayesian Equilibrium in Signaling Games (p. 183); 4.2.B Job-Market Signaling (p. 190); 4.2.C Corporate Investment and Capital Structure (p. 205); 4.2.D Monetary Policy (p. 208).
**Materials:** notes [[Notas/L08/L08-04-signaling-games|L08 signaling games]], [[Notas/L08/L08-06-spence-job-market|L08 Spence]] · quiz [[Simulados/quiz-lecture08-2-signaling-mba-spence-2026-10-25#spence|L8-2 spence]] · audio [[NotebookLM/audio/lecture-08-audio-part2|L8 part 2]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]
### §4.3 — Other Applications of Perfect Bayesian Equilibrium (p. 210)
- 4.3.A Cheap-Talk Games (p. 210); 4.3.B Sequential Bargaining under Asymmetric Information (p. 218); 4.3.C Reputation in the Finitely Repeated Prisoners' Dilemma (p. 224).
**Materials:** notes [[Notas/L04/L04-09-bargaining-private-information|L04 bargaining with private information]] (4.3.B) · quiz [[Simulados/quiz-lecture04-3-rubinstein-legislative-2026-10-25#inf|L4-3 inf]] · cheap talk (4.3.A) out of scope
### §4.4 — Refinements of Perfect Bayesian Equilibrium (p. 233)
**Materials:** notes [[Notas/L08/L08-08-intuitive-criterion|L08 intuitive criterion]] · quiz [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ic|L8-3 ic]], [[Simulados/quiz-lecture08-3-limit-pricing-intuitive-2026-10-25#ref|ref]]
### §4.5 — Further Reading (p. 244) · §4.6 — Problems 4.1–4.16 (pp. 245–253) · §4.7 — References (p. 253)
**Materials:** items [[Listas/pratica-lecture-08#2. Gibbons 4.1|L8 #2 (4.1)]], [[Listas/pratica-lecture-08#9. Gibbons 4.2|L8 #9 (4.2)]], [[Listas/pratica-lecture-08#5. Gibbons 4.3|L8 #5 (4.3)]], [[Listas/pratica-lecture-08#6. Gibbons 4.4|L8 #6 (4.4)]], [[Listas/pratica-lecture-08#20. Gibbons 4.7|L8 #20 (4.7)]], [[Listas/pratica-lecture-08#17. Gibbons 4.16|L8 #17 (4.16)]]

Index (p. 257).

---

# Muñoz-Garcia & Toro-Gonzalez, *Strategy and Game Theory: Practice Exercises with Answers*, 2nd ed. (2019)

#book/munoz-garcia

Added 2026-10-13. Exercise book: each chapter opens with a short introduction, then numbered
exercises, each followed by a worked **Answer**. The superscript letter after each title grades
difficulty (A easy, B intermediate, C hard). Chapter pages and exercise ranges from the TOC (PDF
8–12) and checked against the exercise headings in the body: 134 numbered exercises in all (the
preface says 153). The PDF offset changes by chapter (registry entries `Munoz-Garcia Ch. …`).

## Ch. 1 — Dominance Solvable Games (pp. 1–36) · Lecture 1 · Exercises 1–17
**Topics:** T1 Normal-form games #topic/normal-form · T2 Dominance and IESDS #topic/dominance-iesds
- From extensive to normal form (Ex. 1–4, pp. 2–8); Prisoners' Dilemma (Ex. 5, p. 8); IDSDS (Ex. 6–13, pp. 11–26); applications and continuous strategies (Ex. 14–15, pp. 28–29); IDSDS vs. IDWDS (Ex. 16–17, pp. 31–33).
**Materials:** items [[Listas/pratica-lecture-01#3. Muñoz-Garcia Ex. 2|L1 #3 (Ex. 2)]], [[Listas/pratica-lecture-01#4. Muñoz-Garcia Ex. 5|L1 #4 (Ex. 5)]], [[Listas/pratica-lecture-01#8. Muñoz-Garcia Ex. 9|L1 #8 (Ex. 9)]], [[Listas/pratica-lecture-01#14. Muñoz-Garcia Ex. 12|L1 #14 (Ex. 12)]], [[Listas/pratica-lecture-01#5. Muñoz-Garcia Ex. 13|L1 #5 (Ex. 13)]], [[Listas/pratica-lecture-01#19. Muñoz-Garcia Ex. 16|L1 #19 (Ex. 16)]] · real #5 (Ex. 12) · [[Map/topics-index#Topic: Dominance and IESDS|T2]]
## Ch. 2 — Pure Strategy Nash Equilibrium and Simultaneous-Move Games with Complete Information (pp. 37–84) · Lecture 2 · Exercises 1–17
**Topics:** T4 Nash equilibrium #topic/nash-equilibrium · T5 Oligopoly #topic/oligopoly
- Includes Ex. 12 Political Competition (Hotelling model) (p. 64).
**Materials:** items [[Listas/pratica-lecture-02#1. Muñoz-Garcia Ex. 2 (Ch. 2)|L2 #1 (Ex. 2)]], [[Listas/pratica-lecture-02#5. Muñoz-Garcia Ex. 7 (Ch. 2)|L2 #5 (Ex. 7)]] · [[Map/topics-index#Topic: Nash equilibrium|T4]]
## Ch. 3 — Mixed Strategies, Strictly Competitive Games, and Correlated Equilibria (pp. 85–151) · Lecture 2 · Exercises 1–18
**Topics:** T6 Mixed strategies #topic/mixed-strategies
**Materials:** item [[Listas/pratica-lecture-02#6. Muñoz-Garcia Ex. 1 (Ch. 3)|L2 #6 (Ex. 1)]] · real #8 (Ex. 1) · [[Map/topics-index#Topic: Mixed strategies and existence|T6]]
## Ch. 4 — Sequential-Move Games with Complete Information (pp. 153–214) · Lectures 3–4 · Exercises 1–21
**Topics:** T8 Subgame perfection #topic/spe · T9 Commitment #topic/commitment · T10 Multistage games #topic/multistage · T11 Bargaining #topic/bargaining
- Bargaining: Ex. 1 ultimatum (p. 154), Ex. 16–17 alternating offers (pp. 198–199).
**Materials:** items [[Listas/pratica-lecture-03#3. Muñoz-Garcia Ex. 3|L3 #3 (Ex. 3)]], [[Listas/pratica-lecture-03#4. Muñoz-Garcia Ex. 4|L3 #4 (Ex. 4)]], [[Listas/pratica-lecture-03#7. Muñoz-Garcia Ex. 9|L3 #7 (Ex. 9)]], [[Listas/pratica-lecture-03#8. Muñoz-Garcia Ex. 11|L3 #8 (Ex. 11)]], [[Listas/pratica-lecture-03#17. Muñoz-Garcia Ex. 12|L3 #17 (Ex. 12)]], [[Listas/pratica-lecture-04#7. Muñoz-Garcia Ex. 1|L4 #7 (Ex. 1)]], [[Listas/pratica-lecture-04#8. Muñoz-Garcia Ex. 16|L4 #8 (Ex. 16)]], [[Listas/pratica-lecture-04#9. Muñoz-Garcia Ex. 17|L4 #9 (Ex. 17)]], [[Listas/pratica-lecture-04#5. Muñoz-Garcia Ex. 18|L4 #5 (Ex. 18)]] · real #14 (Ex. 3), #17 (Ex. 12) · [[Map/topics-index#Topic: Backward induction and subgame perfection|T8]], [[Map/topics-index#Topic: Strategic bargaining|T11]]
## Ch. 5 — Applications to Industrial Organization (pp. 215–271) · Lectures 2–3, 6 · Exercises 1–16
**Topics:** T5 Oligopoly #topic/oligopoly · T13 Collusion #topic/collusion
- One-shot cartels: Ex. 4–5 (pp. 228–231), Ex. 8 (p. 239).
**Materials:** items [[Listas/pratica-lecture-06#1. Muñoz-Garcia Ch. 5 Ex. 4|L6 #1 (Ex. 4)]], [[Listas/pratica-lecture-06#2. Muñoz-Garcia Ch. 5 Ex. 5|L6 #2 (Ex. 5)]], [[Listas/pratica-lecture-06#9. Muñoz-Garcia Ch. 5 Ex. 8|L6 #9 (Ex. 8)]] · [[Map/topics-index#Topic: Collusion and price wars|T13]]
## Ch. 6 — Repeated Games and Correlated Equilibria (pp. 273–316) · Lectures 5–6 · Exercises 1–10
**Topics:** T12 Repeated games #topic/repeated-games · T13 Collusion #topic/collusion · T11 (Ex. 8, three-player bargaining; Lecture 4) #topic/bargaining
- Infinitely repeated PD (Ex. 1, p. 274); collusion (Ex. 2–5, pp. 278–290); imperfect monitoring (Ex. 10, p. 310).
**Materials:** items [[Listas/pratica-lecture-05#6. Muñoz-Garcia Ex. 1|L5 #6 (Ex. 1)]], [[Listas/pratica-lecture-05#11. Muñoz-Garcia Ex. 6|L5 #11 (Ex. 6)]], [[Listas/pratica-lecture-05#13. Muñoz-Garcia Ex. 9|L5 #13 (Ex. 9)]], [[Listas/pratica-lecture-06#3. Muñoz-Garcia Ch. 6 Ex. 2|L6 #3 (Ex. 2)]], [[Listas/pratica-lecture-06#11. Muñoz-Garcia Ch. 6 Ex. 3|L6 #11 (Ex. 3)]], [[Listas/pratica-lecture-06#12. Muñoz-Garcia Ch. 6 Ex. 4|L6 #12 (Ex. 4)]], [[Listas/pratica-lecture-06#18. Muñoz-Garcia Ch. 6 Ex. 5|L6 #18 (Ex. 5)]], [[Listas/pratica-lecture-06#20. Muñoz-Garcia Ch. 6 Ex. 10|L6 #20 (Ex. 10)]], [[Listas/pratica-lecture-04#24. Muñoz-Garcia Ch. 6 Ex. 8|L4 #24 (Ex. 8)]] · real #24 (Ex. 8) · [[Map/topics-index#Topic: Repeated games and the folk theorem|T12]]
## Ch. 7 — Simultaneous-Move Games with Incomplete Information (pp. 317–347) · Lecture 7 · Exercises 1–7
**Topics:** T15 Bayesian games #topic/bayesian-games
**Materials:** item [[Listas/pratica-lecture-07#2. Muñoz-Garcia Ch. 7 Ex. 1|L7 #2 (Ex. 1)]] · [[Map/topics-index#Topic: Bayesian games and Bayesian Nash equilibrium|T15]]
## Ch. 8 — Auctions (pp. 349–373) · Lecture 7 · Exercises 1–8
**Topics:** T17 Auctions #topic/auctions
**Materials:** items [[Listas/pratica-lecture-07#7. Muñoz-Garcia Ch. 8 Ex. 1|L7 #7 (Ex. 1)]], [[Listas/pratica-lecture-07#6. Muñoz-Garcia Ch. 8 Ex. 4|L7 #6 (Ex. 4)]] · [[Map/topics-index#Topic: Auctions|T17]]
## Ch. 9 — Perfect Bayesian Equilibrium and Signaling Games (pp. 375–451) · Lecture 8 · Exercises 1–9
**Topics:** T18 PBE #topic/pbe · T19 Signaling #topic/signaling
**Materials:** items [[Listas/pratica-lecture-08#4. Muñoz-Garcia Ch. 9 Ex. 1|L8 #4 (Ex. 1)]], [[Listas/pratica-lecture-08#8. Muñoz-Garcia Ch. 9 Ex. 2|L8 #8 (Ex. 2)]], [[Listas/pratica-lecture-08#11. Muñoz-Garcia Ch. 9 Ex. 5|L8 #11 (Ex. 5)]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]
## Ch. 10 — Cheap Talk Games (pp. 453–479) · Exercises 1–5
- Cheap talk: out of scope (no topic tag).
## Ch. 11 — More Advanced Signaling Games (pp. 481–520) · Lecture 8 · Exercises 1–6
**Topics:** T19 Signaling and refinements #topic/signaling · T9 (entry deterrence) #topic/commitment
**Materials:** items [[Listas/pratica-lecture-08#21. Muñoz-Garcia Ch. 11 Ex. 4|L8 #21 (Ex. 4)]], [[Listas/pratica-lecture-08#14. Muñoz-Garcia Ch. 11 Ex. 5|L8 #14 (Ex. 5)]] · [[Map/topics-index#Topic: Signaling and refinements|T19]]

Index (p. 521).
