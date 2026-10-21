"""Finite falsification checks for the all-n proofs in PROOF.md.

These checks supplement, and do not replace, the mathematical proofs.
Default: n=3..20, all route pairs through n=11, fixed-seed samples above.
Use --max-n 22 to reproduce the recorded Python run.
No external packages or services are used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import time

from backbite_model import (
    backbites, bfs, canonical, compact_core_route, core_paths, corner_extremum,
    decode, encode, enumerate_paths, gap_route, left_outward_options, reflect,
    root_distance, shortest_root_route,
)


def verify_manifest(root):
    manifest = root / "SHA256SUMS.txt"
    if not manifest.exists():
        print("No manifest yet: development run", flush=True)
        return
    for line in manifest.read_text().splitlines():
        expected, name = line.split("  ", 1)
        path = (root / name).resolve()
        assert path.is_relative_to(root.resolve()), name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    print("PASS checkpoint manifest", flush=True)


def check_route(n, route):
    paths = [decode(n, q) for q in route]
    for p, q in zip(paths, paths[1:]):
        assert q in backbites(p), (n, p, q)


def run(max_n, all_routes_to, samples):
    results = []
    rng = random.Random(310021)
    for n in range(3, max_n+1):
        start = time.perf_counter()
        paths = enumerate_paths(n)
        index = {p: i for i, p in enumerate(paths)}
        assert len(index) == len(paths)
        graph = [set(index[q] for q in backbites(p)) for p in paths]
        codes = [encode(p) for p in paths]
        ci = {q: i for i, q in enumerate(codes)}
        assert len(ci) == len(paths)
        predicted = [set() for _ in paths]
        for i, q in enumerate(codes):
            for mirrored in (False, True):
                z = reflect(n, q) if mirrored else q
                for w in left_outward_options(z):
                    v = ci[reflect(n, w) if mirrored else w]
                    predicted[i].add(v)
                    predicted[v].add(i)
        core = core_paths(n)
        assert len(set(core)) == n
        for p, q in zip(core, core[1:]+core[:1]):
            u, v = index[p], index[q]
            predicted[u].add(v)
            predicted[v].add(u)
        assert predicted == graph, n
        distances = bfs(graph, index[tuple(range(n))])
        formula = [root_distance(n, q) for q in codes]
        assert formula == distances, n
        assert all(abs(formula[u]-formula[v]) <= 1
                   for u in range(len(paths)) for v in graph[u])
        for q in codes:
            check_route(n, compact_core_route(n, q))
            check_route(n, shortest_root_route(n, q))
        corner_max = max(distances[i] for i, q in enumerate(codes)
                         if q[0] == 0 and q[1] == n-1)
        if n >= 10:
            assert corner_max == corner_extremum(n)
        if n <= all_routes_to:
            pairs = ((a, b) for a in codes for b in codes)
            count = len(codes)**2
        else:
            pairs = ((rng.choice(codes), rng.choice(codes)) for _ in range(samples))
            count = samples
        separated = 0
        for source, target in pairs:
            route = gap_route(n, source, target)
            if route is not None:
                separated += 1
                check_route(n, route)
                length = len(route)-1
                # Exact integer equivalent of length <= 2n-4sqrt(n)+8.
                rhs = 2*n+8-length
                assert rhs >= 0 and rhs*rhs >= 16*n
            else:
                r1, r2 = compact_core_route(n, source), compact_core_route(n, target)
                length_bound = len(r1)+len(r2)-2+n//2
                assert length_bound <= 3*n//2, (source, target, length_bound)
        record = dict(n=n, vertices=len(paths), edges=sum(map(len, graph))//2,
                      root_eccentricity=max(distances), corner_max=corner_max,
                      normal_form_roundtrip=True, move_classification=True,
                      root_formula_all_states=True, compact_route_all_states=True,
                      shortest_root_route_all_states=True,
                      route_pairs=count, separated_routes=separated,
                      seconds=round(time.perf_counter()-start, 5))
        print(json.dumps(record), flush=True)
        results.append(record)
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=20)
    parser.add_argument("--all-routes-to", type=int, default=11)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--output", default="REPLAY_VERIFICATION.json")
    args = parser.parse_args()
    assert 3 <= args.max_n <= 28
    assert 3 <= args.all_routes_to <= args.max_n
    assert args.samples > 0
    root = Path(__file__).resolve().parent
    verify_manifest(root)
    result = dict(status="PASS", scope="finite checks of internal all-n proofs",
                  independent_external_proof_audit=False,
                  novelty="INCONCLUSIVE", seed=310021,
                  results=run(args.max_n, args.all_routes_to, args.samples))
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")


if __name__ == "__main__":
    main()
