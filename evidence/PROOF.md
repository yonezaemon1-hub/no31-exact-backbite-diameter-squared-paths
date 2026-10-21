# Exact Backbite Diameter of Squared Paths

Ryutaro Yonezu — Yonezu Research Lab  
yonezaemon1+research@gmail.com  
Working proof v0.4, 22 October 2026 (Japan). AI-assisted research. All rights reserved.

**Status:** a user-supplied independent AI audit of v0.3 reports PROOF=PASS
with two minor exposition issues and COMPUTATION=PASS. This v0.4 addresses
those issues; independent review of the revisions is pending. That audit's
REFERENCES and NOVELTY verdicts remain INCONCLUSIVE. Human peer review has
not been performed. This is not a frozen preprint or a public release. No
priority claim is made. The exact diameter is derived in Sections 7–10, with an
analytic proof for n >= 16 and exhaustive finite bases below that threshold.
The exact metric for two specified arbitrary paths is not claimed.

## 1. Setting and statements

The main result of this version is **Theorem D**: the exact diameter equals
$L_n$ for every $n\ge10$, with the seven smaller diameters listed explicitly.
Sections 2–5 establish the rooted-distance and lower-bound tools; Sections
7–9 close the arbitrary-pair upper bound. Section 10 discloses the finite
computational bases.

Let $G_n=P_n^2$ have vertex set $\{0,\ldots,n-1\}$ and edges $xy$ with
$0<|x-y|\le2$. A Hamiltonian path is identified with its reversal. A backbite
at the first endpoint of $p=(p_0,\ldots,p_{n-1})$ selects $k\ge2$ with
$|p_0-p_k|\le2$, adds $p_0p_k$, and deletes $p_{k-1}p_k$. Its new ordering is

$$ (p_{k-1},\ldots,p_0,p_k,\ldots,p_{n-1}). $$

In particular, joining the two endpoints does **not** permit an arbitrary
remote edge of the resulting cycle to be deleted in one move. Write $R_n$
for this backbite graph, $D_n$ for its diameter, and $I_n=(0,1,\ldots,n-1)$.

Kazazi [1] proves connectivity under a spanning squared-path hypothesis and
an $O(n^2)$ bound in that general setting. Proposition 5.1 and the last
paragraph of Section 5 give $D_n=O(n)$ for $P_n^2$ itself. We use the same
move convention. The following are the results derived in this working note;
their novelty relative to other formulations is not certified.

**Theorem A (rooted distance).** Every path has the unique normal form
$(a,b,S)$ defined below. If $S=\{s_1<\cdots<s_k\}$, put

$$\delta_L=\mathbf1_{\{a=0,\ k>0,\ s_1=1\}},\qquad
\delta_R=\mathbf1_{\{b=n-1,\ k>0,\ s_k=n-3\}}.$$

Define, for $0\le j\le k$,

$$ A_j=\begin{cases}a,&j=0,\\
2(s_j+1)-a-2j+\delta_L,&j>0,\end{cases} $$

$$ B_j=\begin{cases}n-1-b,&j=k,\\
b+n-1-2s_{j+1}-2(k-j)+\delta_R,&j<k.\end{cases} $$

Then, for all $n\ge3$,

$$\boxed{d_{R_n}(I_n,(a,b,S))=\min_{0\le j\le k}(A_j+B_j).}$$

The normal form, this value, and a list of shortest backbite instructions can
be obtained in $O(n)$ time from the path ordering. Writing out the entire
length-$n$ path after every instruction would instead take $O(n^2)$ space
and time. This is a single-source result; it is not an
exact distance formula for two arbitrary paths.

**Theorem B (exact extremum with fixed boundary endpoints).** For $n\ge10$,
the largest distance from $I_n$ to a path whose endpoints are $0,n-1$ is

$$\boxed{L_n=\max\left\{
2n+2-2\lceil2\sqrt n\rceil,\quad
2n+1-2\lceil2\sqrt{n-2}\rceil,\quad
2n-2\lceil2\sqrt{n-4}\rceil\right\}.}$$

Consequently $D_n\ge L_n$. Sections 7–10 prove the matching upper bound.
The complete exact statement is Theorem D in Section 10.

**Theorem C (two-term diameter estimate).** For $n\ge10$,

$$\boxed{2n-4\sqrt n\ \le D_n\ \le
\min\{2n-4,\ 2n-4\sqrt n+8\}.}$$

In particular $D_n=2n-4\sqrt n+O(1)$ and $D_n/n\longrightarrow2$.
The two upper bounds hold also for $3\le n<10$.

## 2. Unique normal form

Orient a path from its smaller endpoint $a$ to its larger endpoint $b$.
Define a left curl by

$$ C(0)=(0), $$

and, for $a>0$, let $C(a)$ descend from $a$ in steps of two to $0$ or $1$,
then ascend in the other parity from $1$ or $0$ to $a+1$.
For example $C(3)=(3,1,0,2,4)$ and $C(4)=(4,2,0,1,3,5)$.
The right curl is the reverse of the label reflection of $C(n-1-b)$.
Let

$$\ell=\begin{cases}0,&a=0,\\a+1,&a>0,\end{cases}\qquad
r=\begin{cases}n-1,&b=n-1,\\b-1,&b<n-1.\end{cases}$$

The path consists of the left curl, a middle ordering of $[\ell,r]$, and
the right curl, with shared junction vertices written only once. Its middle
ordering is increasing except for adjacent swaps $(s,s+1)\mapsto(s+1,s)$,
where

$$ S\subseteq\{\ell+1,\ldots,r-2\},\qquad
|s-t|\ge3\quad(s\ne t). $$

The allowed endpoints have $b-a\ge2$, or are $(0,1)$ or $(n-2,n-1)$.
These rules give a bijection between admissible triples and all paths.

To prove necessity of the left curl, suppose $a>0$. Vertex $0$ is not an
endpoint, so its two edges $01,02$ are forced. Inductively, suppose the
forced edges form a path on $\{0,\ldots,t\}$ with endpoints $t-1,t$.
As long as $t-1<a$, vertex $t-1$ is not a path endpoint. Its remaining
neighbor cannot be $t$, which would close a cycle, and cannot have a label
below $t-1$, whose relevant degrees are already used. Its remaining edge is
therefore $(t-1)(t+1)$. Continue until the forced path has endpoints $a,a+1$.
This is exactly $C(a)$. Reflection proves the right-curl assertion.
Two consecutive interior endpoints are impossible, since removing them from
the host disconnects the vertices below and above them, whereas deleting
both endpoints of a Hamiltonian path leaves a connected path. The permitted
endpoint cases make the curls disjoint or sharing one junction.

For the middle, consider a path on $[x,y]$ with endpoints $x,y$.
If its first edge is $x(x+1)$, remove $x$ and repeat. If it starts
$x,x+2$, vertex $x+1$ is internal and cannot use $x$ again. Its two edges
are forced to be $(x+1)(x+2)$ and $(x+1)(x+3)$. The start is consequently
$x,x+2,x+1,x+3$. Remove the first three vertices and repeat. Thus the middle
is a concatenation of single increasing vertices and blocks $(x,x+2,x+1)$.
The swap positions in distinct blocks differ by at least three. Conversely,
every ordering described above is a Hamiltonian path of $G_n$.

## 3. Moves in the normal form

Every backbite is one of the following moves, its inverse, its reflection,
or a rotation on the core cycle described at the end of this section.

* An outward unit move changes $(a,b,S)$ to $(a-1,b,S)$ for $a\ge1$.
* For $a\ge3$, an outward insertion changes
  $(a,b,S)$ to $(a-3,b,\{a-1\}\cup S)$.
* For $a=2$, the boundary insertion changes
  $(2,b,S)$ to $(0,b,\{1\}\cup S)$.

For completeness, inspect the possible targets of a backbite at $a$.
When $a\ge2$, the edge to $a-2$ is already used in its curl. The target
$a+1$ gives the outward unit move. The target $a-1$ gives the insertion
when $a\ge3$, the boundary insertion when $a=2$, and is already used when
$a=1$. The target $a+2$ gives an inward unit move or an inward deletion of
the first swap. At $a=0$ the only eligible unused target gives the inverse
of a unit or insertion move. The order of the endpoints changes only when
closing the unique spanning cycle. This accounts for all targets in
$N_{G_n}(a)$, and reflection treats $b$.

The unique spanning cycle is

$$ C_n=(0,2,4,\ldots,\text{largest even},
\text{largest odd},\ldots,3,1,0). $$

Uniqueness follows by the same forced-degree induction used for a curl,
now with no endpoints. A path with adjacent host endpoints is $C_n-e$ for
a cycle edge $e$. These $n$ paths form a cycle of allowed backbites:
successive rotations move the missing edge to its neighboring cycle edge.
Call these paths the core. Their normal forms have $S=\varnothing$ and
$b-a=2$, or endpoints $(0,1)$ or $(n-2,n-1)$.

This classification also checks that the boundary jump has displacement
two rather than three. Omitting this exception produces wrong distances.

## 4. Proof of Theorem A

Let $F(a,b,S)=\min_j(A_j+B_j)$.

### 4.1 A route of length F

Choose a split $j$. Move the left endpoint inward until it has consumed
$s_1,\ldots,s_j$, and then move it outward to $0$ using unit moves only.
If $j>0$, the turning point is $s_j+1$. Consuming a swap normally advances
the endpoint by three in one move, saving two moves compared with unit
travel. The swap at $1$ when the initial endpoint is $0$ advances it by two
instead, giving the correction $\delta_L$. This costs exactly $A_j$.
If $j=0$, simply move $a$ outward to $0$, costing $a$.

Use the right endpoint symmetrically to consume the remaining swaps and
return to $n-1$. This costs $B_j$. The separation of successive swaps by
at least three ensures that the first sweep never touches the unprocessed
swaps. The final path has endpoints $0,n-1$ and no swaps, hence is $I_n$.
Thus $d(I_n,H)\le F(H)$.

### 4.2 No route can be shorter

We show that $F$ changes by at most one on every edge of $R_n$.
Since $F(I_n)=0$, this implies $F(H)\le d(I_n,H)$.

For an outward unit move each candidate $A_j+B_j$ changes by $-1$ for
$j=0$ and by $+1$ for $j>0$. The boundary indicator stays unchanged:
when $a=1$ the old admissible swaps start at $3$ or later. Taking minima
therefore preserves the one-Lipschitz property.

Consider an outward insertion with $a\ge3$. Write $H'$ for the new path.
For every old split $j$, the new split $j+1$ has cost exactly
$A_j(H)+B_j(H)+1$. The additional new split $0$ has cost

$$ E=b+n-1-a-3-2k+\delta_R(H'). $$

If $k>0$, the largest swap and $\delta_R$ are unchanged, and

$$ E-[A_0(H)+B_0(H)]=2(s_1-a)-3\ge1. $$

Thus in this case $F(H')=F(H)+1$. If $k=0$, then $F(H)=a+n-1-b$ and

$$ E-F(H)=2(b-a)-3+\delta_R(H')\ge-1. $$

Together with the candidates of cost $F(H)+1$, this gives
$F(H)-1\le F(H')\le F(H)+1$.

For the boundary insertion at $a=2$ the same shift of splits again adds
one to every old candidate. The extra candidate is
$E=b+n-1-4-2k+\delta_R(H')$. If $k>0$, its excess over the old split $0$
is $2s_1-6\ge2$. If $k=0$, its excess over $F(H)$ is
$2b-6+\delta_R(H')\ge0$. This proves the same Lipschitz bound.

Reflection preserves $I_n$ as an unoriented path, so right moves follow.
Finally, on the core, $F=n-3$ except at the two missing boundary edges
$01,(n-2)(n-1)$, where $F=n-2$. Core rotations also change $F$ by at most
one. The move classification in Section 3 covers every edge, proving the
lower bound and Theorem A. Scanning the $k+1$ splits takes linear time;
the specified sweeps output the shortest instruction list in linear time as
well. Keep the swap positions in order and update endpoint indices. An
outward unit at $a$ targets $a+1$; an outward insertion targets $a-1$.
An inward step targets $a+2$, except for consuming the boundary swap at
one from endpoint zero, which targets one. Reflection gives the right
instructions. This avoids explicitly reversing a length-$n$ array at each
move. The supplied verifier favors clarity and retains full states rather
than implementing this compressed linear-time output.

## 5. Proof of Theorem B

Fix endpoints $0,n-1$ and a nonempty swap set of size $k$. Define gaps

$$ g_0=s_1+1,\quad g_i=s_{i+1}-s_i\ (1\le i<k),\quad
g_k=n-1-s_k. $$

Their sum is $n$, the boundary gaps are at least two, and the interior
gaps are at least three. Here $\delta_L=\mathbf1_{g_0=2}$ and
$\delta_R=\mathbf1_{g_k=2}$. Theorem A becomes

$$ d(I_n,H)=2n-2k-\max\{2g_0-\delta_R,
2g_k-\delta_L,\ 2g_i-\delta_L-\delta_R\ (0<i<k)\}. $$

There are three cases according to the number of boundary gaps equal to
two. In each case distribute the remaining sum as evenly as possible:

* Neither boundary gap is two: the optimum for fixed $k$ is
  $2n-2k-2\lceil n/(k+1)\rceil$, with $3(k+1)\le n$.
* Exactly one is two: it is
  $2n-2k-2\lceil(n-2)/k\rceil+1$, with $3k\le n-2$.
* Both are two: it is
  $2n-2k-2\lceil(n-4)/(k-1)\rceil+2$, with $3(k-1)\le n-4$.

All these values are attainable by valid gap vectors, hence by paths.
For integer $N\ge6$,

$$\min_{1\le m\le\lfloor N/3\rfloor}
\left(m+\left\lceil\frac Nm\right\rceil\right)=\lceil2\sqrt N\rceil.$$

The lower bound is AM–GM. For attainment let $q=\lceil2\sqrt N\rceil$.
The integers $\lfloor q/2\rfloor,\lceil q/2\rceil$ have product
$\lfloor q^2/4\rfloor\ge N$. For $N\ge12$ the smaller one is at most
$\sqrt N+1/2\le N/3$, and is therefore allowed. For $6\le N\le11$,
$m=2,2,2,3,3,3$, respectively, attains the lower bound. The minimizer is
also at least two, as required in the first gap case.

Substitute $m=k+1,k,k-1$ into the three cases. For $n\ge10$ all three
remaining sums meet the lemma's hypotheses. This proves exactly the three
terms in $L_n$. The empty swap set has distance zero and does not affect
the maximum. The first term alone gives $D_n\ge L_n\ge2n-4\sqrt n$.

## 6. Two constructive upper bounds

### 6.1 The bound 2n-4

Let $K_L=C_n-01$ and $K_R=C_n-(n-2)(n-1)$. For $H=(a,b,S)$ define

$$ \lambda(H)=a+b-1-2k+\delta_R,\qquad
\rho(H)=2n-3-a-b-2k+\delta_L. $$

To reach $K_L$, first move the left endpoint outward to zero, then sweep
the right endpoint inward to one, consuming every swap. The cost is
$\lambda(H)$. The reflected construction costs $\rho(H)$ to reach $K_R$.
These are route lengths, not asserted exact distances to these cores.
Their sum is

$$ \lambda(H)+\rho(H)=2n-4-4k+\delta_L+\delta_R\le2n-4. $$

For any two paths use either the common core $K_L$ or the common core $K_R$.
The smaller of the two route lengths is at most their average, giving
$d(H,J)\le2n-4$.

### 6.2 A short route to some core

Hold the smaller endpoint $a$ fixed and move the larger endpoint inward,
consuming all swaps until the two endpoints are host-adjacent. Each normal
deletion saves two unit moves. The deletion at the right boundary saves
only one ($\delta_R$). If the first swap is at one and $a=0$, the final
core has endpoints $0,1$ instead of $0,2$, adding one unit of displacement
($\delta_L$). If the path already has consecutive boundary endpoints,
the empty route is used. Thus a route to some core has length

$$ q(H)=b-a-2-2k+\delta_L+\delta_R+\tau(H),\qquad
\tau(H)=\mathbf1_{b-a=1}. $$

Notice that $\delta_L+\delta_R+\tau\le2$. The indicator $\tau$ only occurs
for an already-core path with no swaps. Any two core paths can be joined
by at most $\lfloor n/2\rfloor$ rotations.

### 6.3 Separated sweeps for two paths

Let $H=(a,b,S)$ and $J=(c,d,T)$, and put

$$ u=|S|+|T|,\quad X=S\cup T,\quad
A=\max(a,c),\quad B=\min(b,d),\quad
f=a+c+(n-1-b)+(n-1-d). $$

For each split of the ordered set $X$ into a left and a right part, let

$$ h=\max(A,\ \max(X_{\rm left})+1),\qquad
z=\min(B,\ \min(X_{\rm right})), $$

omitting a set-dependent term if its part is empty. Define its clearance
$g=z-h+1$, and let $G$ be the maximum clearance over all splits.
If $A\le B$, the positive clearances partition the integer interval
$[A,B]$ into at most $|X|+1\le u+1$ pieces. Consequently

$$ G\ge\frac{B-A+1}{u+1}\ge\frac{n-f}{u+1}. \tag{1} $$

The last inequality uses $f\ge n-(B-A+1)$.

Suppose $G\ge3$ and choose a split attaining it. Write
$S_L=S\cap X_{\rm left}$, $S_R=S\cap X_{\rm right}$, and similarly
$T_L,T_R$. The definitions give

$$ a,c\le h\le z-2\le b-2,d-2,\qquad
\max X_{\rm left}\le h-1,\qquad \min X_{\rm right}\ge z, $$

where an assertion about an empty set is omitted. We construct four
successive legs and verify each intermediate normal form.

**Left inward leg.** Hold $b$ fixed and advance the left endpoint $x$
from $a$ to $h$. Apply the inward moves of Section 3: delete the first
remaining swap $i=x+2$ by advancing to $i+1=x+3$; at $x=0,i=1$ advance
to $2$ instead; otherwise advance by one. These moves consume $S_L$ in
increasing order. A deletion of a left swap ends at $i+1\le h$, so it
does not overshoot $h$. No right swap is consumed, because its position
is at least $z\ge h+2$. The remaining swaps retain their original
three-spacing. On a unit step the first remaining swap is at least $x+3$,
which is the lower bound at the new endpoint $x+1$. After deleting
$i=x+2$, the next swap is at least $i+3=x+5$, the lower bound at $x+3$.
After the boundary deletion of $1$, the next swap is at least $4$,
the lower bound at endpoint $2$. Thus the lower admissibility bound is
preserved in all three cases. Since $x\le h\le b-2$, the ordered endpoints never cross
and the upper admissibility bound is unchanged. At $x=h$ no left swap
can remain: an admissible swap there would have position at least
$h+2$ (at least $1$ if $h=0$), whereas every left swap is at most $h-1$.
The resulting code is $(h,b,S_R)$.

**Left outward leg.** Hold $b$ fixed and move from $h$ to $c$, creating
the swaps of $T_L$ in decreasing order. For a prescribed swap $i$,
use outward unit moves until the endpoint is $i+1$, then insert $i$:
the new endpoint is $i-2$ if $i\ge2$, and is $0$ if $i=1$. Both are
the insertion moves of Section 3. Target admissibility gives $i-2\ge c$
when $i\ge2$, and $i=1$ requires $c=0$. Successive prescribed swaps
differ by at least three, so an insertion cannot skip the next insertion
position. Newly created left swaps are three-separated from one another
and from $S_R$, since
$\min S_R-\max T_L\ge z-(h-1)\ge3$ when both sets are nonempty.
Each new swap satisfies the current lower admissibility bound, with the
stated boundary exception; subsequent outward motion only relaxes that
bound. Its upper bound follows from $i\le h-1\le b-3$.
Thus every intermediate code is admissible. The leg ends at
$(c,b,T_L\cup S_R)$.

**Right inward and outward legs.** Reflect the labels by $i\mapsto n-1-i$
and apply the same two constructions. The right endpoint moves from
$b$ to $z$, deleting $S_R$ in decreasing order, and then from $z$ to $d$,
creating $T_R$ in increasing order. Throughout these legs the left
endpoint is $c\le h\le z-2$, and retained left swaps have position at
most $h-1\le z-3$. The reflected admissibility and non-overshoot arguments
therefore apply at every step. The final code is $(c,d,T_L\cup T_R)=J$.

This also handles close positions in $S\cup T$: all old swaps on a side
are deleted before any target swap on that side is inserted. No
three-spacing property of the union is used.

For the exact count, put
$\Delta=\delta_L(H)+\delta_R(H)+\delta_L(J)+\delta_R(J)\le4$.
A swap at $1$ must belong to $X_{\rm left}$: assigning it to the right
would give $z\le1$, hence $g\le2$. Likewise a swap at $n-3$ must belong
to $X_{\rm right}$, since assigning it to the left would give
$h\ge n-2$, again $g\le2$. Thus all four boundary indicators are charged
on precisely the legs that encounter the corresponding boundary swap.
Every ordinary deletion or insertion covers displacement three in one
move, saving two moves; a boundary operation covers displacement two
in one move, saving one. All other moves cover displacement one.
Consequently the four lengths are exactly

| Leg | Length |
| --- | --- |
| Left inward | $h-a-2\lvert S_L\rvert+\delta_L(H)$ |
| Left outward | $h-c-2\lvert T_L\rvert+\delta_L(J)$ |
| Right inward | $b-z-2\lvert S_R\rvert+\delta_R(H)$ |
| Right outward | $d-z-2\lvert T_R\rvert+\delta_R(J)$ |

An empty leg has length zero by the same count. Adding these expressions
gives $2h-a-c+b+d-2z-2u+\Delta$. Substituting
$G=z-h+1$ and the definition of $f$ gives the actual route length

$$ U=2n-f-2u-2G+\Delta. \tag{2} $$

If $u\ge1$, (1) and (2) imply

$$ U\le2n-2u-\frac{2n}{u+1}
-\frac{u-1}{u+1}f+4
\le2n+6-2\left((u+1)+\frac n{u+1}\right)
\le2n-4\sqrt n+6. $$

If $u=0$, the same route consists just of endpoint unit moves and has
length $|a-c|+|b-d|$. Since the two endpoint intervals overlap in a span
of at least two when $G\ge3$, this length is at most $n-3$, which is also
at most $2n-4\sqrt n+8$.

### 6.4 No separating clearance

If $G<3$, then $B-A+1\le2(u+1)$; the inequality is also automatic if
$A>B$. Thus $f\ge n-2u-2$. Use the compact routes in Section 6.2 and
rotate between their cores. Since
$(b-a)+(d-c)=2n-2-f$, their combined length is at most

$$ q(H)+q(J)+\lfloor n/2\rfloor
\le2n-2-f-2u+\lfloor n/2\rfloor
\le n+\lfloor n/2\rfloor. $$

Finally,

$$ \frac{3n}{2}\le2n-4\sqrt n+8,
\qquad
2n-4\sqrt n+8-\frac{3n}{2}=
\tfrac12(\sqrt n-4)^2\ge0. $$

This handles the case with no clearance as well. Combined with Section
6.3, it proves the square-root upper bound and Theorem C.

## 7. Height and all shortest projections onto the core

For a path $H$, let

$$ h(H)=|E(H)\setminus E(C_n)|,\qquad
M(H)=E(C_n)\setminus E(H). $$

Since a path has $n-1$ edges and the cycle has $n$ edges,

$$ |M(H)|=h(H)+1. \tag{3} $$

For the normal form $H=(a,b,S)$, write $k=|S|$ and use the indicators of
Theorem A. Directly counting the noncycle edges gives

$$ h(H)=b-a-2-2k+\delta_L+\delta_R+\tau(H),\qquad
\tau(H)=\mathbf1_{b-a=1}. \tag{4} $$

Indeed, the curls use only cycle edges. Before the middle swaps, there are
$b-a-2$ internal consecutive-label edges when $b-a\ge2$. Each swap removes
two such edges, except that a swap at one or at $n-3$ removes one cycle
edge instead of one internal edge. For the two paths with endpoint span
one, $\tau$ corrects the expression to zero. In particular,
$\delta_L+\delta_R+\tau\le2$.

**Lemma 7.1 (all monotone projections).** For every $e\in M(H)$ there is a
route of exactly $h(H)$ backbites from $H$ to $C_n-e$, each decreasing
height by one. Conversely, a route of $h(H)$ moves from $H$ to a core path
can end at $C_n-e$ only if $e\in M(H)$.

**Proof.** A move can remove at most one noncycle edge, so at least $h(H)$
moves are needed to reach height zero. At a noncore path there are two
inward moves, one at each endpoint. Each adds a missing cycle edge and
removes a noncycle edge. Their added edges are distinct.

To check this last assertion explicitly, at the smaller endpoint $a$ the
inward target is $a+2$, except that $a=0$ with a swap at one uses target
one. The deleted edge is respectively $(a+1)(a+2)$ or $(a+2)(a+3)$,
or $12$ in the boundary exception. These are noncycle edges. Reflection
gives the move at $b$. Away from the boundary exceptions, the added edges
could agree only if $b=a+2$, which is already a core path. A boundary
exception adds $01$ or $(n-2)(n-1)$ and cannot agree with the other inward
move on a noncore path.

Fix the desired missing edge $e$. Choose one of the two inward moves
whose added edge is not $e$. The new missing set still contains $e$, and
the height drops by one. Induction ends at $C_n-e$ after $h(H)$ moves.
For the converse, a route of exactly $h(H)$ moves must decrease height at
every move, so it never removes a cycle edge already present in $H$.
Its final missing cycle edge must therefore have been missing initially.
This proves the lemma. $\square$

The lemma concerns projections onto the core, not an isometric embedding
of the core cycle into $R_n$. Such an embedding is not assumed.

**Lemma 7.2 (projection upper bound).** For any paths $H,J$, put
$Q=h(H)+h(J)$. Then

$$ d(H,J)\le\max\{n-1,Q\}. \tag{5} $$

**Proof.** If $M(H)\cap M(J)$ is nonempty, use the same core path as the
projection of both paths and apply Lemma 7.1. This costs $Q$.
Otherwise the two missing sets have total size $Q+2\le n$. In the cyclic
order of the cycle's edges, choose consecutive elements belonging to
different missing sets. The intervening arc contains at most
$n-(Q+2)$ edges belonging to neither set. The number of core rotations
between its two ends is at most $n-Q-1$. Project to these two core paths,
rotate along this arc, and reverse the other projection. The total cost
is at most $Q+(n-Q-1)=n-1$. $\square$

## 8. The rounded deficit changes by at most one

For $n\ge10$ define $c(n)=2n-L_n$ and

$$ c_t(n)=2\lceil2\sqrt{n-2t}\rceil+t-2\quad(0\le t\le2),
\qquad c(n)=\min_{0\le t\le2}c_t(n). $$

**Lemma 8.1.** For every integer $n\ge10$,

$$ 0\le c(n+1)-c(n)\le1. \tag{6} $$

**Proof.** Each $c_t$ is nondecreasing, so their minimum is nondecreasing.
If the minimum at $n$ is attained by $t=0$, then

$$ c(n+1)\le c_1(n+1)
=2\lceil2\sqrt{n-1}\rceil-1\le c_0(n)+1. $$

If it is attained by $t=1$, use
$c(n+1)\le c_2(n+1)=2\lceil2\sqrt{n-3}\rceil\le c_1(n)+1$.

It remains to consider a minimum attained by $t=2$. For $n\ge21$, put
$q=\lceil2\sqrt{n-4}\rceil\ge9$. Then

$$ n+1\le\lfloor q^2/4\rfloor+5
\le\lfloor(q+1)^2/4\rfloor, $$

because successive floors on the right differ by at least five for
$q\ge9$. Hence
$c(n+1)\le c_0(n+1)\le2(q+1)-2=2q=c_2(n)$.
The remaining transitions $10\le n\le20$ follow directly from

$$
\begin{array}{c|rrrrrrrrrrrr}
n&10&11&12&13&14&15&16&17&18&19&20&21\\\hline
c(n)&10&11&12&12&13&14&14&15&15&16&16&17
\end{array}
$$

This proves (6). $\square$

Two consequences used below are

$$ L_n\ge n\quad(n\ge10),\qquad L_n\ge n+2\quad(n\ge16), \tag{7} $$

since $L_{10}=10$, $L_{16}=18$, and (6) implies
$L_{n+1}-L_n\ge1$. Also, whenever integers $e\ge0$ and $n-e\ge10$,

$$ c(n)\le e+c(n-e). \tag{8} $$

## 9. Exact upper bound for every n >= 16

Use the two normal forms and notation of Section 6.3:

$$ H=(a,b,S),\ J=(c,d,T),\quad u=|S|+|T|,\quad X=S\cup T,
\quad v=|X|,\quad A=\max(a,c),\ B=\min(b,d). $$

Write $C=n-1-B$ for the largest fold from the right, and retain

$$ f=a+c+(n-1-b)+(n-1-d),\qquad G=\max(z-h+1). $$

Here $G$ is the largest clipped clearance over the splits of $X$ described
in Section 6.3. Let

$$ t_L=\mathbf1_{1\in X},\quad t_R=\mathbf1_{n-3\in X},\quad t=t_L+t_R,
\quad \Delta=\delta_L(H)+\delta_R(H)+\delta_L(J)+\delta_R(J). $$

Because $n\ge16$, the two boundary positions are distinct. Every boundary
indicator is the occurrence of one boundary swap. Consequently

$$ \Delta\le u,\qquad 2u-\Delta\ge2v-t. \tag{9} $$

For the second inequality, write $u-v=|S\cap T|$. A boundary position
occurring in both paths contributes twice to $\Delta$, once to $t$, and
once to $|S\cap T|$. Thus $\Delta-t$ is at most $u-v$.

**Clipped capacity.** Suppose $G\ge3$. Define the nonnegative integer

$$ e=A+C-t_L\min(A,2)-t_R\min(C,2),\qquad 0\le e\le f. $$

Then

$$ n-e-2t\le(v+1-t)G. \tag{10} $$

To prove (10), partition the integer interval $[0,n-1]$ using the full
gaps of the ordered set $X$, with the same convention as in Section 5.
There are $v+1$ gaps in total. Clip them to $[A,B]$; their lengths sum to
$n-A-C$, and every clipped gap has length at most $G$. If $t_L=1$, the
first full gap has length two and its clipped length is at most
$\max(0,2-A)$. If $t_R=1$, the last clipped gap has length at most
$\max(0,2-C)$. Bound every other gap by $G$ and add back $A+C$ to obtain

$$ n\le(v+1-t)G+2t+e. $$

This argument does not require the union $X$ to have three-separated
positions. The individual sets $S,T$ have that separation; their union
need not have it.

We now show $d(H,J)\le L_n$ by cases.

**Case 1: $G<3$.** As in Section 6.4,
$f\ge n-2u-2$. Equation (4) gives

$$ Q=h(H)+h(J)=2n-6-f-2u+\Delta+\tau(H)+\tau(J)\le n, $$

using $\Delta+\tau(H)+\tau(J)\le4$. Lemma 7.2 and (7) imply
$d(H,J)\le n\le L_n$.

**Case 2: $G\ge3$ and $u=0$.** The separated sweep uses only unit endpoint
moves, with length $|a-c|+|b-d|\le n-3\le L_n$.

**Case 3: $G\ge3$, $u>0$, and $n-e\ge10$.** Since $h\ge A$ and $z\le B$,
$G=z-h+1\le B-A+1$. Thus $G\ge3$ implies $B-A\ge2$.
Both endpoint intervals contain $[A,B]$, so $b-a\ge2$ and $d-c\ge2$;
therefore $\tau(H)=\tau(J)=0$. Let
$m=v+1-t\ge1$; this is positive because the distinct boundary positions
counted by $t$ belong to $X$. From (10) and AM–GM,

$$ m+G\ge\lceil2\sqrt{n-e-2t}\rceil. $$

The separated-sweep length from Section 6.3 is
$U=2n-f-2u-2G+\Delta$. By (9),

$$
\begin{aligned}
2n-U
&=f+2u+2G-\Delta\\
&\ge f+2v-t+2G\\
&=f+2(m+G)+t-2\\
&\ge f+c_t(n-e)\\
&\ge e+c(n-e)\\
&\ge c(n).
\end{aligned}
$$

The last two inequalities use $f\ge e$ and (8). Hence
$d(H,J)\le U\le2n-c(n)=L_n$.

**Case 4: $G\ge3$, $u>0$, and $n-e<10$.** Now $f\ge e\ge n-9$,
and the same $G\ge3$ argument in Case 3 gives $\tau(H)=\tau(J)=0$. By (9),

$$ Q=2n-6-f-2u+\Delta\le n+3-u\le n+2\le L_n. $$

Lemma 7.2 completes this case. The four cases cover every pair of paths,
so $D_n\le L_n$ for $n\ge16$. Together with Theorem B this proves
$D_n=L_n$ for all $n\ge16$.

## 10. Finite bases and the complete diameter statement

The smaller graphs were enumerated directly from the host graph, without
using the normal form or diameter formula to generate vertices or edges.
Full all-pairs BFS gave:

| n | Paths, reversal identified | Reconfiguration edges | Diameter |
| --- | --- | --- | --- |
| 3 | 3 | 3 | 1 |
| 4 | 6 | 8 | 3 |
| 5 | 10 | 15 | 3 |
| 6 | 17 | 28 | 5 |
| 7 | 28 | 49 | 6 |
| 8 | 44 | 80 | 7 |
| 9 | 68 | 127 | 8 |
| 10 | 104 | 198 | 10 |
| 11 | 157 | 303 | 11 |
| 12 | 235 | 458 | 12 |
| 13 | 350 | 687 | 14 |
| 14 | 519 | 1024 | 15 |
| 15 | 767 | 1519 | 16 |

For $10\le n\le15$ these values equal $L_n$. The Python implementation
uses prefix reversals to construct adjacency. The C++ implementation
instead uses edge-set addition/deletion at the selected target, checks
degrees and connectivity, and enumerates paths in the reverse traversal
order. All counts, diameters, and full eccentricity histograms agree.
The two implementations cover 1,078,618 ordered state pairs in these bases.

**Theorem D (exact diameter, with a finite computational base).** The
backbite reconfiguration graph of $P_n^2$, with path reversals identified,
has, for every $n\ge10$,

$$\boxed{D_n=\max\left\{
2n+2-2\lceil2\sqrt n\rceil,\quad
2n+1-2\lceil2\sqrt{n-2}\rceil,\quad
2n-2\lceil2\sqrt{n-4}\rceil\right\}.}$$

The values for $3\le n\le9$ are $1,3,3,5,6,7,8$, respectively.
For $n\ge10$, a pair attaining $D_n$ consists of $I_n$ and a path with
the same endpoints $0,n-1$; construct it by balancing the gaps in the case
of Theorem B attaining the maximum. The supplied `diameter_witness`
function performs this integer construction without enumerating $R_n$.

The proof for $n\ge16$ is analytic. The extension to $10\le n\le15$ and
the seven smaller values uses the explicitly disclosed exhaustive finite
computation. Thus the complete statement has a finite computational part.
The new tests above $n=15$ are supplemental checks, not a substitute for
the general proof. In particular, the stored BFS run through $n=32$ is a
rooted-distance run, not 32 new full all-pairs diameter computations.

Theorem D does not give an exact metric for two arbitrary specified paths.
Neither isometry of the core nor equality of edge-flip distance and
backbite distance is assumed. The independent AI report for v0.3 finds
no counterexample or invalid inference in Theorem D, while requesting the
two exposition clarifications incorporated in v0.4. This report is
preserved in INDEPENDENT_AI_AUDIT_v0_3.md; its raw independent code and
logs have not been supplied here. Review of these revisions, human peer
review, and a conclusive novelty assessment remain outstanding.

## References

[1] Albi Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian
paths*, arXiv:2610.05068v1, submitted 4 October 2026, especially Sections
1–2 and 4–5. https://arxiv.org/html/2610.05068v1

[2] Sudip Biswas, Stephane Durocher, Debajyoti Mondal, and Rahnuma Islam
Nishat, *Hamiltonian Paths and Cycles in Planar Graphs*, COCOA 2012,
LNCS 7402, pp. 83–94. https://doi.org/10.1007/978-3-642-31770-5_8
Author's text: https://www.cs.usask.ca/faculty/dmondal/Papers/COCOA12.pdf

The ZigZag outerplanar family and its Hamiltonian-path counting problem
are established literature. We make no novelty claim for the host family,
the standard outer-cycle uniqueness fact, or the familiar one/three-block
enumeration pattern. The novelty question concerns the distance results
and remains INCONCLUSIVE.
