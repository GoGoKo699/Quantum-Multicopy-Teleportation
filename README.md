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

## Read the science

Start with the [scientific route](science/README.md) and [model and exact claims](science/model.md).

| Question | Authoritative account |
|---|---|
| How does the collective measurement work and preserve the remaining specimens? | [Construction and global return](science/construction.md) |
| Why can no sender measurement beat the resource order? | [Haar-score converse](science/converse.md) |
| What do known gates, finite precision, work and routing cost? | [Alice-only circuit](science/implementation.md) |
| Why do extra input copies help before input tomography is accurate? | [Examples and interpretation](science/examples.md) |
| What is inherited, and how does this differ from earlier teleportation and program results? | [Related work](references/RELATED_WORK.md) |
| Which finite identities and channels were checked? | [Verification](verification/README.md) |

The measurement and polar-normalization machinery are inherited from port-based teleportation, entanglement recycling and [Quantum Program Composition](https://github.com/GoGoKo699/Quantum-Program-Composition). The contribution here is the finite-input resource frontier, its port-selection converse, and an implementation respecting the sender/receiver boundary. The [attribution account](references/RELATED_WORK.md) separates these claims.

## Scope

All supplied specimens, collective gates and workspace count. There is no QRAM or free state-loading oracle. The repeated inputs are independent copies of one pure state. Global return is approximate and one-shot; repeated reuse needs its own error budget. Optimal exact heralded performance and vanishing-error constants are not established. The copy advantage is not an end-to-end runtime or hardware crossover claim.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
