"""Figures for Lecture 8 (signaling and perfect Bayesian equilibrium). Estimated unit.

Run from anywhere:  python Notas/L08/figures/make_figures.py
Writes L08-*.png beside this file. Every number is the book's own, cited by printed page:
Tadelis (2013) Ch. 15-16, Milgrom & Roberts (1992) pp. 155-156, Gibbons (1992) Sec. 4.2.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt

apply()


# ---------------------------------------------------------------- tree helpers
def node(ax, xy, label="", col=None, r=0.06):
    ax.add_patch(plt.Circle(xy, r, color=col or C["ink"], zorder=3))
    if label:
        ax.annotate(label, xy, xytext=(0, 9), textcoords="offset points", ha="center",
                    fontsize=10, color=col or C["ink"], fontweight="semibold")


def edge(ax, a, b, label, col=None, lw=1.3, off=(0, 0)):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=col or C["ref"], lw=lw, zorder=1)
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    ax.annotate(label, (mx, my), xytext=off, textcoords="offset points", ha="center",
                va="center", fontsize=9.5, color=col or C["ink"],
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))


def leaf(ax, xy, pay, col=None, dy=-0.17):
    ax.text(xy[0], xy[1] + dy, pay, ha="center", va="top", fontsize=9.5,
            color=col or C["ink"], family="monospace")


def infoset(ax, a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], ls=(0, (4, 3)), color=C["hi"], lw=1.4, zorder=0)


# ---------------------------------------------------------------- 1. entry game
def entry_game():
    """Tadelis Fig. 15.2 (p. 305) and why F is never a best response (p. 310)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw=dict(width_ratios=[1.35, 1]))
    a1.set_axis_off(); a1.set_aspect("equal")
    N, x1, x2 = (0, 3), (-1.6, 2.1), (1.6, 2.1)
    x3, x4 = (-0.8, 1.0), (0.8, 1.0)
    G, W = C["good"], C["warn"]
    edge(a1, N, x1, "C  ($p$)"); edge(a1, N, x2, "W  ($1-p$)")
    node(a1, N, "Nature", C["ref"]); node(a1, x1, "1"); node(a1, x2, "1")
    o1, o2 = (-2.5, 1.0), (2.5, 1.0)
    edge(a1, x1, o1, "O"); edge(a1, x1, x3, "E", G, 2.6)      # (EO, A): type C enters
    edge(a1, x2, o2, "O", G, 2.6); edge(a1, x2, x4, "E")      # type W stays out
    leaf(a1, o1, "0, 2"); leaf(a1, o2, "0, 2", G)
    node(a1, x3, "2"); node(a1, x4, "2"); infoset(a1, x3, x4)
    a1.text(0, 1.13, r"$\mu(x_3)$ vs $1-\mu(x_3)$", color=C["hi"], fontsize=9.5, ha="center")
    for x, fp, ap in [(x3, "-1, -1", "1, 1"), (x4, "-2, 0", "-1, 1")]:
        f, a = (x[0] - 0.45, -0.1), (x[0] + 0.45, -0.1)
        edge(a1, x, f, "F", W); edge(a1, x, a, "A", G, 2.6 if x is x3 else 1.6)
        leaf(a1, f, fp, W); leaf(a1, a, ap, G)
    a1.set_xlim(-3, 3); a1.set_ylim(-0.6, 3.4)
    a1.set_title("Entry with an unknown entrant (Tadelis Fig. 15.2)")
    # player 2's expected payoff at the information set after E, as a function of the belief
    mu = np.linspace(0, 1, 201)
    vA = mu * 1 + (1 - mu) * 1            # A: 1 against C, 1 against W
    vF = mu * (-1) + (1 - mu) * 0         # F: -1 against C, 0 against W
    a2.plot(mu, vA, color=G, label="accommodate A: $1$")
    a2.plot(mu, vF, color=W, label=r"fight F: $-\mu(x_3)$")
    a2.fill_between(mu, vF, vA, color=G, alpha=0.08)
    a2.set(xlabel=r"belief $\mu(x_3)=\Pr\{\theta_1=C\mid E\}$", ylabel="player 2's expected payoff",
           title="F is never a best response (p. 310)", ylim=(-1.3, 1.4), xlim=(0, 1))
    a2.legend(loc="lower left")
    save(fig, "L08-entry-game")
    return float(np.min(vA - vF))         # gap is at least 1 for every belief


# ---------------------------------------------------------------- 2. MBA tree
MBA = {  # (type, message, response): (worker, employer) -- Tadelis Fig. 16.1, p. 321
    ("H", "U", "M"): (10, 10), ("H", "U", "B"): (6, 5), ("H", "D", "M"): (8, 10), ("H", "D", "B"): (4, 5),
    ("L", "U", "M"): (10, 0), ("L", "U", "B"): (6, 3), ("L", "D", "M"): (5, 0), ("L", "D", "B"): (1, 3),
}


def mba_tree():
    """Tadelis Fig. 16.1 (p. 321) with the separating PBE (DU, BM) highlighted (p. 322)."""
    fig, ax = plt.subplots(figsize=(9.6, 5.2))
    ax.set_axis_off(); ax.set_aspect("equal")
    N, H, L = (0, 0), (0, 1.1), (0, -1.1)
    node(ax, N, "", C["ref"])
    ax.text(0.12, -0.05, "Nature", color=C["ref"], fontsize=10, va="center")
    edge(ax, N, H, "H  ($p$)", off=(-22, 0)); edge(ax, N, L, "L  ($1-p$)", off=(-28, 0))
    node(ax, H, "1 (H)"); ax.add_patch(plt.Circle(L, 0.06, color=C["ink"]))
    ax.text(0, -1.38, "1 (L)", ha="center", fontsize=10, fontweight="semibold")
    eq = {("H", "D"), ("L", "U"), ("U", "B"), ("D", "M")}      # (DU, BM)
    pos = {("H", "U"): (-1.8, 1.1), ("H", "D"): (1.8, 1.1), ("L", "U"): (-1.8, -1.1), ("L", "D"): (1.8, -1.1)}
    for (t, m), xy in pos.items():
        src = H if t == "H" else L
        on = (t, m) in eq
        edge(ax, src, xy, m, C["good"] if on else None, 2.6 if on else 1.3)
        node(ax, xy, "", C["ink"], 0.05)
        for r, dy in [("M", 0.45), ("B", -0.45)]:
            sgn = -1 if m == "U" else 1
            end = (xy[0] + sgn * 1.0, xy[1] + dy)
            hit = on and (m, r) in eq
            edge(ax, xy, end, r, C["good"] if hit else None, 2.6 if hit else 1.1)
            w, e = MBA[(t, m, r)]
            ax.text(end[0] + sgn * 0.08, end[1], f"{w}, {e}", ha="right" if sgn < 0 else "left",
                    va="center", fontsize=9.5, family="monospace",
                    color=C["good"] if hit else C["ink"])
    infoset(ax, pos[("H", "U")], pos[("L", "U")]); infoset(ax, pos[("H", "D")], pos[("L", "D")])
    ax.text(-1.8, 0, r"$I_U$: $\mu_U$", color=C["hi"], ha="center", fontsize=10)
    ax.text(1.8, 0, r"$I_D$: $\mu_D$", color=C["hi"], ha="center", fontsize=10)
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-1.9, 1.9)
    ax.set_title("The MBA game (Tadelis Fig. 16.1); green = separating PBE (DU, BM)")
    save(fig, "L08-mba-tree")


def mba_beliefs():
    """Employer's best response vs belief: M iff 10 mu >= 5 mu + 3(1 - mu), i.e. mu >= 3/8 (p. 323)."""
    fig, ax = plt.subplots()
    mu = np.linspace(0, 1, 401)
    vM, vB = 10 * mu + 0 * (1 - mu), 5 * mu + 3 * (1 - mu)
    star = 3 / 8
    ax.plot(mu, vM, color=C["main"], label=r"assign M: $10\mu$")
    ax.plot(mu, vB, color=C["ref"], label=r"assign B: $5\mu+3(1-\mu)$")
    ax.axvline(star, color=C["hi"], ls="--", lw=1.2)
    ax.text(star + 0.01, 8.6, r"$\mu^*=3/8$", color=C["hi"])
    ax.axvspan(0, star, color=C["warn"], alpha=0.08)
    ax.text(0.02, 9.2, r"pooling (UU, BB) needs $\mu_D\leq 3/8$", color=C["warn"], fontsize=9.5)
    pts = [(0.25, 3 + 2 * 0.25, r"$\mu_U=p=1/4$ (pooling): B", C["warn"], (12, -34)),
           (0.0, 3.0, r"$\mu_U=0$ (separating): B", C["good"], (8, 16)),
           (1.0, 10.0, r"$\mu_D=1$ (separating): M", C["good"], (-150, -4))]
    for x, y, lab, col, off in pts:
        ax.plot(x, y, "o", color=col, ms=7, zorder=3)
        ax.annotate(lab, (x, y), xytext=off, textcoords="offset points", color=col, fontsize=9.5)
    ax.set(xlabel=r"employer's belief $\mu=\Pr\{\theta=H\mid$ message$\}$",
           ylabel="employer's expected profit", xlim=(0, 1), ylim=(0, 10.5),
           title="One threshold settles every information set (Tadelis pp. 321-323)")
    ax.legend(loc="center right")
    save(fig, "L08-mba-beliefs")
    return float(np.interp(star, mu, vM - vB))


# ---------------------------------------------------------------- Spence, M&R pp. 155-156
TH, TL, P, CH, CL = 50.0, 20.0, 0.30, 10.0, 20.0   # $/hour; 30% high; cost per unit of education


def spence_separating():
    """Separating interval [ (TH-TL)/CL, (TH-TL)/CH ] = [1.5, 3]; pooling e_p in [0, 0.45]."""
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    e = np.linspace(0, 3.6, 361)
    lo, hi = (TH - TL) / CL, (TH - TL) / CH
    wbar = P * TH + (1 - P) * TL
    ep_max = (wbar - TL) / CL
    ax.plot(e, TL + CL * e, color=C["warn"], label=r"L's indifference through $(0,\theta_L)$: $w=20+20e$")
    ax.plot(e, TL + CH * e, color=C["main"], label=r"H's indifference through $(0,\theta_L)$: $w=20+10e$")
    ax.hlines([TH, TL], 0, 3.6, color=C["ref"], lw=1, ls=":")
    ax.hlines(wbar, 0, 3.6, color=C["hi"], lw=1, ls=":")
    ax.text(3.62, TH, r"$\theta_H=50$", va="center", color=C["ref"])
    ax.text(3.62, TL, r"$\theta_L=20$", va="center", color=C["ref"])
    ax.text(3.62, wbar, r"$\bar w=29$", va="center", color=C["hi"])
    ax.plot([lo, hi], [TH, TH], color=C["good"], lw=6, alpha=0.55, solid_capstyle="butt",
            label=r"separating $e_H\in[1.5,\,3]$")
    ax.plot(lo, TH, "o", color=C["good"], ms=9, zorder=4)
    ax.annotate("least-cost separating\n$e_H=1.5$: H nets 35", (lo, TH), xytext=(40, -95),
                textcoords="offset points", color=C["good"], arrowprops=dict(arrowstyle="->", color=C["good"]))
    ax.plot([0, ep_max], [wbar, wbar], color=C["hi"], lw=6, alpha=0.55, solid_capstyle="butt",
            label=r"pooling $e_p\in[0,\,0.45]$")
    ax.plot(0, TL, "o", color=C["warn"], ms=8, zorder=4)
    ax.set(xlabel="education $e$ (units)", ylabel="wage $w$ (dollars per hour)", xlim=(0, 3.6), ylim=(10, 60),
           title="Spence with M&R's numbers (pp. 155-156)")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "L08-spence-separating")
    return lo, hi, wbar, ep_max


def spence_welfare():
    """Who gains from the signal: H's LCS payoff vs the no-signal pooled wage, against the prior."""
    fig, ax = plt.subplots()
    p = np.linspace(0, 1, 401)
    lcs_H = TH - CH * (TH - TL) / CL                   # 50 - 10 * 1.5 = 35, independent of p
    pool = p * TH + (1 - p) * TL                       # no-signal wage, both types
    pstar = 1 - CH / CL                                # 0.5
    ax.plot(p, np.full_like(p, lcs_H), color=C["good"], label="H, least-cost separating: 35")
    ax.plot(p, np.full_like(p, TL), color=C["warn"], label="L, separating: 20")
    ax.plot(p, pool, color=C["main"], label=r"either type, no signal: $20+30p$")
    ax.axvline(pstar, color=C["hi"], ls="--", lw=1.2)
    ax.text(pstar + 0.01, 22, r"$p^*=1-c_H/c_L=0.5$", color=C["hi"])
    ax.plot(P, P * TH + (1 - P) * TL, "o", color=C["main"], ms=7)
    ax.annotate("M&R: $p=0.3$, $\\bar w=29<35$", (P, 29), xytext=(14, -22), textcoords="offset points",
                color=C["main"], fontsize=9.5)
    ax.fill_between(p, lcs_H, pool, where=pool > lcs_H, color=C["warn"], alpha=0.1)
    ax.text(0.72, 40.2, "H worse off\nwith signaling", color=C["warn"], fontsize=9.5)
    ax.set(xlabel=r"prior $p=\Pr\{\theta=H\}$", ylabel="net payoff (dollars per hour)", xlim=(0, 1), ylim=(15, 52),
           title="The separating outcome does not move with $p$; the pooled wage does")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "L08-spence-welfare")
    return lcs_H, pstar


def intuitive_spence():
    """Pooling at e_p = 0.3 fails the intuitive criterion: deviations in (e', e'') (MWG 13.AA, Tadelis 16.3)."""
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ep = 0.3
    wbar = P * TH + (1 - P) * TL
    uL, uH = wbar - CL * ep, wbar - CH * ep            # 23, 26
    e1, e2 = (TH - uL) / CL, (TH - uH) / CH            # 1.35, 2.4
    e = np.linspace(0, 3.2, 321)
    ax.plot(e, uL + CL * e, color=C["warn"], label=r"L's equilibrium indifference: $w=23+20e$")
    ax.plot(e, uH + CH * e, color=C["main"], label=r"H's equilibrium indifference: $w=26+10e$")
    ax.hlines(TH, 0, 3.2, color=C["ref"], lw=1, ls=":")
    ax.text(0.05, TH + 1, r"best wage any belief can give: $\theta_H=50$", color=C["ref"], fontsize=9.5)
    ax.plot(ep, wbar, "o", color=C["hi"], ms=8, zorder=4)
    ax.annotate(r"pooling $(e_p,\bar w)=(0.3,29)$", (ep, wbar), xytext=(10, -22),
                textcoords="offset points", color=C["hi"])
    ax.plot([e1, e2], [TH, TH], color=C["good"], lw=6, alpha=0.55, solid_capstyle="butt")
    for x, lab in [(e1, "$e'=1.35$"), (e2, "$e''=2.4$")]:
        ax.vlines(x, 10, TH, color=C["ref"], lw=0.8, ls="--")
        ax.text(x, 11, lab, ha="center", fontsize=9.5)
    ax.annotate("L loses here even if paid 50;\nH gains if believed: deviation breaks pooling",
                ((e1 + e2) / 2, TH), xytext=(-40, 36), textcoords="offset points", color=C["good"],
                fontsize=9.5, arrowprops=dict(arrowstyle="->", color=C["good"]))
    ax.set(xlabel="education $e$", ylabel="wage $w$ (dollars per hour)", xlim=(0, 3.2), ylim=(10, 72),
           title="Why every pooling equilibrium fails the intuitive criterion")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "L08-intuitive-criterion")
    return e1, e2


# ---------------------------------------------------------------- limit pricing, Tadelis Sec. 16.2
def limit_pricing():
    """Two-period profits of each incumbent type from first-period output q (pp. 327-332)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.3), sharey=True)
    q = np.linspace(0.5, 3.8, 661)
    H_stay = (3 - q) * q + 2.25          # (5-q-2)q now, monopoly 2.25 next period (no entry)
    L_stay = (4 - q) * q + 4.0           # (5-q-1)q now, monopoly 4 next period
    s_lo, s_hi = (3 + np.sqrt(5)) / 2, 2 + np.sqrt(1.75)     # 2.618, 3.323
    a1.plot(q, H_stay, color=C["main"], label="H imitates and deters entry")
    a1.plot(q, L_stay, color=C["warn"], label="L deters entry")
    a1.axhline(3.25, color=C["main"], ls=":", lw=1.2); a1.text(0.55, 3.35, "H's best with entry: 3.25", color=C["main"], fontsize=9)
    a1.axhline(6.25, color=C["warn"], ls=":", lw=1.2); a1.text(0.55, 6.35, "L's best with entry: 6.25", color=C["warn"], fontsize=9)
    a1.axvspan(s_lo, s_hi, color=C["good"], alpha=0.12)
    a1.text(s_lo + 0.02, 0.4, "separating\n$q_1^L\\in[2.62,3.32]$", color=C["good"], fontsize=9.5)
    a1.set(xlabel="first-period output $q$", ylabel="two-period profit", ylim=(0, 8.5),
           title="Separating: H must not mimic (pp. 327-329)")
    a1.legend(loc="lower left", fontsize=9)
    vH, vL = (13 / 12) ** 2, (19 / 12) ** 2  # Bayesian Cournot profits after pooled entry (p. 331)
    p_lo, p_hi = (4 - np.sqrt(148) / 12) / 2, 23 / 12                  # 1.493, 1.917
    a2.plot(q, (3 - q) * q + vH, color=C["main"], label="H pools (entry, Bayesian Cournot)")
    a2.plot(q, (4 - q) * q + vL, color=C["warn"], label="L pools (entry, Bayesian Cournot)")
    a2.axhline(3.25, color=C["main"], ls=":", lw=1.2); a2.axhline(6.25, color=C["warn"], ls=":", lw=1.2)
    a2.axvspan(p_lo, p_hi, color=C["hi"], alpha=0.14)
    a2.text(p_lo - 0.02, 0.4, "pooling\n$q_1\\in[1.49,1.92]$", color=C["hi"], fontsize=9.5, ha="right")
    a2.set(xlabel="pooled first-period output $q$", title="Pooling: no type deviates (pp. 330-332)")
    a2.legend(loc="lower left", fontsize=9)
    save(fig, "L08-limit-pricing")
    return s_lo, s_hi, p_lo, p_hi


if __name__ == "__main__":
    gap = entry_game()
    assert abs(gap - 1.0) < 1e-12                       # A beats F by at least 1 at every belief
    mba_tree()
    assert abs(mba_beliefs()) < 1e-2                    # M and B tie at mu = 3/8 (p. 323)
    lo, hi, wbar, ep_max = spence_separating()
    assert (lo, hi) == (1.5, 3.0) and abs(wbar - 29) < 1e-12 and abs(ep_max - 0.45) < 1e-12  # M&R p. 155-156
    lcs_H, pstar = spence_welfare()
    assert lcs_H == 35 and pstar == 0.5
    e1, e2 = intuitive_spence()
    assert abs(e1 - 1.35) < 1e-12 and abs(e2 - 2.4) < 1e-12
    s_lo, s_hi, p_lo, p_hi = limit_pricing()
    assert abs(s_lo - 2.618) < 1e-3 and abs(s_hi - 3.323) < 1e-3   # book: 2.62 <= q <= 3.32 (p. 329)
    assert abs(p_lo - 1.493) < 1e-3 and abs(p_hi - 1.917) < 1e-3   # book: 1.493 <= q <= 1.917 (p. 332)
    print("L08 figures written and checked.")
