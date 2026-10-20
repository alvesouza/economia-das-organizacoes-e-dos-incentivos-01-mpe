"""Figures for Lecture 7 (Bayesian games, adverse selection and auctions). ESTIMATED unit.

Run from anywhere:  python Notas/L07/figures/make_figures.py
Writes L07-*.png beside this file. Page numbers are printed pages: Tadelis (2013) Ch. 12-13,
Gibbons (1992) Ch. 3, Mas-Colell-Whinston-Green (1995) Sec. 13.B. Numbers marked "illustrative"
are not in any book (the book states the model in letters only); everything else is the book's.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt


def cournot_private_costs():
    """Gibbons Sec. 3.1.A (pp. 144-146): firm 2's cost is cH w.p. theta, cL w.p. 1-theta.
    Calibration a=10, c=2, cH=3, cL=1, theta=1/2 is illustrative (Gibbons uses letters only)."""
    a, c, cH, cL, th = 10.0, 2.0, 3.0, 1.0, 0.5
    q2H = (a - 2 * cH + c) / 3 + (1 - th) * (cH - cL) / 6
    q2L = (a - 2 * cL + c) / 3 - th * (cH - cL) / 6
    q1 = (a - 2 * c + th * cH + (1 - th) * cL) / 3
    Eq2 = th * q2H + (1 - th) * q2L
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    x = np.linspace(0, 5, 200)
    ax.plot(x, (a - x - cH) / 2, color=C["warn"], label="firm 2, high cost: $q_2=(a-q_1-c_H)/2$")
    ax.plot(x, (a - x - cL) / 2, color=C["good"], label="firm 2, low cost: $q_2=(a-q_1-c_L)/2$")
    # firm 1's best response to the EXPECTED rival quantity: q1 = (a - c - E q2)/2  <=>  E q2 = a - c - 2 q1
    ax.plot(x, a - c - 2 * x, color=C["main"], label="firm 1 vs. $E[q_2]$: $q_1=(a-c-E[q_2])/2$")
    for y, col, lab, ty in [(q2H, C["warn"], "$q_2^*(c_H)$", 1.75), (q2L, C["good"], "$q_2^*(c_L)$", 3.75),
                            (Eq2, C["main"], "$E[q_2^*]$", 2.8)]:
        ax.plot(q1, y, "o", color=col, ms=7)
        ax.annotate(f"{lab} = {y:.3f}", (q1, y), xytext=(3.35, ty), color=col,
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.8))
    # complete-information Cournot points (hollow): firm i produces (a - 2c_i + c_j)/3
    for cj, col in [(cH, C["warn"]), (cL, C["good"])]:
        ax.plot((a - 2 * c + cj) / 3, (a - 2 * cj + c) / 3, "o", mfc="white", mec=col, ms=7, mew=1.8)
    ax.axvline(q1, color=C["ref"], lw=1, ls=":")
    ax.set(xlim=(0, 5), ylim=(0, 5), xlabel="$q_1$", ylabel="$q_2$",
           title="Cournot with a privately known cost: one $q_1$, two $q_2$'s")
    ax.text(0.15, 0.3, "hollow = complete-information Cournot points", color=C["ref"], fontsize=9)
    ax.legend(loc="upper right", fontsize=8.5)
    save(fig, "L07-cournot-private-costs")
    return q1, q2H, q2L


def study_group_thresholds():
    """Tadelis Sec. 12.2.2 (pp. 255-258), eq. (12.5) and Fig. 12.4: BR_i(t_j) = sqrt(c/t_j) if t_j >= c, else 1.
    c = 1/8 is illustrative (Tadelis keeps c general); it puts the BNE threshold at c^(1/3) = 1/2."""
    c = 1 / 8
    t = np.linspace(0.001, 1, 600)
    br = np.where(t >= c, np.sqrt(c / np.maximum(t, c)), 1.0)
    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    ax.plot(t, br, color=C["main"], label=r"$BR_2(\hat\theta_1)$")
    ax.plot(br, t, color=C["hi"], label=r"$BR_1(\hat\theta_2)$")
    ts = c ** (1 / 3)
    ax.plot(ts, ts, "o", color=C["good"], ms=9)
    ax.annotate(rf"BNE: $\hat\theta^*=c^{{1/3}}={ts:.2f}$", (ts, ts), xytext=(12, 8),
                textcoords="offset points", color=C["good"])
    for v, lab in [(c, "$c$"), (c ** 0.5, "$c^{1/2}$")]:
        ax.axvline(v, color=C["ref"], lw=0.9, ls=":")
        ax.text(v + 0.01, 0.03, lab, color=C["ref"])
    ax.set(xlim=(0, 1.02), ylim=(0, 1.05), xlabel=r"threshold $\hat\theta_1$",
           ylabel=r"threshold $\hat\theta_2$", title="Study groups: best-response thresholds ($c=1/8$)")
    ax.legend(loc="upper right")
    save(fig, "L07-study-group-thresholds")
    return ts, br[-1]


def lemons_unravelling():
    """Left: Tadelis Sec. 12.3 (pp. 258-260): seller values 10/20/30, buyer values 14/24/34, prob. 1/3.
    Right: MWG Example 13.B.1 (p. 442): theta ~ U[0,2], home value r = alpha*theta;
    E[theta | alpha*theta <= w] = min(w/(2 alpha), 1). alpha = 0.75 and 0.4 are illustrative."""
    v1 = np.array([10.0, 20.0, 30.0])
    v2 = v1 + 4.0
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.0, 4.4))
    p = np.linspace(10, 40, 3001)
    pool = np.array([v2[v1 <= x].mean() for x in p])      # buyer's value of the pool that accepts p
    a1.plot(p, pool, color=C["main"], drawstyle="steps-post",
            label="buyer's expected value of sellers who accept $p$")
    a1.plot(p, p, color=C["ref"], ls="--", label="price $p$ (45° line)")
    ok = pool >= p
    a1.fill_between(p, 0, 45, where=ok, color=C["good"], alpha=0.15, step="post")
    a1.annotate("BNE prices $[10,14]$:\nonly $L$ trades", (12, 14), xytext=(16, 36),
                textcoords="data", color=C["good"], arrowprops=dict(arrowstyle="->", color=C["good"]))
    for x, lab in zip(v1, "LMH"):
        a1.axvline(x, color=C["ref"], lw=0.8, ls=":")
        a1.text(x + 0.3, 41.5, f"{lab} sells", color=C["ref"], fontsize=9)
    a1.text(20.5, 16.0, "pool $\\{L,M\\}$ worth 19 < 20", color=C["warn"], fontsize=9.5)
    a1.text(30.5, 21.0, "all: 24 < 30", color=C["warn"], fontsize=9.5)
    a1.set(xlim=(8, 40), ylim=(8, 44), xlabel="price offered $p$", ylabel="value",
           title="Tadelis's orange grove: the market unravels to $L$")
    a1.legend(loc="lower right", fontsize=8.5)
    w = np.linspace(0, 2, 400)
    a2.plot(w, w, color=C["ref"], ls="--", label="45° line")
    for alpha, col in [(0.75, C["warn"]), (0.4, C["good"])]:
        a2.plot(w, np.minimum(w / (2 * alpha), 1.0), color=col,
                label=rf"$E[\theta\mid \alpha\theta\leq w]$, $\alpha={alpha}$")
    a2.plot(0, 0, "o", color=C["warn"], ms=8)
    a2.annotate(r"$\alpha>1/2$: only $w^*=0$" "\n(complete unravelling)", (0, 0), xytext=(1.12, 0.3),
                color=C["warn"], arrowprops=dict(arrowstyle="->", color=C["warn"]))
    a2.plot(1, 1, "o", color=C["good"], ms=8)
    a2.annotate(r"$\alpha<1/2$: $w^*=E[\theta]=1$, all hired", (1, 1), xytext=(0.08, 1.22),
                color=C["good"], arrowprops=dict(arrowstyle="->", color=C["good"]))
    a2.set(xlim=(0, 2), ylim=(0, 2), xlabel="wage $w$", ylabel="average productivity of applicants",
           title=r"MWG Example 13.B.1: $\theta\sim U[0,2]$, $r(\theta)=\alpha\theta$")
    a2.legend(loc="upper left", fontsize=8.5)
    save(fig, "L07-lemons-unravelling")
    return pool[np.searchsorted(p, 25.0)], [v2[v1 <= x].mean() for x in (10, 20, 30)]


def double_auction_regions():
    """Gibbons Sec. 3.2.C (pp. 158-163), Figs. 3.2.1 and 3.2.3: trade sets in the (v_s, v_b) square.
    Linear BNE: p_b = 2/3 v_b + 1/12, p_s = 2/3 v_s + 1/4, trade iff v_b >= v_s + 1/4.
    One-price BNE drawn at x = 1/2 (any x in [0,1] is an equilibrium)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.8))
    s = np.linspace(0, 1, 200)
    for ax in (a1, a2):
        ax.fill_between(s, s, 1, color=C["grid"], alpha=0.8, label="efficient trade: $v_b\\geq v_s$")
        ax.plot(s, s, color=C["ref"], lw=1)
        ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="seller's value $v_s$", ylabel="buyer's value $v_b$",
               aspect="equal")
    x = 0.5
    a1.add_patch(plt.Rectangle((0, x), x, 1 - x, color=C["main"], alpha=0.35, label="trade at price $x$"))
    a1.set_title("One-price equilibrium, $x=1/2$ (Fig. 3.2.1)")
    a1.legend(loc="lower right", fontsize=8.5)
    a2.fill_between(s, np.minimum(s + 0.25, 1), 1, where=s <= 0.75, color=C["good"], alpha=0.45,
                    label="trade: $v_b\\geq v_s+1/4$")
    a2.set_title("Linear equilibrium (Fig. 3.2.3)")
    a2.legend(loc="lower right", fontsize=8.5)
    save(fig, "L07-double-auction-regions")
    gains_lin = 9 / 64                                     # closed form, derived in L07-05 Sec. 6
    grid = np.linspace(0, 1, 801)
    VS, VB = np.meshgrid(grid, grid)
    num = np.where(VB >= VS + 0.25, VB - VS, 0).mean()
    return gains_lin, num


def spa_dominance():
    """Tadelis Sec. 13.1.1 (pp. 272-274), Fig. 13.1: payoff of bidding theta vs. b<theta vs. b'>theta
    against the highest rival bid m. theta = 0.6, b = 0.4, b' = 0.8 are illustrative."""
    th, lo, hi = 0.6, 0.4, 0.8
    m = np.linspace(0, 1, 1001)
    u = lambda bid: np.where(m < bid, th - m, 0.0)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.axvspan(0, lo, color=C["grid"], alpha=0.6)
    ax.axvspan(lo, th, color=C["warn"], alpha=0.10)
    ax.axvspan(th, hi, color=C["hi"], alpha=0.10)
    ax.plot(m, u(th), color=C["good"], lw=2.6, label=r"bid $b_i=\theta_i=0.6$ (truthful)")
    ax.plot(m, u(lo), color=C["warn"], ls="--", label=r"underbid $b_i=0.4$")
    ax.plot(m, u(hi), color=C["hi"], ls="-.", label=r"overbid $b_i=0.8$")
    ax.axhline(0, color=C["ref"], lw=0.8)
    for x0, x1, lab in [(0, lo, "region L:\nsame payoff"), (lo, th, "region M:\nunderbid loses\na profitable win"),
                        (th, hi, "overbid wins\nat a loss"), (hi, 1, "region H:\nall lose")]:
        ax.text((x0 + x1) / 2, 0.47, lab, ha="center", va="top", fontsize=8.5, color=C["ink"])
    ax.set(xlim=(0, 1), ylim=(-0.25, 0.65), xlabel=r"highest rival bid $m=\max_{j\neq i} b_j$",
           ylabel=r"payoff $u_i$", title="Second-price auction: bidding $\\theta_i$ is weakly dominant")
    ax.legend(loc="lower left", fontsize=8.5)
    save(fig, "L07-spa-dominance")
    return float(u(th)[500] - u(lo)[500])                   # at m = 0.5 (region M): 0.1


def fpa_bidding():
    """Tadelis Sec. 13.1.3 (pp. 276-279), eq. (13.8): s(theta) = (n-1) theta / n, uniform [0,1].
    Right panel: expected payoff of bid b when the n-1 rivals play (13.8): (min(1, b n/(n-1)))^(n-1) (theta - b).
    theta = 0.8 is illustrative; n = 2 is Gibbons's case (p. 155)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.0, 4.4))
    t = np.linspace(0, 1, 200)
    a1.plot(t, t, color=C["ref"], ls="--", label="second price: $b=\\theta$")
    for n, col in [(2, C["main"]), (3, C["hi"]), (5, C["good"]), (10, C["warn"])]:
        a1.plot(t, (n - 1) * t / n, color=col, label=f"first price, $n={n}$: $b={n - 1}\\theta/{n}$")
    a1.set(xlim=(0, 1), ylim=(0, 1), xlabel=r"value $\theta$", ylabel="bid",
           title="Equilibrium bids: shading falls with $n$")
    a1.legend(loc="upper left", fontsize=8.5)
    th = 0.8
    b = np.linspace(0, th, 801)
    peaks = []
    for n, col in [(2, C["main"]), (5, C["good"])]:
        U = np.minimum(1, b * n / (n - 1)) ** (n - 1) * (th - b)
        a2.plot(b, U, color=col, label=f"$n={n}$")
        bs = (n - 1) * th / n
        Us = (n / (n - 1) * bs) ** (n - 1) * (th - bs)
        a2.plot(bs, Us, "o", color=col, ms=8)
        a2.annotate(f"$b^*={bs:.2f}$, $E[u]={Us:.3f}$", (bs, Us), xytext=(-110, 10),
                    textcoords="offset points", color=col, fontsize=9)
        peaks.append((bs, Us, b[np.argmax(U)]))
    a2.axvline(th, color=C["warn"], lw=1, ls=":")
    a2.text(th - 0.01, 0.38, r"$b=\theta$: payoff 0", ha="right", color=C["warn"], fontsize=9)
    a2.set(xlim=(0, 0.85), ylim=(0, 0.42), xlabel="own bid $b$", ylabel="expected payoff",
           title=r"Value $\theta=0.8$: margin $\times$ probability of winning")
    a2.legend(loc="upper left")
    save(fig, "L07-fpa-bidding")
    return peaks


def revenue_equivalence():
    """Tadelis Sec. 13.1.4 (pp. 279-282), eqs. (13.9)-(13.10): E[highest FPA bid] = E[2nd-highest value]
    = (n-1)/(n+1). Left: the two densities for n = 3; right: the closed form vs. Monte Carlo, n = 2..10."""
    n = 3
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.0, 4.4))
    x = np.linspace(0, 1, 600)
    top = (n - 1) / n
    f1 = np.where(x <= top, n * (n / (n - 1)) ** n * x ** (n - 1), 0.0)   # density of the highest bid
    f2 = n * (n - 1) * (x ** (n - 2) - x ** (n - 1))                       # density of the 2nd-highest value
    a1.plot(x, f1, color=C["main"], label="first price: highest bid, $f^{(1)}_n$")
    a1.plot(x, f2, color=C["hi"], label="second price: 2nd-highest value, $f^{(2)}_n$")
    a1.axvline((n - 1) / (n + 1), color=C["good"], ls="--")
    a1.text(0.69, 2.6, "dashed line:\nboth means\n$=(n-1)/(n+1)$\n$=1/2$", color=C["good"], fontsize=9.5)
    a1.set(xlim=(0, 1), ylim=(0, 4.8), xlabel="price paid", ylabel="density",
           title="$n=3$: different distributions, same mean")
    a1.legend(loc="upper left", fontsize=8.5)
    rng = np.random.default_rng(20261117)
    ns = np.arange(2, 11)
    mc_f, mc_s = [], []
    for k in ns:
        v = rng.random((200_000, k))
        v.sort(axis=1)
        mc_f.append(((k - 1) / k * v[:, -1]).mean())
        mc_s.append(v[:, -2].mean())
    a2.plot(ns, (ns - 1) / (ns + 1), color=C["good"], label="$(n-1)/(n+1)$")
    a2.plot(ns, mc_f, "o", color=C["main"], label="simulated first price")
    a2.plot(ns, mc_s, "x", color=C["hi"], ms=9, mew=2, label="simulated second price")
    a2.set(xlabel="number of bidders $n$", ylabel="expected revenue",
           title="Revenue equivalence, uniform values on $[0,1]$")
    a2.legend(loc="lower right")
    save(fig, "L07-revenue-equivalence")
    means = (np.trapezoid(x * f1, x), np.trapezoid(x * f2, x))
    return means, np.array(mc_f), np.array(mc_s), (ns - 1) / (ns + 1)


if __name__ == "__main__":
    apply()
    q1, q2H, q2L = cournot_private_costs()
    assert abs(q1 - 8 / 3) < 1e-12 and abs(q2H - 13 / 6) < 1e-12 and abs(q2L - 19 / 6) < 1e-12
    assert q2H > (10 - 6 + 2) / 3 and q2L < (10 - 2 + 2) / 3        # Gibbons p. 146: the two inequalities
    assert abs(q1 - 0.5 * ((10 - 4 + 3) / 3 + (10 - 4 + 1) / 3)) < 1e-12   # q1* = average of the CI quantities

    ts, br_at_1 = study_group_thresholds()
    assert abs(br_at_1 - (1 / 8) ** 0.5) < 1e-12                     # BR(1) = c^(1/2), Tadelis p. 258
    assert abs(ts - 0.5) < 1e-12 and abs(ts ** 2 * ts - 1 / 8) < 1e-12   # theta*^3 = c

    p25, pools = lemons_unravelling()
    assert pools == [14.0, 19.0, 24.0] and p25 == 19.0               # Tadelis p. 260: 19 and 24

    g_lin, g_num = double_auction_regions()
    assert abs(g_lin - g_num) < 2e-3 and g_lin < 1 / 6              # 9/64 < 1/6 (efficient)

    assert abs(spa_dominance() - 0.1) < 1e-12

    peaks = fpa_bidding()
    for bs, Us, bgrid in peaks:
        assert abs(bs - bgrid) < 2e-3                               # numerical argmax = (n-1)theta/n
    assert abs(peaks[0][0] - 0.4) < 1e-12 and abs(peaks[0][1] - 0.8 ** 2 / 2) < 1e-12  # E[u] = theta^n/n
    assert abs(peaks[1][1] - 0.8 ** 5 / 5) < 1e-12

    means, mc_f, mc_s, closed = revenue_equivalence()
    assert abs(means[0] - 0.5) < 1e-3 and abs(means[1] - 0.5) < 1e-3
    assert np.allclose(mc_f, closed, atol=4e-3) and np.allclose(mc_s, closed, atol=4e-3)

    here = pathlib.Path(__file__).resolve().parent
    names = ["cournot-private-costs", "study-group-thresholds", "lemons-unravelling",
             "double-auction-regions", "spa-dominance", "fpa-bidding", "revenue-equivalence"]
    assert all((here / f"L07-{s}.png").exists() for s in names)
    print("L07 figures written; all asserts pass")
