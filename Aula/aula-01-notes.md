---
tags: [aula, aula-01, notes, topic/organizacoes-importam]
date: 2026-10-09
---

# Aula 1 — Does Organization Matter? Ford × GM × Toyota

> **Syllabus item** · *Aplicação: As organizações importam? Ford x GM x Toyota* · [[rules/01_organizacoes_importam|Topic 1]] · [[Map/study-guide#Aula 1 — Does organization matter? Ford × GM × Toyota|class plan]]
> **Read** · Milgrom & Roberts (1992), Ch. 1 "Does Organization Matter?" (pp. 2–18) · Ch. 4 "Coordination and Business Strategy" (pp. 106–113) · Cabral (2017) §3.5 "Why are firms different?" (pp. 56–59)
> **Play** · three interactive companions in `Aula/aula-01-companions/`: [Two Coherent Systems](aula-01-companions/two_systems.html) · [The Valley Between Systems](aula-01-companions/valley.html) · [The Complementarity Multiplier](aula-01-companions/multiplier.html) (published, private: [1](https://claude.ai/artifact/Lj8hXzAiHiSqvzbBNC3mMs) · [2](https://claude.ai/artifact/KShLdDVsrgtdCAchVTg9Hk) · [3](https://claude.ai/artifact/WurEuyriXGN9UezjhaiqXL))
> **Watch** · `Videos/aula-01-does-organization-matter/` (plan and script; same numbers as the companions)

Page numbers are M&R's printed pages unless another book is named. Facts that do not come from
M&R carry their source inline; the stylized numbers are illustrative and checked by
`aula-01-companions/check_companions.py` and the video's `check_numbers.py`.

---

## 0. The question

Ford had the technology, the scale and the cost advantage. GM beat it. Toyota was small, short of
capital and technologically behind. It beat GM. M&R's answer, which this class builds up to:

> "organization and business strategy can be as important as technology, cost, and demand in
> determining a firm's success" (p. 16) — and what matters most is "the match of their strategies
> and their structures" (p. 16).

The class has two halves. First the cases, read as answers to two problems every organization
faces, **coordination** and **motivation** (p. 17). Then the mathematics of **fit**:
complementarities, why they make good systems coherent, and why coherent systems are hard to
change one piece at a time.

---

## 1. Ford: one product, one system

M&R's picture of Ford is short and exact: "producing a single product (the Model T Ford) in
high-volume factories using specialized equipment and rigidly disciplined labor paid according to
the job being done" (p. 109). It was "an entirely different but equally coherent strategy that was
appropriate for its time" and it took Ford past 50% of the US car market (p. 109). By 1921 the
Model T held **55%** of the market, against **4%** for Chevrolet and **11%** for all GM brands
together (p. 2).

The pieces, and why each raised the value of the others:

| Choice | What it did | What it needed from the rest |
|---|---|---|
| One model, one colour | long, identical runs | a buyer who wanted a cheap standard car |
| Dedicated machines, moving line | labour per car collapsed | huge, steady volume |
| Narrow, repetitive tasks | unskilled labour could be used | close supervision, a pay premium to keep workers |
| High wage (the $\$5$ day, 1914) | turnover fell | the productivity of the line to pay for it |
| Making its own parts | scale in components | the single design |

History outside M&R (sources in `Videos/aula-01-does-organization-matter/provenance.md`): the
Model T sold for about $\$850$ in 1908 and about $\$260$ by the mid-1920s; the moving chassis line
(1913) cut assembly time from about 12.5 hours to 93 minutes by early 1914; 1913 labour turnover
was 370% before the $\$5$ day (Raff & Summers 1987; the turnover figures are marked *to confirm*
there). The wage story is efficiency wages, M&R Ch. 8 (p. 250), outside this course's core.

**The weakness was the same as the strength.** Ford's 1920 answer to the recession was a price cut
of about 25%, which GM, with higher costs, could not match (p. 2). Cost leadership worked while
buyers wanted the same car. It stopped working when they wanted different cars.

---

## 2. GM: variety, and the organization it demanded

Sloan took over a GM in crisis in 1921: unsold inventories piling up, sales down 75% between
summer and fall 1920, divisions "competed mostly with one another" (pp. 2–3).

**Strategy.** A car "for different segments of the market": Cadillac at the top, each division a
lower-income segment, Chevrolet below the Model T's price (p. 3).

**Why the strategy required a new organization.** Variety multiplied the decisions: new designs,
dealers, market information per segment, separate factories and supplies. At the same time the
divisions had to be coordinated: not compete too much, share ideas, coordinate R&D, standardize
parts "enough to achieve economies of scale in parts production" (p. 3). Neither Ford's
centralized one-product organization nor the old GM, "a collection of car companies and suppliers
operating without any central direction", could do this (p. 3). The old accounting system had not
even charged divisions for the inventories they built up, so they kept producing into the
recession (p. 3).

**The multidivisional form** (p. 3):

- divisions keep operating autonomy, each with its own management team and market segment;
- a strong central office does *not* run day-to-day operations; it audits and evaluates
  divisions, plans and coordinates strategy, and keeps research, legal and financial functions;
- the centre checks internal accounting prices against market prices, so supply divisions can be
  judged "as if each were a separate firm" (p. 4).

Henry Ford mocked the "great big chart" where a message takes six weeks to travel (p. 4). The
result: from 1927 to 1937 Ford lost $\$200$ million and GM earned over $\$2$ billion; by 1940 GM
had 45% of the market, Ford 16% (p. 4).

**GM's system fit together too.** Shared components across models let GM afford specialized
equipment for chassis, engines and brakes (p. 5); its volumes fully used efficient parts plants,
so it integrated vertically (p. 5), and it made suppliers compete on price (p. 6). The price of
specialization: major redesigns only about every 12 years in the 1950s and 1960s (p. 5).

---

## 3. Toyota: small, poor, and coherent in the other direction

Early-1950s Toyota had a "drastic lack of capital" and a scale too small to match US costs (p. 4).
It first tried to copy mass production, then built a different system under Eiji Toyoda and
Taiichi Ohno (p. 4).

| Practice (M&R pp. 4–6) | Why it followed from Toyota's position | What it then required |
|---|---|---|
| **Just-in-time / kanban**: no buffer inventories | inventory systems have large scale economies Toyota could not reach | every step reliable; defects caught at once |
| **Operators maintain and repair their own machines** | without buffers, a breakdown stops everything | broader skills, authority on the floor |
| **Flexible equipment**, quick resets, robots by the 1960s | too small to dedicate machines to one model | frequent model changes became cheap: redesign twice as often as GM |
| **Outside suppliers for complex components** | could neither reach efficient scale in parts nor afford to own parts makers | close day-to-day coordination with suppliers |
| **Few suppliers, long-term relations** | high-level components that must fit, frequent redesigns | suppliers willing to invest in Toyota-specific skills and machines |

M&R's summary of the logic: "If low inventories were to be achieved, the rest of the organization
had to emphasize reliability, quick response to machine breakdowns, quick and close communications
with suppliers, stable production plans, and other features that substitute for the buffer function
of inventories" (p. 17). Cabral adds why the system was hard to copy: "the system involved so many
different aspects that it was difficult to pin down what the crucial success factors were"
(Cabral 2017, §3.5, p. 57).

### Ford, GM, Toyota side by side

| Dimension | Ford (1910s) | GM (1920s on) | Toyota (1950s on) |
|---|---|---|---|
| Product line | one model | a ladder of segments | several models, frequent redesign |
| Equipment | dedicated | specialized, shared components | flexible |
| Inventories | buffers | buffers | none (just-in-time) |
| Suppliers | made its own parts | vertically integrated; price competition | few, long-term, outside |
| Decisions | centralized in Henry Ford | divisions operate; centre audits and sets strategy | problem solving on the floor |
| Workers | narrow tasks, high wage | (not developed in M&R) | multi-skilled, maintain machines |

Each column is coherent. None is a list of independent "best practices".

---

## 4. Three more cases, one lesson each

M&R widen the claim beyond cars (pp. 6–16). Each case isolates one piece of the argument.

- **Hudson's Bay vs. North West Company** (pp. 6–9): **incentives and decision rights.** HBC had
  half the import costs, a royal monopoly and posts on the bay. It was run from London, with
  15-month communication lags, flat salaries and rules enforced by flogging. NWC traders paddled an
  extra 1,500 miles. Its "wintering partners" decided on the spot and shared the profits. By about
  1810 NWC had nearly 80% of the trade (p. 8). HBC recovered only by copying the *organization*:
  inland posts, half of profits to field officers, more freedom of action (pp. 8–9).
- **Salomon Brothers** (pp. 9–12): **incentives that are too individual.** Near piece-rate bonuses
  made traders work hard and take risks but discouraged sharing information across departments
  (p. 11). The 1990 reform paid part of each bonus in stock held in trust for five years; the
  announcement raised the firm's value by 7–10% (p. 12). FFT 1.3 (p. 18) asks what the 1991 scandal
  says about that scheme.
- **Eastern Europe** (pp. 12–16): **information, incentives and interdependent reforms.** Central
  planning replaced prices with vertical information flows (p. 13). The **ratchet effect**: a
  manager who beats the quota gets a higher quota, so nobody beats it; capacity is hidden and
  resources hoarded (p. 14). Reform pieces depend on each other (property rights, capital markets,
  contract enforcement), so "the worst outcome might be some halfway compromise" (p. 16): the
  country that moved only its trucks to the other side of the road. The ratchet effect returns in
  Aula 16 (M&R p. 232).

---

## 5. The patterns: coordination, motivation, and fit (pp. 16–17)

M&R draw four patterns out of the cases.

1. **Organization and strategy can matter as much as technology, cost and demand.** Ford lost to
   GM despite better technology and scale; GM lost share to a smaller, weaker Toyota; HBC lost to
   NWC (p. 16).
2. **Incentives matter.** HBC employees got no share of extra profits; GM's divisions were not
   charged for inventories; Salomon rewarded individuals and so discouraged cooperation; planned
   economies "ran afoul of incentives at every turn" (p. 16).
3. **Put authority where the information is.** Salomon's traders, GM's divisions, Toyota's
   operators, NWC's wintering partners (p. 17).
4. **Incentives and delegated authority are complements.** Delegation is worth little "unless the
   decision makers share the organization's objectives", and incentives matter most "when more
   initiative is expected from employees". In M&R's words: "incentives and delegated authority are
   complements: each makes the other more valuable" (p. 17).

And the organizing pair for the course: "The study of organization is not about how berries are
arranged on a tree of authority but about how people are coordinated and motivated to get things
done" (p. 16).

| | **Coordination**: getting the plans to fit (information) | **Motivation**: getting people to carry them out (interests) |
|---|---|---|
| Ford | one product, one centre, the line sets the pace | high wage, close supervision |
| GM | divisions per segment; centre plans strategy, shared parts | divisions judged on profit, internal prices checked against the market |
| Toyota | just-in-time signals, close supplier links | multi-skilled teams, long-term supplier relations |
| HBC → NWC | decisions moved to the field | profit shares for those deciding |

Course map: coordination in Aulas 6–8 (M&R Ch. 3–4), motivation in Aulas 9–16 (Ch. 5–7).

---

## 6. Complementarities: the mathematics of fit (M&R Ch. 4, pp. 108–109)

### 6.1 Definition

The market definition: two inputs are complements if a fall in the price of one raises demand for
the other. M&R use a "more inclusive" definition that also covers internal activities:

> "Several activities are mutually complementary if doing more of any one activity increases (or at
> least does not decrease) the marginal profitability of each other activity in the group" (p. 108).

**Smooth version** (footnote 8, p. 108). With activity levels $x = (x_1, \dots, x_n)$ and profit
$\pi(x)$:

$$\frac{\partial^2 \pi}{\partial x_i \, \partial x_j} \;\ge\; 0 \qquad \text{for all } i \ne j .$$

**Discrete version: increasing differences.** For two yes/no choices $x, y \in \{0, 1\}$:

$$\underbrace{\pi(1,1) - \pi(0,1)}_{\text{gain from } x \text{ when } y = 1} \;\ge\; \underbrace{\pi(1,0) - \pi(0,0)}_{\text{gain from } x \text{ when } y = 0}.$$

Rearranging the same inequality three ways shows it is symmetric (the gain from $y$ is larger when
$x=1$) and equivalent to **supermodularity**, $\pi(1,1) + \pi(0,0) \ge \pi(1,0) + \pi(0,1)$: the
two "matched" corners together beat the two "mixed" ones.

**Worked example** (the video's 2×2 table). $\pi(0,0)=0$, $\pi(1,0)=-2$, $\pi(0,1)=-1$,
$\pi(1,1)=5$.

- gain from $x$ when $y=0$: $-2 - 0 = -2$; when $y = 1$: $5 - (-1) = 6$. Increasing differences hold.
- each practice **alone loses money**, and the pair gains 5. The cross effect is $6 - (-2) = 8$.
- A firm that tests each practice separately rejects both.

Complementarity says nothing about whether each practice is good on its own. It says each is
**better where the other is present**.

### 6.2 Why complements move together

**One choice, one parameter (Topkis, stated).** If $x^*(t)$ maximizes $f(x, t)$ and $f$ is concave
in $x$, differentiate the first-order condition $f_x(x^*(t), t) = 0$:

$$f_{xx}\, x^{*\prime}(t) + f_{xt} = 0 \;\;\Longrightarrow\;\; x^{*\prime}(t) = -\frac{f_{xt}}{f_{xx}} \;\ge\; 0 \quad\text{whenever } f_{xt} \ge 0 .$$

Topkis' theorem gives the same conclusion without derivatives or concavity: if $f$ has increasing
differences in $(x, t)$, the optimal $x$ is non-decreasing in $t$. Milgrom & Roberts (1990, *AER*
80(3), 511–528) used it to explain why the elements of modern manufacturing were adopted together.
Stated, not proved: the lattice proof is beyond the course.

**Two choices, the systems effect.** Let $x$ be delegated authority and $y$ incentive intensity
(M&R's p. 17 pair), with

$$\pi(x, y) = t x + s y + b\, x y - \tfrac{c}{2} x^2 - \tfrac{c}{2} y^2, \qquad \frac{\partial^2 \pi}{\partial x\, \partial y} = b .$$

First-order conditions and their solution:

$$t + b y = c x, \qquad s + b x = c y$$

$$x^* = \frac{c t + b s}{c^2 - b^2}, \qquad y^* = \frac{c s + b t}{c^2 - b^2}, \qquad \text{a maximum iff } c > |b| .$$

How delegation responds to more valuable local information $t$:

$$\frac{\partial x^*}{\partial t} = \frac{c}{c^2 - b^2} = \frac{1}{c} \cdot \frac{1}{1 - (b/c)^2} = \frac{1}{c}\Big(1 + \big(\tfrac{b}{c}\big)^2 + \big(\tfrac{b}{c}\big)^4 + \cdots\Big), \qquad \frac{\partial y^*}{\partial t} = \frac{b}{c^2 - b^2}.$$

- $1/c$ is the response with $y$ held fixed. The geometric series is M&R's footnote 8 in numbers:
  more $x$ raises the return to $y$, more $y$ raises the return to $x$, "possibly leading to
  another round of increases" (p. 108).
- $t$ never enters the condition for $y$, yet $y^*$ moves: with $b > 0$ incentives rise when
  delegation becomes more valuable.
- At $c = 2$, $b = 1$: multiplier $1/(1 - 1/4) = 4/3$. With $t$ from 1 to 3 ($s = 1$), $x^*$ goes
  from 1 to $7/3$ instead of from $0.5$ to $1.5$.
- With **substitutes** ($b < 0$) the multiplier is still above one, because $(b/c)^2 > 0$:
  incentives fall, which raises delegation's return again. Only the sign of $\partial y^*/\partial t$
  flips.

▶ **Companion:** [The Complementarity Multiplier](aula-01-companions/multiplier.html). Move $t$
and watch the staircase of rounds; set $b = 0$ to see the multiplier fall to 1; push $|b|$ toward
$c$ to see it explode, then the optimum vanish.

### 6.3 Substitutes are complements upside down

If $\partial^2 f/\partial x\,\partial y \le 0$ (buffer inventories and floor-level problem solving
are substitutes: each makes the other less needed), define $z = -y$ and $g(x, z) = f(x, -z)$. Then
$g_{xz} = -f_{xy} \ge 0$. Every result above applies to $(x, z)$. "Many buffers, narrow jobs" (Ford)
and "no buffers, problem solvers" (Toyota) are both coherent; the mixtures are not.

### 6.4 Strong complementarity and design attributes (p. 109)

Complementarity makes the choices **predictable**: high levels go together. M&R add a second,
separate feature, the **high cost of failing to fit**, and call a group *strongly complementary*
when raising some activities "greatly increases the returns" to raising the others; then "design
attributes are always present" (p. 109). The box "Modern Manufacturing Strategy" (pp. 109–110)
traces one chain: small demand per product → no finished-goods inventories → close sales–factory
communication → short production runs → frequent changeovers → flexible equipment →
multi-skilled workers paid for skills, not piece rates → machine-time cost accounting.

---

## 7. More than one coherent system (M&R Ch. 4, pp. 111–113)

### 7.1 Figure 4.3, made exact

M&R's figure: a **marketing manager** chooses the number of product varieties $n$; a
**manufacturing manager** chooses the batch size $b$ (p. 111). More varieties at a fixed batch size
raise inventories, so the larger the batch, the fewer varieties are worth offering; more varieties
raise the marginal inventory cost of a larger batch, so the more varieties, the smaller the best
batch (p. 111). Both best replies slope down, and they can cross more than once (p. 112).

M&R draw the curves without a formula. A form that produces them, with equipment
$\theta \in \{\text{specialized}, \text{flexible}\}$ added (pp. 5, 113):

$$\pi(n, b, \theta) = mQ + A \ln n - \frac{S_\theta Q}{b} - \frac{h\, n\, b}{2} - \Delta c_\theta\, Q, \qquad n \ge 1,$$

where $A$ is the taste for variety, $Q$ total volume, $S_\theta Q / b$ the changeover cost
($Q/b$ changeovers), $h n b / 2$ the cost of holding average inventory $b/2$ for each of $n$
models, and $\Delta c_\theta$ the unit-cost premium of flexible equipment (zero for specialized).

- Manufacturing's reply (the EOQ formula): $b^*(n) = \sqrt{2 S_\theta Q / (h n)}$, decreasing in $n$.
- Marketing's reply: $A/n = h b / 2 \Rightarrow n^*(b) = \max\{1, \; 2A/(h b)\}$, decreasing in $b$.
- Cross effect $\partial^2 \pi / \partial n\, \partial b = -h/2 < 0$: variety and batch size are
  substitutes, so variety and **small batches** are complements (§6.3).
- Within one equipment type: $b^* = S Q / A$, $n^* = 2A^2/(h S Q)$,
  $\pi^* = mQ + A \ln n^* - 2A - \Delta c\, Q$; corner $n^* = 1$ (Ford's single model) when
  $2A^2 \le h S Q$.
- Manufacturing switches to flexible equipment once $n$ exceeds
  $n_s = (\Delta c\, Q)^2 / \big(2 Q h (\sqrt{S_s} - \sqrt{S_F})^2\big)$. Its reply **jumps down**
  there.

With the companion's calibration ($A = 20$, $Q = 100$, $h = 1$, $S_s = 50$, $S_F = 2$,
$\Delta c = 1$, $m = 2$):

| System | $n^*$ | $b^*$ | Profit |
|---|---|---|---|
| Specialized (Ford-type) | 1 (corner) | 100 | 100.0 |
| Flexible (Toyota-type) | 4 | 10 | 87.7 |

Both are coherent: at each, neither manager wants to move. Between them, profit along
manufacturing's reply falls to **83.9**. Raise $A$ to 30 and the flexible system earns 105.9,
better than 100, yet the valley is still there (88.4).

### 7.2 What the figure teaches

- **Alignment is not optimality.** Each crossing is "a coherent strategy" (p. 112); "only one
  combination is actually profit maximizing" (p. 112). Ford's crossing was best for the early
  century; the many-varieties, small-batch crossing is best for many industries now (p. 112).
- **Local adjustment cannot find the global shift.** Managers can track the *local* movement of
  their own crossing, "but recognizing that a radical strategic shift is desirable is likely to
  require information that neither manager has" (p. 113). Smooth changes in the curves can hide a
  jump in which crossing is best (p. 112).
- **So the choice among coherent patterns is a job for central management** (p. 113, p. 115),
  with innovation attributes, because the information is outside the organization. This is
  Aula 7's argument, met here first.

**A careful reading of footnote 9.** M&R picture the profit surface as "a mountain with three
peaks, one at each of the intersections" (p. 112). With two *smooth* decreasing best replies that
cross three times, the middle crossing is a **saddle**, not a peak: there the replies cross the
"wrong" way, $\pi_{nb}^2 > \pi_{nn}\pi_{bb}$, and the Hessian is indefinite. The outer two crossings
are the peaks. The book's point is unaffected: several coherent systems, one best.

▶ **Companion:** [Two Coherent Systems](aula-01-companions/two_systems.html). Plate 1 is Figure
4.3; plate 2 is the "ridge line" of footnote 9. Try *More taste for variety* and *Cheaper
flexibility*: each system moves a little, the best one switches.

---

## 8. The valley, and the plant that tested it

### 8.1 Three practices on a cube

Take three Toyota practices from §3: just-in-time $J$, multi-skilled teams $T$, long-term
suppliers $S$, each 0 or 1. The class's stylized payoff:

$$\pi(J, T, S) = 10 - 4J - 2T - S + 4JT + 5JS + 2TS + 2JTS .$$

| Corner | 000 | 100 | 010 | 001 | 110 | 101 | 011 | 111 |
|---|---|---|---|---|---|---|---|---|
| Profit | **10** (Ford) | 6 | 8 | 9 | 8 | 10 | 9 | **16** (Toyota) |

- Supermodular: the pairwise gains $4 + 2S$, $5 + 2T$, $2 + 2J$ are all positive.
- **Every first step loses**: 6, 8, 9 < 10. Ford's corner is a local peak.
- **Every adoption order dips.** Of the six orders from 000 to 111, the best one still falls to 9
  before reaching 16.
- 111 is also a local peak (its neighbours earn 9, 10, 8). Two peaks, and marginal analysis cannot
  tell them apart: the package gain is $+6$; the best single step is $-1$.

Complementarity tells you **where** the optimum is (all practices together). It does not make the
road uphill. It **creates** the valley, because a practice is worth least where its complements
are missing.

▶ **Companion:** [The Valley Between Systems](aula-01-companions/valley.html). Set the
interactions to zero (*No interactions*) to see "best practices" thinking: profits add up and the
package loses. Remove the stand-alone losses (*No stand-alone losses*) and some order climbs
without a dip.

### 8.2 NUMMI: the same workers under two systems

History outside M&R (sources and status in `Videos/aula-01-does-organization-matter/provenance.md`):

- GM closed its Fremont, California plant in 1982. It reopened in 1984 as **NUMMI**, a GM–Toyota
  joint venture run on Toyota's system, and over 85% of its first workforce were the laid-off GM
  workers.
- 1987 assembly hours per car: **31** at a comparable GM plant (Framingham), **19** at NUMMI, 16 at
  Toyota's Takaoka plant; assembly defects per 100 cars 135, 45 and 45. These figures come from a
  secondary reproduction of Womack, Jones & Roos (1990) and are marked *to confirm against the book*.
- GM owned half the plant and its managers could study it, yet its efforts to spread the system
  piece by piece across its US plants "proved largely unsuccessful". The exception was Brazil, where
  NUMMI-trained managers ran the transfer.

Read with §8.1: Toyota moved the whole system at once (the jump across the valley). GM, adopting
practice by practice, kept landing on the low corners.

### 8.3 Evidence beyond one plant

A test regression: $y = \beta_0 + \beta_1 x + \beta_2 z + \beta_3 x z + \varepsilon$. The effect of
$x$ is $\beta_1$ when $z = 0$ and $\beta_1 + \beta_3$ when $z = 1$: $\beta_3$ is the cross effect.
Ichniowski, Shaw & Prennushi (1997, *AER* 87(3), 291–313), on 36 steel finishing lines: the bundle
of innovative HR practices raises productivity; single practices adopted in isolation do not.
Caution: firms that adopt practices together may differ in other ways, so correlated adoption
alone does not prove complementarity.

---

## 9. Common mistakes

| Mistake | Correction |
|---|---|
| "Copy best practices one at a time" | Profit is not additive; with complements, a practice adopted alone can lose money (§6.1, §8.1). |
| "Complements means each is good" | Complements means each is *better with* the other. Both can lose alone (the 2×2 table). |
| "A coherent system is the best system" | Coherence is a local property. Several coherent systems coexist; only one is best (§7.2). |
| "If it is better, managers will drift to it" | Marginal adjustment stays at a local peak; reaching the other needs a coordinated jump (pp. 112–113). |
| Using the market definition of complements (cross-price) for internal choices | M&R's definition is about marginal profitability, $\partial^2\pi/\partial x_i\partial x_j \ge 0$ (p. 108). |
| "Substitutes have a multiplier below one" | In the two-choice model the own response is amplified for either sign of $b$; only the other choice's direction changes (§6.2). |
| Reading organization as the org chart | "not about how berries are arranged on a tree of authority but about how people are coordinated and motivated" (p. 16). |

---

## 10. Exercises (number and page only)

| Exercise | Where | Practises |
|---|---|---|
| M&R Food for Thought 1.1 | p. 18 | splitting a business's decisions between centre and units; coordination vs. motivation |
| M&R Food for Thought 1.2 | p. 18 | the same split in a non-business organization |
| M&R Food for Thought 1.3 | p. 18 | the Salomon incentive scheme (§4) against a later scandal |
| Cabral 1.1 | p. 11 | competition and performance |
| Cabral 3.14 | p. 63 | sustained competitive advantage (§3.5) |
| Cabral 3.20 | p. 64 | productivity dispersion across firms (applied, data) |

For the formal part (§6–§8) there are no book exercises in M&R Ch. 1; use the companions'
presets as problems: predict the read-out, then move the control.

---

## Sources

- Milgrom, P. & Roberts, J. (1992). *Economics, Organization, and Management*. Prentice-Hall.
  Ch. 1 (pp. 2–18), Ch. 4 (pp. 106–115). Read from `Livros/` on 2026-10-09.
- Milgrom, P. & Roberts, J. (1990). "The Economics of Modern Manufacturing: Technology, Strategy,
  and Organization". *American Economic Review* 80(3), 511–528.
- Cabral, L. (2017). *Introduction to Industrial Organization*, 2nd ed. MIT Press. §3.5, pp. 56–59.
- Ichniowski, C., Shaw, K. & Prennushi, G. (1997). *American Economic Review* 87(3), 291–313.
- Ford and NUMMI history: `Videos/aula-01-does-organization-matter/provenance.md` (each claim with
  its source and status).
