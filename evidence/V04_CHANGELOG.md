# No.31 v0.4 — 凍結前の最終差分監査への変更

2026-10-22（日本時間）。対象主張はTheorem D。

## 入力

No31_Exact_Diameter_Audit_v0_3_20261021.zip

SHA256: 1b5464ea0e6404f05a7dfb3ae3927066abf5df3bb6437eddc388fb40fed52071

入力ZIPの24ファイル、SHA256SUMS.txtの23件を全件照合した。
独立AI監査の受領報告はINDEPENDENT_AI_AUDIT_v0_3.mdへ保存した。

## 指摘と修正の対応

| 指摘 | v0.4での修正 |
| --- | --- |
| §9 Case 3のτ=0の理由不足 | G≤B−A+1よりG≥3⇒B−A≥2。両端点区間が[A,B]を含むことからb−a,d−c≥2。Case 4も同じ理由を参照 |
| §6.3の掃引の合法性とΔの説明不足 | 4段階を個別に定義し、中間表示の合法性、折返し位置の非超過、旧交換の消去後に目標交換を生成する順序、反対側との分離を記述。4段階の手数表を加え、境界のジャンプ2と通常のジャンプ3から同じUを再導出 |
| 独立監査側で一次資料を取得できず | Kazazi v1本文、Biswasほかの著者PDFと出版社書誌を取得。該当節・ページをLITERATURE_AUDIT.mdへ記録。独立監査のINCONCLUSIVE判定は維持 |

PROOF_v03_to_v04.diffに証明本文の全差分を収録する。
Theorem D、全ての主張の適用範囲、既存コード6本、計算証拠10ファイル、LICENSE.txtを変更していない。これら計17ファイルは入力ZIPとのSHA256一致をPROVENANCE.jsonに記録する。旧版ZIPも変更しない。

## 追加内部検査

verify_sweep_lemma.pyをLinuxの既存Pythonで実行。標準ライブラリのみ。

- n=3..12の全順序付き状態対98,468組を候補とし、G≥3の経路を検査。
- n=16..32は各1,000組、合計17,000組をサンプル。
- 候補115,468組中、掃引経路94,887本、実際のbackbite 646,974手、4段階の手数379,548件が全てPASS。
- 境界指標(δ_L(H),δ_R(H),δ_L(J),δ_R(J))の全16通りを検査。
- 共通の交換、和集合内の近接位置、0手の各段階も含む。

この検査は継承した掃引コードを使用し、その出力を実際のprefix backbiteと照合する内部検査。独立実装や全点対直径の再計算ではない。従来の高コストな検証を再実施したとの表示はしない。生結果はSWEEP_LEMMA_CHECKS.json、実行ログはsweep_lemma_checks.log。

## 研究評価と次の確認

- v0.3の受領判定：PROOF=PASS（軽微2点）、COMPUTATION=PASS、REFERENCES=INCONCLUSIVE、NOVELTY=INCONCLUSIVE。
- v0.4の補強箇所への独立差分監査：未実施。
- 独立監査の追加実装・生ログ：未受領。受領報告と同梱証拠を区別。
- 人間査読：未実施。AI-assisted researchを明示。
- 優先権：未確認、主張なし。ライセンス：All rights reserved。
- 本版は凍結前の監査用。正式凍結・GitHub公開・Zenodo登録・DOI取得は実施していない。
