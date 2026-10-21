# No.31 v0.4 — 一次文献の再照合

2026-10-22（日本時間）。照合者：本助手。
独立AI監査者のREFERENCES=INCONCLUSIVEは維持する。
この記録は対象となる引用・既知結果の照合範囲を示す。

## Kazazi

Albi Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*,
arXiv:2610.05068v1（2026-10-04）。

https://arxiv.org/html/2610.05068v1

| 対象 | 一次本文での位置・確認結果 |
| --- | --- |
| 一手の定義、反転同一視 | §1冒頭。0始まりのk≥2と1始まりのk≥3が対応 |
| edge flip | §1。同一の到達可能性から同じ距離は主張しない |
| 外周閉路 | Lemma 4.2。一意性は既知結果として扱う |
| 既存の上界 | Theorem 1.1は一般のO(n²)、Proposition 5.1と§5末尾はP_n²でO(n) |

短い原文抜粋（§5）：

> Proposition 5.1 costs O(n) backbites

一般上界についての厳密最悪回数の課題と、この特殊クラスの閉形式を区別する。取得したv1で本研究の厳密式を確認できなかったことだけでは、新規性の確定にはならない。

## Biswasほか

Sudip Biswas, Stephane Durocher, Debajyoti Mondal, Rahnuma Islam Nishat,
*Hamiltonian Paths and Cycles in Planar Graphs*, COCOA 2012,
LNCS 7402, pp.83–94.

著者本文：
https://www.cs.usask.ca/faculty/dmondal/Papers/COCOA12.pdf

出版社：
https://link.springer.com/chapter/10.1007/978-3-642-31770-5_8

| 対象 | 著者PDFでの位置・確認結果 |
| --- | --- |
| 書誌 | 表紙、出版社の著者・年・会議・巻・ページ・DOIと一致 |
| 外周の道 | p.3、Fact 1 |
| 既知のグラフ族 | p.7、§3 Step 2、ZigZag定義 |
| 操作の違い | pp.7–8、child flip / parent flipはホストを変更する |
| 既存の列挙 | pp.8–9、Step 3、次数2を始点とする漸化式 |

短い原文抜粋（p.7）：

> We then call G a ZigZag outerplanar graph.

P_n²とZigZagの対応は、三角形列{i,i+1,i+2}と交互の弱双対を使う本助手側の定義照合である。ホストグラフ族や既存の数え上げを本研究の新規性に含めない。

## 限界と今回の追加検索

本助手は上記の引用対応を確認した。監査者本人による一次資料との突き合わせは未確認のまま。資料を取得できなかったという留保を、引用に誤りを発見したという判定へ読み替えない。

追加検索語：

- "backbite" "diameter" "squared paths"
- "ZigZag" "Hamiltonian" "reconfiguration" diameter
- "Hamiltonian paths" "backbite" "exact diameter"

この検索でも同一の厳密式を確認できなかったが、文献全件や等価な別定式化を網羅したものではない。NOVELTY=INCONCLUSIVE、優先権主張なし。
