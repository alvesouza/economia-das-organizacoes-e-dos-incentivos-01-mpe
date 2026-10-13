---
quiz: "Aula 1 · Quiz 1 of 3 — Ford, GM, Toyota and the other cases"
tags:
  ford-gm: "Ford and GM"
  toyota: "Toyota"
  cases: "HBC, Salomon, central planning"
  patterns: "Coordination, motivation and fit"
---

## ford-gm

Q: A car maker can assemble on stationary stands (fixed cost $F_0$, unit cost $c_0$) or on a moving line (fixed cost $F_1 > F_0$, unit cost $c_1 < c_0$), with average cost $AC = F/q + c$ at volume $q$. For which volumes does the line give the lower average cost, and what does that imply for Ford's other choices?
- For $q > (c_0 - c_1)/(F_1 - F_0)$: the threshold falls as the fixed-cost gap grows, so a costlier line pays at lower volume and the single model is a separate choice
- For $q > (F_1 - F_0)/(c_0 - c_1)$: the line pays only at very high volume, which needs one cheap standard model, so line and single product go together
- For $q < (F_1 - F_0)/(c_0 - c_1)$: the line pays at low volume because its unit cost is lower, so Ford could have kept many different models running on the same line
- For $q > F_1/c_1 - F_0/c_0$: what matters is each technology's own ratio of fixed to unit cost, so the volume needed does not depend on the gap between them
<!-- YW5zOjE= -->
> Setting $F_1/q + c_1 < F_0/q + c_0$ gives $q > (F_1 - F_0)/(c_0 - c_1)$: the larger the extra fixed cost and the smaller the unit-cost saving, the higher the volume needed. Volume of that size needs one cheap, standard car, and a standard car is what the dedicated line makes cheap: the choices form a loop, the first sighting of fit. The distractors invert the ratio, flip the inequality, or compare each technology's own cost ratio, which is not what equating average costs gives.
> Ref: Milgrom & Roberts (1992), Ch. 4 "Scale, Scope, and Core Competencies", pp. 106–107; Ch. 4 p. 109 (Ford's coherent strategy); Aula 1 notes §1
> Similar: Practice plan Aula 1, item 16 (M&R Math. Ex. 4.2, p. 120)

Q: A firm sells volume $q$ split across $n \ge 1$ models at margin $\bar p + a\ln n - c$, where $a > 0$ is buyers' taste for variety, and pays a fixed cost $F$ per model, so $\Pi(n) = q(\bar p + a\ln n - c) - nF$. Which pair gives the interior optimum and the cross effect between $n$ and $a$?
- $n^* = F/(aq)$ and $\partial^2\Pi/\partial n\,\partial a = -q/n^2 < 0$: a stronger taste for variety lowers the marginal value of an extra model
- $n^* = aq/F$ and $\partial^2\Pi/\partial n\,\partial a = 0$: since $a$ multiplies $\ln n$ additively, the taste for variety shifts profit but not the marginal model
- $n^* = aq/F$ and $\partial^2\Pi/\partial n\,\partial a = q/n > 0$: taste for variety and number of models are complements, so GM's ladder follows a rise in $a$
- $n^* = qF/a$ and $\partial^2\Pi/\partial n\,\partial a = q/n > 0$: more volume per model raises the optimal line, and taste for variety reinforces it
<!-- YW5zOjI= -->
> The first-order condition is $qa/n = F$, so $n^* = aq/F$ (the second-order condition $-qa/n^2 < 0$ holds). Differentiating $\Pi'(n) = qa/n - F$ with respect to $a$ gives $q/n > 0$: by the monotone comparative statics of the class, $n^*$ rises with $a$. Ford sits at the corner $n^* = 1$ when $aq \le F$; GM's segmented ladder is the interior solution once buyers want different cars. The zero cross-effect answer forgets that $a$ multiplies $\ln n$, whose derivative depends on $n$.
> Ref: Milgrom & Roberts (1992), Ch. 1 "Crisis and Change at General Motors", pp. 2–3; Aula 1 video plan, BeatVariety; Aula 1 notes §6.2
> Similar: Companion "Two Coherent Systems" (taste for variety control)

P: A plant manager earns a bonus $\beta > 0$ per unit of output $q_t$ above the period's quota $\bar q_t$. The planner revises the quota as $\bar q_{t+1} = (1-\lambda)\bar q_t + \lambda q_t$ with $0 < \lambda \le 1$, and the manager discounts future periods by $\delta \in (0,1)$. Consider one extra unit produced today, holding all future outputs fixed.

Q: What is the present value of the manager's net reward from that extra unit?
- $\beta(1-\delta)/(1-\delta+\lambda\delta)$, because the unit raises every future quota by a geometrically decaying amount
- $\beta/(1-\delta(1-\lambda))$, because the unit's effect on the quota compounds over time and so raises future bonuses
- $\beta(1-\lambda\delta)$, because only next period's quota rises, by $\lambda$, and that single loss is discounted once
- $\beta(1-\lambda)$, because the planner absorbs a share $\lambda$ of the extra unit into the current quota right away
<!-- YW5zOjA= -->
> Today's bonus rises by $\beta$. The quota rises by $\lambda$ next period, by $\lambda(1-\lambda)$ the period after, and so on, so the lost bonuses are worth $\beta\sum_{t\ge1}\delta^t\lambda(1-\lambda)^{t-1} = \beta\lambda\delta/(1-\delta(1-\lambda))$. Net: $\beta[1 - \lambda\delta/(1-\delta+\lambda\delta)] = \beta(1-\delta)/(1-\delta+\lambda\delta)$. The distractors keep only the first period of the loss, treat the quota effect as a gain, or ignore discounting.
> Ref: Milgrom & Roberts (1992), Ch. 1 "Building Socialism", p. 14 (the ratchet effect); Ch. 7 "Intertemporal Incentives: The Ratchet Effect", p. 232
> Similar: Practice plan Aula 1, item 5 (M&R FFT 4.1, p. 119)

Q: Using the net reward $\beta(1-\delta)/(1-\delta+\lambda\delta)$, which statement about the ratchet effect is correct?
- With $\lambda \to 0$ the net reward vanishes, because a planner who barely revises quotas offers no reason at all to produce above the target
- With $\delta \to 0$ the net reward vanishes, because an impatient manager values only the future quota loss and not the bonus paid today
- With $\lambda = 1$ the net reward is zero for any $\delta$, because the whole extra unit is added to every future quota at once and permanently
- With $\lambda = 1$ it is $\beta(1-\delta)$: a full ratchet still leaves some incentive, which vanishes only as managers grow perfectly patient
<!-- YW5zOjM= -->
> At $\lambda = 1$ the denominator is $1$, giving $\beta(1-\delta)$; as $\delta \to 1$ the reward goes to zero for any $\lambda > 0$, and as $\lambda \to 0$ it goes to $\beta$, the static bonus. So the effect is worst when quotas adjust fast and managers care about the future, which is the planners' situation on M&R p. 14: managers hide capacity and hoard resources. The claim that a full ratchet gives zero forgets that today's bonus is still paid.
> Ref: Milgrom & Roberts (1992), Ch. 1, p. 14; Ch. 7, p. 232; Aula 1 notes §4
> Similar: Practice plan Aula 1, item 5 (M&R FFT 4.1, p. 119)

P:

Q: Why, in Milgrom and Roberts' account, could neither Ford's organization nor the pre-1921 GM carry Sloan's segmented-market strategy?
- Both lacked capital: the strategy needed new plants for every segment, and only the 1920s bond market could fund them at the scale GM required at that time
- The strategy needed lower unit costs than the Model T's, and only a single dedicated line could deliver them, which neither firm's divisions could operate jointly
- It needed far more decisions and information plus coordination across divisions; Ford's was built for one product run from the top, and old GM had no central direction
- The strategy needed prices set by a central planner for every part, and both firms relied on market prices that could not be checked against their own internal costs
<!-- YW5zOjI= -->
> M&R p. 3: variety meant new designs, dealers, market information and factories per segment, while divisions had to avoid competing too much, share ideas, coordinate R&D and standardize parts. Ford's organization concentrated decisions in Henry Ford; old GM was "a collection of car companies and suppliers operating without any central direction", whose accounting did not even charge divisions for inventories. Hence the multidivisional form: operating autonomy plus central audit and strategy. The unit-cost answer has it backwards: GM could not beat the Model T on cost.
> Ref: Milgrom & Roberts (1992), Ch. 1 "Crisis and Change at General Motors", pp. 2–4
> Similar: M&R FFT 1.1, p. 18

## toyota

Q: Which chain of reasoning matches Milgrom and Roberts' derivation of Toyota's system from its starting position?
- Small scale made buffer stocks costly, so Toyota dropped them; then every step had to be reliable, operators had to fix machines, and suppliers had to be closely linked
- Cheap labour made inventories affordable, so Toyota held large buffers and used them to run its flexible machines at full speed between model changes
- High capital let Toyota buy dedicated machines for each model, so it could redesign often and needed only short-term contracts with many suppliers competing on price
- Long-term supplier contracts came first, and just-in-time followed because suppliers demanded small, frequent orders to protect their own economies of scale
<!-- YW5zOjA= -->
> M&R pp. 4–6 and p. 17: inventory systems have large scale economies Toyota could not reach, so it built just-in-time instead; without buffers, reliability, quick repair by operators, close supplier communication and stable plans had to "substitute for the buffer function of inventories". Toyota had little capital, not the capital for dedicated machines, and lower labour costs alone were no advantage, since many countries had lower ones (p. 4).
> Ref: Milgrom & Roberts (1992), Ch. 1 "Toyota", pp. 4–6; "Patterns of Organizational Success and Failure", p. 17
> Similar: Cabral 3.9 Car parts, p. 62

## cases

Q: The Hudson's Bay Company had half its rival's import costs, yet by about 1810 the North West Company held nearly 80% of the trade. What does the case isolate, and what shows that the lesson was organizational rather than geographic?
- It isolates technology: canoe transport turned out cheaper per pelt than shipping through the bay, and HBC recovered once it bought canoes for its own posts
- It isolates monopoly rights: NWC won by ignoring the royal charter, and HBC recovered once the courts enforced the charter against the Montreal traders
- It isolates recruitment: NWC hired more experienced traders, and HBC recovered only by acquiring NWC's staff through the merger that followed the competition
- It isolates decision rights plus incentives: wintering partners decided on the spot and shared profits, and HBC recovered by copying posts and profit shares
<!-- YW5zOjM= -->
> M&R pp. 6–9: HBC was run from London with lags up to 15 months, flat salaries and flogging; NWC's wintering partners had authority and profit shares. HBC's 1809 owners copied the organization (inland posts, half of profits to field officers, more freedom, new recruits), and its cost advantage then became decisive by 1820, before the merger. The cost advantage never moved; the organization did.
> Ref: Milgrom & Roberts (1992), Ch. 1 "The Hudson's Bay Company" and "The North West Company", pp. 6–9
> Similar: M&R FFT 1.2, p. 18

Q: Salomon Brothers' 1990 reform paid part of each bonus in company stock held in trust for five years. Which assessment matches Milgrom and Roberts' account?
- It removed most of the risk from pay, since stock bought on the open market is less volatile than an individual trader's profit contribution
- It tied pay to the firm's value five years ahead to foster cooperation and a long view, at the cost of undiversified risk in employees' pay
- It raised the firm's capital, since the stock was newly issued to the trust, and investors rewarded the dilution with a higher share price
- It replaced performance evaluation, since bonuses were thereafter computed from the share price alone rather than from each department's profit
<!-- YW5zOjE= -->
> M&R pp. 11–12: the old near piece-rate bonus discouraged sharing information across departments; the reform withheld part of the bonus to buy stock (on the open market, leaving capitalization unchanged) held five years, aiming at cooperation and long-run focus, while adding risk the firm partly offset by buying 15% more stock. The market test: firm value rose by roughly 7–10% on announcement (an empirical magnitude from p. 12).
> Ref: Milgrom & Roberts (1992), Ch. 1 "Salomon Brothers and the Investment Banking Industry", pp. 9–12
> Similar: M&R FFT 1.3, p. 18

## patterns

Q: M&R state that incentives and delegated authority are complements. Which observation from the cases supports that claim most directly?
- Toyota gained from delegation alone, since its operators repaired machines without any change in pay, so delegation does not need incentives to pay off
- Salomon's traders had information and authority but weak incentives, so the 1990 reform shows that incentives substitute for authority rather than complement it
- GM's divisions gained autonomy while the centre kept strategy, so delegation and central control are complements and incentives play no role in the account
- Eastern European reforms that gave managers more discretion without decentralized ownership failed, while NWC paired field authority with profit shares
<!-- YW5zOjM= -->
> M&R p. 17: delegation "is of little use unless the decision makers share the organization's objectives", and incentives matter most "when more initiative is expected". Their evidence runs both ways: NWC both relied on traders' judgment and made them partners; in Eastern Europe, discretion without decentralized ownership "could not resolve the problems". Each raises the return to the other: that is complementarity, formalized in Quiz 2.
> Ref: Milgrom & Roberts (1992), Ch. 1 "Patterns of Organizational Success and Failure", pp. 16–17
> Similar: M&R FFT 2.4, p. 52 (team pay with team self-organization)

Q: Cabral notes that Toyota's system "involved so many different aspects that it was difficult to pin down what the crucial success factors were". Why does that, combined with M&R's view of fit, make the system hard to copy even for a rival allowed to watch it?
- Because a watcher sees practices but not their interactions, and with complements a practice copied alone may lower profit, so piecemeal imitators reject them
- Because the practices were protected by patents in the 1980s, so a rival could see them but not legally use them until the patents expired in the 1990s
- Because each practice was individually unprofitable in every setting, so Toyota earned its returns from labour costs that an American rival could not reproduce
- Because the system depended on Japanese workers' attitudes, so a rival using its own workforce could not have obtained the same results with the same practices
<!-- YW5zOjA= -->
> Causal ambiguity (Cabral §3.5, p. 57) plus complementarity: value lies in the cross effects, which an observer cannot see practice by practice, and a practice adopted without its complements can lose money (Quiz 3, the valley). The workforce-attitude answer is what NUMMI refutes: the same GM workforce reached Toyota-level productivity under Toyota's system. The unprofitable-everywhere answer confuses "worth less alone" with "unprofitable everywhere".
> Ref: Cabral (2017) §3.5, pp. 56–59; Milgrom & Roberts (1992), Ch. 4, pp. 108–113; Aula 1 notes §3, §8.2
> Similar: Cabral 3.14 Intel, p. 63
