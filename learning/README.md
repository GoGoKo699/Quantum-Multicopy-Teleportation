# Learning the result

How much can extra copies of an unknown input save when the receiver can only select a Bell port? At fixed uniform squared fidelity above one half, the deterministic task needs a port budget of order $`d+d^2/n`$. Here $`d`$ is the input dimension and $`n`$ is the number of identical pure specimens. A second task asks the sender to announce when the transfer is exact and all unused resources have been returned. Its optimal success probability for $`m`$ ports and $`n`$ specimens is $`\max(m,n)/[d(\max(m,n)+d-1)]`$.

Read the [Watrous bridge](anchor.md) for the physical story, source-to-project notation and a complete two-copy qubit example. Then follow the [30-milestone map](milestones.md): 12 background milestones assemble the operational language, and 18 narrative milestones connect the mechanism, lower bound, finite circuit and scientific meaning. The map describes this project's common understanding targets; the linked scientific pages remain authoritative for exact claims.

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Its [targeted section map](anchor.md#source-map) makes selected foundations available without assigning the whole book. Primary research sources in the scientific account provide attribution and specialist ingredients rather than a second educational anchor.

| Reading purpose | Route |
|---|---|
| Understand the task and the conditional/unconditional distinction | [Bridge and worked example](anchor.md#one-complete-small-example), then [model](../science/model.md) |
| Follow the complete conceptual progression | [Milestones](milestones.md), with [science entrypoint](../science/README.md) alongside |
| Work through the deterministic protocol and its joint fidelity guarantee | [Construction](../science/construction.md) |
| Find the exact success probability, the conditional fidelity tradeoff, or the cost of spending several pairs | [Exact return](../science/exact-return.md) |
| Understand why every sender measurement obeys the same resource order | [Converse](../science/converse.md) |
| Inspect known gates, storage, routing and finite precision | [Implementation](../science/implementation.md) |
| Compare useful regimes and prior results | [Examples](../science/examples.md) and [related work](../references/RELATED_WORK.md) |
| Reproduce the finite checks and understand their limits | [Verification](../verification/README.md) |

Both tasks assume independent Bell pairs, identical pure input copies and a receiver restricted to port selection. The deterministic theorem evaluates every branch through one joint fidelity score. The heralded theorem constrains the accepted branches, including the spare Bell pairs and the specimens returned to Alice. The one-pair budget includes the selected pair.
