# Short paper — analysis of the three papers in `Artigos/` (2026-11-22)

Assessed against `Aula/Short_paper_guia_rubrica.pptx`. Deadline 24/11, Lecture 8: 3 papers plus
the model idea, 5 min, 3–4 slides, formative feedback. For each paper the group must show its
question, how it relates to the course, its mechanism, its result, and how it feeds the model. The
paper is **theoretical**: empirical work enters only through the literature review and the
motivation. The model, its equilibrium and its comparative statics must be the group's own work.

Common thread: **cartels in Brazil and CADE's enforcement mix** (leniency, multi-sphere
sanctions, private damages under Law 14.470/22).

| | Paper | Type | Role in the short paper |
|---|---|---|---|
| 1 | Sabino, Lara & Sarto (2024), "Game Theory Applied to the Brazilian Antitrust Leniency Program", *RDP* 21(111), 330–357, doi 10.11117/rdp.v21i111.7589 | Theory (toy model, law journal) | Direct theoretical precedent, and the gap |
| 2 | Fraga, Zenkner & Micheli (2023), "Responsabilização 360°…", *Revista de Defesa da Concorrência* 11(1), 169–185, doi 10.52896/rdc.v11i1.1035 | Legal, descriptive empirics | Institutions and parameters (sanction spheres, Law 14.470/22) |
| 3 | Oliveira & Lima, CADE/DEE *Documento de Trabalho 003*, "Estimativa de Sobrepreço em Cartéis: Evidências do Cartel do Cimento no Brasil" (2025; references accessed Mar 2025) | Empirical (DiD) | Motivation and evidence |

## 1. Sabino, Lara & Sarto (2024): leniency as a sequential game

- **Question.** Do the benefits of CADE's leniency program (Law 12.529/11, arts. 86–87) make a
  cartel member want to self-report, and would immunity from civil damages change that?
- **Course link.** Lectures 3–4: a perfect-information sequential game, Nash equilibrium versus
  SPE, backward induction, Nature replaced by expected payoffs (as in the Brexit game).
- **Model.** Two players. The Applicant chooses Propose or Not propose, then CADE chooses Accept
  or Reject. Detection probability $p=0.5$ (stated as an assumption with no empirical basis).
  Revenue 100; $L=20$ (cartel profit), $M=20$ (fine), $A=5$ (administrative sanction), $C=1$
  (litigation), $I=0.1M$, $M_i=4L$ (fines on 4 other members), $RC=L$ (damages, doubled to $2RC$
  without an agreement, per art. 47 §1).
  - Not propose (or rejected): Applicant gets $p(L-A-M-2RC-C)+(1-p)L=-13$; CADE gets $41.5$.
  - Propose and accepted: Applicant gets $-RC=-20$ (Game 1) or $0$ (Game 2, damages immunity);
    CADE gets $80$.
- **Result.** Game 1: SPE (Not propose, Accept), so current law does not induce leniency. Game 2:
  NE (Propose, Accept) and (Not propose, Reject); the SPE is (Propose, Accept). Conclusion: grant
  immunity from civil damages.
- **Problems (recomputed 2026-11-22):**
  1. **The headline result depends on an accounting inconsistency.** The cartel profit $L$ is
     kept in both no-leniency branches but dropped from the leniency branch ($X=-RC$ instead of
     $L-RC$). The applicant proposes iff the leniency payoff is at least $20-66p$:

     | Leniency payoff | Propose iff | At $p=0.5$ |
     |---|---|---|
     | Paper, G1: $-20$ | $p\ge 0.606$ | No |
     | Paper, G2: $0$ | $p\ge 0.303$ | Yes |
     | Consistent, G1: $L-RC=0$ | $p\ge 0.303$ | **Yes, so the result flips** |
     | Consistent, G2: $L=20$ | always (weakly) | Yes |

  2. $A$ is defined as "a quarter of the gross revenue" (which would be 25) but set to 5.
     Elsewhere the paper writes "RC = M" where it means RC = L, and "40.5" where it means 41.5.
  3. **There is no strategic interaction among cartel members**, which is the core of leniency
     (the race to report, Motta–Polo 2003, Spagnolo, Harrington 2008). The other 4 members do
     not play, $p$ is exogenous, and the cartel-formation (deterrence) stage is not modeled,
     although the conclusion is about deterrence.
  4. CADE's move is trivial (Accept dominates), and its payoff is "fines collected", not welfare.
  5. There are no comparative statics: everything is solved at $p=0.5$, although the threshold in
     $p$ is the interesting object.
- **Use for the group.** It is the closest precedent, and its weaknesses *are* the gap. Its
  references hold the economics core: Buccirossi, Marvão & Spagnolo (2020, *JLS*), Pinha & Braga
  (2021, *JCLE*, Brazil-specific), Silbye (2012), Bodnar et al. (2023), Leslie (2006). Check each
  one by DOI before citing it, as the guide requires.

## 2. Fraga, Zenkner & Micheli (2023): "Responsabilização 360°"

- **Question.** Does CADE actively push for cartel liability beyond antitrust (criminal, other
  administrative, civil)?
- **Method and result.** A count of CADE Tribunal decisions, Jan 2018–Apr 2023. Of 40 bid-rigging
  cases, 24 (60%) referred the decision to other bodies (prosecutors, audit courts, Federal
  Police, victims). Of 26 public-procurement cases, 20 ended in conviction, and 80% of those
  carried a "360°" referral; they add up to R$ 2.3 bn in fines (R$ 2.52 bn across all 40).
  Descriptive only: no causal claim, no deterrence measure.
- **Course link (indirect).** In the model it raises the **expected punishment** and adds
  **debarment** (a 5-year ban on public tenders, art. 38 II), which removes future collusive rents.
  Both tighten the collusion incentive constraint of a repeated game (Lecture 5, grim trigger) and
  change the payoff of reporting.
- **Most useful content: the parameters of Law 14.470/22.** Non-signatories pay double damages,
  leniency and TCC signatories pay single damages and are not jointly liable, there is a 5-year
  limitation period from CADE's decision, pass-on is not presumed, and CADE's decision supports
  "tutela de evidência". Together these mean that more liability from more sanction spheres makes
  confessing more costly *unless* the leniency protection extends to those spheres. That is the
  tension Paper 1 points to.
- **Weakness for the rubric.** It is neither a theory paper nor causal empirics. Present it as
  institutional evidence, not as one of the "theory" papers.

## 3. CADE/DEE DT 003: cement-cartel overcharge

- **Question.** What overcharge did the cement cartel (convicted 2014, R$ 3.1 bn in fines, the
  largest ever; active since at least 1987) impose, and what did breaking it save consumers?
- **Method.** Difference-in-differences with an event study. Treated: cement CP II-E-32 per kg.
  Controls: CA-50 and CA-60 steel bars and hydrated lime. Monthly median prices by state from
  SINAPI-IBGE, 13 months before and 7–8 months after the Feb 2007 dawn raids. The window is
  chosen to avoid the PAC programme (Jan 2007).
- **Result.** Prices fell 1.40–2.35% (preferred estimate 2.02%; robustness range 1.55–2.74%), with
  no pre-trends. Savings 2007–2022: about R$ 11.8 bn at 2.02%; with alternative windows and 10% or
  20% overcharges, R$ 2.1–88.7 bn. The estimate is read as a lower bound.
- **Course link (strong, through the interpretation).** The paper explains its small estimate with
  game theory:
  - Harrington (2004a): after detection, firms keep prices high to lower the damages counterfactual.
  - Harrington (2004b, 2005): cartels price below the monopoly level to avoid detection.
  - Post-cartel **tacit collusion**: prices rise from Sept 2007; Turner (2024) shows the same in
    air cargo.
  - Green–Porter and Rotemberg–Saloner price wars.

  These are repeated-game predictions (Lecture 5).
- **Hooks.** The cartel was exposed by an **employee whistleblower**, not by corporate leniency.
  The market (high transport costs, homogeneous product, high barriers, 7 firms with about 85%)
  is a textbook case for sustainable collusion.
- **Use.** Motivation (a real case, with numbers) and evidence for the prediction that damages
  measured on post-cartel prices distort pricing incentives.

## Assessment of the set

- One weak theory paper, one institutional paper, one empirical paper. The rubric ("distinguishes
  theory and evidence", "bridge from theory to model") would reward **replacing Paper 2, or adding
  a fourth paper, with a canonical economics theory paper**. Candidates, all cited in Papers 1 or
  3 (verify each before using it): Motta & Polo (2003, *IJIO*); Harrington (2008, "Optimal
  corporate leniency programs", *J. Ind. Econ.*); Buccirossi, Marvão & Spagnolo (2020, *JLS*,
  leniency versus damages); Pinha & Braga (2021, *JCLE*, Brazil).
- **Candidate gap and question.** Under Law 14.470/22 (double damages for non-signatories, single
  for leniency applicants), does private damages exposure make the leniency race stronger or
  weaker, and thus cartels less or more stable? Paper 1 asks this with one player, an exogenous
  $p$ and an accounting error; Paper 2 documents the rising multi-sphere exposure; Paper 3 shows
  that the cartel is real and that damages measurement feeds back into pricing.

## Model directions (for the group to choose and solve; not to be delegated to AI)

- **A. Static reporting game** (Lectures 1–2): two cartel members choose Report or Stay silent
  simultaneously, with detection $p$, fine $F$, damages multiplier $k\in\{1,2\}$ and a leniency
  discount. When is (Report, Report) a prisoner's dilemma, and how does $k$ for the applicant shift
  it?
- **B. Repeated collusion with leniency** (Lectures 5–6): $n$ firms, grim trigger, and per-period
  detection $p$ followed by fine plus damages plus debarment. Derive the critical discount factor
  $\delta^*(p,F,k,\text{debarment})$ with and without a reporting option, and do comparative
  statics on the damages differential.
- **C. Sequential** (Lecture 4): Paper 1's game, corrected and extended with a second member and an
  endogenous $p$ (the other member may report first).
- B is the most complete for the "Modelo" criterion (30%). A or C is safer for 5 minutes on 24/11.
