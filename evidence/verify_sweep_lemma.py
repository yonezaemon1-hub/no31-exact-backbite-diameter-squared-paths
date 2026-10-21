"""Focused internal check of the expanded v0.4 Section 6.3.

Uses the unchanged v0.3 route implementation, and checks its actual path
transitions using prefix backbites. This is not an independent implementation,
an all-pairs diameter computation, or the external auditor's missing source.
Python standard library only. All rights reserved.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import random

from backbite_model import (backbites, decode, deltas, encode, enumerate_paths,
                           gap_route, left_sweep, reflect)
from exact_diameter import sweep_parameters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="REPLAY_SWEEP_LEMMA.json")
    args = parser.parse_args()
    counts = Counter()
    masks = Counter()
    empty_legs = Counter()
    per_n = []

    @lru_cache(maxsize=200000)
    def actual_neighbors(n, code):
        return frozenset(backbites(decode(n, code)))

    def check(n, source, target):
        counts["candidate_pairs"] += 1
        p = sweep_parameters(n, source, target)
        if p["G"] < 3:
            counts["no_separating_clearance"] += 1
            return
        a, b, ss = source
        c, d, tt = target
        h, z, j = p["h"], p["z"], p["split"]
        points = sorted(set(ss) | set(tt))
        left, right = set(points[:j]), set(points[j:])
        sl = tuple(i for i in ss if i in left)
        sr = tuple(i for i in ss if i in right)
        tl = tuple(i for i in tt if i in left)
        tr = tuple(i for i in tt if i in right)
        assert a <= h and c <= h and h+2 <= z <= min(b, d)
        assert b-a >= 2 and d-c >= 2
        assert 1 not in right and n-3 not in left
        dl_s, dr_s = deltas(n, source)
        dl_t, dr_t = deltas(n, target)
        masks["".join(map(str, (dl_s, dr_s, dl_t, dr_t)))] += 1

        left_route = left_sweep(n, source, h, c, tl)
        peak = next(i for i, code in enumerate(left_route) if code[0] == h)
        assert left_route[peak] == (h, b, sr)
        assert left_route[-1] == (c, b, tuple(sorted(tl+sr)))
        reflected_target = tuple(sorted(n-2-i for i in tr))
        reflected_route = left_sweep(
            n, reflect(n, left_route[-1]), n-1-z, n-1-d, reflected_target)
        right_route = [reflect(n, code) for code in reflected_route]
        right_peak = next(i for i, code in enumerate(right_route) if code[1] == z)
        assert right_route[right_peak] == (c, z, tl)
        assert right_route[-1] == target
        lengths = (peak, len(left_route)-1-peak,
                   right_peak, len(right_route)-1-right_peak)
        expected = (h-a-2*len(sl)+dl_s, h-c-2*len(tl)+dl_t,
                    b-z-2*len(sr)+dr_s, d-z-2*len(tr)+dr_t)
        assert lengths == expected, (n, source, target, lengths, expected)
        for name, length in zip(("left_in", "left_out", "right_in", "right_out"), lengths):
            empty_legs[name] += int(length == 0)

        route = left_route + right_route[1:]
        assert route == gap_route(n, source, target)
        assert len(route)-1 == p["sweep_bound"]
        for code in left_route:
            assert code[0] <= h and code[1] == b
            assert set(sr) <= set(code[2])
        for code in right_route:
            assert code[0] == c and code[1] >= z
            assert set(tl) <= set(code[2])
        for x, y in zip(route, route[1:]):
            assert decode(n, y) in actual_neighbors(n, x), (n, x, y)
        counts["legal_separated_routes"] += 1
        counts["checked_backbite_steps"] += len(route)-1
        counts["four_leg_length_checks"] += 4
        if set(ss) & set(tt):
            counts["routes_with_shared_swaps"] += 1
        if any(y-x < 3 for x, y in zip(points, points[1:])):
            counts["routes_with_close_union_positions"] += 1

    # All ordered state pairs, checking separated-sweep routes only.
    # There is no BFS in this additional check.
    for n in range(3, 13):
        codes = [encode(path) for path in enumerate_paths(n)]
        before = counts.copy()
        for source in codes:
            for target in codes:
                check(n, source, target)
        record = dict(n=n, states=len(codes), ordered_pairs=len(codes)**2,
                      separated_routes=counts["legal_separated_routes"]-before["legal_separated_routes"])
        per_n.append(record)
        print(json.dumps(record), flush=True)
        actual_neighbors.cache_clear()

    # Larger n: sampled codes, not exhaustive graph enumeration or diameter.
    rng = random.Random(31000422)

    def sample_code(n):
        a = 0 if rng.randrange(2) else rng.randrange(n-2)
        b = n-1 if rng.randrange(2) else rng.randrange(a+2, n)
        lo = 1 if a == 0 else a+2
        hi = n-3 if b == n-1 else b-3
        swaps = []
        cursor = lo
        while cursor <= hi:
            if rng.randrange(2):
                swaps.append(cursor)
                cursor += 3
            else:
                cursor += 1
        return a, b, tuple(swaps)

    for n in range(16, 33):
        for _ in range(1000):
            check(n, sample_code(n), sample_code(n))
        actual_neighbors.cache_clear()
    assert set(masks) == {format(i, "04b") for i in range(16)}
    assert all(empty_legs.values())
    assert counts["routes_with_shared_swaps"] > 0
    assert counts["routes_with_close_union_positions"] > 0
    result = dict(
        status="PASS", version="0.4",
        check_kind="internal_focused_route_check_not_independent_audit",
        all_pairs_diameter_computed=False,
        exhaustive_ordered_pair_range=[3, 12],
        sampled_n_range=[16, 32], sampled_pairs_per_n=1000, seed=31000422,
        exhaustive_records=per_n, counts=dict(counts),
        boundary_indicator_masks=dict(sorted(masks.items())),
        zero_length_legs=dict(empty_legs),
        claims_checked=["each intermediate transition is an actual backbite",
                        "each of the four leg lengths and the total U",
                        "retained opposite-side swaps are unchanged",
                        "G>=3 implies both endpoint spans are at least two"])
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                                encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
