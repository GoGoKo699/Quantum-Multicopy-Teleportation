# Watrous bridge to multicopy teleportation

The single educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. Use the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) to find the source and its errata. The section identities below were checked against the author-hosted 2018 contents and relevant chapters. The book is not reproduced in this repository.

The [30-milestone map](milestones.md) follows this project's scientific story. The book supplies the mathematical language; the bridge below explains where that language enters the result and which further arguments this project supplies.

## The task before the formulas

Imagine an unknown quantum input arriving after an operation has already been stored in quantum program states. Ordinary teleportation often needs a receiver correction. For a stored unknown operation, the required corrected action may itself depend on the unknown operation. Port-based retrieval instead gives the receiver several possible output registers and asks the sender to indicate which one to keep.

Here Alice receives several identical specimens of the input. She cannot read their amplitudes without disturbance or assume access to their preparation circuit. Alice also holds one half of each shared Bell pair; Bob holds the other halves. Alice may process all her registers together. Bob may select and reorder ports, but cannot apply a conditional correction or replace an output by a freshly prepared state.

The question is how much the input specimens can reduce the Bell-port supply. For a fixed uniform squared fidelity $F_0\in(1/2,1)$, the answer is a port budget of order $d+d^2/n$. Its constants depend on the chosen fixed fidelity. The [model](../science/model.md) remains authoritative for every assumption.

## Source map

These are targeted entry points, not a requirement to read the book in order. Section descriptions are paraphrases of their role in this project.

| Watrous location | Foundation to take from it | Where the project uses it |
|---|---|---|
| §§1.1.2–1.1.3 | Positive operators, spectral decompositions, singular values and operator norms | [Bell-sum and polar argument](../science/construction.md); [finite encoding](../science/implementation.md) |
| §1.2.2 | Expectations and finite-dimensional probability tools | [Moment bound](../science/construction.md#3-the-two-moments-that-determine-the-bound); [spectral cutoff](../science/implementation.md#4-why-a-state-dependent-cutoff-preserves-the-global-target) |
| §§2.1.1–2.1.3 | Registers, product states, reductions and purifications | [Input contract and return target](../science/model.md) |
| §§2.2.1–2.2.2 | Channels, complete positivity, Kraus and Choi representations | [Physical instrument](../science/construction.md#1-an-alice-only-bell-sum-instrument); [stored-channel retrieval](../science/construction.md#6-stored-channel-retrieval) |
| §§2.3.1–2.3.2 | Measurement effects and outcome probabilities | [Alice POVM reduction](../science/converse.md#1-every-alice-protocol-gives-a-port-povm) |
| §§3.2.1–3.2.3 | Fidelity, its characterizations and monotonicity | [Joint return and channel extension](../science/construction.md); [return and reuse](../science/examples.md#return-and-reuse) |
| §6.3.1 | Teleportation and the role of receiver corrections | [Restricted receiver model](../science/model.md#operational-contract); [worked example below](#one-complete-small-example) |
| §7.1.1 | Symmetric vectors and symmetric-subspace projectors | [Common routed output](../science/construction.md#2-symmetry-gives-one-common-polar-output) |
| §§7.2.1–7.2.2 | Unitary-invariant measures and their applications | [Haar score identity](../science/converse.md#2-the-haar-score-identity) |

The map uses the 2018 book, rather than the earlier course notes with different numbering. Chapter 7 is especially useful because it connects the repeated-copy promise to finite symmetric-projector identities. The concrete Bell-sum moments and port converse are proved in this repository.

## Notation dictionary

The following conventions matter when moving between the source and this project.

| In the book | In this project | Conversion or caution |
|---|---|---|
| A unit vector $u$ and its rank-one operator $uu^{*}$ | $\lvert\psi\rangle$ and $\psi=\lvert\psi\rangle\langle\psi\rvert$ | The vector represents a pure state up to an overall phase. The density operator is the state. |
| The adjoint $X^{*}$ | $X^{\dagger}$ | Both are conjugate transpose. Entrywise conjugation is denoted by an overline or a starred ket label where explicitly defined. |
| A channel's Choi operator $J(\mathcal E)$ | The normalized program state $J_{\mathcal E}$ | For input dimension $d$, $J_{\mathcal E}=J(\mathcal E)/d$; the program has trace one. |
| Fidelity $F_{\mathrm W}(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1$ | Squared fidelity $F(\rho,\sigma)$ | Here $F=F_{\mathrm W}^{2}$. For a pure target $\lvert w\rangle$, our score is $\langle w\rvert\rho\lvert w\rangle$. |
| A partial trace | Discarding specified registers | Discarding the return registers cannot lower fidelity with the corresponding output target. |
| A permutation-invariant input sector | Separate symmetry of whole pairs and of input copies | Permute whole $AB$ resources together. The proof does not allow the compiler to act on Bob's ports. |

The repeated use of $r$ also needs care. In the protocol it can label a port. In [implementation](../science/implementation.md), the scalar $r=(d-1)(d+n)/(mn)$ is a relative variance. Their roles are stated locally and should not be mixed.

## One complete small example

Take dimension $d=2$, one shared Bell pair ($m=1$), and two independent specimens ($n=2$) of

```math
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad |\alpha|^2+|\beta|^2=1.
```

Bob holds $A$. Alice holds $B,C_1,C_2$. Their joint initial state is

```math
|\Phi_2\rangle_{AB}
\otimes|\psi\rangle_{C_1}
\otimes|\psi\rangle_{C_2}.
```

First consider only one input specimen. Bell contraction at Alice gives

```math
(\langle\Phi_2|_{BC_1}\otimes I_A)
  (|\Phi_2\rangle_{AB}\otimes|\psi\rangle_{C_1})
=\frac12|\psi\rangle_A.
```

The selected outcome therefore occurs with probability $1/4$, and its normalized output is exactly the desired state. The other Bell outcomes require corrections in ordinary teleportation. Those corrections are unavailable here.

With two specimens, Alice can do something more collective than run that one test. Let $E_1$ and $E_2$ project $BC_1$ and $BC_2$ onto the Bell state, respectively. The protocol uses

```math
G=2(E_1+E_2),
\qquad
J_s=\sqrt2\,L_sG^{-1/2},
\quad s\in\{1,2\},
```

where $L_s$ Bell-contracts the selected specimen and orders the survivor. The inverse square root is zero on the kernel. It is a known Alice operator, independent of $\alpha,\beta$.

The two-input symmetric sector has one nonzero spectral value $3$ for $G$. The useful branch therefore transfers one exact copy to Bob and leaves one exact specimen at Alice with total probability $1/3$. This agrees with the established single-port multicopy result and illustrates the normalization used by the general construction.

All outcomes must still be included in the deterministic score:

| Events retained | Probability | Receiver output or score |
|---|---:|---|
| Useful polar outcomes | $1/3$ | Exact $\lvert\psi\rangle$; Alice retains one specimen |
| Complementary outcome | $2/3$ | The same existing Bob port must still be selected |
| Every outcome together | $1$ | Bob's marginal is $I/2$, giving output fidelity $1/2$ |

The probability $1/3$ and the unconditional fidelity $1/2$ are different quantities. With only one port and no correction, Alice's local processing cannot change Bob's unconditional marginal. The global constructive bound $1/3$ is a valid lower bound, not the exact deterministic output fidelity in this example. [Endpoint checks](../science/construction.md#5-the-two-endpoint-checks) and [examples](../science/examples.md#one-port-exact-success-and-deterministic-output-differ) give the formal details.

## How the small mechanism becomes the resource law

For arbitrary $m,n$, Alice combines all pairs of port and input labels. Their Bell projectors overlap, so they cannot be treated as independent classical attempts. On the repeated-copy input, symmetry makes every useful branch give the same polar output after known routing.

Two moments then control its global fidelity. A shared inner resource half coupled to two identical pure inputs contributes $1/d$ to the relevant off-diagonal moment; other distinct pairs contribute $1/d^2$. This difference produces

```math
F_{\mathrm{global}}
\ge\frac{mn}{mn+(d-1)(d+n)}.
```

That is the constructive part. For necessity, averaging the exact fidelity score over unknown pure inputs produces a positive operator built from a symmetric projector and Bell terms. Completeness bounds its baseline; positivity bounds its other terms. The result, together with the receiver's marginal ceiling, matches the port budget order at fixed $F_0\in(1/2,1)$.

In the intermediate regime, for example $n$ of order $\sqrt d$, the required port supply has order $d^{3/2}$ rather than the one-specimen order $d^2$. Once $n$ reaches order $d$, the port supply saturates at order $d$. The [unequal-budget examples](../science/examples.md#the-intermediate-regime) explain why the regime before input tomography is accurate is the significant allocation change.

## What the book supplies and what this project adds

Watrous provides the mathematical foundations for states, channels, measurements, fidelity, teleportation and invariant averages. This project supplies the simultaneous finite-input/multiport task, the collective moment calculation, matching port-selection converse, joint-return statement and charged finite circuit. The [research attribution](../references/RELATED_WORK.md) separately credits port-based measurements, single-port multicopy teleportation, known-state preparation, the earlier two-Choi-pool construction, singular-value transformation and phase compilation.

The finite circuit requires research ingredients beyond the textbook. [Implementation](../science/implementation.md) states those ingredients and their resource/error accounting directly. They are proof dependencies, not additional educational anchors or an implicit requirement to learn an unrelated curriculum first.

Keep the result at its stated scope: identical pure specimens rather than an arbitrary reference-entangled input; Bob selecting a supplied port rather than applying general quantum processing; a fixed-fidelity resource frontier rather than exact heralded optimality; approximate joint return rather than an exact reusable catalyst. Stored noisy channels inherit the construction, while unrestricted programmable-processor optimality and end-to-end application advantage are not established.
