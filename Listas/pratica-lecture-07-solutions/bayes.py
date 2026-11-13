"""Helper for the Lecture 7 check scripts: exact pure-strategy BNE of finite 2-player Bayesian games.

Strategy of player i = tuple of actions, one per type (index = type index). Every type has positive
probability, so ex-ante best responses coincide with interim best responses (Gibbons p. 144-149).
"""
from fractions import Fraction as F
from itertools import product


def strategies(types, actions):
    return list(product(actions, repeat=len(types)))


def exante(i, s, prior, types, u):
    """Expected payoff of player i (0/1) at the strategy pair s = (s1, s2)."""
    tot = F(0)
    for (t1, t2), pr in prior.items():
        a = (s[0][types[0].index(t1)], s[1][types[1].index(t2)])
        tot += pr * u(i, a[0], a[1], t1, t2)
    return tot


def pure_bne(types, actions, prior, u):
    """All pure BNE as (s1, s2); also returns the ex-ante payoff table."""
    S = [strategies(types[0], actions[0]), strategies(types[1], actions[1])]
    U = {(s1, s2): (exante(0, (s1, s2), prior, types, u), exante(1, (s1, s2), prior, types, u))
         for s1 in S[0] for s2 in S[1]}
    out = []
    for s1, s2 in U:
        if all(U[(s1, s2)][0] >= U[(x, s2)][0] for x in S[0]) and \
           all(U[(s1, s2)][1] >= U[(s1, y)][1] for y in S[1]):
            out.append((s1, s2))
    return out, U


def interim_ok(i, s, prior, types, actions, u):
    """Interim check: each type of i plays a best reply (conditional on own type) to the other's s."""
    for ti, t in enumerate(types[i]):
        def val(a):
            tot = F(0)
            for (t1, t2), pr in prior.items():
                if (t1, t2)[i] != t:
                    continue
                other = s[1 - i][types[1 - i].index((t1, t2)[1 - i])]
                acts = (a, other) if i == 0 else (other, a)
                tot += pr * u(i, acts[0], acts[1], t1, t2)
            return tot
        if val(s[i][ti]) < max(val(a) for a in actions[i]):
            return False
    return True
