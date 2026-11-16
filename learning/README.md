# Learning the result

The starting question is concrete: **if a receiver cannot correct a teleported state, how much can additional copies of the unknown input save in shared Bell ports?** The answer is a matched port budget of order $d+d^2/n$ at any fixed uniform squared fidelity above one half. Here $d$ is the input dimension and $n$ is the number of identical pure specimens supplied to the sender.

Read the [Watrous bridge](anchor.md) for the physical story, source-to-project notation and a complete two-copy qubit example. Then follow the [30-milestone map](milestones.md): 12 background milestones assemble the operational language, and 18 narrative milestones connect the mechanism, lower bound, finite circuit and scientific meaning. The map describes this project's common understanding targets; the linked scientific pages remain authoritative for exact claims.

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Its [targeted section map](anchor.md#source-map) makes selected foundations available without assigning the whole book. Primary research sources in the scientific account provide attribution and specialist ingredients rather than a second educational anchor.

| Reading purpose | Route |
|---|---|
| Understand the task and the conditional/unconditional distinction | [Bridge and worked example](anchor.md#one-complete-small-example), then [model](../science/model.md) |
| Follow the complete conceptual progression | [Milestones](milestones.md), with [science entrypoint](../science/README.md) alongside |
| Check the collective mechanism and returned-resource statement | [Construction](../science/construction.md) |
| Understand why every sender measurement obeys the same resource order | [Converse](../science/converse.md) |
| Inspect known gates, storage, routing and finite precision | [Implementation](../science/implementation.md) |
| Compare useful regimes and prior results | [Examples](../science/examples.md) and [related work](../references/RELATED_WORK.md) |
| Reproduce the finite checks and understand their limits | [Verification](../verification/README.md) |

The resource law assumes independent Bell pairs, identical pure input copies and a receiver restricted to port selection. The construction approximately returns unused pairs and specimens under one joint fidelity guarantee. It does not provide exact catalysts, an arbitrary entangled-input channel simulator, or a demonstrated end-to-end runtime advantage. These distinctions are part of understanding the theorem, not optional details after the formulas.
