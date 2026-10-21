# 一次資料の照合記録 — v0.4

照合日：2026-10-22（日本時間）／2026-10-21（UTC）。

**受領したv0.3独立監査のREFERENCES=INCONCLUSIVEは維持する。**
以下は本助手による一次資料の照合記録。監査者側での一次資料確認やv0.4差分再監査は未実施。NOVELTYもINCONCLUSIVE。

## 1. Kazazi

Albi Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*,
arXiv:2610.05068v1, 4 October 2026.

一次本文：
https://arxiv.org/html/2610.05068v1

| 照合対象 | 本文で確認する箇所 |
| --- | --- |
| backbite一手と逆向き同一視 | §1の最初の2段落。こちらの0始まりのk≥2は、本文の1始まりのk≥3に対応 |
| edge flipとの差 | §1、backbite以外のflipを閉路の回転で実現する段落。到達可能性の一致から距離の一致を推論しない |
| 外周Hamilton閉路の一意性 | Lemma 4.2 |
| P_n²自体での上界 | Proposition 5.1と§5の末尾 |

The primary text gives connectivity and an O(n²) diameter bound under a
spanning squared-path hypothesis, and O(n) for P_n² itself. Its final
open-problem sentence concerns the general bound; it does not explicitly
pose this special family's closed-form diameter as a separate problem.

確認範囲は取得できたv1。最新版・後続研究全件を確認したとは表示しない。上記は既知の土台として扱い、新規性に含めない。

## 2. Biswas・Durocher・Mondal・Nishat

*Hamiltonian Paths and Cycles in Planar Graphs*, COCOA 2012,
LNCS 7402, pp.83–94.

出版社の書誌：
https://link.springer.com/chapter/10.1007/978-3-642-31770-5_8

DOI：
https://doi.org/10.1007/978-3-642-31770-5_8

著者公開本文（全12ページ）：
https://www.cs.usask.ca/faculty/dmondal/Papers/COCOA12.pdf

| 照合対象 | 著者PDFのページ・箇所 |
| --- | --- |
| 外周に沿う道の一意性 | p.3、§2 Fact 1 |
| ZigZagの定義 | p.7、§3のStep 2。弱双対の道で子の左右が交互 |
| child flip / parent flip | pp.7–8。ホストグラフを変える操作で、固定ホスト上のbackbiteとは区別 |
| 従来の数え上げ | pp.8–9、Step 3と次数2の頂点を始点とする漸化式 |

照合上の推論：P_n²の三角形{i,i+1,i+2}を外周埋め込みで順に並べると、弱双対は交互の道になり、同資料のZigZag族に対応する。グラフ族、外周の一意性、既存の列挙パターンを本研究の新規性に含めない。

## 3. v0.3から継承するその他の候補（今回の追加照合対象外）

前回の照合記録ではWeighted Padovan graphs（Iršič Chenowethほか、
arXiv:2409.17318v1）と、Wei–Yang, *On a conjecture of Eǧecioǧlu and
Iršič*, arXiv:2401.14610v1を参照した。

- https://arxiv.org/html/2409.17318v1
- https://arxiv.org/abs/2401.14610

本研究のR_nは奇数nでcoreの奇閉路を含む。これはmedian graphや誘導hypercubeとの直接同型をその次数で除くための内部推論であり、商・拡張・既知定理の帰結まで排除するものではない。

v0.3の検索語はHamiltonian path reconfiguration / backbite / Pósa rotation /
path square / squared paths / outerplanar / ZigZag / flip graph /
adjacent transpositions / exact diameter / lamplighter。
今回、新たな包括的新規性検索を完了したとの主張はしない。

## 4. 留保

独立監査者が資料にアクセスできなかった事実と、今回こちらで取得できた事実を区別する。同一結果が検索で見つからないことは新規性の証明ではない。別表現の既知定理からの直接帰結の包括的監査は未完了。優先権は未確認で、主張しない。
