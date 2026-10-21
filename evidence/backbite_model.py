"""Exact rooted-distance formula and constructive backbite routes.

Research working material, 2026-10-21. Python standard library only.
Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
The arbitrary-pair exact diameter is NOT claimed here.
"""
from __future__ import annotations

from collections import deque
from math import isqrt


def canonical(p):
    p = tuple(p)
    return p if p[0] < p[-1] else p[::-1]


def backbites(p):
    """Actual prefix reversals; no use of the normal-form move model."""
    result = set()
    for q in (p, p[::-1]):
        for k in range(2, len(q)):
            if abs(q[0] - q[k]) <= 2:
                result.add(canonical(q[:k][::-1] + q[k:]))
    return result


def enumerate_paths(n):
    """Host-graph DFS, independent of the normal-form enumeration."""
    host = [tuple(j for j in range(n) if 0 < abs(i-j) <= 2) for i in range(n)]
    answer = []

    def dfs(p, mask):
        if len(p) == n:
            if p[0] < p[-1]:
                answer.append(tuple(p))
            return
        for v in host[p[-1]]:
            if not mask & (1 << v):
                dfs(p + [v], mask | (1 << v))

    for s in range(n):
        dfs([s], 1 << s)
    return answer


def curl(a):
    if a == 0:
        return (0,)
    return tuple(range(a, -1, -2)) + tuple(range(1 if a % 2 == 0 else 0, a+2, 2))


def decode(n, code):
    a, b, swaps = code
    swaps = tuple(swaps)
    assert 0 <= a < b < n
    left = curl(a)
    right = tuple(n-1-x for x in curl(n-1-b))[::-1]
    low, high = left[-1], right[0]
    assert low <= high, code
    assert all(low+1 <= i <= high-2 for i in swaps), code
    assert all(y-x >= 3 for x, y in zip(swaps, swaps[1:])), code
    middle = list(range(low, high+1))
    for i in swaps:
        middle[i-low], middle[i+1-low] = middle[i+1-low], middle[i-low]
    return left[:-1] + tuple(middle) + right[1:]


def encode(p):
    n = len(p)
    a, b = p[0], p[-1]
    left = curl(a)
    right = tuple(n-1-x for x in curl(n-1-b))[::-1]
    assert p[:len(left)] == left and p[-len(right):] == right, p
    low, high = left[-1], right[0]
    middle = p[len(left)-1:n-len(right)+1]
    i, j, swaps = low, 0, []
    while i <= high:
        if j < len(middle) and middle[j] == i:
            i, j = i+1, j+1
        else:
            assert middle[j:j+2] == (i+1, i), (p, i, j)
            swaps.append(i)
            i, j = i+2, j+2
    assert j == len(middle)
    code = (a, b, tuple(swaps))
    assert decode(n, code) == p
    return code


def reflect(n, code):
    a, b, swaps = code
    return n-1-b, n-1-a, tuple(n-2-i for i in swaps[::-1])


def deltas(n, code):
    a, b, swaps = code
    return (int(a == 0 and bool(swaps) and swaps[0] == 1),
            int(b == n-1 and bool(swaps) and swaps[-1] == n-3))


def root_distance(n, code):
    """Theorem: d((0,1,...,n-1), code), evaluated in O(n) time."""
    a, b, swaps = code
    k = len(swaps)
    dl, dr = deltas(n, code)
    return min(
        (a if j == 0 else 2*(swaps[j-1]+1)-a-2*j+dl)
        + (n-1-b if j == k else b+n-1-2*swaps[j]-2*(k-j)+dr)
        for j in range(k+1)
    )


def ceil_twice_sqrt(m):
    q = isqrt(4*m)
    return q + int(q*q < 4*m)


def corner_extremum(n):
    """Exact maximum rooted distance AMONG paths with endpoints 0,n-1.

    This is a lower bound on the full diameter, not its proved exact value.
    """
    assert n >= 10
    return max(2*n+2-2*ceil_twice_sqrt(n),
               2*n+1-2*ceil_twice_sqrt(n-2),
               2*n-2*ceil_twice_sqrt(n-4))


def left_outward_options(code):
    a, b, swaps = code
    if a > 0:
        yield (a-1, b, swaps)
    if a == 2:
        yield (0, b, (1,) + swaps)
    elif a >= 3:
        yield (a-3, b, (a-1,) + swaps)


def core_cycle(n):
    return tuple(range(0, n, 2)) + tuple(range(n-1 if n % 2 == 0 else n-2, 0, -2))


def core_paths(n):
    cycle = core_cycle(n)
    return [canonical(cycle[i+1:] + cycle[:i+1]) for i in range(n)]


def is_core(code):
    a, b, swaps = code
    return not swaps and b-a <= 2


def left_inward_step(n, code):
    a, b, swaps = code
    if a == 0 and swaps and swaps[0] == 1:
        return (2, b, swaps[1:])
    if swaps and swaps[0] == a+2:
        return (a+3, b, swaps[1:])
    return (a+1, b, swaps)


def left_sweep(n, code, peak, final_a, target_left_swaps):
    """Consume encountered old swaps, then create prescribed swaps on return.

    The caller supplies a separating gap of size at least three, ensuring
    that the other endpoint and the unprocessed swaps stay out of the route.
    """
    route = [code]
    while route[-1][0] < peak:
        q = left_inward_step(n, route[-1])
        assert q[0] <= peak
        decode(n, q)
        route.append(q)
    todo = list(target_left_swaps)
    while route[-1][0] > final_a:
        a, b, swaps = route[-1]
        if todo and a == todo[-1]+1:
            i = todo.pop()
            q = (0 if i == 1 else i-2, b, (i,) + swaps)
        else:
            q = (a-1, b, swaps)
        decode(n, q)
        route.append(q)
    assert not todo
    return route


def shortest_root_route(n, code):
    """Construct the Theorem A route from code to the natural-order path.

    This verification implementation retains every full state. The proof's
    linear-time algorithm instead emits the O(n) endpoint/target instructions.
    """
    a, b, swaps = code
    k = len(swaps)
    dl, dr = deltas(n, code)
    costs = [
        (a if j == 0 else 2*(swaps[j-1]+1)-a-2*j+dl)
        + (n-1-b if j == k else b+n-1-2*swaps[j]-2*(k-j)+dr)
        for j in range(k+1)
    ]
    j = min(range(k+1), key=costs.__getitem__)
    route = left_sweep(n, code, a if j == 0 else swaps[j-1]+1, 0, ())
    reflected = reflect(n, route[-1])
    peak = reflected[0] if j == k else n-1-swaps[j]
    right = left_sweep(n, reflected, peak, 0, ())
    route.extend(reflect(n, q) for q in right[1:])
    assert route[-1] == (0, n-1, ())
    assert len(route)-1 == costs[j]
    return route


def gap_route(n, source, target):
    """Construct the route used in the separated-sweep upper-bound proof.

    Return None if no separating gap of size >=3 exists.
    """
    a, b, ss = source
    c, d, tt = target
    points = sorted(set(ss) | set(tt))
    A, B = max(a, c), min(b, d)
    choices = []
    for j in range(len(points)+1):
        h = max(A, points[j-1]+1) if j else A
        z = min(B, points[j]) if j < len(points) else B
        choices.append((z-h+1, h, z, j))
    gap, h, z, j = max(choices)
    if gap < 3:
        return None
    left_points = set(points[:j])
    right_points = set(points[j:])
    route = left_sweep(n, source, h, c, tuple(i for i in tt if i in left_points))
    mirrored = reflect(n, route[-1])
    right_target = tuple(sorted(n-2-i for i in tt if i in right_points))
    right_route = left_sweep(n, mirrored, n-1-z, n-1-d, right_target)
    route.extend(reflect(n, q) for q in right_route[1:])
    assert route[-1] == target, (source, target, route[-1])
    fold = a+c+2*n-2-b-d
    u = len(ss)+len(tt)
    delta = sum(deltas(n, source)) + sum(deltas(n, target))
    expected = 2*n-fold-2*u-2*gap+delta
    assert len(route)-1 == expected
    return route


def compact_core_route(n, code):
    """Keep the smaller endpoint, consume swaps until the endpoints meet."""
    route = [code]
    while not is_core(route[-1]):
        q = reflect(n, left_inward_step(n, reflect(n, route[-1])))
        decode(n, q)
        route.append(q)
    a, b, swaps = code
    tau = int(b-a == 1)
    expected = b-a-2-2*len(swaps)+sum(deltas(n, code))+tau
    assert len(route)-1 == expected, (n, code, expected, route)
    return route


def bfs(graph, root):
    distance = [-1] * len(graph)
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] < 0:
                distance[v] = distance[u]+1
                queue.append(v)
    assert min(distance) >= 0
    return distance
