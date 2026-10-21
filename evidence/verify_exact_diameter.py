"""Finite falsification support for the v0.3 exact-diameter proof.

Default runtime uses only Python's standard library. No API or downloads.
Finite n=3..15 bases use full all-pairs BFS. Larger n checks are clearly
separated into all-state projection checks, sampled pairs, and integer-only
stress checks; they are NOT represented as additional exact BFS diameters.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import time

from backbite_model import (backbites, bfs, decode, encode, enumerate_paths,
                           gap_route, root_distance)
from exact_diameter import (core_route_bound, deficit, diameter_formula,
                            diameter_witness, edge_projection, height,
                            verify_integer_reduction)


def manifest_check(root):
    p = root/'SHA256SUMS.txt'
    if not p.exists():
        print('Development run: manifest not finalized', flush=True)
        return
    for line in p.read_text().splitlines():
        expected, name = line.split('  ', 1)
        f = (root/name).resolve()
        assert f.is_relative_to(root.resolve())
        assert hashlib.sha256(f.read_bytes()).hexdigest() == expected, name
    print('PASS manifest', flush=True)


def verify_graphs(max_n, samples, rng):
    output = []
    for n in range(3, max_n+1):
        start = time.perf_counter()
        paths = enumerate_paths(n)
        index = {p:i for i,p in enumerate(paths)}
        graph = [{index[q] for q in backbites(p)} for p in paths]
        codes = [encode(p) for p in paths]
        projection = [edge_projection(n,p) for p in paths]
        levels = [x[0] for x in projection]
        missing = [x[1] for x in projection]
        assert all(height(n,codes[i]) == levels[i] for i in range(len(paths)))
        assert all(len(missing[i]) == levels[i]+1 for i in range(len(paths)))
        reachable = [None]*len(paths)
        for i in sorted(range(len(paths)), key=levels.__getitem__):
            if levels[i] == 0:
                reachable[i] = missing[i]
            else:
                downward = [v for v in graph[i] if levels[v] == levels[i]-1]
                additions = set()
                for v in downward:
                    added = missing[i]-missing[v]
                    assert len(added) == 1 and missing[v] < missing[i]
                    additions |= added
                assert len(additions) >= 2
                reachable[i] = frozenset().union(*(reachable[v] for v in downward))
                assert reachable[i] == missing[i], (n,paths[i])
        record = dict(n=n, vertices=len(paths), edges=sum(map(len,graph))//2,
                      projection_all_states=True, distinct_downward_edges=True)
        if n <= 15:
            eccentricities = []
            diameter = 0
            witness = None
            for i in range(len(paths)):
                dist = bfs(graph, i)
                ecc = max(dist)
                eccentricities.append(ecc)
                if ecc > diameter:
                    diameter = ecc
                    witness = [paths[i], paths[dist.index(ecc)]]
            assert diameter == diameter_formula(n), (n,diameter,diameter_formula(n))
            record.update(all_pairs=True, diameter=diameter,
                          eccentricity_histogram=dict(sorted(Counter(eccentricities).items())),
                          witness=witness)
        else:
            counts = Counter()
            for sample in range(samples):
                i,j = rng.randrange(len(paths)),rng.randrange(len(paths))
                branch = verify_integer_reduction(n,codes[i],codes[j])
                counts[branch] += 1
                bound = core_route_bound(n,levels[i],levels[j],missing[i],missing[j])
                route = gap_route(n,codes[i],codes[j])
                if route is not None:
                    bound = min(bound,len(route)-1)
                    if sample < 50:
                        actual = [decode(n,q) for q in route]
                        assert all(q in backbites(p) for p,q in zip(actual,actual[1:]))
                assert bound <= diameter_formula(n)
            record.update(all_pairs=False, sampled_pairs=samples, branches=dict(counts))
        record['seconds'] = round(time.perf_counter()-start,5)
        output.append(record)
        print(json.dumps(record),flush=True)
    return output


def random_code(n,rng,mode):
    if mode % 3 == 0:
        a,b = 0,n-1
    else:
        a = 0 if rng.randrange(3)==0 else rng.randrange(n-2)
        b = n-1 if rng.randrange(3)==0 else rng.randrange(a+2,n)
    low = 0 if a==0 else a+1
    high = n-1 if b==n-1 else b-1
    swaps = []
    if mode % 4 != 0:
        step = max(3,int(n**0.5)) if mode % 4 == 1 else 4
        x = low+1+rng.randrange(step)
        while x <= high-2:
            swaps.append(x)
            x += 3+rng.randrange(step)
    return a,b,tuple(swaps)


def stress_checks(count,rng):
    branches = Counter()
    for j in range(count):
        if j % 2:
            n = rng.randrange(16,4001)
        else:
            q = rng.randrange(9,129)
            n = max(16,(q*q)//4+rng.randrange(-4,8))
        a,b = random_code(n,rng,j),random_code(n,rng,j+1)
        branches[verify_integer_reduction(n,a,b)] += 1
    last = deficit(10)
    for n in range(11,100001):
        current = deficit(n)
        assert 0 <= current-last <= 1, n
        last = current
    witnesses = []
    for n in list(range(10,101)) + [128,255,256,257,999,1000,10000]:
        code = diameter_witness(n)
        assert root_distance(n,code) == diameter_formula(n)
        if n <= 1000:
            p = decode(n,code)
            assert sorted(p) == list(range(n))
            assert all(0<abs(x-y)<=2 for x,y in zip(p,p[1:]))
        witnesses.append(dict(n=n,diameter=diameter_formula(n),code=code))
    return dict(parameter_pairs=count, branches=dict(branches),
                deficit_step_check=[10,100000],extremal_witnesses=witnesses)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--max-n',type=int,default=20)
    p.add_argument('--samples',type=int,default=1000)
    p.add_argument('--stress',type=int,default=10000)
    p.add_argument('--output',default='REPLAY_EXACT_DIAMETER.json')
    a = p.parse_args()
    assert 16<=a.max_n<=24 and a.samples>0 and a.stress>0
    root = Path(__file__).resolve().parent
    manifest_check(root)
    rng = random.Random(31000321)
    result = dict(status='PASS',external_independent_proof_audit=False,
                  novelty='INCONCLUSIVE',seed=31000321,
                  graphs=verify_graphs(a.max_n,a.samples,rng),
                  integer_checks=stress_checks(a.stress,rng))
    cpp_path = root/'FINITE_BASES_CPP.jsonl'
    if cpp_path.exists():
        cpp = {x['n']:x for x in map(json.loads,cpp_path.read_text().splitlines())}
        for x in result['graphs']:
            if x['n']<=15:
                y=cpp[x['n']]
                for key in ['vertices','edges','diameter']:
                    assert x[key]==y[key],(x['n'],key)
                assert {str(k):v for k,v in x['eccentricity_histogram'].items()} == y['eccentricity_histogram']
        result['cpp_finite_base_comparison']='PASS'
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')


if __name__ == '__main__':
    main()
