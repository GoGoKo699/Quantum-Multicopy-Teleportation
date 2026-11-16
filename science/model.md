# Model and resource frontier

The resource question is how additional specimens of quantum data change correction-free teleportation. The sender has repeated copies of one unknown state. The receiver has several candidate output ports. The receiver may choose a port, but cannot correct its quantum state after the sender's message.

## Operational contract

Fix integers $d\ge2$, $m\ge1$ and $n\ge1$. Alice and Bob initially share

```math
|\Phi_d\rangle_{A_1B_1}\cdots|\Phi_d\rangle_{A_mB_m},
\qquad
|\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j,j\rangle.
```

Bob holds the $A$ registers and Alice the $B$ registers. Alice additionally receives $n$ independent identical copies of an arbitrary unknown pure state $|\psi\rangle\in\mathbb C^d$, in registers $C_1,\ldots,C_n$.

Alice can apply any known joint quantum instrument to her registers, use private ancillas and adaptive measurements, and send a classical output-port label $r\in\{1,\ldots,m\}$. Bob routes $A_r$ to the output. His only quantum operations are the register permutations and discarding required for port selection and ordering. There is no conditional quantum correction, fresh-state preparation at the receiver, or quantum communication from Alice. Multiple Alice outcomes selecting the same port are allowed and can be coarse-grained for an output-only converse.

All $m$ resource pairs and all $n$ supplied input specimens count. Arbitrary connectivity for known local gates is permitted; [implementation](implementation.md) separately charges the collective measurement, routing, ancillas and finite synthesis. No QRAM, state description, preparation oracle, state reflection or execution oracle for an unknown channel is supplied. The basis defining the Bell pairs is known.

Let $\rho_{\mathrm{out}}(\psi)$ be Bob's unconditional output, including every instrument outcome. The output score is squared pure-state fidelity

```math
F_\psi=\langle\psi|\rho_{\mathrm{out}}(\psi)|\psi\rangle.
```

An average over Haar-random $\psi$ will be denoted $F_{\mathrm{av}}$. An upper bound on this average implies a necessary condition for a guarantee holding for every $\psi$.

The input contract concerns identical pure specimens. It does not provide $n$ copies of an arbitrary reference-entangled input, nor a diamond-norm simulation guarantee for a channel acting on an independently supplied quantum register.

## Constructive theorem: one joint return guarantee

There is an Alice-only collective instrument, independent of $\psi$, and port selection by Bob, with a global output state $\Omega_\psi$ satisfying

```math
F\bigl(\Omega_\psi,|w_\psi\rangle\bigr)
\ge \frac{mn}{mn+(d-1)(d+n)},
```

where the ideal jointly ordered target is

```math
|w_\psi\rangle
=|\psi\rangle_{\mathrm{out}}
 |\Phi_d\rangle^{\otimes(m-1)}
 |\psi\rangle^{\otimes(n-1)}.
```

The unselected pairs are shared between Alice and Bob; unselected input specimens remain at Alice. Known local routing places their registers in a fixed order. For a pure target, $F(\rho,|w\rangle)=\langle w|\rho|w\rangle$.

Tracing out the returned systems gives the same lower bound on $F_\psi$. Return is approximate and covered by this one global fidelity. Individual marginal fidelity statements would be weaker. Repeated use needs a separate accumulated-error calculation; the theorem does not supply exact catalysts.

The [construction proof](construction.md) gives the physical Kraus operators on the whole ordered input space. In particular, its kernel/failure outcome selects an existing Bob port and respects the same operational contract.

## Converse for every port-selection protocol

Every protocol in the contract above obeys

```math
F_{\mathrm{av}}
\le \min\left\lbrace 1,\frac{m}{d},
\frac{d+mn}{d(d+n)}\right\rbrace .
```

This converse applies to output fidelity alone, allows every input specimen and every resource pair to be consumed, and imposes no restriction on Alice's collective measurement or classical computation. Requiring a joint return cannot evade it. The [proof](converse.md) uses an exact Haar score operator and positivity, with a separate no-signalling bound.

For a uniform target fidelity $F_0$, it implies

```math
m\ge F_0d+\frac{F_0d^2-d}{n},
\qquad m\ge F_0d.
```

These are necessary inequalities, not an exact finite-budget optimum. The restrictions on Bob and the fixed independent Bell-pair resource are material. In particular, the proof is not a lower bound for an arbitrary global processor supplied with Choi programs.

## Matched order at fixed error

Fix $F_0\in(1/2,1)$, independent of $d,m,n$. The construction achieves $F_\psi\ge F_0$, including joint return, whenever

```math
m\ge \frac{F_0}{1-F_0}\,
\frac{(d-1)(d+n)}{n}.
```

Conversely, since $d\ge2$,

```math
m\ge F_0d+(F_0-1/2)\frac{d^2}{n}.
```

Consequently the minimum port budget for the stated output task, and also for its strengthened joint-return version, has order

```math
m_{\mathrm{opt}}(d,n;F_0)
=\Theta_{F_0}\!\left(d+\frac{d^2}{n}\right).
```

The constants are uniform over all integer $d\ge2,n\ge1$ and depend on $F_0$. This is a fixed-fidelity resource law. It does not determine the optimal constants, the exact heralded success probability, or the sharp joint dependence as $F_0\uparrow1$.

The [finite compiled circuit](implementation.md) attains the same fixed-error order, with a larger sufficient constant. An abstract POVM is therefore not being counted as a free physical operation.

## Stored-channel retrieval

For a CPTP map $\mathcal E:\mathcal L(\mathbb C^d)\to\mathcal L(\mathbb C^{d'})$, with known finite output dimension $d'$, define its normalized Choi state

```math
J_{\mathcal E}
=(\mathcal E_A\otimes\mathrm{id}_B)
 (|\Phi_d\rangle\langle\Phi_d|).
```

Replace the $m$ Bell pairs by independent copies of $J_{\mathcal E}$. Alice uses exactly the same measurement and Bob the same routing. The output target becomes

```math
\mathcal E(|\psi\rangle\langle\psi|)
\otimes J_{\mathcal E}^{\otimes(m-1)}
\otimes(|\psi\rangle\langle\psi|)^{\otimes(n-1)}.
```

The same global lower bound holds in squared Uhlmann fidelity, including noisy and nonunital channels. Apply $\mathcal E$ to every Bob register in the Bell-resource theorem: it commutes with Alice's measurement, is equivariant under port permutations, and cannot reduce fidelity. This is an upper bound for retrieval from supplied program specimens; it does not infer free physical preparation of those specimens.

For unitary $\mathcal E(\rho)=U\rho U^\dagger$, the target output is $U|\psi\rangle$ and each returned program is a pure normalized Choi state. This application illustrates a quantum-data algorithm. The matching necessity theorem remains the port-teleportation theorem above.

## Reading route

Read [construction](construction.md) for the common-branch polar mechanism, [converse](converse.md) for necessity, [implementation](implementation.md) for the Alice-only circuit, and [examples](examples.md) for the unequal-budget regimes. [Related work](../references/RELATED_WORK.md) separates inherited ingredients from the result proved here.
