# No.31 v0.4 — 凍結前判定

2026-10-22（日本時間）。

**判定：未査読プレプリントの凍結・公開候補の整備へ進める。**
本判定の新規性区分はINCONCLUSIVE。新規性PASS、優先権確定、人間査読済みとは表示しない。

## 研究評価

| 区分 | 現在の状態 |
| --- | --- |
| PROOF | v0.4の独立AI差分監査PASSを受領。v0.3の軽微2点は解消 |
| COMPUTATION | v0.4の独立AI差分監査PASSを受領 |
| REFERENCES：独立監査 | INCONCLUSIVE。監査者側で一次本文を取得できず |
| REFERENCES：本助手 | 対象となる一次資料2本の引用箇所と既知結果を照合済み。PRIMARY_REFERENCE_RECHECK.md参照 |
| NOVELTY | INCONCLUSIVE。先行性は確定していない |
| Human peer review | 未実施 |
| AI-assisted research | 明示 |
| Priority | 未確認、主張なし |
| Rights | All rights reserved |

## 公開候補に載せる評価文

Independent AI audits report PASS for the mathematical proof and computation,
including the v0.4 revisions. The independent reference audit remains
INCONCLUSIVE because the auditor could not access the primary sources.
The author-side reference check identified the cited passages in the two
primary sources. Scholarly novelty remains INCONCLUSIVE, and no priority is
claimed. This is AI-assisted research and has not undergone human peer
review. All rights reserved.

数学的主張の適用範囲を維持する。n≥16の直径上界は解析的証明、
n=3..15は明示された有限全探索の基底。Theorem Dのn≥10の式と、
任意の2本を入力した場合の厳密な最短距離式を区別する。

## 固定して保持する対象

No31_Exact_Diameter_Final_Audit_v0_4_20261022.zip

SHA256：929ed470771e0dab445dbc72f894ba0c2a9b9b52c609f79e937529ceb424a8c8

対象ZIP内の30ファイルと、29件のマニフェストを照合済み。
原ZIPは変更しない。新しい数学内容・コード版を導入せず、今回の監査受領記録を外付けした。

独立監査者のsweep4.pyと生ログは未受領。
n=16の1,216,035経路、n=20の40万対、n=26の10万対は
受領報告の数値として扱う。n=21,23の前回中断した検査は未実施のまま。

本一式で完了したのは監査の受領、原本照合、一次文献の再照合、凍結前判定。
正式論文PDF・LaTeXの凍結一式作成、GitHub公開、Zenodo登録は未実施。
