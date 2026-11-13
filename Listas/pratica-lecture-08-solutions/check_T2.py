"""Checks every number and equilibrium claim in the Lecture 8 solutions, Tier 2 (items 9-17):
sol-gibbons-4-2, sol-tadelis-15-5, sol-munoz-garcia-9-5, sol-tadelis-16-4, sol-tadelis-16-3,
sol-munoz-garcia-11-5, sol-tadelis-16-6, sol-tadelis-16-8, sol-gibbons-4-16.
Exact arithmetic (fractions). Equilibria are computed by enumeration, not typed in.

Run: python check_T2.py  -> one line per item and "all T2 checks passed", or an
AssertionError on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

from ne_tools import bayes_game, pure_ne, pure_pbe, refine, simplex

h = F(1, 2)

# -------------------------------------------------------------------------- gibbons-4-2
# P1: L, M, R (R ends, (2,2)); P2 after L/M: L' or R'. q = Pr(L'), p = Pr(L | reached)
n = 12
found = []
for a, b, c in simplex(n, 3):
    for q in [F(k, n) for k in range(n + 1)]:
        beliefs = [a / (a + b)] if a + b > 0 else [F(k, n) for k in range(n + 1)]
        uP1 = {"L": 3 * q, "M": 3 * (1 - q), "R": F(2)}
        p1_ok = all(x == 0 or uP1[k] == max(uP1.values()) for k, x in zip("LMR", (a, b, c)))
        for p in beliefs:
            uL, uR = 1 - p, p                                  # P2: L' pays 1-p, R' pays p
            p2_ok = (q == 1 and uL >= uR) or (q == 0 and uR >= uL) or (0 < q < 1 and uL == uR)
            if p1_ok and p2_ok:
                found.append(((a, b, c), q, p))
assert {x[0] for x in found} == {(0, 0, 1)}                  # P1 plays R for sure
assert sorted({x[1] for x in found}) == [F(k, n) for k in range(4, 9)]   # q in [1/3, 2/3]
assert {x[2] for x in found} == {h}                          # belief 1/2 after (the off-path) L, M
# no pure PBE: every pure reply is answered by a deviation to L or M
assert 3 * 1 > 2 and 3 * 1 > 2 and 3 * 0 < 2
print("gibbons-4-2: no pure PBE; unique family P1 plays R, P2 plays L' with q in [1/3,2/3], "
      "belief p=1/2")

# -------------------------------------------------------------------------- tadelis-15-5
# types T(0), W(1); messages S=0, B=1, X=2; replies A=0, F=1 (X: single dummy reply)
nact = [2, 2, 1]
Tt = [[(6, 4), (4, 2)], [(4, 6), (2, 4)], [(10, 0)]]         # (incumbent, entrant) payoffs
Wk = [[(6, -2), (8, -6)], [(4, 0), (2, -6)], [(10, 0)]]
pay = [Tt, Wk]
US = [[[pay[t][m][a][1] for a in range(len(pay[t][m]))] for m in range(3)] for t in range(2)]
UR = [[[pay[t][m][a][0] for a in range(len(pay[t][m]))] for m in range(3)] for t in range(2)]
allowed = [[0, 1], [0, 1, 2]]
rows, cols, A, B = bayes_game([h, h], allowed, nact, US, UR)
bne = {(rows[r], cols[c][:2], A[r][c], B[r][c]) for r, c in pure_ne(A, B)}
assert bne == {((0, 2), (0, 1), 2, 8),                       # (S_T X_W; A after S, F after B)
               ((1, 1), (0, 0), 3, 4), ((1, 1), (1, 0), 3, 4),
               ((1, 2), (0, 0), 3, 7), ((1, 2), (1, 0), 3, 7)}
assert max(b[3] for b in bne) == 8                           # the incumbent's preferred BNE
pbe = pure_pbe([h, h], allowed, nact, US, UR)
assert {(s, c[:2]) for s, c, o in pbe} == {((1, 1), (0, 0)), ((1, 1), (1, 0)),
                                           ((1, 2), (0, 0)), ((1, 2), (1, 0))}
# A strictly dominates F after B for both entrant types: F after B is never sequentially rational
assert Tt[1][0][0] > Tt[1][1][0] and Wk[1][0][0] > Wk[1][1][0]
# after S the incumbent fights iff Pr(W|S) >= 1/2
for mu in simplex(60, 2):
    fight = mu[0] * Tt[0][1][0] + mu[1] * Wk[0][1][0]
    acc = mu[0] * Tt[0][0][0] + mu[1] * Wk[0][0][0]
    assert (fight >= acc) == (mu[1] >= h)
inc = lambda s, c: sum(h * pay[t][s[t]][c[s[t]]][0] for t in range(2))
assert inc((1, 1), (0, 0, 0)) == 4 and inc((1, 2), (0, 0, 0)) == 7
print("tadelis-15-5: 5 pure BNE (incumbent best: S_T X_W with A after S, F after B, payoff 8, "
      "not PBE); PBE = B_T B_W (payoff 4) and B_T X_W (payoff 7), off-path reply to S by belief")

# --------------------------------------------------------------------- munoz-garcia-9-5
# types High(0), Low(1); messages Bet=0 (Call=0, Fold=1), Resign=1 (dummy)
nact = [2, 1]
US = [[[2, 1], [-1]], [[-2, 1], [-1]]]
UR = [[[-2, -1], [1]], [[2, -1], [1]]]
assert pure_pbe([h, h], [[0, 1]] * 2, nact, US, UR, n=60) == []   # no pure PBE at all
# semi-separating: High bets, Low bets w.p. beta, P2 calls w.p. gamma
beta, gamma = F(1, 3), F(2, 3)
mu = h / (h + h * beta)                                      # Bayes: Pr(High | Bet)
assert mu == F(3, 4)
callv = mu * -2 + (1 - mu) * 2
assert callv == -1                                           # P2 indifferent: Call = Fold = -1
assert gamma * -2 + (1 - gamma) * 1 == -1                    # Low indifferent: Bet = Resign = -1
assert gamma * 2 + (1 - gamma) * 1 > -1                      # High strictly prefers Bet
for b2 in (F(0), F(1, 4), F(1, 2), F(1)):                    # uniqueness of beta: mu = 3/4 only
    m2 = h / (h + h * b2)
    assert (m2 * -2 + (1 - m2) * 2 == -1) == (b2 == beta)
print("munoz-garcia-9-5: no pure PBE; semi-separating PBE: High bets, Low bets w.p. 1/3, "
      "P2 calls w.p. 2/3, mu=3/4")

# -------------------------------------------------------------------------- tadelis-16-4
P1 = {"E": {"B": {"H": 4, "L": 0}, "S": {"H": 6, "L": 2}},
      "G": {"B": {"H": -2, "L": -6}, "S": {"H": 4, "L": 0}}}
FM = {"E": {"B": {"H": 6, "L": 4}, "S": {"H": -2, "L": 0}},
      "G": {"B": {"H": 4, "L": 3}, "S": {"H": -4, "L": -1}}}
# payoff table of the exercise, recomputed from wages and productivity
prod = {("E", "B"): (2, 12), ("E", "S"): (0, 4), ("G", "B"): (8, 10), ("G", "S"): (2, 2)}
for (t, m), (cost, y) in prod.items():
    assert P1[t][m] == {"H": 6 - cost, "L": 2 - cost}
    assert FM[t][m] == {"H": y - 6, "L": F(y, 2) - 2}
ms, rs = "BS", "HL"
US = [[[P1[t][m][r] for r in rs] for m in ms] for t in "EG"]
UR = [[[FM[t][m][r] for r in rs] for m in ms] for t in "EG"]
rows, cols, A, B = bayes_game([h, h], [[0, 1], [0, 1]], [2, 2], US, UR)
bne = {("".join(ms[x] for x in rows[r]), "".join(rs[x] for x in cols[c])) for r, c in pure_ne(A, B)}
assert bne == {("BS", "HL"), ("SS", "LL")}
pbe = pure_pbe([h, h], [[0, 1], [0, 1]], [2, 2], US, UR)
assert [(s, c) for s, c, o in pbe] == [((0, 1), (0, 1))]     # E: B, G: S ; H after B, L after S
for pr in [F(k, 20) for k in range(21)]:                     # H after B, L after S for every p
    assert pr * 6 + (1 - pr) * 4 > pr * 4 + (1 - pr) * 3
    assert pr * -2 + (1 - pr) * -4 < pr * 0 + (1 - pr) * -1
print("tadelis-16-4: BNE (BS;HL) and (SS;LL); PBE only (BS;HL); firm's replies dominant at "
      "each information set for every p")

# -------------------------------------------------------------------------- tadelis-16-3
def limit(delta):
    pi = [[6, 8], [1, 5]]                                    # period-1 profit [type][price]
    u2 = [[8, 0], [5, 0]]                                    # incumbent period 2 [type][O, E]
    US = [[[pi[t][m] + delta * u2[t][a] for a in range(2)] for m in range(2)] for t in range(2)]
    UR = [[[0, -2]] * 2, [[0, 1]] * 2]                       # entrant: type L: O 0, E -2; H: O 0, E 1
    return pure_pbe([h, h], [[0, 1]] * 2, [2, 2], US, UR)


one = limit(F(1))
assert ((0, 0), (0, 1)) in [(s, c) for s, c, o in one]       # pooling p_L: O after p_L, E after p_H
pool_pL = [o for s, c, o in one if s == (0, 0)]
assert min(b[1] for b in pool_pL[0][1]) == F(2, 3)           # E after p_H needs Pr(H|p_H) >= 2/3
for k in range(0, 41):
    d = F(k, 40)
    sep = [1 for s, c, o in limit(d) if s == (0, 1)]
    assert bool(sep) == (F(1, 4) <= d <= F(4, 5))            # separating iff 1/4 <= delta <= 4/5
    assert any(s == (1, 1) for s, c, o in limit(d))          # pooling on p_H for every delta
    assert not any(s == (1, 0) for s, c, o in limit(d))      # never the reverse separating
assert 6 + 8 * F(1, 4) == 8 and 5 == 1 + 5 * F(4, 5)         # the two binding incentive constraints
print("tadelis-16-3: pooling p_L at delta=1 (O after p_L, E after p_H, belief>=2/3); "
      "separating iff 1/4<=delta<=4/5; also pooling on p_H for every delta")


# ----------------------------------------------------------------------- munoz-garcia-11-5
def mg115(fE, aE, fI, aI, m, p):
    """sane(0) may Acc(0) or Fight(1); crazy(1) only Fight. Replies Stay(0), Exit(1)."""
    US = [[[2 * aI, aI + m], [aI - fI, m - fI]], [[0, 0], [0, 0]]]
    UR = [[[2 * aE, aE], [aE - fE, -fE]], [[0, 0], [-2 * fE, -fE]]]
    return pure_pbe([p, 1 - p], [[0, 1], [1]], [2, 2], US, UR, n=12)


random.seed(8)
checked = {"sep": 0, "pool": 0}
for _ in range(400):
    fE, aE, fI, aI = (random.randint(1, 6) for _ in range(4))
    m = random.randint(0, 20)
    p = F(random.randint(1, 11), 12)
    res = mg115(fE, aE, fI, aI, m, p)
    lam = F(fE, fE + aE)
    sep = any(s == (0, 1) for s, c, o in res)                # sane accommodates, crazy fights
    pool = any(s == (1, 1) for s, c, o in res)
    assert sep == (m - fI <= 2 * aI)                         # part (b)
    assert pool == (m - fI >= 2 * aI and p <= lam)           # part (c)
    checked["sep"] += sep
    checked["pool"] += pool
assert checked["sep"] > 20 and checked["pool"] > 20
print("munoz-garcia-11-5: separating iff m-f_I<=2a_I; pooling (both fight) iff m-f_I>=2a_I and "
      "p<=f_E/(f_E+a_E) (400 random parameter draws)")

# -------------------------------------------------------------------------- tadelis-16-6
V, thL, thH, pr = F(3), F(1), F(2), F(3, 10)                 # p < 1/2
grid = [F(k, 4) for k in range(0, 41)]                       # papers 0, 1/4, ..., 10


def prof(q, th, tenured):
    return (V if tenured else F(0)) - q / th


def separating_ok(qstar):
    """High publishes qstar, Low publishes 0; dept tenures iff q >= qstar (belief 1 there, else 0)."""
    tenure = lambda q: q >= qstar
    for th, eq in ((thH, qstar), (thL, F(0))):
        if any(prof(q, th, tenure(q)) > prof(eq, th, tenure(eq)) for q in grid):
            return False
    return True


sep_set = [q for q in grid if q > 0 and separating_ok(q)]
assert sep_set == [q for q in grid if V * thL <= q <= V * thH]   # q* in [3, 6]
assert not separating_ok(F(11, 4)) and not separating_ok(F(25, 4))
assert min(sep_set) == V * thL                               # least-cost separating level


def pooling_ok(qbar):
    """Both publish qbar, belief p < 1/2 -> deny; deviations get belief 0 -> deny."""
    for th in (thL, thH):
        if any(prof(q, th, False) > prof(qbar, th, False) for q in grid):
            return False
    return True


assert [q for q in grid if pooling_ok(q)] == [F(0)]          # the only pooling outcome: 0 papers, no tenure
assert 2 * pr - 1 < 0                                        # dept's payoff from tenuring at belief p<1/2
print("tadelis-16-6: pooling only at q=0 (no tenure); separating (0, q*) with q* in [V*thL, V*thH] "
      "(grid check with V=3, thL=1, thH=2); least-cost q*=V*thL")

# -------------------------------------------------------------------------- tadelis-16-8
# types W(0), S(1); messages B=0, Q=1; replies D=0, N=1
pW = F(1, 10)
US = [[[0, 2], [1, 3]], [[1, 3], [0, 2]]]
UR = [[[2, 1], [2, 1]], [[0, 1], [0, 1]]]
rows, cols, A, B = bayes_game([pW, 1 - pW], [[0, 1], [0, 1]], [2, 2], US, UR)
bne = {("".join("BQ"[x] for x in rows[r]), "".join("DN"[x] for x in cols[c]))
       for r, c in pure_ne(A, B)}
assert bne == {("BB", "ND"), ("QQ", "DN")}                      # pure BNE; both are PBE
pbe = pure_pbe([pW, 1 - pW], [[0, 1], [0, 1]], [2, 2], US, UR, n=60)
assert {s for s, c, o in pbe} == {(0, 0), (1, 1)}            # only pooling profiles
poolB = [(c, o) for s, c, o in pbe if s == (0, 0)]
poolQ = [(c, o) for s, c, o in pbe if s == (1, 1)]
assert [c for c, o in poolB] == [(1, 0)]                     # N after B, D after Q
assert min(b[0] for b in poolB[0][1][1]) == h                # Pr(W|Q) >= 1/2
assert [c for c, o in poolQ] == [(0, 1)]                     # D after B, N after Q
assert min(b[0] for b in poolQ[0][1][0]) == h                # Pr(W|B) >= 1/2
keep, drop = refine([pW, 1 - pW], [[0, 1], [0, 1]], [2, 2], US, UR, n=60)
assert {s for s, c in keep} == {(0, 0)} and {s for s, c in drop} == {(1, 1)}   # Quiche pooling fails
# the key identity: gain from B over Q is 2 larger for Surly than for Wimp, any replies
for dB, dQ in product([F(k, 10) for k in range(11)], repeat=2):
    gain = lambda t: (US[t][0][0] * dB + US[t][0][1] * (1 - dB)) - (US[t][1][0] * dQ + US[t][1][1] * (1 - dQ))
    assert gain(1) == gain(0) + 2
print("tadelis-16-8: PBE = pooling Beer (N after B, D after Q, Pr(W|Q)>=1/2) and pooling Quiche "
      "(N after Q, D after B, Pr(W|B)>=1/2); only Quiche pooling fails the intuitive criterion")

# --------------------------------------------------------------------------- gibbons-4-16
nact = [2, 2]                                                # messages L=0,R=1; replies u=0,d=1
US2 = [[[1, 2], [0, 3]], [[0, 3], [1, 2]]]
UR2 = [[[2, 0], [1, 0]], [[0, 1], [0, 2]]]
US3 = [[[1, 1], [0, 0]], [[2, 0], [1, 1]], [[1, 0], [0, 2]]]
UR3 = [[[1, 0], [1, 0]], [[1, 0], [1, 0]], [[1, 0], [0, 1]]]
for tag, (prior, US_, UR_, nn, pool) in {
        "a": ([h, h], US2, UR2, 60, (1, 1)),
        "b": ([F(1, 3)] * 3, US3, UR3, 12, (0, 0, 0))}.items():
    k = len(prior)
    k5, d5 = refine(prior, [[0, 1]] * k, nact, US_, UR_, n=nn, rule="dominated")
    k6, d6 = refine(prior, [[0, 1]] * k, nact, US_, UR_, n=nn, rule="eq-dominated")
    assert pool in {s for s, c in k5}                         # Requirement 5 satisfied
    assert pool not in {s for s, c in k6}                     # Requirement 6 violated
# the dominance tables quoted in the solution
assert max(US2[0][0]) == 2 and max(US2[1][0]) == 3 and 3 > 2 and 2 < 3   # (a): L eq-dominated for t1 only
assert [max(US3[t][1]) for t in range(3)] == [0, 1, 2]       # (b): payoffs from R
assert [min(US3[t][0]) for t in range(3)] == [1, 0, 0]       # (b): worst payoffs from L
print("gibbons-4-16: both pooling PBE satisfy Requirement 5 and violate Requirement 6")

print("all T2 checks passed")
