---
quiz: "Topic T13 · Hard conceptual quiz — Collusion and price wars"
tags:
  monitor: "Monitoring, transparency and price wars on the path"
  structure: "Market structure, asymmetries and the effective discount factor"
  practices: "Facilitating practices and why collusion is rarer than predicted"
---

## monitor

Q: $n$ identical Bertrand firms with constant marginal cost collude on the monopoly price under grim strategies with discount factor $\delta$, but a secret price cut is detected only $k \ge 1$ periods after it starts, so the cheater can undercut for $k$ periods before the price war begins. When is collusion sustainable?
- Iff $\delta \ge 1 - 1/n$, as with immediate detection, since the price war that eventually follows is permanent and so dwarfs any finite run of deviation profits
- Iff $\delta \ge 1 - k/n$, since each period of undetected cheating adds one more share of the monopoly profit to the gain, set against the same punishment
- Iff $\delta^k \ge 1/n$, since the deviator collects the whole monopoly profit for $k$ periods, and the cartel's share must cover each of them in present value
- Iff $\delta^k \ge 1 - 1/n$, since the cheater collects the whole monopoly profit for $k$ periods, so the lag acts like replacing $\delta$ by $\delta^k$
<!-- YW5zOjM= -->
> Right: conforming is worth $\frac{\pi_M/n}{1-\delta}$; cheating yields $\pi_M$ in each of the $k$ undetected periods and zero afterwards, $\pi_M\frac{1-\delta^k}{1-\delta}$. The condition $\frac1n \ge 1 - \delta^k$ is the immediate-detection condition with $\delta^k$ in place of $\delta$: slow detection is equivalent to less patience. Wrong: the first option ignores that the deviation gain grows with $k$; the second adds whole shares rather than discounted monopoly profits; the third inverts the inequality ($k = 1$ would give $\delta \ge 1/n$, not $1 - 1/n$).
> Ref: MWG (1995), §12.D, the time needed to detect a deviation (p. 403); Cabral (2017), §9.1 (pp. 218–222) and §9.2, secret price cuts (pp. 222–224); `Resolucao/homework-lecture-05.pdf`, item 5, point 3
> Similar: Cabral (2017), Exercise 9.19, p. 245

Q: In 1993 the Danish competition authority began to publish the transaction prices of individual ready-mixed concrete firms, so that buyers could shop around. Prices became less dispersed and rose on average. Which repeated-game mechanism explains this?
- Published prices let buyers compare offers, which raised demand at the cheapest firms and let them raise prices, since a firm facing more buyers can charge more
- Published prices made secret discounts impossible, so any price cut was seen at once and punished, which raised the value of collusion over cheating
- Published prices revealed each firm's costs to its rivals, which removed the private information that had kept the cartel from agreeing on a common price
- Published prices told buyers the market was collusive, so they stopped searching, which removed the competitive pressure that had kept prices near cost
<!-- YW5zOjE= -->
> Right: collusion is limited by the gain from cutting price secretly; once every transaction price is public, a cut is detected at once, the deviation gain shrinks to one period, and the collusive price becomes sustainable. Cabral reads the episode exactly so: transparency meant to protect buyers facilitated coordination. Wrong: more informed buyers make demand more elastic, which pushes prices down, not up; prices reveal little about costs, and the problem was enforcement, not agreement; and buyer search was what the policy encouraged, not what it ended.
> Ref: Cabral (2017), §9.3, the transparency paragraph (p. 231) and Box 9.6 (p. 232); §9.2 on secret price cuts (pp. 222–224)

Q: Cartel members observe only a market price that depends on their outputs and on an unobserved demand shock, and a price below a trigger level starts a price war. Why does the best such equilibrium use price wars of limited length rather than permanent Nash reversion?
- Because wars start after bad shocks even when nobody cheats, so a permanent war would surely end collusion in finite time, while a limited one deters at less cost
- Because a permanent war would not deter cheating at all, since firms know that a war is caused by demand and not by a rival, so they would ignore the trigger
- Because firms can identify the cheater once the war starts, so a short war aimed at the deviator alone is enough to remove his gain from the secret price cut
- Because the trigger is reached only when someone has cheated, so a short war is enough to restore trust, and a longer war would punish innocent firms needlessly
<!-- YW5zOjA= -->
> Right: in a trigger-price equilibrium no one deviates, yet low prices must still be punished, or each firm would cut secretly and blame demand. Punishment therefore happens by accident, and a permanent war is reached with probability one; a war of limited length keeps the deterrent while returning to collusion, so it yields higher profits. Wrong: the threat does deter, which is why no one cheats on the path; the cheater cannot be identified, which is the whole problem; and the trigger is hit by bad luck, not only by cheating.
> Ref: Cabral (2017), §9.2, the three candidate policies (pp. 223–224) and Box 9.2; Gibbons (1992), §2.3.C, Green and Porter (pp. 106–107); Tadelis (2013), §10.4 (pp. 203–204)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 10, p. 310

## structure

Q: Two Bertrand firms have constant marginal costs $c_1 < c_2$, with $c_2$ below firm 1's monopoly price. Why is collusion harder to sustain than between two firms with equal costs, whatever the profit split?
- Because the joint-profit-maximizing cartel has both firms price at $c_2$, which leaves firm 1 a margin too small to be worth protecting against a deviation
- Because firm 2 cannot punish firm 1 at all, since any price below $c_2$ is a loss for firm 2, so firm 1 can always undercut its partner with impunity
- Because the efficient cartel leaves firm 2 no sales, so it undercuts at any $\delta$, while equal prices tempt firm 1, whom firm 2 can punish only weakly
- Because firms with different costs value the future differently, the low-cost firm being more patient, so both discount factors cannot exceed the cutoff $1/2$
<!-- YW5zOjI= -->
> Right: joint profit is maximized with firm 1 at its monopoly price and firm 2 selling nothing, but then firm 2 has no stake in the cartel and undercuts whatever $\delta$ is. Giving firm 2 a share by pricing equally makes firm 1's margin, hence its gain from cutting, large, while firm 2's harshest punishment, pricing at its own cost $c_2$, still leaves firm 1 a profit. Agreeing on the split is an extra strain, as in the bromide cartel. Wrong: the cartel prices at firm 1's monopoly price, not at $c_2$; firm 2 can punish, by pricing down to $c_1$, but only at a loss to itself, so the punishment is weak rather than absent; cost differences say nothing about discount factors.
> Ref: Cabral (2017), §9.3, market structure and footnote i (pp. 227–228); `Resolucao/homework-lecture-05.pdf`, item 5, point 5

Q: Two firms meet in two markets. In market 1 firm 1 has the lower marginal cost, in market 2 firm 2 does, and each market on its own is a Bertrand duopoly. Why can contact across the two markets sustain collusion that neither market sustains alone?
- Because the deviation gain and the punishment both double, which halves the discount factor needed relative to one market, as in the case of identical markets
- Because each firm can leave the other its own market at monopoly prices, and a cut in one market is deterred by retaliation in the market the cheater leads
- Because meeting in two markets doubles the frequency of interaction, which raises the effective discount factor exactly as more frequent price revisions would
- Because a firm that deviates in one market reveals its costs in the other, so the rival can match its price there and remove the advantage that made cheating pay
<!-- YW5zOjE= -->
> Right: alone, each market's efficient cartel leaves the high-cost firm nothing to lose, so it undercuts. Together, each firm's stake in the market it leads becomes the hostage that keeps it from invading the other's: a cut in market 1 by firm 2 is answered by a price war in market 2, where firm 2 earns its monopoly profit. Wrong: with identical markets, gain and punishment double together and the cutoff stays at $1/2$, so contact helps only when the markets differ; contact across markets does not change the timing of interaction; and costs are not revealed by prices in this model.
> Ref: Cabral (2017), §9.3, multimarket contact (pp. 228–229), Boxes 9.3–9.4 (pp. 229–230)
> Similar: Cabral (2017), Exercise 9.18, p. 245

Q: A cartel member runs into financial trouble, so its chance of leaving the industry soon rises sharply. Write the effective discount factor as $\delta = (1+g)(1-h)/(1+r/f)$, with $g$ the growth of demand, $h$ the hazard that the firm's market ends for it, $r$ the interest rate and $f$ the frequency of price revisions. Why may this firm start a price war, although the war hurts it too?
- Because its higher exit hazard raises $g$, the growth it expects in the market share it can grab before leaving, which makes deviating more attractive
- Because its distress raises $r/f$, so it reprices less often, and a firm that reprices less often becomes the natural price leader in a downturn
- Because a firm close to exit cannot be punished at all once it leaves, so the rivals' threat is void for it whatever its $\delta$, which no cartel design can fix
- Because its higher exit hazard $h$ lowers its own $\delta$, possibly below the cutoff, so a punishment in periods it may not survive no longer deters it
<!-- YW5zOjM= -->
> Right: the punishment bites only in periods the firm is still in the industry, so a higher $h$ lowers its effective $\delta$; once that falls below the cutoff, deviating pays even though a war follows. Cabral quotes an airline executive: fares are dictated by the financially troubled. Wrong: $h$ and $g$ are different ingredients, and a higher hazard does not raise growth; repricing frequency is a feature of the market, not of one firm's balance sheet; and a firm that may exit can still be punished in the periods before it does, so the threat is weakened, not void.
> Ref: Cabral (2017), §9.1, eq. (9.5) (pp. 219–220) and §9.2, price wars started by weak firms (pp. 225–227)

## practices

Q: A seller adopts a most-favoured-customer clause: if it ever sells below its list price, every customer of the past six months is refunded the difference. Why can such a clause, presented as protecting buyers, raise prices in a repeated oligopoly?
- It makes a price cut costly on all recent sales, not just on the new ones, which lowers the gain from cheating and so relaxes the cartel's constraint
- It raises buyers' willingness to pay, since they no longer fear paying more than others, which shifts demand out and lets every firm charge more at the same margin
- It makes the punishment harsher, since a firm that deviates must later refund its customers, which lowers its profits during the price war that follows
- It reveals each firm's costs to its rivals through the refunds, which removes the asymmetric information that would otherwise make the cartel unstable
<!-- YW5zOjA= -->
> Right: the clause attaches a refund on past sales to any price cut, so the one-period gain from deviating, the numerator of the cartel's cutoff, falls; the collusive price becomes easier to sustain. GE and Westinghouse used price books with such clauses from 1963 to 1975, with stable, identical prices, until the Department of Justice stopped them. Wrong: the effect runs through the deviation gain, not through demand; the refund falls in the period of the cut, not in the war that follows; and refunds reveal prices, not costs.
> Ref: Cabral (2017), §9.3, institutional factors (pp. 230–231) and Box 9.5 (p. 231)

Q: Two Bertrand duopolists with equal constant marginal cost both guarantee to match any lower price a customer finds at the rival. What does this do to the discount factor needed to sustain the monopoly price $p^M$?
- It raises it above $1/2$, since a matched price cut spreads the deviator's gain over both firms' customers and so makes deviating more attractive than before
- It leaves it at $1/2$, since the guarantee changes only how a price cut is shared, while the deviation gain and the price-war punishment stay the same
- It removes the need for patience: an undercut is matched at once and only lowers both prices, so $(p^M, p^M)$ is a Nash equilibrium of the one-shot game
- It lowers it to $1/4$, since the guarantee halves the deviation gain, which now lasts only until the rival matches, while the punishment is unchanged
<!-- YW5zOjI= -->
> Right: with matching, a firm that undercuts to $p < p^M$ does not win the market; it keeps half of it at the lower price, earning $\pi(p)/2 < \pi(p^M)/2$. No price cut pays even once, so the monopoly price is a stage equilibrium and needs no repeated-game support, for any $\delta$; Cabral's exercise shows that any price between cost and $p^M$ can be a Nash equilibrium. Wrong: the matched cut gives the deviator no extra customers, so the gain falls rather than rises; the deviation gain does not stay the same, it disappears; and nothing is halved, it is removed.
> Ref: Cabral (2017), §9.3, institutional factors (p. 231) and Exercise 9.16 (pp. 244–245)
> Similar: Cabral (2017), Exercise 9.16, pp. 244–245

Q: How does spare capacity affect the sustainability of tacit collusion among price-setting firms?
- It always helps collusion, since spare capacity lets every firm punish a deviator harder by flooding the market, and a harsher stick lowers the cutoff
- It always hurts collusion, since a firm with spare capacity can serve the whole market after a price cut, which raises the gain from cheating for every member
- It does not matter in the repeated game, since the grim-trigger cutoff for Bertrand competition, $1 - 1/n$, depends only on the number of firms
- Its effect is ambiguous: spare capacity in rivals' hands makes punishment harsher, while spare capacity in a cheater's hands makes cheating more profitable
<!-- YW5zOjM= -->
> Right: capacity enters both sides of the cartel's constraint. Rivals able to flood the market can impose a harsh price war, raising the loss from deviating; a would-be cheater able to serve the whole market at a slightly lower price gains more from deviating. Which effect dominates depends on who holds the capacity; collusion is easiest when capacities are similar and matched to cartel output. Wrong: the first two options each keep one side of the trade-off; the $1 - 1/n$ cutoff assumes no capacity constraints at all, so it cannot answer the question.
> Ref: `Resolucao/homework-lecture-05.pdf`, item 5, point 7; Cabral (2017), §9.1, the no-capacity-constraint assumption of the model (p. 218)

Q: With an annual interest rate of 10% and monthly price revisions, Cabral's effective discount factor implies that up to about 121 symmetric Bertrand firms could sustain the monopoly price. Which explanation of why actual collusion is far rarer is consistent with the repeated-game model itself?
- A permanent price war is not credible, since after a deviation all firms gain by renegotiating back to collusion, and foreseeing this removes the deterrent
- Firms are not patient enough, since a 10% interest rate gives a monthly discount factor far below the cutoff $1 - 1/n$ for any industry with several firms
- The model assumes that firms know the monopoly price, while in practice demand is unknown, so firms cannot agree on any price to collude on at all
- Collusion on the monopoly price is not an equilibrium with more than two firms, since the Bertrand cutoff of $1/2$ is derived only for a duopoly
<!-- YW5zOjA= -->
> Right: grim punishments are Pareto-dominated by a return to collusion, so after a deviation everyone, the deviator included, prefers to "let bygones be bygones"; if that is expected, the threat loses its force. Cabral's other answers are antitrust, turnover (a high hazard $h$) and imperfect observation of prices. Wrong: monthly, $\delta = 1/(1 + 0.1/12) \approx 0.992$, and $1 - 1/n \le 0.992$ holds up to $n = 121$, so patience is not the problem; demand uncertainty is not among the model's mechanisms; and the $n$-firm cutoff $1 - 1/n$ is exactly what produces the 121.
> Ref: Cabral (2017), §9.1, "why don't firms collude more often?" (pp. 221–222); Gibbons (1992), renegotiation (p. 111)
