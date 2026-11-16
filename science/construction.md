# A collective protocol with returned resources

Alice holds $n$ copies of an unknown pure state $|\psi\rangle\in\mathbb C^d$ and the registers $B_1,\ldots,B_m$ of $m$ independent maximally entangled pairs. Bob holds their partners $A_1,\ldots,A_m$. This page constructs an Alice instrument after which Bob only selects a port. The complete [model](model.md) fixes the allowed operations and fidelity convention; the [converse](converse.md) proves that its resource scaling is necessary.

The protocol retains the unused registers. After the selected port and the survivors have been put in a common, known order, its target is

$$
|w_\psi\rangle
=|\psi\rangle_{\mathrm{out}}
 \otimes|\Phi_d\rangle^{\otimes(m-1)}
 \otimes|\psi\rangle^{\otimes(n-1)},
\qquad
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{a=0}^{d-1}|a,a\rangle.
$$

The returned pairs are still shared between Alice and Bob. The returned input specimens remain with Alice. Their guarantee is one global squared fidelity with this product target, rather than exact return of each register.

## The constructive guarantee

**Theorem 1.** For all integers $d\ge2$ and $m,n\ge1$, there is a protocol in the correction-free port-selection model such that, for every pure input $|\psi\rangle$,

$$
F_{\mathrm{global}}
\ge
\frac{mn}{mn+(d-1)(d+n)}.
\tag{1}
$$

Consequently, the selected output alone has at least this fidelity with $|\psi\rangle$. In particular, global infidelity at most $\varepsilon\in(0,1)$ is guaranteed if

$$
m\ge
\frac{1-\varepsilon}{\varepsilon}
\frac{(d-1)(d+n)}{n}.
\tag{2}
$$

There is no preparation unitary for $|\psi\rangle$, preparation inverse, coherent source-index oracle, or classical description of the input. The resources supplied to the protocol are the actual pairs and specimens. Its known operations and approximation costs are treated separately in [implementation](implementation.md).

## 1. An Alice-only Bell-sum instrument

Write the input specimens on $C_1,\ldots,C_n$. All operators in the next display act only on Alice's $B,C$ registers:

$$
E_{rs}=|\Phi_d\rangle\langle\Phi_d|_{B_rC_s}
       \otimes I_{\mathrm{other\ inner\ registers}},
\qquad
Q_{rs}=dE_{rs},
\qquad
G=\sum_{r=1}^m\sum_{s=1}^n Q_{rs}.
\tag{3}
$$

The Bell projectors need not commute. Define $G^{-1/2}$ to be zero on the kernel of $G$.

For a pair $(r,s)$, let $L_{rs}$ contract $B_rC_s$ with $\langle\Phi_d|$. Route $A_r$ to the output, list the remaining whole pairs $(A_t,B_t)$ in increasing $t$, and then list the remaining $C$ registers in increasing index order. This convention gives every $L_{rs}$ the same output Hilbert space, and

$$
L_{rs}^{\dagger}L_{rs}=E_{rs}.
\tag{4}
$$

The associated Kraus operators are

$$
J_{rs}=\sqrt d\,L_{rs}G^{-1/2}.
\tag{5}
$$

Here and below, an inner operator is tensored with the identity on Bob's registers when it acts on the full state. Equation (5) is physical: its Alice part is a linear operator from $B,C$ to the surviving Alice registers, while its Bob part merely relabels the selected port and surviving ports. Its effects obey

$$
\sum_{r,s}J_{rs}^{\dagger}J_{rs}
=G^{-1/2}\left(\sum_{r,s}dE_{rs}\right)G^{-1/2}
=\Pi_{\mathrm{supp}G}\le I.
\tag{6}
$$

Thus these maps form an incomplete instrument. Alice can retain $(r,s)$ as an internal record and communicate only $r$ to Bob. The selected input index $s$ only tells Alice how to order her remaining specimens.

The complementary outcome must also respect the port restriction. Alice measures the kernel effect

$$
\Pi_0=I-\Pi_{\mathrm{supp}G},
$$

discards $B_1,C_1$, and always signals port $1$. Bob keeps $A_1$, and both parties retain their other registers in the prescribed order. This is a completely positive branch with trace $\mathrm{Tr}(\Pi_0\rho)$, so it completes (6) to a trace-preserving protocol. It needs no preparation or correction at Bob. Its contribution to fidelity with the target is nonnegative, which is all the proof will use.

The normalization in (5) is a polar or pretty-good-measurement construction. Square-root measurements and the accompanying moment method are established tools; related port measurements and return guarantees appear in generalized teleportation and entanglement recycling. The two-pool [Quantum Program Composition construction](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/main/science/construction.md) supplies the direct precursor of this instrument and routing argument. The new input marginal and its moments below are different. See [related work](../references/RELATED_WORK.md) for attribution and the operational comparisons.

## 2. Symmetry gives one common polar output

It is useful to prove the claim with a unitary $U$ already applied to every Bob half. Use the normalized row-first Choi convention

$$
|U\rangle_{AB}
=\frac1{\sqrt d}\sum_{a,b=0}^{d-1}U_{ab}|a,b\rangle.
$$

The input and ideal global output are

$$
\begin{aligned}
|v\rangle&=|U\rangle^{\otimes m}\otimes|\psi\rangle^{\otimes n},\\
|w\rangle&=U|\psi\rangle\otimes|U\rangle^{\otimes(m-1)}
                 \otimes|\psi\rangle^{\otimes(n-1)}.
\end{aligned}
\tag{7}
$$

Taking $U=I$ gives teleportation. Direct Bell contraction fixes the normalization and product order:

$$
(\langle\Phi_d|_{BC}\otimes I_A)
 (|U\rangle_{AB}\otimes|\psi\rangle_C)
=\frac1d U|\psi\rangle_A.
\tag{8}
$$

Let $P$ project onto

$$
\mathcal S
=\mathrm{Sym}^{m}(\mathbb C^{d^2})
 \otimes\mathrm{Sym}^{n}(\mathbb C^d).
\tag{9}
$$

The first symmetry permutes **whole $AB$ pairs**, not Bob or Alice halves separately. The input belongs to this subspace. The complete sum $G$ commutes with these pair permutations and with permutations of the $C$ registers, so $G$ preserves $\mathcal S$.

With the routing convention already specified,

$$
L_{rs}P=L_{11}P
\quad\text{for every }r,s.
\tag{10}
$$

Indeed, move the selected pair and input register to position $1$ by a permutation. Such a permutation fixes every vector in $\mathcal S$. Any permutation that it induces among the surviving registers fixes their separate symmetric sectors as well. This is an identity on the whole subspace (9), not just on the product vector (7).

Write $L=L_{11}|_{\mathcal S}$ and $G_{\mathcal S}=G|_{\mathcal S}$, and define

$$
M=\sqrt{dmn}\,L,
\qquad
\mu=\frac{mn}{d}.
\tag{11}
$$

Equations (4) and (10) imply

$$
M^{\dagger}M=G_{\mathcal S},
\qquad
M|v\rangle=\sqrt\mu\,|w\rangle.
\tag{12}
$$

For the first identity, equivalently use
$dmn\,P E_{11}P=P(\sum_{r,s}dE_{rs})P$.
Individual Bell projectors need not preserve $\mathcal S$; the complete sum does.

The polar partial isometry

$$
K=MG_{\mathcal S}^{-1/2}
$$

is zero on the kernel and obeys $K^{\dagger}K=\Pi_{\mathrm{supp}G_{\mathcal S}}$. Since $G^{-1/2}|v\rangle$ remains in $\mathcal S$, every routed useful branch satisfies

$$
J_{rs}|v\rangle=\frac1{\sqrt{mn}}K|v\rangle.
\tag{13}
$$

Discarding the classical branch label therefore gives the unnormalised pure contribution $K|v\rangle\langle v|K^{\dagger}$. Its unconditional contribution to global fidelity is exactly

$$
f_{\mathrm{pol}}
=|\langle w|K|v\rangle|^2
=\frac{\langle v|\sqrt G|v\rangle^2}{\mu}.
\tag{14}
$$

The second equality follows by substituting $|w\rangle=M|v\rangle/\sqrt\mu$ and $M^{\dagger}M=G_{\mathcal S}$. There is no assumption of coherent classical outcome labels or physical bosonic modes.

## 3. The two moments that determine the bound

The reduced state of the inner registers in (7) is

$$
\rho_{\mathrm{in}}
=\frac{I_{B_1\cdots B_m}}{d^m}
 \otimes(|\psi\rangle\langle\psi|)^{\otimes n}.
\tag{15}
$$

Write $\mathbb E[X]=\mathrm{Tr}(\rho_{\mathrm{in}}X)$ for inner operators. The following identities hold for any pure $|\psi\rangle$:

$$
\mathbb E[Q_{rs}]=\frac1d,
\qquad
\mathbb E[Q_{rs}^2]=1,
\tag{16}
$$

and, for distinct ordered pairs,

$$
\mathbb E[Q_{rs}Q_{tu}]
=\begin{cases}
1/d,&r=t,\ s\ne u,\\
1/d^2,&r\ne t.
\end{cases}
\tag{17}
$$

For (16), trace the Bell projector against a maximally mixed $B$ and use $Q_{rs}^2=dQ_{rs}$. For (17), disjoint pairs factor. If two pairs share $C_s$, tracing over the two independent maximally mixed $B$ registers replaces each $Q$ by $I_C/d$, giving $1/d^2$.

The exceptional case shares one $B$ with two identical pure inputs. Expanding

$$
Q_{BC}=\sum_{a,b}|a\rangle\langle b|_B
                  \otimes|a\rangle\langle b|_C
$$

and tracing $Q_{BC_s}Q_{BC_u}$ against $I_B/d\otimes\psi_{C_s}\otimes\psi_{C_u}$ gives

$$
\frac1d\sum_{a,b}
 |\langle a|\psi\rangle|^2
 |\langle b|\psi\rangle|^2
=\frac1d.
\tag{18}
$$

This term is why repeated pure input specimens behave differently from a second pool of unitary Choi programs, whose corresponding inner marginal is maximally mixed.

There are $mn$ diagonal terms and $mn(n-1)$ exceptional ordered terms in $G^2$. The remaining $mn^2(m-1)$ ordered terms have expectation $1/d^2$. Therefore

$$
\begin{aligned}
\mathbb E[G]&=\frac{mn}{d}=\mu,\\
\mathbb E[G^2]&=mn+\frac{mn(n-1)}d
                     +\frac{mn^2(m-1)}{d^2},\\
\mathrm{Var}(G)&=mn\left[1+\frac{n-1}{d}-\frac{n}{d^2}\right].
\end{aligned}
\tag{19}
$$

For $X=G/\mu$, the spectral distribution in state (15) consequently satisfies

$$
\mathbb E[X]=1,
\qquad
\mathbb E[X^2]=1+r,
\qquad
r=\frac{(d-1)(d+n)}{mn}.
\tag{20}
$$

No independence of the noncommuting Bell projectors has been assumed.

## 4. From moments to fidelity

Apply Hölder's inequality, with exponents $3/2$ and $3$, to the nonnegative spectral variable $X$:

$$
1=\mathbb E[X]
=\mathbb E\left[(\sqrt X)^{2/3}(X^2)^{1/3}\right]
\le
(\mathbb E[\sqrt X])^{2/3}
(\mathbb E[X^2])^{1/3}.
\tag{21}
$$

It follows that

$$
f_{\mathrm{pol}}
=(\mathbb E[\sqrt X])^2
\ge\frac1{\mathbb E[X^2]}
=\frac{mn}{mn+(d-1)(d+n)}.
\tag{22}
$$

The permitted kernel completion only adds a nonnegative target overlap, proving (1). Tracing out returned registers cannot lower fidelity, so (1) also holds for the selected output alone.

The useful-instrument probability itself satisfies

$$
p_{\mathrm{pol}}
=\mathbb E[\mathbf 1_{G>0}]
\ge\frac{\mathbb E[G]^2}{\mathbb E[G^2]}
=\frac1{1+r}.
\tag{23}
$$

This is Cauchy–Schwarz applied to $G\mathbf 1_{G>0}$. A useful outcome generally produces an approximate target, with conditional global fidelity $f_{\mathrm{pol}}/p_{\mathrm{pol}}$. Equations (22) and (23) are **not** an exact-teleportation success formula for arbitrary $m,n$.

## 5. The two endpoint checks

For one input specimen, (1) becomes

$$
n=1:
\qquad
F_{\mathrm{global}}\ge\frac{m}{m+d^2-1}.
\tag{24}
$$

This is the familiar moment-type deterministic approximate PBT bound, now retaining the unused pairs in the target. It should not be confused with the exact success probability of a probabilistic PBT protocol with fixed maximally entangled resources.

For one port, the useful branch is special. On the symmetric $C$ sector, the nonzero spectrum of $G$ consists of the single value $d+n-1$. One way to see this is to use $M=\sqrt{dn}L$ from (11). Its image is $\mathbb C^d_A\otimes\mathrm{Sym}^{n-1}(\mathbb C^d)$, and

$$
MM^{\dagger}=(d+n-1)I
\quad\text{on this image}.
\tag{25}
$$

To verify (25), let $P_n$ be the $n$-fold symmetric projector. Unitary invariance and its trace give

$$
\mathrm{Tr}_{C_1}P_n
=\frac{D_n}{D_{n-1}}P_{n-1}
=\frac{d+n-1}{n}P_{n-1},
\qquad
D_k=\binom{d+k-1}{k}.
$$

The Bell contraction in $L$ contributes another factor $1/d$, so $LL^{\dagger}=(d+n-1)/(dn)$ times the identity on its image. Multiplication by $dn$ gives (25). Since $M^{\dagger}M=G_{\mathcal S}$, the nonzero eigenvalues agree.

Consequently $G^{-1/2}$ is a scalar on its support and the polar branch gives the exact target, including the $n-1$ returned specimens, with probability

$$
m=1:
\qquad
p_{\mathrm{exact}}=\frac{n}{d(d+n-1)}.
\tag{26}
$$

This recovers the single-port multicopy theorem of Grosshans and coauthors. The main result of this project is the simultaneous finite-$n$, finite-$m$ resource frontier, not a new claim to that endpoint or to the known-state limit.

## 6. Stored-channel retrieval

Let $\mathcal E:\mathcal L(\mathbb C^d)\to\mathcal L(\mathbb C^{d'})$ be any CPTP map and let its normalized Choi program be

$$
J_{\mathcal E}
=(\mathcal E_A\otimes\mathrm{id}_B)
 (|\Phi_d\rangle\langle\Phi_d|).
$$

Supply $m$ independent copies of $J_{\mathcal E}$ and $n$ independent pure input specimens. Alice uses the same inner-register instrument, and the selected outer program register is the output. The channel need not be unitary, unital, noiseless, or classically known.

The complete protocol, including the kernel completion, acts on $B,C$ and only relabels outer $A$ registers. Applying $\mathcal E$ to every outer half therefore commutes with it, up to the known output ordering. Apply $\mathcal E^{\otimes m}$ to both the actual and ideal global states of the $U=I$ construction. Monotonicity of squared Uhlmann fidelity gives

$$
F\left(
\rho_{\mathrm{actual}},
\mathcal E(\psi)\otimes
J_{\mathcal E}^{\otimes(m-1)}\otimes
\psi^{\otimes(n-1)}
\right)
\ge\frac{mn}{mn+(d-1)(d+n)},
\tag{27}
$$

where $\psi=|\psi\rangle\langle\psi|$.

This is an achievable program-and-data tradeoff, including approximate joint return of the unused programs. The matching [teleportation converse](converse.md) allows every Alice instrument while Bob only selects a port. It does not prove optimality against arbitrary global processors acting jointly on both halves of all Choi programs and all data.

The finite calculations in [verification](../verification/README.md) check the Bell-sum moments, routing, score identity and boundary cases. They support the implementation of the argument; finite enumeration is not a substitute for the all-dimensional proof above.
