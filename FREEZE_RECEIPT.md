# No.31 v0.4 — Freeze receipt

Frozen 22 October 2026 (Japan time).
Author: Ryutaro Yonezu / Yonezu Research Lab.
Research contact: yonezaemon1+research@gmail.com.

The author authorized preparation and publication on GitHub and Zenodo.
This receipt fixes the mathematical manuscript, reproducibility files and
audit evidence at version 0.4. Public availability and DOI registration
must be verified in a separate publication receipt.

## Manuscript

| File | SHA256 |
| --- | --- |
| No31_Exact_Backbite_Diameter_v0_4_20261022.pdf | 69af4a33706ced6dbfdf4b9cd4e67576c1917d6b0c962ad081ab0a232f8c6068 |
| No31_Exact_Backbite_Diameter_v0_4_20261022.tex | 6a1e16955add26e98feb737e14497d0755df05de0b9901327052e16cf391c8bc |

The PDF has 13 pages. The audited Markdown's 498 mathematical spans are
identical in the publication-body Markdown. All pages were rendered and
visually reviewed; final LaTeX compilation had no layout warnings.
Typesetting changes consist of typography, an abstract describing the
existing results, and updated research-status metadata. One display is
wrapped onto two lines. No proof argument, theorem, computation or data
was changed. The audited original remains in evidence/PROOF.md.

## Audited originals

| Source archive | SHA256 |
| --- | --- |
| No31_Exact_Diameter_Final_Audit_v0_4_20261022.zip | 929ed470771e0dab445dbc72f894ba0c2a9b9b52c609f79e937529ceb424a8c8 |
| No31_v0_4_Audit_Closure_20261022.zip | 72866a5b50bec5a4a9ec257c3e66aaa545bbbaad90e48c36c027e8870372d71c |

All 30 source files are byte-preserved under evidence/, including its
29-entry original manifest. The v0.4 audit receipt is preserved separately.
The v0.3-to-v0.4 comparison verifies six existing code files, ten data/log
files and LICENSE.txt unchanged. The received report's different count is
retained with a note in audit/AUDIT_RECEIPT_v0_4.md.

## Assessment and proof scope

Independent AI audit reports: PROOF PASS; COMPUTATION PASS;
REFERENCES INCONCLUSIVE; NOVELTY INCONCLUSIVE.
The two exposition issues in v0.3 were resolved in v0.4.
The author-side cited-source check is documented separately.
Human peer review: not performed. AI-assisted research: disclosed.
Priority: unconfirmed; no priority or first-discovery claim.

The diameter upper bound is analytic for n>=16. The smaller n=3..15
bases are explicitly exhaustive computations. Theorem D gives the exact
diameter for n>=10, not an exact metric between arbitrary specified paths.
Extended computations in received independent reports are attributed to
their auditor; the independent source and raw logs were not supplied.
Interrupted random checks at n=21,23 remain unperformed.

Historical pending-audit or HOLD labels in the unchanged source snapshots
are retained. The later audit receipt and publication metadata record
subsequent decisions. No new mathematical paper version is introduced.

## Integrity and rights

FROZEN_SHA256SUMS.txt covers each immutable member except itself.
The frozen ZIP excludes mutable repository README, CITATION and publication
status files, so DOI and mutual-link metadata may be finalized separately.

Copyright (c) 2026 Ryutaro Yonezu / Yonezu Research Lab.
All rights reserved. No MIT, Apache, CC BY or other general reuse license.
