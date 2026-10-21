# Exact Backbite Diameter of Squared Paths

No.31 — Yonezu Research Lab  
Ryutaro Yonezu  
Version 0.4 / frozen 22 October 2026  
Research contact: yonezaemon1+research@gmail.com

**AI-assisted, unrefereed preprint. All rights reserved.**

## Publication status

GitHub repository: https://github.com/yonezaemon1-hub/no31-exact-backbite-diameter-squared-paths

Published as version 0.4 on 22 October 2026.

Zenodo: https://zenodo.org/records/23548698  
DOI: [10.5281/zenodo.23548698](https://doi.org/10.5281/zenodo.23548698)

The public Zenodo PDF and frozen ZIP were retrieved after publication and matched the original SHA256 hashes. Both platforms specify All rights reserved.

## Result and scope

The host is the square of a path, $P_n^2$. States are Hamiltonian paths with reversal identified; one edge is one actual endpoint backbite.

For every $n\ge10$, the exact diameter is

$$D_n=\max\{2n+2-2\lceil2\sqrt n\rceil,\quad
2n+1-2\lceil2\sqrt{n-2}\rceil,\quad
2n-2\lceil2\sqrt{n-4}\rceil\}.$$

For n=3..9 the diameters are 1, 3, 3, 5, 6, 7, 8. The arbitrary-pair upper bound is analytic for n≥16; the finite n=3..15 bases use explicitly disclosed exhaustive BFS. The paper also proves an exact distance formula from the natural-order path and constructs diameter-attaining pairs.

Theorem D gives a diameter, not an exact distance formula for two arbitrary specified paths. The known host family, connectivity, outer-cycle uniqueness and prior enumeration results are attributed and excluded from novelty claims.

## Research assessment

| Category | Status |
| --- | --- |
| PROOF | PASS in the received independent AI audit, including the v0.4 differential audit |
| COMPUTATION | PASS in the received independent AI audit |
| REFERENCES | Independent audit INCONCLUSIVE: primary sources were inaccessible to that auditor |
| Author-side reference check | Cited passages in the two primary sources checked; scope recorded in audit/PRIMARY_REFERENCE_RECHECK.md |
| NOVELTY | INCONCLUSIVE |
| Human peer review | Not performed |
| AI-assisted research | Substantial generative AI assistance and reported independent AI checks disclosed |
| Priority | Unconfirmed; no priority or first-discovery claim |
| Rights | All rights reserved; no general reuse license |

AI audit PASS is not human peer review or a certification of scholarly novelty. The independent auditor's source code and raw logs were not supplied. Extended checks described only in the audit reports remain attributed to the auditor. Previously interrupted random checks at n=21,23 remain unperformed.

## Files and provenance

- No31_Exact_Backbite_Diameter_v0_4_20261022.pdf — typeset paper.
- No31_Exact_Backbite_Diameter_v0_4_20261022.tex — matching LaTeX source.
- No31_Frozen_v0_4_20261022.zip — immutable manuscript, evidence and audit package.
- evidence/ — all 30 files of the audited v0.4 package, preserved byte for byte.
- audit/ — received v0.4 independent audit and reference/gate records.
- source_archives/ — the original audited ZIP and audit-closure ZIP, unchanged.
- typesetting/ — publication Markdown and the typesetting-integrity record.
- FREEZE_RECEIPT.md and FROZEN_SHA256SUMS.txt — freeze scope and immutable-file checksums.
- SHA256SUMS.txt — checksums for the current repository files except itself.

The typeset paper preserves all 498 mathematical spans in the audited Markdown. Changes comprise typography, an abstract describing the existing results, and updated research-status metadata. The audited Markdown, code, numerical evidence and original archives remain unchanged. Historical pending-audit or HOLD labels in those archives describe the preparation stage; later audit receipts supply the subsequent status.

## Reproduce

Existing Python 3.12 or later, standard library only:

```powershell
cd evidence
python .\verify_exact_diameter.py --max-n 22 --samples 1000 --stress 10000
python .\verify_sweep_lemma.py
```

Replay results use separate filenames and do not replace the stored evidence. The bundled Python/C++ finite all-pairs bases stop at n=15; larger recorded checks have the scope stated in the paper and source README. In particular, n≤32 rooted BFS is not an all-pairs diameter run.

The recorded author-side checks ran on Linux. Windows hardware reproduction has not been performed. No paid API, cloud compute service or new runtime is required. A C++17 compiler is optional for rerunning the second bundled finite-base implementation.

With an existing LaTeX installation, compile the root .tex source with pdflatex twice. The supplied PDF is already compiled.

## Citation and contact

Use CITATION.cff to cite the unrefereed preprint, DOI [10.5281/zenodo.23548698](https://doi.org/10.5281/zenodo.23548698).

Research Inquiries — Yonezu Research Lab  
Contact: yonezaemon1+research@gmail.com

Copyright © 2026 Ryutaro Yonezu / Yonezu Research Lab. All rights reserved.
