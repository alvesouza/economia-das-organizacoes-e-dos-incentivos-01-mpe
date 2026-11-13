"""Checks every number and equilibrium claim in the Lecture 8 solutions, Tier 1 (items 1-8):
sol-tadelis-15-1, sol-gibbons-4-1, sol-tadelis-15-3, sol-munoz-garcia-9-1, sol-gibbons-4-3,
sol-gibbons-4-4, sol-tadelis-16-5, sol-munoz-garcia-9-2.
Exact arithmetic (fractions). Equilibria are computed by enumeration, not typed in.

Run: python check_T1.py  -> one line per item and "all T1 checks passed", or an
AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

from ne_tools import grid_ne, pure_ne, pure_pbe, simplex

h = F(1, 2)


def span(beliefs, k=0):
    """(min, max) of coordinate k over a list of belief tuples."""
    return (min(b[k] for b in beliefs), max(b[k] for b in beliefs))


# ------------------------------------------------------------------------ tadelis-15-1
# rows A, B, C ; cols L, M, R ; payoffs (P1, P2)
A1 = [[0, 0, 4], [4, 0, 0], [1, 1, 1]]
B1 = [[4, 1, 0], [0, 1, 4], [3, 3, 3]]
assert pure_ne(A1, B1) == {(2, 1)}                           # (C, M) is the only pure NE


def claimed(p, q):
    return ((p == (0, 0, 1) and q[0] <= F(1, 4) and q[2] <= F(1, 4))
            or (p == (h, h, 0) and q == (h, 0, h)))


every = [(p, q) for p in simplex(12, 3) for q in simplex(12, 3) if claimed(p, q)]
assert sorted(grid_ne(A1, B1, 12)) == sorted(every)          # all NE on the 1/12 grid
for mu in simplex(60, 2):                                    # M is never a best reply once reached
    assert not (1 >= 4 * mu[0] and 1 >= 4 * mu[1])
assert 1 < (4 * 1 + 0) / 2 and 1 < (0 + 4 * 1) / 2           # (L+R)/2 beats M at x2 (2>1) and x3 (2>1)
print("tadelis-15-1: unique pure NE (C,M), not PBE (M never optimal); NE = {C, Pr(L),Pr(R)<=1/4} "
      "and (A/2+B/2, L/2+R/2); unique PBE = the mixed one")

# ------------------------------------------------------------------------- gibbons-4-1
A = [[4, 0], [3, 0], [2, 2]]
B = [[1, 0], [0, 1], [2, 2]]
assert pure_ne(A, B) == {(0, 0), (2, 1)}                     # (L,L'), (R,R')
assert [p[0] for p in simplex(60, 2) if (1 - p[0]) >= p[0]][-1] == h     # R' optimal iff p <= 1/2
A = [[1, 1, 4], [4, 0, 3], [2, 2, 2]]
B = [[3, 2, 0], [0, 2, 3], [4, 4, 4]]
assert pure_ne(A, B) == {(2, 1)}                             # (R, M')
ok = [p[0] for p in simplex(60, 2) if 2 >= 3 * p[0] and 2 >= 3 * (1 - p[0])]
assert (min(ok), max(ok)) == (F(1, 3), F(2, 3))              # M' optimal iff p in [1/3, 2/3]
print("gibbons-4-1: (a) NE=SPE (L,L'),(R,R'); PBE (L,L') p=1, (R,R') p<=1/2; "
      "(b) NE=SPE=PBE (R,M') with p in [1/3,2/3]")


# ------------------------------------------------------------------------- tadelis-15-3
def trust(p):
    """P1: L or S. Type N of P2 has (x,y)=(1,0), type J has (0,1). Returns (BNE, PBE)."""
    val = {"D": 1, "T": -1}
    bne, pbe = set(), set()
    for a1 in ("L", "S"):
        for aN, aJ in product("DT", repeat=2):
            u1 = {"L": F(0), "S": p * val[aN] + (1 - p) * val[aJ]}
            if u1[a1] < max(u1.values()):
                continue
            if a1 == "S" and not (aN == "D" and aJ == "T"):
                continue                                     # types move after S: optimal there
            bne.add((a1, aN, aJ))
            if aN == "D" and aJ == "T":
                pbe.add((a1, aN, aJ))
    return bne, pbe


bne, pbe = trust(F(3, 4))
assert bne == {("S", "D", "T"), ("L", "T", "T"), ("L", "T", "D")} and pbe == {("S", "D", "T")}
for k in range(0, 21):                                       # (d): never all BNE are PBE
    b, q = trust(F(k, 20))
    assert ("L", "T", "T") in b and ("L", "T", "T") not in q
assert trust(F(1, 4))[1] == {("L", "D", "T")}
assert trust(F(1, 2))[1] == {("L", "D", "T"), ("S", "D", "T")}   # p=1/2: S gives 2p-1 = 0 = L
print("tadelis-15-3: p=3/4 BNE (S;DT),(L;TT),(L;TD); PBE only (S;DT); (L;TT) is a BNE for "
      "every p in {0,1/20,...,1}, so no p makes all BNE perfect Bayesian")

# --------------------------------------------------------------------- munoz-garcia-9-1
# messages: 0 = L (game ends, (2,0)), 1 = R ; replies after R: 0 = U, 1 = D
nact = [1, 2]
US = [[[2], [3, 1]], [[2], [1, 1]]]                          # [type H, type L][msg][reply]
UR = [[[0], [2, 0]], [[0], [0, 1]]]
res = pure_pbe([h, h], [[0, 1], [0, 1]], nact, US, UR)
d = {(s, c): o for s, c, o in res}
assert set(d) == {((1, 0), (0, 0)), ((0, 0), (0, 1))}        # (R L', U) and (L L', D)
assert span(d[((0, 0), (0, 1))][1]) == (F(0), F(1, 3))
assert max(b[0] for b in d[((0, 0), (0, 1))][1]) == F(1, 3)  # beliefs q = Pr(high | R) <= 1/3
print("munoz-garcia-9-1: PBE (R for H, L' for L; U; q=1) and pooling (L,L'; D; q<=1/3); "
      "no (L,R') separating, no (R,R') pooling")

# ------------------------------------------------------------------------- gibbons-4-3
nact = [2, 2]                                                # messages L=0,R=1; replies u=0,d=1
US = [[[1, 2], [0, 3]], [[0, 3], [1, 2]]]                    # [type][msg][reply]
UR = [[[2, 0], [1, 0]], [[0, 1], [0, 2]]]
res = pure_pbe([h, h], [[0, 1]] * 2, nact, US, UR)
assert [(s, c) for s, c, o in res] == [((1, 1), (0, 1))]     # only RR; u after L, d after R
nu = [b[0] for b in res[0][2][0]]
assert (min(nu), max(nu)) == (F(1, 3), F(1))                 # u after L needs Pr(t1|L) >= 1/3
US3 = [[[1, 1], [0, 0]], [[2, 0], [1, 1]], [[1, 0], [0, 2]]]
UR3 = [[[1, 0], [1, 0]], [[1, 0], [1, 0]], [[1, 0], [0, 1]]]
res = pure_pbe([F(1, 3)] * 3, [[0, 1]] * 3, nact, US3, UR3, n=12)
pools = [(s, c, o) for s, c, o in res if s == (0, 0, 0)]
assert [c for s, c, o in pools] == [(0, 0)]                  # u after L, u after R
offb = pools[0][2][1]
assert offb and all(b[2] <= h for b in offb) and any(b[2] == h for b in offb)   # r3 <= 1/2
print("gibbons-4-3: (a) only pooling PBE RR with u after L (belief >=1/3), d after R; "
      "(b) pooling LLL with u,u and Pr(t3|R)<=1/2")


# ------------------------------------------------------------------------- gibbons-4-4
def classify(US, UR):
    res = pure_pbe([h, h], [[0, 1]] * 2, nact, US, UR)
    return {(s, c): o for s, c, o in res}


US = [[[1, 2], [2, 0]], [[0, 0], [1, 1]]]                    # (a)
UR = [[[1, 0], [2, 0]], [[0, 1], [0, 1]]]
d = classify(US, UR)
sep = {(s, c) for s, c in d if s[0] != s[1]}
pool = {(s, c) for s, c in d if s[0] == s[1]}
assert sep == {((0, 1), (0, 1))}                             # LR; u after L, d after R
assert {s for s, c in pool} == {(1, 1)} and all(c[1] == 0 for s, c in pool)   # RR, u after R
assert {c[0] for s, c in pool} == {0, 1}                     # after L: u or d by belief
US = [[[3, 1], [0, 4]], [[3, 0], [1, 2]]]                    # (b)
UR = [[[0, 1], [0, 1]], [[3, 1], [2, 0]]]
d = classify(US, UR)
sep = {(s, c) for s, c in d if s[0] != s[1]}
pool = {(s, c) for s, c in d if s[0] == s[1]}
assert sep == {((0, 1), (1, 0)), ((1, 0), (0, 1))}           # LR (d,u); RL (u,d)
assert pool == {((0, 0), (0, 0))}                            # LL with u,u
assert max(b[0] for b in d[((0, 0), (0, 0))][1]) == F(2, 3)  # Pr(t1|R) <= 2/3
print("gibbons-4-4: (a) pooling RR, separating LR; (b) pooling LL (u,u; Pr(t1|R)<=2/3), "
      "separating LR and RL")


# ------------------------------------------------------------------------- tadelis-16-5
def drug(R, c, r):
    # messages A=0 (cost c), N=1; replies buy=0, no buy=1; types H, L
    US = [[[R - c, -c], [R, 0]], [[r - c, -c], [r, 0]]]
    UR = [[[1, 0], [1, 0]], [[-1, 0], [-1, 0]]]
    return pure_pbe([h, h], [[0, 1]] * 2, [2, 2], US, UR)


res = drug(10, 6, 3)                                         # R > c > r
assert [(s, c) for s, c, o in res if s[0] != s[1]] == [((0, 1), (0, 1))]   # H adverts; buy iff A
assert {s for s, c, o in res if s[0] == s[1]} == {(1, 1)}    # pooling only on N
res = drug(10, 2, 3)                                         # R > r > c
assert [1 for s, c, o in res if s[0] != s[1]] == []
assert {s for s, c, o in res if s[0] == s[1]} == {(0, 0), (1, 1)}
print("tadelis-16-5: R>c>r separating (A_H,N_L) + pooling on N; R>r>c no separating, "
      "pooling on A and on N")

# --------------------------------------------------------------------- munoz-garcia-9-2
# types H, L ; messages E=0, N=1 ; replies M=0, C=1 ; payoffs (worker, firm)
US = [[[6, 0], [10, 4]], [[3, -3], [10, 4]]]
UR = [[[10, 4], [10, 4]], [[0, 4], [0, 4]]]
d = {(s, c): o for s, c, o in pure_pbe([h, h], [[0, 1]] * 2, [2, 2], US, UR)}
sep = {(s, c) for s, c in d if s[0] != s[1]}
pool = {(s, c) for s, c in d if s[0] == s[1]}
assert sep == {((0, 1), (0, 1))}                             # [EN']: M after E, C after N
assert {s for s, c in pool} == {(1, 1)} and all(c[1] == 0 for s, c in pool)   # [NN'], M after N
assert all(c[0] in (0, 1) for s, c in pool)                  # after E: M or C by belief
print("munoz-garcia-9-2: PBE only [EN'] (M after E, C after N) and pooling [NN'] (M after N); "
      "[NE'] and [EE'] fail")

print("all T1 checks passed")
