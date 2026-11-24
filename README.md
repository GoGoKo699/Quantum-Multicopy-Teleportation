# Quantum Multicopy Teleportation

**How much shared entanglement can extra copies of an unknown input save when teleportation must work without a receiver correction?**

Alice receives $n$ identical unknown pure states of dimension $d$. Alice and Bob share $m$ independent maximally entangled pairs. Alice performs a collective measurement; Bob selects an output port without applying a correction. At any fixed uniform squared fidelity above one half, the optimal port budget is

```math
m_{\mathrm{opt}}
=\Theta\!\left(d+\frac{d^2}{n}\right).
```

The constants depend on the fixed target fidelity. The [exact model](science/model.md) keeps the receiver restriction, resource state and output convention explicit.

| Input supply | Fixed-error Bell-port order |
|---|---:|
| One input specimen | $d^2$ |
| $1\ll n\ll d$ specimens | $d^2/n$ |
| $n$ of order $d$ or larger | $d$ |

The construction also approximately returns the unused resource pairs and input specimens under one global fidelity guarantee:

```math
F_{\mathrm{global}}
\ge\frac{mn}{mn+(d-1)(d+n)}.
```

A matching converse allows every sender instrument and requires only output fidelity. It applies to the correction-free port-selection model. Moving an arbitrary channel to the outer halves gives the same constructive bound for retrieving that stored channel from normalized Choi specimens, including noisy and nonunital channels. No unrestricted programmable-processor optimality is inferred.

## Exact return of unused Bell pairs

When success must certify the exact selected output and the exact return of every unused Bell pair, the optimal worst-case success probability is

```math
p_0=\frac{\max(m,n)}{d[\max(m,n)+d-1]}\lt\frac1d.
```

An optimal protocol also returns the $`n-1`$ unused input specimens on success. The bound holds even if Alice is free to discard them. The [exact-return theorem](science/exact-return.md) also gives the complete tradeoff between heralding probability and conditional output fidelity when all unused Bell pairs are returned exactly.

Constant success for exact output requires spending a number of Bell pairs proportional to $`d`$ on the accepted branch. Spending that order suffices with enough input specimens. This counts the selected pair and any other pairs sacrificed before the success flag.

The [three-project comparison](science/exact-return.md#how-exact-return-compares-across-three-tasks) follows the same contraction norm into [Quantum Program Composition](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/main/science/exact_joint_return.md) and [Canonical Purification Cost](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/main/science/exact_joint_return.md). Exact composition with all spare Choi programs returned has the same success probability as exact Bell-port teleportation. Canonical purification has a different success probability because its target includes a known vacuum component.

## Read the science

Start with the [scientific route](science/README.md) and [model and exact claims](science/model.md).

| Question | Authoritative account |
|---|---|
| How does the collective measurement work and preserve the remaining specimens? | [Construction and global return](science/construction.md) |
| What changes when unused Bell pairs must be returned exactly? | [Exact heralding and Bell-pair expenditure](science/exact-return.md) |
| Why can no sender measurement beat the resource order? | [Haar-score converse](science/converse.md) |
| What do known gates, finite precision, work and routing cost? | [Alice-only circuit](science/implementation.md) |
| Why do extra input copies help before input tomography is accurate? | [Examples and interpretation](science/examples.md) |
| What is inherited, and how does this differ from earlier teleportation and program results? | [Related work](references/RELATED_WORK.md) |
| Which finite identities and channels were checked? | [Verification](verification/README.md) |

The measurement and polar-normalization machinery are inherited from port-based teleportation, entanglement recycling and [Quantum Program Composition](https://github.com/GoGoKo699/Quantum-Program-Composition). The contribution here is the finite-input resource frontier, its port-selection converse, and the sharp cost of exact Bell-pair return. The Alice-only implementation treats the deterministic approximate protocol. The [attribution account](references/RELATED_WORK.md) separates these claims.

## Learn the mechanism

The [learning route](learning/README.md) begins with a concrete teleportation task and connects it to the construction and converse. Its [30 milestones](learning/milestones.md) move from states and instruments to the complete resource law. The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018); the [source bridge](learning/anchor.md) maps its foundations to this project's notation and identifies the arguments supplied here.

## Reproduce the finite checks

With Python 3.10 or later, run these commands from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/verify.py
python3 verification/check_exact_return.py
```

The [verification account](verification/README.md) explains the checked physical instruments, Bell moments, Haar identities, projected encoding, noisy channels, and the exact-return laws. Dense finite checks support those identities; the general bounds and finite-precision circuit costs use the analytical proofs.

## Scope

All supplied specimens, collective gates and workspace count. There is no QRAM or free state-loading oracle. The repeated inputs are independent copies of one pure state. The deterministic joint-return guarantee is approximate and one-shot. The heralded protocol returns the stated resources exactly on successful branches. The unrestricted exact-output optimum with both resources finite and the sharp vanishing-error constants for approximate return remain open. The copy advantage is not an end-to-end runtime or hardware crossover claim.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
