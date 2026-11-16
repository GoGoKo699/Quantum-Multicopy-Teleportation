# A finite circuit using only Alice's registers

The collective processor can be compiled without a reflection about the unknown input or a symmetry test involving Bob's ports. The circuit acts on Alice's inner resource halves and input copies. Bob receives a classical port label and selects that port. The separate whole-copy symmetries used in the [construction proof](construction.md) identify the output mathematically; they are not gates in this implementation.

## 1. Circuit guarantee and charged resources

Let $`d\geq2`$, $`m,n\geq1`$, and put

```math
\mu=\frac{mn}{d},\qquad
r=\frac{(d-1)(d+n)}{mn},\qquad
\ell=\lceil\log_2d\rceil.
```

Here $`r`$ is the relative variance of the Bell-sum operator on the supplied input, rather than a port index. Fix polynomial accuracy $`0<\eta<1/2`$ and total circuit accuracy $`0<\nu<1`$. There is a deterministic, correction-free port protocol with global squared fidelity

```math
F_{\mathrm{global}}
\geq \max\!\left\{0,1-\frac{41}{9}r-2\eta-2\nu\right\}.
```

The target is one teleported state, $`m-1`$ returned Bell pairs and $`n-1`$ returned input copies, in the specified common order. The bound is uniform over the unknown pure input. It permits arbitrarily small nonzero singular values of the known Bell-sum operator; no global spectral gap is promised.

For the gate count, write

```math
q=O\!\left(d\log\frac1\eta\right),\qquad
C_{\mathrm{step}}=
O\!\left((m+n)\bigl(\ell+\log(mn+1)\bigr)+\ell^2+1\right).
```

The circuit uses $`O(q)`$ calls to a **known** routing-and-Bell circuit or its inverse, and $`O(q)`$ known projector-controlled phases. Its two-qubit and known-rotation gate count is

```math
G_0=O(qC_{\mathrm{step}}).
```

An inverse here reverses the compiled known circuit; no inverse of a source, state preparation, stored channel, or unknown unitary is supplied. Compiling the known rotations into a fixed universal gate set adds a factor polynomial in $`\log(G_0/\nu)`$. Consequently a conservative finite-gate bound is

```math
G_{\mathrm{finite}}=
O\!\left(G_0\,\operatorname{polylog}\frac{G_0}{\nu}\right).
```

Alice stores $`(m+n)\ell`$ input qubits and uses $`O(\ell+\log(mn+1))`$ additional clean workspace, including port labels, arithmetic work and a constant number of signal flags. Bob stores $`m\ell`$ input qubits. All-to-all connectivity and sequential gate count are used; geometric routing and parallel depth require their own accounting.

For a desired global infidelity $`0<\epsilon<1`$, the explicit sufficient choice

```math
r\leq\frac{9\epsilon}{123},\qquad
\eta=\nu=\frac\epsilon6
```

makes the displayed infidelity at most $`\epsilon`$. At fixed error, $`q=O(d)`$ and the cost is $`\widetilde O(d(m+n))`$, with the logarithmic terms and precision costs above understood. These bounds establish a finite implementation of the copy tradeoff. They do not establish a practical speedup over another teleportation architecture.

## 2. An Alice-only projected encoding

Alice's data registers are $`B_1,\ldots,B_m,C_1,\ldots,C_n`$. Each $`B_j`$ is the inner half of a Bell pair, while each $`C_k`$ contains one input copy. Bob's registers $`A_1,\ldots,A_m`$ do not participate in this circuit.

For labels $`j\in\{1,\ldots,m\}`$ and $`k\in\{1,\ldots,n\}`$, let $`T_{jk}`$ be the rectangular map that contracts $`B_jC_k`$ with $`\langle\Phi_d|`$ and places the remaining $`B`$ registers and remaining $`C`$ registers in increasing original order. It acts on Alice's registers only. In particular,

```math
T_{jk}^{\dagger}T_{jk}=E_{jk},\qquad
E_{jk}=|\Phi_d\rangle\langle\Phi_d|_{B_jC_k}\otimes I.
```

Define the flagged contraction

```math
\mathcal A=
\frac1{\sqrt{mn}}\sum_{j=1}^m\sum_{k=1}^n
|j,k\rangle\otimes T_{jk}.
```

Orthogonal labels remove cross terms, so

```math
\mathcal A^{\dagger}\mathcal A
=\frac1{mn}\sum_{j,k}E_{jk}
=\frac{G}{dmn},\qquad
G=d\sum_{j,k}E_{jk}.
```

Each $`E_{jk}`$ is a projector, hence $`0\leq G\leq dmn\,I`$ and $`\|\mathcal A\|\leq1`$. This identity holds on the entire ordered Alice input space. It does not require a promise that the input lies in a symmetric subspace.

Here is a unitary projected encoding of $`\mathcal A`$.

1. Prepare two label registers in the known state $`(mn)^{-1/2}\sum_{j,k}|j,k\rangle`$.
2. Controlled by those labels, move $`B_j`$ and $`C_k`$ into the first position of their respective pools, preserving the order of each pool's surviving registers.
3. Apply a known Bell-unpreparation unitary to those two first registers. It maps $`|\Phi_d\rangle`$ to $`|0,0\rangle`$.

Call the complete known unitary $`W`$. Its right projector $`\Pi_{\mathrm{in}}`$ tests that the labels were initialized to zero, while its left projector $`\Pi_{\mathrm{out}}`$ tests that the two selected data registers are zero after Bell unpreparation. Identifying those two zero registers with deleted output registers gives

```math
\Pi_{\mathrm{out}}W\Pi_{\mathrm{in}}
\equiv\mathcal A.
```

The output labels remain quantum registers until the final measurement. Neither projector acts on Bob's systems. Binary labels encode $`j-1`$ and $`k-1`$; invalid padded labels can be rejected at the final success test.

## 3. Transforming singular vectors

Let $`X=G/\mu`$. A singular value of $`\mathcal A`$ corresponding to an eigenvalue $`x`$ of $`X`$ is

```math
\sigma=\sqrt{\frac{\mu x}{dmn}}=\frac{\sqrt x}{d}.
```

Choose a real odd polynomial $`p`$ with

```math
|p(z)|\leq1\quad(z\in[-1,1]),\qquad
|p(z)-1|\leq\eta\quad
\left(z\in\left[\frac1{2d},1\right]\right).
```

A bounded sign approximation has degree $`q=O(d\log(1/\eta))`$. Singular-value transformation of the projected encoding implements the rectangular map $`p^{(\mathrm{SV})}(\mathcal A)`$ as one measured block of a unitary. All signal phases and both encoding projectors are known Alice operations. A constant number of additional signal ancillas accommodates the real-polynomial construction.

We use the projected-unitary singular-value transformation and bounded sign-polynomial results of Gilyén, Su, Low and Wiebe. In the inspected [June 2018 preprint](https://arxiv.org/pdf/1806.01838), these are Corollary 18, Lemma 25 and Theorem 26; the theorem numbering depends on the version. The construction needs only an approximation above the specified cutoff, not a lower bound on every nonzero singular value.

On the branch with labels $`(j,k)`$, the transformed contraction is

```math
\sqrt d\,T_{jk}G^{-1/2}
p\!\left(\frac{\sqrt X}{d}\right),
```

where the inverse square root vanishes on the kernel. Thus the exact polar instrument from the construction is obtained formally by replacing $`p(\sigma)`$ with one on positive singular values. The finite circuit instead regularizes the small-singular-value part through a bounded polynomial.

After the signal-success test, Alice measures $`(j,k)`$. Bob selects $`A_j`$ as output and relabels his surviving ports in their prescribed order. Alice retains her surviving $`B`$ and $`C`$ registers in their prescribed order. The input-copy label $`k`$ remains local to Alice. On a failed signal test or an invalid label, Alice discards two fixed local registers and sends the fixed output-port label $`j=1`$. This is a deterministic port protocol in every branch; failure does not require preparing or replacing any of Bob's states.

## 4. Why a state-dependent cutoff preserves the global target

This section analyzes the finite circuit on the supplied identical-copy input $`v`$ and its pure global target $`w`$. It does not impose extra input restrictions on the physical encoding. The construction proves

```math
\mathbb E X=1,\qquad
\operatorname{Var}X=r,\qquad
f_{\mathrm{pol}}=(\mathbb E\sqrt X)^2\geq\frac1{1+r},
```

where $`\mathbb E h(X)=\langle v|h(X)|v\rangle`$ is its spectral measure. Separate permutations of whole resource pairs and of input copies imply that, after the local output routing, all $`mn`$ transformed success branches have the same vector up to their common $`1/\sqrt{mn}`$ factor. Therefore their summed contribution to target fidelity is exactly

```math
f_p=
\left|\mathbb E\left[
\sqrt X\,p\!\left(\frac{\sqrt X}{d}\right)
\right]\right|^2.
```

This identity includes the output and every returned specimen together. It is not merely a bound on Bob's output marginal.

Chebyshev's inequality gives

```math
\Pr\{X<1/4\}\leq\frac{16}{9}r.
```

Above this cutoff, the polynomial differs from one by at most $`\eta`$. Below it, $`|p-1|\leq2`$ and $`\sqrt X\leq1/2`$. Jensen's inequality gives $`\mathbb E\sqrt X\leq1`$. Consequently

```math
\left|\mathbb E\left[
\sqrt X\,p\!\left(\frac{\sqrt X}{d}\right)
\right]-\mathbb E\sqrt X\right|
\leq\eta+\frac{16}{9}r.
```

Squaring the amplitude and using $`\mathbb E\sqrt X\leq1`$ yields

```math
f_p\geq f_{\mathrm{pol}}-2\eta-\frac{32}{9}r
\geq1-\frac{41}{9}r-2\eta.
```

The deterministic failure contribution has nonnegative overlap with the target. If the complete implemented Alice unitary differs in operator norm by at most $`\nu`$ from the ideal polynomial circuit, every pure input's resulting density operators differ in trace norm by at most $`2\nu`$. Subsequent measurements, local routing and partial traces cannot increase that distance. The fidelity with the fixed pure target therefore decreases by at most $`2\nu`$, proving the circuit guarantee.

The small-eigenvalue mass estimate is specific to the charged identical-copy resource. It does not assert a whole-space approximation to the discontinuous polar map. Conversely, finite-gate errors are bounded on the entire padded circuit space, so uncontrolled behavior outside the symmetric proof subspace is not silently ignored.

## 5. Routing, padding and finite precision

**Linear-size selection.** A port can be moved to the front stably by descending adjacent swaps. For the $`B`$ pool, for $`t=m,m-1,\ldots,2`$, swap $`B_{t-1}`$ and $`B_t`$ if $`j\geq t`$. This sends $`B_j`$ to the first position and preserves the order of every other port. Compute each comparison from the binary label, perform $`\ell`$ controlled qubit swaps, and uncompute its flag. This costs $`O(m(\ell+\log(m+1)))`$ known elementary gates. The same construction for $`C`$ costs $`O(n(\ell+\log(n+1)))`$. Their inverses reverse the gate lists. There is no table lookup or QRAM assumption.

**General dimension.** Each qudit occupies the valid span of the first $`d`$ basis states in $`\ell`$ qubits. Bell unpreparation first subtracts the first qudit from the second modulo $`d`$, then unprepares the known uniform state $`d^{-1/2}\sum_{a=0}^{d-1}|a\rangle`$ on the first. Extend the modular operation as a known reversible permutation outside the valid span. A binary-prefix preparation for a uniform interval uses at most polynomial logarithmic overhead; a conservative gate bound is $`O(\ell^2)`$, with $`O(\ell)`$ arithmetic workspace. Uniform label preparations have the same form with $`d`$ replaced by $`m`$ or $`n`$. For powers of two, these uniform preparations are Hadamard layers.

**Projector phases.** Testing an all-zero label or the two all-zero Bell registers uses reversible AND/comparison circuitry. Compute the predicate, apply one controlled phase, and uncompute. The work returns to zero. These costs are included in $`C_{\mathrm{step}}`$.

**Synthesis accuracy.** If the ideal circuit has $`G_0`$ gates requiring approximation, compile each to operator error at most $`\nu/(2G_0)`$ and reserve the remaining error for phase-list computation. A telescoping product bound gives total operator error at most $`\nu`$. The final angle list needs $`O(\log(G_0/\nu))`$ accurate bits per angle. A stable polynomial-time classical QSP preprocessing algorithm is available from [Haah, Quantum 3, 190 (2019)](https://quantum-journal.org/papers/q-2019-10-07-190/); its degree-dependent arithmetic and precision costs are charged classical preprocessing, rather than oracle calls. This use of ordinary classical memory does not supply coherent data loading.

The circuit description and its $`O(q)`$ QSP phases are computed from $`d,m,n,\eta,\nu`$ only. They do not depend on the unknown input state or stored channel. An implementation may use more efficient uniform-state or phase-compilation routines; the conservative bounds above already suffice for finite resource accounting.

## 6. Stored channels and preparation costs

Apply any CPTP channel $`\mathcal E`$ to every Bob half of the Bell resources. These outer maps commute with the complete compiled Alice circuit, including its failure branches, and with the branch-conditioned port relabeling. Fidelity monotonicity therefore carries the same bound to the global target

```math
\mathcal E(|\psi\rangle\langle\psi|)
\otimes J_{\mathcal E}^{\otimes(m-1)}
\otimes(|\psi\rangle\langle\psi|)^{\otimes(n-1)}.
```

Here $`J_{\mathcal E}`$ is the normalized Choi state. Mixed or nonunital stored channels are allowed. For this mixed target, use squared Uhlmann fidelity; it agrees with the squared-overlap convention in the pure Bell/unitary case. If the channel output dimension is $`d'`$ rather than $`d`$, Alice's circuit and its bounds are unchanged, while Bob stores $`m\lceil\log_2d'\rceil`$ qubits and uses the corresponding register width for local port routing. The port-model converse does not become an unrestricted-program-processor converse through this reduction.

The theorem charges $`m`$ supplied Choi specimens and $`n`$ supplied input specimens separately from the known-gate count. Producing a Choi specimen from a live channel uses a prepared Bell pair and one channel application; when the specimens are supplied as data, no live-channel access is assumed. Preparing and distributing the $`m`$ Bell pairs in the teleportation task is likewise a separate resource. With a common laboratory and known local gates, their preparation takes $`O(m\ell^2)`$ gates under the conservative general-dimension construction; entanglement distribution between laboratories is not free.

Approximate return is one joint finite-use guarantee. This circuit establishes no indefinite catalyst reuse, noisy-source threshold, hardware crossover or optimal vanishing-error gate count.
