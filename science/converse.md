# Why both resources are necessary

Additional identical input specimens can reduce the number of Bell ports, but cannot reduce it indefinitely. This page proves the matching resource lower bound in the [correction-free port-selection model](model.md): Alice may process all her registers collectively and adaptively, while Bob can only select one of the supplied ports. No restriction is placed on Alice's known computation, ancillas, measurement depth or classical records.

The [construction](construction.md) also gives a stored-channel retrieval protocol. The converse here is a teleportation theorem; it does not cover arbitrary global processors that may act on the outer Choi-program halves.

## The finite bound

**Theorem 2.** Suppose the resource consists of $`m`$ independent $`d`$-dimensional maximally entangled pairs and Alice receives $`n`$ identical copies of an unknown pure input. For every deterministic correction-free port-selection protocol, its Haar-average output fidelity obeys

**Equation (1)**

```math
\overline F\le
\min\left\lbrace 
1,\ \frac md,\ \frac{d+mn}{d(d+n)}
\right\rbrace .
```

In particular, a protocol whose output fidelity is at least $`F_0`$ for every pure input must satisfy

**Equation (2)**

```math
m\ge F_0d,
\qquad
mn\ge F_0d(d+n)-d.
```

The second inequality can equivalently be written

**Equation (3)**

```math
m\ge F_0d+\frac{F_0d^2-d}{n}.
```

These are exact finite-parameter necessary inequalities. They are not an exact formula for the optimal fidelity or for the success probability of exact heralded teleportation.

## 1. Every Alice protocol gives a port POVM

Let $`C_1,\ldots,C_n`$ be the input registers, and let Alice's halves of the resource pairs be $`B_1,\ldots,B_m`$. Bob holds $`A_1,\ldots,A_m`$.

Because Bob's final action is only to keep the port specified by Alice, all of Alice's measurements, internal adaptivity and classical processing can be combined into effects

**Equation (4)**

```math
M_r\ge0,
\qquad
\sum_{r=1}^m M_r=I
```

on $`C_1\cdots C_nB_1\cdots B_m`$. Fixed local ancillas can be absorbed into these effects. Alice's retained quantum outputs are irrelevant to Bob's reduced output after they are traced out. Coarse-graining all histories that select the same port therefore gives exactly (4).

A deterministic protocol may include an internal failure outcome, but it must still output a port; assign such an outcome to its selected port before forming (4). This proof does not assume that useful branches are exact, nor that Alice measures each specimen separately.

For a fixed input $`\psi=|\psi\rangle\langle\psi|`$, Bell-state contraction gives the fidelity contribution of port $`r`$ as

**Equation (5)**

```math
f_r(\psi)
=\frac1{d^m}\mathrm{Tr}\left[
M_r\left(
\psi_C^{\otimes n}\otimes\psi_{B_r}^{T}
\otimes I_{B_{\ne r}}
\right)\right].
```

The transpose is in the specified Bell basis. Summing (5) over $`r`$ gives the deterministic output fidelity $`F(\psi)`$.

## 2. The Haar score identity

Write

```math
P_n=P_{\mathrm{Sym}^n(\mathbb C^d)},
\qquad
D_n=\binom{d+n-1}{n}.
```

For one distinguished port half $`B`$, define

**Equation (6)**

```math
R_n=\int \psi_C^{\otimes n}\otimes\psi_B^T\,d\psi,
\qquad
Q_{sB}=d|\Phi_d\rangle\langle\Phi_d|_{C_sB}.
```

Here $`d\psi`$ is normalized Haar measure over pure states. The required identity is

**Equation (7)**

```math
R_n=
\frac{
P_n\otimes I_B+
\sum_{s=1}^n
(P_n\otimes I_B)Q_{sB}(P_n\otimes I_B)
}{(d+n)D_n}.
```

**Proof.** The symmetric-subspace Haar identity gives

**Equation (8)**

```math
R_n=\frac{P_{n+1}^{T_B}}{D_{n+1}}.
```

Resolve permutations of $`n+1`$ systems into $`n+1`$ cosets of permutations of the first $`n`$. If $`V_{sB}`$ swaps $`C_s`$ with $`B`$, this yields

**Equation (9)**

```math
P_{n+1}
=\frac1{n+1}
(P_n\otimes I_B)
\left(I+\sum_{s=1}^n V_{sB}\right)
(P_n\otimes I_B).
```

Partial transpose on $`B`$ sends $`V_{sB}`$ to $`Q_{sB}`$. It leaves the two $`P_n`$ factors untouched because they act only on $`C`$. Finally,

```math
D_{n+1}=\frac{d+n}{n+1}D_n.
```

Substitution into (8) proves (7). Each summand involving $`Q_{sB}`$ in (7) is positive semidefinite, despite the use of partial transpose in the derivation. $`\square`$

The identity is a symmetric-subspace calculation. It does not require a classical description of $`|\psi\rangle`$ in the protocol, and it is used only to average the performance of an arbitrary protocol for the lower bound.

## 3. Bounding the entire port measurement

Insert (7) into the Haar average of (5):

**Equation (10)**

```math
\overline F
=\frac1{d^m}\sum_{r=1}^m
\mathrm{Tr}\left[
M_r\left(R_{n,r}\otimes I_{B_{\ne r}}\right)
\right].
```

The $`P_n\otimes I`$ terms in this expression have the same operator for every $`r`$. Completeness of the POVM gives their total contribution exactly:

**Equation (11)**

```math
\begin{aligned}
\frac1{d^m(d+n)D_n}
\sum_r\mathrm{Tr}
[M_r(P_n\otimes I_{B_1\cdots B_m})]
&=\frac{\mathrm{Tr}(P_n\otimes I)}{d^m(d+n)D_n}\\
&=\frac1{d+n}.
\end{aligned}
```

For a positive Bell term, use $`0\le M_r\le I`$. For any positive operator $`T`$, this implies $`\mathrm{Tr}(M_rT)\le\mathrm{Tr}(T)`$. Also,

**Equation (12)**

```math
\mathrm{Tr}_B Q_{sB}=I_{C_s}.
```

Thus, for each pair $`(r,s)`$,

**Equation (13)**

```math
\begin{aligned}
&\frac1{d^m(d+n)D_n}
\mathrm{Tr}\left[
M_r\bigl((P_n\otimes I)Q_{sB_r}(P_n\otimes I)
         \otimes I_{B_{\ne r}}\bigr)
\right]\\
&\hspace{2em}\le
\frac{d^{m-1}\mathrm{Tr}[(P_n\otimes I)Q_{sB_r}]}{d^m(d+n)D_n}
=\frac1{d(d+n)}.
\end{aligned}
```

There are $`mn`$ such terms. Adding (11) and (13) proves

**Equation (14)**

```math
\overline F\le\frac1{d+n}+\frac{mn}{d(d+n)}
=\frac{d+mn}{d(d+n)}.
```

This argument permits all coherent processing and adaptivity on Alice's side. Its restriction is the physical output rule at Bob, rather than a restriction on Alice's estimator.

## 4. The no-signalling ceiling

There is also a simple bound that makes the port floor transparent. For fixed $`\psi`$, let $`\sigma_r(\psi)`$ be Bob's unnormalised state in port $`A_r`$ on the event that Alice selects it. Since the corresponding Alice effect satisfies $`M_r\le I`$, positivity gives

**Equation (15)**

```math
0\le\sigma_r(\psi)\le\frac{I_{A_r}}d.
```

The upper operator is the port marginal when Alice's outcome is ignored. Alice's local processing cannot alter that marginal. Therefore

**Equation (16)**

```math
\langle\psi|\sigma_r(\psi)|\psi\rangle\le\frac1d,
\qquad
F(\psi)\le\frac md.
```

This bound already holds pointwise, hence also after Haar averaging. Together with the trivial ceiling $`1`$ and (14), it proves (1).

At large dimension and fixed positive target fidelity, (14) already exposes the same $`m`$-of-order-$`d`$ floor. The separate no-signalling argument is useful as an exact finite bound and explains why unlimited input copies cannot remove the need for enough receiver ports.

## 5. The matched fixed-fidelity frontier

Fix $`F_0\in(0,1)`$ independently of $`d,n`$, and let $`m_{F_0}(d,n)`$ be the least number of ports giving uniform output fidelity at least $`F_0`$. The [construction](construction.md) supplies the sufficient condition

**Equation (17)**

```math
m\ge\frac{F_0}{1-F_0}\frac{(d-1)(d+n)}n.
```

The exact lower inequalities are (2). For example, whenever $`d\ge2/F_0`$, (3) gives

**Equation (18)**

```math
m\ge F_0d+\frac{F_0d^2}{2n}.
```

Equations (17) and (18), with an integer ceiling in the construction, establish uniformly over $`n\ge1`$ that

**Equation (19)**

```math
m_{F_0}(d,n)
=\Theta_{F_0}\left(d+\frac{d^2}{n}\right).
```

The constants depend on the fixed target fidelity. This is a matched asymptotic resource law, not an assertion that either finite bound in (1) is always attained. In particular, it leaves the optimal dependence on vanishing infidelity and the exact heralded multicopy/multiport success probability open.

The global-return construction attains (19), whereas the converse only demands one good output and imposes no return requirement. The return guarantee therefore does not change the fixed-fidelity order, even though reusing those approximate resources in a longer computation would require a separate accumulated-error analysis.

For stored-channel retrieval, the construction applies to arbitrary CPTP Choi programs. Equation (19) remains an optimality statement for the teleportation interface with Bob restricted to choosing ports; it must not be relabelled as a lower bound against every global programmable processor.
