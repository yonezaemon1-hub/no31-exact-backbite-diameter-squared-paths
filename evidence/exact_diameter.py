"""Exact-diameter working theorem and certificates, 2026-10-21.

Depends only on the supplied Python standard-library model.
Internal proof; external independent proof audit and novelty unresolved.
Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
"""
from __future__ import annotations

from backbite_model import ceil_twice_sqrt, core_cycle, corner_extremum, deltas, root_distance


def diameter_formula(n):
    if n < 3:
        raise ValueError("The working theorem is stated for n >= 3")
    if n < 10:
        return (0, 0, 0, 1, 3, 3, 5, 6, 7, 8)[n]
    return corner_extremum(n)


def deficit(n):
    assert n >= 10
    return 2*n-corner_extremum(n)


def diameter_witness(n):
    """Return a normal form at distance D_n from the natural-order path.

    For n>=10, the integer gap construction in Theorem B gives the witness
    without enumerating Hamiltonian paths or the reconfiguration graph.
    """
    assert n >= 10
    choices = []
    for t in range(3):
        N = n-2*t
        if N < 12:
            m = (2, 2, 2, 3, 3, 3)[N-6]
        else:
            m = ceil_twice_sqrt(N)//2
        assert m >= 1 and 3*m <= N
        v, rem = divmod(N, m)
        middle = [v+1]*rem + [v]*(m-rem)
        gaps = middle if t == 0 else ([2]+middle if t == 1 else [2]+middle+[2])
        swaps, total = [], 0
        for gap in gaps[:-1]:
            total += gap
            swaps.append(total-1)
        code = (0, n-1, tuple(swaps))
        choices.append((root_distance(n, code), code))
    value, code = max(choices)
    assert value == diameter_formula(n)
    return code


def cycle_edges(n):
    c = core_cycle(n)
    return tuple(tuple(sorted((c[i], c[(i+1) % n]))) for i in range(n))


def edge_projection(n, path):
    """Count actual noncycle edges; return indices of missing cycle edges."""
    ce = cycle_edges(n)
    pe = {tuple(sorted(e)) for e in zip(path, path[1:])}
    return len(pe-set(ce)), frozenset(i for i, e in enumerate(ce) if e not in pe)


def height(n, code):
    a, b, swaps = code
    return b-a-2-2*len(swaps)+sum(deltas(n, code))+int(b-a == 1)


def sweep_parameters(n, source, target):
    a, b, S = source
    c, d, T = target
    points = sorted(set(S) | set(T))
    A, B = max(a, c), min(b, d)
    C = n-1-B
    fold = a+c+(n-1-b)+(n-1-d)
    cuts = []
    for j in range(len(points)+1):
        h = max(A, points[j-1]+1) if j else A
        z = min(B, points[j]) if j < len(points) else B
        cuts.append((z-h+1, h, z, j))
    G, h, z, j = max(cuts)
    u, v = len(S)+len(T), len(points)
    delta = sum(deltas(n, source)) + sum(deltas(n, target))
    tl, tr = int(1 in points), int(n-3 in points)
    t = tl+tr
    excess = A+C-tl*min(A, 2)-tr*min(C, 2)
    sweep_bound = 2*n-fold-2*u-2*G+delta if G >= 3 else None
    return dict(A=A, B=B, C=C, fold=fold, G=G, h=h, z=z, split=j,
                u=u, v=v, delta=delta, t_left=tl, t_right=tr, t=t,
                excess=excess, sweep_bound=sweep_bound)


def core_route_bound(n, qh, qj, mh, mj):
    """Explicit projection-set route upper bound using core rotations."""
    if mh & mj:
        return qh+qj
    gap = min(min((i-j) % n, (j-i) % n) for i in mh for j in mj)
    return qh+qj+gap


def verify_integer_reduction(n, source, target):
    """Check the exact inequalities of the analytic n>=16 proof for a pair.

    This is finite falsification support, not a replacement for PROOF.md.
    """
    assert n >= 16
    p = sweep_parameters(n, source, target)
    qsum = height(n, source)+height(n, target)
    L = diameter_formula(n)
    assert L >= n+2
    if p['G'] < 3:
        assert p['fold'] >= n-2*p['u']-2
        assert qsum <= n <= L
        return 'core_no_clearance'
    assert p['fold'] >= p['excess'] >= 0
    if p['u'] == 0:
        assert p['sweep_bound'] <= n-3 <= L
        return 'no_swaps'
    m = p['v']+1-p['t']
    assert m >= 1
    reduced_n = n-p['excess']
    assert reduced_n-2*p['t'] <= m*p['G']
    assert p['delta'] <= p['u']
    assert 2*p['u']-p['delta'] >= 2*p['v']-p['t']
    if reduced_n >= 10:
        assert deficit(n) <= p['excess']+deficit(reduced_n)
        assert p['fold']+2*p['u']+2*p['G']-p['delta'] >= deficit(n)
        assert p['sweep_bound'] <= L
        return 'clipped_capacity'
    assert p['fold'] >= n-9
    assert qsum <= n+3-p['u'] <= n+2 <= L
    return 'core_short_reduction'
