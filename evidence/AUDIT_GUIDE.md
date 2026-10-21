# No.31 v0.4 — 凍結前の最終差分監査ガイド

対象：PROOF.md、主定理Theorem D。
必要な旧版の定義・下界・単一始点距離証明はPROOF.md内に統合済み。
v0.3への独立AI監査報告を受領済み。PROOF=PASS（軽微2点）、COMPUTATION=PASS、REFERENCES=INCONCLUSIVE、NOVELTY=INCONCLUSIVE。原報告はINDEPENDENT_AI_AUDIT_v0_3.md。以下の変更を含むv0.4に、判定を自動で移さない。

## 今回の差分監査の重点

1. §9 Case 3：G≥3からG≤B−A+1、B−A≥2、両方の端点スパン≥2、τ(H)=τ(J)=0へ至る理由を追記した。Case 4はこの理由を参照する。
2. §6.3：左内向き・左外向き・右内向き・右外向きの4段階を明記した。各中間状態の表示条件、折返し位置の非超過、同じ側の旧交換を全て消してから目標交換を作る順序、反対側との3間隔を確認してほしい。
3. 同節の手数表：通常の交換では2手、境界の交換では1手を節約する。境界位置1が左、n−3が右に必ず割り当てられ、4つのδが対応する段階に1回ずつ入ること、和が従来どおりUとなることを確認してほしい。
4. 文献：LITERATURE_AUDIT.mdの一次資料・節・ページを、監査者自身で確認してほしい。今回こちらで取得できたことだけを根拠に、前回の独立監査のREFERENCESをPASSへ変更しない。

verify_sweep_lemma.pyとSWEEP_LEMMA_CHECKS.jsonはこの差分の追加内部検査。継承コードを使うため第三者の独立実装とは呼ばない。v0.3の全コードと計算証拠は原バイトで保持し、PROVENANCE.jsonにSHA256を記録した。独立監査者のap.cpp / proofcheck.pyや生ログは未受領。

## 主張

P_n^2上のHamilton道のbackbite再構成グラフについて、n≥10の直径がTheorem Dの3項の最大値に等しい。n≥16の上界は一般証明、n=3..15は全点対BFSの有限基底を明示。

## 全体を再確認する場合の従来の重点

1. 全Hamilton道がcurlと3間隔の隣接交換で一意に表せるか。
2. Theorem Aの最短距離関数が全backbiteで1-Lipschitzか。a=2の境界ジャンプ、core上の回転、空集合の場合を落としていないか。
3. Lemma 7.1：非coreの両端に、高さを1減らし、互いに異なる外周辺を追加する2手が常にあるか。これにより欠辺集合M(H)の全てを最短core到達先にできるという帰納法は正しいか。
4. Lemma 7.2：2つの欠辺集合が交わる場合と、外周の循環順序で離れる場合の上界max(n−1,h(H)+h(J))。coreを等長部分グラフと仮定していないか。
5. Lemma 8.1：切り上げ平方根の欠損量c(n)が0または1しか増えない証明。特にt=2、q≥9、有限算術表10..21。
6. Section 9の容量式。SとTの和集合は3間隔ではない。u=|S|+|T|とv=|S union T|、境界補正Deltaとtの重複計数、eとfの相違を確認。
7. Section 9のn−e<10の場合が、n≥16でL_n≥n+2を使って閉じるか。高さ式のtauと境界補正を落としていないか。
8. n=3..15の実際の全点対BFS。Pythonはprefix reversal、C++は追加辺の接続先に接する辺の削除・次数・連結性による別実装。同じ欠陥を共有していないか。

## 計算の読み分け

- EXACT_DIAMETER_CHECKS.json：有限基底、全状態のcore到達先、サンプル対、整数不等式の検査。
- FINITE_BASES_CPP.jsonl：独立した隣接構成による全点対BFSの有限基底。
- ROOT_BFS_CPP.jsonl：旧版のn≤32単一始点距離。全点対直径の計算記録ではない。
- COMPARISON.csv：旧実測直径と一般定理の値を区別。
- SWEEP_LEMMA_CHECKS.json：v0.4の追加内部検査。全点対直径の再計算ではない。
- SHA256SUMS.txt：一式のハッシュ。

再現はREADME.mdのPythonコマンドで可能。外部API、追加パッケージ、コンパイラ新規導入は不要。Windowsで実行したとの主張はしていない。

## 先行・claim監査

Kazazi arXiv:2610.05068v1との一手の定義を照合する。一般のedge flipとbackbiteは距離が異なり得る。
ZigZag外平面グラフとHamilton道の数え上げはBiswasほか(COCOA 2012)にあるため、ホストグラフや列挙の発明として評価しない。
距離・直径の既知の等価な定式化や直接帰結がないかを別に確認する。

望む監査結果は、PROOF / COMPUTATION / REFERENCES / NOVELTYを分けたPASS・FAIL・INCONCLUSIVE。未実行・未確認の工程をPASSとせず、欠陥がある場合は具体的な反例または最初の無効な推論を示す。

v0.3の独立AI監査結果と、未監査のv0.4差分を区別する。優先権主張なし、人間査読なし、AI-assisted research、All rights reserved。凍結・GitHub公開・Zenodo登録はこの作業に含まない。
