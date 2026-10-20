---
tags: [notes, lecture-08, pitfalls, true-false, self-test, pbe, signaling]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 15–16, pp. 303–338; Gibbons (1992) §4.1–4.2, §4.4; Milgrom & Roberts (1992) pp. 154–157; MWG §13.C; rules/00_estilo_avaliacao.md (True/False style)"
---

# Lecture 8 · Pitfalls and an original True/False self-test

> Prev: [[L08-09-formulas]] · Next: [[L08-11-python]] · Map: [[L08-00-map]]

---

## Part I — the confusions this material produces

### 1 · "A PBE is a strategy profile"

**It is a profile *and* a belief system.** Stating $(UU,BB)$ alone is not a PBE of the MBA game;
$(UU,BB)$ with $\mu_U=\tfrac14$ and $\mu_D=0.9$ is **not** one (at $\mu_D=0.9>\tfrac38$ the employer
would promote after an MBA). The beliefs are part of the answer; "$\mu_D\le\tfrac38$" is what makes it
an equilibrium. → [[L08-05-mba-game]] §5.2.

### 2 · "Off the path, beliefs must be the prior"

**No — off the path Bayes' rule is $\tfrac00$ and Requirement 15.3 allows any belief.** On the path
in a *pooling* equilibrium the belief equals the prior; at an *unused* message it is free. Confusing
the two makes one wrongly "derive" $\mu_D=p=\tfrac14$ in the MBA pooling equilibrium (it happens to
support $B$, but $\mu_D=0.3$ would too, and $\mu_D=0.5$ would not). → [[L08-02-beliefs-and-pbe]] §3–4.

### 3 · "Subgame perfection already handles credibility"

**Not with private types.** In the entry game with types, the incumbent's nodes after entry form
one information set; the only proper subgame is the whole game, so the non-credible $(OO,F)$ is
subgame perfect. Only a belief at the information set kills it. → [[L08-01-subgame-perfection-fails]] §3.

### 4 · "Separating means the high type does what it would do under full information"

**In the envy case it over-invests.** With unproductive education, full information gives
$e^*(H)=0$; separation needs $e_H\ge1.5$ (M&R numbers). The low type is the one who keeps his
full-information choice ($e_L=0$, MWG Lemma 13.C.2). → [[L08-06-spence-job-market]] §2–3.

### 5 · "Education raises wages, so it must raise productivity"

**False in the pure Spence model**: output is $\theta$ whatever the education, yet wages rise with
education in a separating equilibrium because education **reveals** $\theta$. The rules style guide
uses exactly this trap (`rules/00_estilo_avaliacao.md` §2). → [[L08-06-spence-job-market]] §1.

### 6 · "Signaling makes the able better off"

**Not necessarily.** The low type is always worse off (20 < 29); the high type is better off only if
$p\le p^*=1-c_H/c_L$. With M&R's costs and 70% high types, the pooled wage $20+30(0.7)=41$ beats the
35 a high type nets after signaling. → [[L08-06-spence-job-market]] §5.

### 7 · "Any cost difference makes a signal work"

**What matters is the marginal cost, and its ranking.** If $c_H\ge c_L$ the separating interval
$[\Delta/c_L,\Delta/c_H]$ is empty: any education the high type would buy, the low type buys too
(M&R p. 156). In the MBA game, separation needs $c_H\le w_M-w_B\le c_L$: with $c_L=3<4$, the low type
mimics and only pooling survives. → [[L08-05-mba-game]] §5.1.

### 8 · Signaling vs screening

**Who moves first.** Signaling: the **informed** party acts (education, output, advertising) and the
uninformed infers. Screening: the **uninformed** party offers a menu and the informed self-select
(M&R pp. 154, 156–157; e.g. deductible vs no-deductible insurance). The self-selection constraints
look alike; the timing and the solution concept differ (screening is a design problem — out of
this course's scope as mechanism design).

### 9 · "The intuitive criterion picks the equilibrium the Sender likes best"

**It picks the one that survives a credible-deviation test.** In the two-type games here that is the
least-cost separating equilibrium, but that need not be the high type's favourite: at $p>p^*$ the
high type prefers the pooling outcome the criterion eliminates (note 06 §5). → [[L08-08-intuitive-criterion]].

### 10 · "Pooling on the off-path message tells you nothing, so ignore it"

**The reply to the unused message is the equilibrium's enforcement device.** In Gibbons's Fig. 4.2.2,
pooling on $L$ requires the reply $d$ after $R$; with $u$ after $R$, type $t_1$ deviates (2 > 1).
Writing the receiver strategy for used messages only is an incomplete strategy. → [[L08-04-signaling-games]] §3.

---

## Part II — True/False self-test (original items)

Scoring as in `rules/00_estilo_avaliacao.md`: score $=\max\{0,\ \text{correct}-\text{wrong}/2\}\times$
item value; blanks are not wrong. **[E]** easy · **[M]** medium · **[P]** hard.

### Block A — beliefs and PBE

**1.** In a perfect Bayesian equilibrium, beliefs at every information set must follow Bayes'
rule. **[E]**
**F.** Only on the equilibrium path (Requirement 15.2). Off the path Bayes' rule gives $0/0$ and
Requirement 15.3 allows any belief — which is precisely what lets pooling equilibria exist.

**2.** If a Bayesian Nash equilibrium reaches every information set with positive probability, it
is a PBE once beliefs are computed by Bayes' rule. **[E]**
**T.** Proposition 15.1: any failure of sequential rationality at a reached information set would
be a profitable ex-ante deviation, contradicting BNE.

**3.** In the entry game with a weak and a competitive entrant, the BNE in which both types stay out
is subgame perfect but not a PBE. **[M]**
**T.** The only proper subgame is the whole game, so the BNE $(OO,F)$ is subgame perfect; but after
entry $A$ yields 1 and $F$ yields $-\mu\le0$, so no belief makes $F$ a best reply.

**4.** A strategy that is never played on the equilibrium path cannot affect whether a profile is a
PBE. **[E]**
**F.** Off-path actions must be sequentially rational given some belief, and they deter
deviations: the employer's $B$ after an unused MBA is what sustains the MBA pooling equilibrium.

**5.** Every sequential equilibrium is a PBE, but some PBE are not sequential equilibria. **[M]**
**T.** Sequential equilibrium adds consistency (Def. 15.5). In Tadelis's Fig. 15.4, $(U,R)$ is a
PBE with $\mu>\tfrac23$, but trembles force $\mu=\tfrac12$, under which $R$ is not optimal.

**6.** Consistency requires off-path beliefs to equal the prior distribution of Nature's moves.
**[P]**
**F.** It requires them to be limits of Bayes' rule under totally mixed strategies; they equal the
prior in Fig. 15.4 only because player 1 cannot condition on Nature. In general the trembles of
players who do observe Nature can shift the odds.

### Block B — signaling games

**7.** In a pooling equilibrium of a signaling game, the receiver's belief after the equilibrium
message equals the prior. **[E]**
**T.** All types send it, so Bayes' rule gives $\mu(t\mid m)=p(t)$: the message carries no
information.

**8.** In a separating equilibrium with two types and two messages, the receiver's beliefs are
unrestricted at some information set. **[M]**
**F.** Both messages are used, so both beliefs are pinned (0 and 1). Free beliefs arise in
separating equilibria only when there are more messages than types.

**9.** In Tadelis's MBA game at the book's numbers, the employer promotes a worker after an MBA
whenever its belief that he is high-skill is at least 3/8. **[E]**
**T.** $10\mu\ge5\mu+3(1-\mu)\iff8\mu\ge3$.

**10.** The MBA game's separating equilibrium exists for every prior $p\in(0,1)$, holding costs and
wages at the book's values. **[M]**
**T.** It uses beliefs 0 and 1 and the constraints $c_H\le w_M-w_B\le c_L$ ($2\le4\le5$), none of
which involves $p$.

**11.** In the MBA game, the pooling equilibrium in which no one studies would still exist if the
employer believed that an MBA holder is high-skill with probability 0.5. **[M]**
**F.** At $\mu_D=0.5>\tfrac38$ the employer promotes after an MBA; the high type then gets
$10-2=8>6$ from studying and deviates.

**12.** For a costly action to work as a signal, it must be cheaper for the type that wants to be
identified. **[E]**
**T.** Otherwise the other type mimics (M&R p. 156: if $C_H\le C_L$ fails the self-selection
inequalities cannot both hold); formally single crossing, $c_e(L,e)>c_e(H,e)$.

### Block C — Spence

**13.** In Spence's model with unproductive education, a separating equilibrium raises wages with
education and therefore raises output with education. **[E]**
**F.** Output is $\theta$ regardless of $e$; wages differ because education reveals $\theta$.

**14.** With $\theta_H=50$, $\theta_L=20$, $c_H=10$ and $c_L=20$, any $e_H$ between 1.5 and 3
supports a separating equilibrium. **[E]**
**T.** L will not mimic iff $50-20e_H\le20$, i.e. $e_H\ge1.5$; H prefers signaling iff
$50-10e_H\ge20$, i.e. $e_H\le3$.

**15.** In those separating equilibria the low-ability worker chooses a strictly positive amount of
education. **[E]**
**F.** He is paid $\theta_L$ whatever he does, so any $e>0$ is a pure loss: $e_L=0$ (MWG Lemma
13.C.2).

**16.** A higher share of high-ability workers raises the least-cost separating education level.
**[M]**
**F.** $e^*=(\theta_H-\theta_L)/c_L$ does not involve the prior: the separating set is independent of
$p$ (MWG p. 456). The prior moves the pooled wage and $p^*$-comparisons only.

**17.** With M&R's numbers and 70% high-ability workers, high-ability workers are worse off in the
least-cost separating equilibrium than if signaling were impossible. **[M]**
**T.** Signaling nets them $50-10(1.5)=35$; no signaling pays everyone $0.7(50)+0.3(20)=41>35$
($p=0.7>p^*=0.5$).

**18.** In the separating equilibria of the Spence model, the expenditure on education is socially
wasted when education is unproductive. **[E]**
**T.** It changes no output, only who is paid what; M&R call it "a pure social waste" (p. 156).

**19.** In a hybrid equilibrium in which the low type randomizes, the belief after the high type's
education level lies strictly between the prior and 1. **[M]**
**T.** $\mu=\dfrac{q}{q+(1-q)\pi}$ with $\pi\in(0,1)$ lies in $(q,1)$ (Gibbons 4.2.8).

### Block D — limit pricing and refinements

**20.** In Tadelis's limit-pricing game, the low-cost incumbent can separate by producing its
monopoly output of 2 in the first period. **[M]**
**F.** The high-cost type would mimic: $2+2.25=4.25>3.25$. Separation needs $q_1^{1L}\ge2.62$.

**21.** In the separating equilibria of the limit-pricing game, the low-cost incumbent's first-period
price is below its marginal cost. **[P]**
**F.** At $q\in[2.62,3.32]$ the price is $5-q\in[1.68,2.38]>1$. Below-cost pricing needs a growing
market or more deterrence periods (pp. 329–330).

**22.** In the pooling equilibria of the limit-pricing game, the entrant stays out. **[M]**
**F.** With belief $\tfrac12$ the Bayesian Cournot game gives the entrant $\tfrac7{36}>0$, so it enters;
pooling buys the incumbent no deterrence.

**23.** The intuitive criterion eliminates the MBA game's pooling equilibrium because the low type
could never gain by getting an MBA, whatever the employer then believes. **[E]**
**T.** L's best payoff from $D$ is $10-5=5<6$; excluding L, the employer promotes after $D$ and the
high type gets $8>6$.

**24.** A message that is equilibrium-dominated for a type is necessarily dominated for that type.
**[P]**
**F.** The converse holds (dominated ⇒ equilibrium-dominated). In Beer–Quiche, Beer is
equilibrium-dominated for the wimpy type ($2<3$) but not dominated (its best from Beer, 2, exceeds its
worst from Quiche, 1) — Gibbons p. 239.

**25.** In the two-type Spence model with single crossing, every pooling equilibrium fails the
intuitive criterion. **[M]**
**T.** Between $(\theta_H-u_L^*)/c_L$ and $(\theta_H-u_H^*)/c_H$ there is always an education level the low
type would refuse even at $\theta_H$ and the high type would take if believed (Gibbons pp. 239–244;
MWG p. 471).

**26.** The intuitive criterion selects, among the separating equilibria of the limit-pricing game,
the one with the largest first-period output. **[M]**
**F.** It selects the **least-cost** one, $q_1^{1L}=2.62$ — the smallest output that still deters
mimicry (p. 335).

---

## Links

- Map: [[L08-00-map]] · Formulas: [[L08-09-formulas]] · Code: [[L08-11-python]].
- Style: `rules/00_estilo_avaliacao.md` (True/False rule) · Rules: [[../../rules/07_selecao_adversa|rules/07]].
