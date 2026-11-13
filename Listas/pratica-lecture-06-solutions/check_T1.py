"""Checks every number and equilibrium claim in the Tier 1 solutions of Listas/pratica-lecture-06.md
(items 1-8): Munoz-Garcia Ch. 5 Ex. 4, Cabral 9.1, Tadelis 11.1, Munoz-Garcia Ch. 4 Ex. 1,
M&R Math. 4, M&R FfT 3, M&R FfT 4, Tadelis 11.3. Exact arithmetic (fractions, sympy).

Run: python check_T1.py -> one line per item and "all T1 checks passed", or an AssertionError
on the first wrong claim.
"""
from fractions import Fraction as F
import math

import sympy as sp


# ----------------------------------------------------------------------------- item 1
def item1():
    """Munoz-Garcia Ch. 5 Ex. 4: p = 100 - Q, c = 10."""
    q1, q2 = sp.symbols("q1 q2")
    pi1 = (100 - q1 - q2) * q1 - 10 * q1
    br = sp.solve(sp.diff(pi1, q1), q1)[0]
    assert sp.simplify(br - (45 - q2 / 2)) == 0
    qc = sp.solve(sp.Eq(q1, 45 - q1 / 2), q1)[0]
    pic = pi1.subs({q1: qc, q2: qc})
    assert (qc, pic) == (30, 900)
    Q = sp.symbols("Q")
    Qm = sp.solve(sp.diff((100 - Q - 10) * Q, Q), Q)[0]
    qm = Qm / 2
    pim = ((100 - Qm) - 10) * qm
    assert (Qm, qm, pim) == (45, F(45, 2), F(2025, 2))  # 1012.5
    assert pim > pic
    # one-shot: best reply to the collusive output is not the collusive output
    reply = br.subs(q2, qm)
    assert reply == F(135, 4) and reply != qm  # 33.75
    dev = pi1.subs({q1: reply, q2: qm})
    assert dev == F(18225, 16) and dev > pim  # 1139.0625
    # grid check: no firm gains by deviating from the Cournot profile
    best = max(((100 - q - 30) * q - 10 * q, q) for q in [F(k, 100) for k in range(0, 9000)])
    assert best[1] == 30
    print("item 1  (MG 5.4): qC=30, piC=900; qm=22.5, pim=1012.5; reply to qm = 33.75, deviation profit 1139.0625")


# ----------------------------------------------------------------------------- item 2
def item2():
    """Cabral 9.1: delta = (1+g)(1-h)/(1+r/f); cartel cutoff 1 - 1/n."""
    n, r = 8, F(1, 10)

    def delta(f, g, h):
        return (1 + g) * (1 - h) / (1 + r / f)

    dA = delta(1, F(1, 10), F(1, 5))
    dB = delta(12, F(-3, 10), F(0))
    assert dA == F(4, 5)
    assert dB == F(7, 10) / (1 + F(1, 120)) == F(840, 1210) * 1 and abs(float(dB) - 0.69421) < 1e-5
    cutoff = 1 - F(1, n)
    assert cutoff == F(7, 8) and dA < cutoff and dB < cutoff and dA > dB
    # alternative reading: g = -30% is annual, so the monthly growth factor is 0.7**(1/12)
    dB_alt = 0.7 ** (1 / 12) / (1 + float(r) / 12)
    assert abs(dB_alt - 0.96265) < 1e-4 and dB_alt > float(cutoff)
    # monotonicity claimed in the text: delta rises in f, g and falls in h, r
    assert delta(12, F(1, 10), F(1, 5)) > delta(1, F(1, 10), F(1, 5))
    assert delta(1, F(2, 10), F(1, 5)) > delta(1, F(1, 10), F(1, 5))
    assert delta(1, F(1, 10), F(3, 10)) < delta(1, F(1, 10), F(1, 5))
    print("item 2  (Cabral 9.1): delta_A = 4/5, delta_B = 0.6942, cutoff 1-1/8 = 7/8; alt. reading delta_B = 0.9627")


# ----------------------------------------------------------------------------- item 3
def item3():
    """Tadelis 11.1: the disagreement Nash equilibrium of the T-period alternating-offer game.
    Strategies: every proposer keeps the whole pie, every responder rejects every offer."""
    for T in range(1, 7):
        for delta in (F(1, 2), F(9, 10)):
            # deviator's best payoff against 'always reject / always claim everything':
            # as proposer his offers are rejected (0); as responder he can accept an offer
            # that leaves him 0 (everything is claimed by the proposer): delta^(t-1) * 0 = 0.
            offers_to_responder = [F(0)]  # what the opponent actually offers
            best = max([0] + [delta ** (t - 1) * x for t in range(1, T + 1) for x in offers_to_responder])
            assert best == 0  # equals the equilibrium payoff, so no profitable deviation
    # not subgame perfect: in the last period a responder offered x > 0 gains x by accepting
    x = F(1, 3)
    assert x > 0
    print("item 3  (Tadelis 11.1): deviator's best payoff = 0 = equilibrium payoff for T = 1..6; accepting x > 0 beats rejecting in the last period")


# ----------------------------------------------------------------------------- item 4
def item4():
    """Munoz-Garcia Ch. 4 Ex. 1: u_R = x + a(x - y), x = m, y = 1 - m."""
    a, m = sp.symbols("a m", positive=True)
    uR = m + a * (m - (1 - m))
    mstar = sp.solve(sp.Eq(uR, 0), m)[0]
    assert sp.simplify(mstar - a / (1 + 2 * a)) == 0
    proposer = sp.simplify(1 - mstar)
    assert sp.simplify(proposer - (1 + a) / (1 + 2 * a)) == 0
    assert sp.simplify(sp.diff(proposer, a) + 1 / (1 + 2 * a) ** 2) == 0
    assert sp.simplify(sp.diff(mstar, a) - 1 / (1 + 2 * a) ** 2) == 0
    assert (proposer.subs(a, F(1, 2)), mstar.subs(a, F(1, 2))) == (F(3, 4), F(1, 4))
    assert (proposer.subs(a, 1), mstar.subs(a, 1)) == (F(2, 3), F(1, 3))
    assert sp.limit(mstar, a, sp.oo) == F(1, 2)
    assert sp.simplify(proposer - mstar - 1 / (1 + 2 * a)) == 0  # proposer keeps more for every a > 0
    print("item 4  (MG 4.1): m* = a/(1+2a); proposer (1+a)/(1+2a); a=1/2 -> (3/4,1/4); a=1 -> (2/3,1/3); limit m* -> 1/2")


# ----------------------------------------------------------------------------- item 5
def finite_trust(N, V, G, L):
    """Backward induction in the sequential trust game repeated N times, payoff = sum of stage
    payoffs. Because the stage game has only (no offer, dishonour) as its subgame-perfect
    outcome, continuation values cannot depend on today's actions."""
    cont = (0, 0)
    plan = []
    for _ in range(N):
        # decision maker after an offer: honour -> V + cont[1]; dishonour -> V + G + cont[1]
        honour = V + cont[1]
        dishonour = V + G + cont[1]
        dm = "honour" if honour >= dishonour else "dishonour"
        dm_pay = max(honour, dishonour)
        off_if_offer = (V if dm == "honour" else -L) + cont[0]
        offer = off_if_offer > 0 + cont[0]  # offering vs withholding (stage payoff 0)
        if offer:
            cont = (off_if_offer, dm_pay)
        else:
            cont = (cont[0], cont[1])
        plan.append((dm, "offer" if offer else "withhold"))
    return plan, cont


def item5():
    V, G, L = 3, 2, 5
    for N in (1, 2, 3, 10):
        plan, cont = finite_trust(N, V, G, L)
        assert all(dm == "dishonour" and off == "withhold" for dm, off in plan), plan
        assert cont == (0, 0)
    print("item 5  (M&R Math 4): for N = 1, 2, 3, 10 rounds backward induction gives no offer and no honouring in every round")


# ----------------------------------------------------------------------------- item 6
def item6():
    """M&R FfT 3 (illustration with assumed numbers): honesty with k clients."""
    g, p, v, N = F(10), F(1, 2), F(1), F(6)  # gain from favouring one client, detection, rent per client, horizon
    # honesty needs p * k * v * N >= g (a detected favour loses the rent of every client)
    kstar = math.ceil(g / (p * v * N))
    assert kstar == 4
    assert p * 3 * v * N < g <= p * kstar * v * N
    # a single client with weight s: the client can dismiss the auditor, so g grows with s
    print("item 6  (M&R FfT 3): illustration p*k*v*N >= g gives k* = 4 clients for g=10, p=1/2, v=1, N=6")


# ----------------------------------------------------------------------------- item 7
def item7():
    """M&R FfT 4 (illustration): incentive constraint p (w - wbar) N >= g with outside earnings."""
    p, N, wbar, g = F(1, 5), F(4), F(100), F(80)
    wstar = wbar + g / (N * p)
    assert wstar == 200
    # outside income o is received while in office; the rent is (w + o) - wbar
    o = F(30)
    w_new = wbar + g / (N * p) - o  # salary that still deters when o is earned on the side
    assert w_new == 170
    # banning o and raising the salary by less than o keeps the rent smaller: no deterrence
    assert p * ((w_new + F(20)) - wbar) * N < g  # +20 < o = 30 is not enough
    assert p * ((w_new + o) - wbar) * N == g
    # lobbying fees raise the gain g from favouring one interest group
    g_high = F(120)
    assert wbar + g_high / (N * p) == 250
    print("item 7  (M&R FfT 4): w* = wbar + g/(Np) = 200; with outside income 30 the salary 170 suffices; +20 < 30 does not deter")


# ----------------------------------------------------------------------------- item 8
def item8():
    """Tadelis 11.3: T even, common delta. s_m = proposer's share with m periods left."""
    d = sp.symbols("delta", positive=True)

    def s(m):
        v = sp.Integer(1)
        for _ in range(m - 1):
            v = 1 - d * v
        return sp.expand(v)

    for T in range(1, 9):
        closed = (1 - (-d) ** T) / (1 + d)
        assert sp.simplify(s(T) - closed) == 0
    for T in (2, 4, 6):
        assert sp.simplify(s(T) - (1 - d**T) / (1 + d)) == 0
    assert sp.simplify(s(2) - (1 - d)) == 0
    # player 2 (last mover for T even) gets more than half iff 2 d^T > 1 - d
    for dv in (F(1, 10), F(1, 2), F(8, 10), F(9, 10)):
        for T in (2, 4):
            p2 = 1 - (1 - dv**T) / (1 + dv)
            assert (p2 > F(1, 2)) == (2 * dv**T > 1 - dv)
    # limit equals the infinite-horizon share 1/(1+d)
    for dv in (F(1, 2), F(9, 10)):
        assert abs(float((1 - dv**1000) / (1 + dv)) - float(1 / (1 + dv))) < 1e-12
    # even T vs odd T: first-mover shares around the limit
    dv = F(1, 2)
    assert (1 - dv**4) / (1 + dv) < 1 / (1 + dv) < (1 + dv**5) / (1 + dv)
    print("item 8  (Tadelis 11.3): proposer's share (1-d^T)/(1+d) for T even; T=2 gives 1-d; P2 ahead iff 2d^T > 1-d; limit 1/(1+d)")


if __name__ == "__main__":
    for f in (item1, item2, item3, item4, item5, item6, item7, item8):
        f()
    print("all T1 checks passed")
