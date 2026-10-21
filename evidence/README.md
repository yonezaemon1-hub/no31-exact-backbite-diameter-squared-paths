# No.31 — Exact Backbite Diameter of Squared Paths

凍結前の最終差分監査用 v0.4 / 2026年10月22日（日本時間）  
Ryutaro Yonezu / Yonezu Research Lab  
yonezaemon1+research@gmail.com  
AI-assisted research. All rights reserved.

**v0.3への独立AI監査報告を受領し、指摘された記述2点を補強した版。v0.4の差分への独立再監査は未実施。正式凍結・公開版ではない。**

## v0.4で反映した監査

ユーザー提供の独立AI監査報告について、対象はv0.3であることを維持する。

| 区分 | 受領したv0.3監査の判定 | v0.4での対応 |
| --- | --- | --- |
| PROOF | PASS（軽微な記述不備2点） | §9のτ=0の理由、§6.3の掃引の合法性と境界補正を明文化。差分再監査待ち |
| COMPUTATION | PASS | 従来のコード・計算証拠を全て原バイトで継承。4段階の掃引を対象に追加の内部検査 |
| REFERENCES | INCONCLUSIVE（監査側で一次資料を取得できず） | こちらで一次資料2本を取得して該当箇所を照合。LITERATURE_AUDIT.mdに記録。独立監査の判定は維持 |
| NOVELTY | INCONCLUSIVE | 維持 |

独立監査の原報告はINDEPENDENT_AI_AUDIT_v0_3.md。第三の実装によるn≤24の直径検証、n=16..18の証明内部の全点対検査などは**受領報告に記載された結果**であり、その独立ソース・生ログは本ZIPには含まれない。監査者が途中停止したn=21,23のランダムサンプル検査も未確認のまま記録する。AI監査は人間査読の代わりではない。

数学的主張・閉形式・既存の計算プログラムは変更していない。変更内容はV04_CHANGELOG.mdを参照。

## 厳密直径の主張

二乗パス $P_n^2$ のHamilton道をbackbiteでつなぎ替える。逆向きの道は同じ状態とする。最悪必要回数、すなわち再構成グラフの直径を $D_n$ とする。

v0.2では自然順序からの厳密距離と、直径の二次漸近評価までだった。v0.3で任意の道の対に対する上界を追加し、下界と一致させた。v0.4はその証明の記述を補強する。

全ての $n\ge10$ に対する内部導出の結論は

$$D_n=\max\{2n+2-2\lceil2\sqrt n\rceil,\quad
2n+1-2\lceil2\sqrt{n-2}\rceil,\quad
2n-2\lceil2\sqrt{n-4}\rceil\}.$$

n=3..9は、それぞれ1, 3, 3, 5, 6, 7, 8。

**証明の区分：n≥16は一般の解析的証明。残るn=3..15は、明示した有限全探索による確認を含む。** 特にn=10..15の全点対BFSが閉形式と一致する。計算を含まない純粋な解析証明が全小次数まである、という表示はしない。

## 上界を閉じた仕組み

1. 各道の「外周Hamilton閉路に含まれない辺数」を高さhとする。
2. 道に欠けている外周辺はちょうどh+1本。それぞれを欠いたcoreの道へ、高さを毎手1ずつ下げるh手で到達できると証明。
3. 2本の道の欠辺集合を使い、core経由の上界を得る。
4. 既存の両端掃引と、切り詰めた空き区間の容量不等式を組み合わせる。
5. 切り上げ平方根からなる欠損量が、nを1増やしても高々1しか増えないことを示し、任意の2道の上界をL_n以下にする。

PROOF.mdは旧版の必要な証明も統合した全文。直径を閉じた部分はSections 7–10。今回の数学的な記述変更は§6.3と§9のCase 3・4。

## v0.3から継承した計算証拠

| 検査 | 範囲 | 結果 |
| --- | --- | --- |
| 全点対BFS・Python | n=3..15、2,308状態、計1,078,618組の順序付き対 | PASS |
| 別実装C++・全点対BFS | 同じ範囲。辺集合・次数・連結性から隣接を構成 | PASS |
| 両実装の道数・辺数・直径・全離心率ヒストグラム | n=3..15 | 全一致 |
| 高さと全ての最短core到達先 | n=3..22、全35,535状態 | PASS |
| 上界の4場合分け・実際の手順 | n=16..22、各1,000組。手順の全手検査は各次数の先頭50組 | PASS |
| 整数パラメータの追加検査 | 10,000組、4場合分け全てを含む | PASS |
| 切り上げ欠損量の隣接差 | n=10..100,000 | PASS |
| 極値対を作る整数ギャップ構成 | 98次数。最大n=10,000 | PASS |

後二つの大きいnの検査は整数式・構成の検査であり、巨大グラフの全点対BFSを実行したという意味ではない。

v0.2から継承した検証も同梱した。自然順序からの厳密距離はC++でn=32・520,490状態まで全一致している。この記録も単一始点のBFSであり、n=32の全点対直径を再計算した記録ではない。旧版の厳密直径計算はn=28まで。COMPARISON.csvで実測範囲と一般定理の値を区別する。

全て本セッションのLinuxで実行。Windows実機再現は未実施。Pythonは標準ライブラリのみ。新規Runtime・有料API・外部計算サービスは不要。

## v0.4の追加内部検査

verify_sweep_lemma.pyは、継承した掃引コードの出力を実際のprefix backbiteと照合し、4段階それぞれの手数、境界補正、反対側の交換の保持を検査する。n=3..12は全順序付き状態対、n=16..32は各1,000組のサンプル対を対象とする。全16通りの境界指標の組合せ、近接した和集合、共通の交換、0手の各段階も含む。

これは今回の補強箇所を対象にした内部検査であり、独立実装や新たな全点対直径計算ではない。94,887本の経路・646,974手が全てPASS。結果はSWEEP_LEMMA_CHECKS.jsonとsweep_lemma_checks.logに保存済み。既存の計算記録は再生成・上書きしていない。

## 再現

ZIPを展開し、そのフォルダで、既存のPython 3.12以降を利用する。

```powershell
python .\verify_exact_diameter.py
```

今回のn=22までの記録を再現する場合：

```powershell
python .\verify_exact_diameter.py --max-n 22 --samples 1000 --stress 10000
```

結果はREPLAY_EXACT_DIAMETER.jsonに保存され、収録済みEXACT_DIAMETER_CHECKS.jsonを上書きしない。

今回の掃引の追加検査：

```powershell
python .\verify_sweep_lemma.py
```

結果はREPLAY_SWEEP_LEMMA.jsonに保存され、収録済みの結果を上書きしない。

旧版の単一始点距離・最短手順・操作分類の検査：

```powershell
python .\verify_backbite_proof.py --max-n 22
```

C++17コンパイラが既にある場合のみ、独立した有限基底の計算も任意で再現できる。コンパイラの新規導入は要求しない。

```text
g++ -O3 -std=c++17 verify_finite_bases.cpp -o verify_finite_bases
./verify_finite_bases 15 REPLAY_FINITE_BASES_CPP.jsonl
```

## 残る監査と公開状態

- General proof：v0.3に独立AI監査PASSの報告あり。v0.4の2点の補強は差分再監査待ち。
- Computation：v0.3に独立AI監査PASSの報告あり。収録証拠の範囲と追加内部検査の範囲を上記で区別。
- References：受領した独立監査はINCONCLUSIVE。一次資料の著者側照合記録を追加。
- Novelty：INCONCLUSIVE。
- Human peer review：未実施。
- Priority：未確認、主張なし。
- Publication：HOLD。GitHub・Zenodoへの公開操作はしていない。
- Rights：All rights reserved。

対象グラフは既知であり、ZigZag外平面グラフという名称の文献も確認した。グラフの発明、連結性、外周閉路の一意性、従来の数え上げを新規性に含めない。LITERATURE_AUDIT.mdを参照。

任意の2本を入力したときの正確な最短距離式までは主張しない。直径の厳密値と、任意点対の距離を返すアルゴリズムは区別する。

AUDIT_GUIDE.mdに差分再監査の重点をまとめた。旧ログ内のexternal_independent_proof_audit=falseは、その計算記録の作成時点の表示であり、改変せずに保持した。同じ助手による追加検査を別AIの独立監査とは呼ばない。
