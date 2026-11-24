# Thirty milestones for multicopy teleportation

This is a common understanding map for the project. The first **12 milestones** assemble the objects and operational distinctions needed to state the problem. The remaining **18 milestones** connect the deterministic frontier, finite implementation and heralded return laws. Both phases move from individual objects to the complete scientific account.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Section references below use the [verified source map](anchor.md#source-map). The textbook supplies foundations; the linked scientific pages supply this project's arguments. The map does not replace the proofs or prescribe a personal study schedule.

## Background and preliminaries

### M01 — Name the three resources

- **Central question:** What do the state dimension, input-copy supply and port supply count?
- **Understanding target:** Distinguish $d$ basis dimensions from $n$ supplied input specimens and $m$ shared Bell pairs; identify Alice's and Bob's registers.
- **Dependencies and story role:** No earlier milestone. Establishes the physical objects before any complexity formula appears.
- **Conceptual connection:** Register tensor products turn a resource inventory into a precise input state.
- **Source pointers:** Watrous §§2.1.1–2.1.2; [operational contract](../science/model.md#operational-contract).

### M02 — Copies are a promise about the input

- **Central question:** What information does a source of identical pure specimens provide?
- **Understanding target:** Explain the product state $\psi^{\otimes n}$ without assuming knowledge of $\psi$, a preparation inverse, or access to a reference-entangled input.
- **Dependencies and story role:** M01. Specifies what the second resource supplies and prevents a channel-simulation interpretation from entering unnoticed.
- **Conceptual connection:** Independence of specimens differs from a classical description and from coherent oracle access.
- **Source pointers:** Watrous §2.1.2; [operational contract](../science/model.md#operational-contract).

### M03 — A Bell pair has an uninformative local marginal

- **Central question:** How can a shared pure resource look maximally mixed at either laboratory?
- **Understanding target:** Obtain the marginal $I/d$ by a partial trace and distinguish the shared state from either local state.
- **Dependencies and story role:** M01–M02. Introduces the resource that makes teleportation possible and the marginal constraint used in the converse.
- **Conceptual connection:** Global correlations and local ignorance coexist; local outcome selection must be distinguished from altering an unconditional remote marginal.
- **Source pointers:** Watrous §2.1.3; [Bell resources](../science/model.md#operational-contract); [no-signalling bound](../science/converse.md#4-the-no-signalling-ceiling).

### M04 — Store an operation as a state

- **Central question:** What is present when a channel is supplied through Choi specimens?
- **Understanding target:** Define the normalized program $J_{\mathcal E}$ and explain why possessing copies is different from having a live execution oracle.
- **Dependencies and story role:** M01–M03. Opens the computational application while keeping its input interface explicit.
- **Conceptual connection:** A channel acting on half of a known Bell pair converts an operation into quantum data; the inverse conversion is a processing task.
- **Source pointers:** Watrous §2.2.2; [normalization dictionary](anchor.md#notation-dictionary); [stored-channel model](../science/model.md#stored-channel-retrieval).

### M05 — An instrument has outcomes and physical branches

- **Central question:** How is a collective measurement represented without assuming its outcomes are exact successes?
- **Understanding target:** Relate Kraus operators to positive measurement effects, and recognize completeness as the condition that includes every outcome.
- **Dependencies and story role:** M01–M03. Supplies the language for both the constructive protocol and the unrestricted Alice measurement in the lower bound.
- **Conceptual connection:** An outcome probability and the normalized state conditioned on that outcome are separate pieces of an instrument.
- **Source pointers:** Watrous §§2.2.2, 2.3.1–2.3.2; [physical instrument](../science/construction.md#1-an-alice-only-bell-sum-instrument).

### M06 — Conditional success and deterministic quality differ

- **Central question:** Which outcomes enter each teleportation guarantee?
- **Understanding target:** Distinguish exact heralded success probability, squared fidelity conditional on acceptance, and deterministic fidelity across all outcomes.
- **Dependencies and story role:** M03 and M05. Establishes the three quantities that already differ in the one-port example.
- **Conceptual connection:** A herald selects the branches to score. Averaging all outcomes restores the deterministic channel and its marginal constraints.
- **Source pointers:** Watrous §§2.1.2, 2.3.2 and 3.2.1, [one-port distinction](../science/examples.md#one-port-exact-success-and-deterministic-output-differ), and [conditional fidelity](../science/exact-return.md).

### M07 — Score a joint quantum output

- **Central question:** How are the teleported output and the returned resources scored together?
- **Understanding target:** Compare the deterministic squared fidelity to a global product target with the requirement that spare pairs and specimens return exactly on an accepted branch.
- **Dependencies and story role:** M02–M06. Defines the two return contracts before their proofs.
- **Conceptual connection:** Tracing out the return registers passes a joint fidelity guarantee to the selected output. Exact return of a pure spare Bell pair also forces it to factor from the rest of an accepted branch.
- **Source pointers:** Watrous §§3.2.1–3.2.3, [deterministic joint target](../science/model.md#constructive-theorem-one-joint-return-guarantee), and [exact-return contract](../science/exact-return.md).

### M08 — Remove the receiver correction

- **Central question:** What changes when Bob is allowed to select a port but cannot correct its state?
- **Understanding target:** Contrast ordinary teleportation with the permitted port-selection operations, including the absence of fresh-state preparation at Bob.
- **Dependencies and story role:** M03, M05 and M06. Identifies the physical restriction whose resource cost the project determines.
- **Conceptual connection:** A classical outcome can specify a correction in ordinary teleportation; here it can specify only a register to keep.
- **Source pointers:** Watrous §6.3.1; [operational contract](../science/model.md#operational-contract); [bridge](anchor.md#the-task-before-the-formulas).

### M09 — Repeated states occupy a symmetric sector

- **Central question:** Which register permutations leave the supplied input unchanged?
- **Understanding target:** Recognize symmetry among identical input specimens and symmetry among whole resource pairs, without assuming that separate resource halves can be exchanged as if they were whole pairs.
- **Dependencies and story role:** M01–M03. Prepares the mathematical reduction that makes all useful routed branches coincide.
- **Conceptual connection:** Permutation symmetry is a property used in a proof; it is not a gate requiring access to Bob's systems.
- **Source pointers:** Watrous §7.1.1; [whole-copy symmetry](../science/construction.md#2-symmetry-gives-one-common-polar-output).

### M10 — Average over unknown pure inputs

- **Central question:** How can a lower bound test every possible input without knowing which one was supplied?
- **Understanding target:** Explain normalized Haar averaging, the symmetric-subspace projector and the role of a basis transpose in a Bell contraction.
- **Dependencies and story role:** M03, M05 and M09. Joins symmetry to the score calculation used for necessity.
- **Conceptual connection:** A bad average performance rules out a uniformly good protocol; partial transpose in the calculation is not a physical operation performed by Alice.
- **Source pointers:** Watrous §§7.1.1, 7.2.1–7.2.2; [Haar score](../science/converse.md#2-the-haar-score-identity).

### M11 — Read a positive operator through its spectrum

- **Central question:** Why can an operator calculation use expectations and variances?
- **Understanding target:** Interpret the spectral measure of a positive operator in a specified input state, and connect square roots and polar decomposition to singular values.
- **Dependencies and story role:** M05 and M09. Introduces the linear-algebra and probability tools used by the protocol and its finite circuit.
- **Conceptual connection:** Spectral expectations are ordinary moments of a nonnegative variable; this does not make the underlying Bell projectors independent or commuting.
- **Source pointers:** Watrous §§1.1.3, 1.2.2; [moments](../science/construction.md#3-the-two-moments-that-determine-the-bound); [singular vectors](../science/implementation.md#3-transforming-singular-vectors).

### M12 — Assemble the operational question

- **Central question:** What must be fixed before the expression $d+d^2/n$ has scientific meaning?
- **Understanding target:** State the input-copy promise, independent Bell-pair resource, Alice's freedom and Bob's restriction. Specify whether the task scores every branch or imposes exact return obligations on accepted branches.
- **Dependencies and story role:** M01–M11. Integrates the background phase into the exact problem the research solves.
- **Conceptual connection:** The same asymptotic expression can describe different tasks; its controls, resources and output convention determine which theorem applies.
- **Source pointers:** Watrous Chapters 2–3 and §6.3.1; [model and frontier](../science/model.md).

## Narrative and innovation

### M13 — Follow one Bell contraction

- **Central question:** What happens when one input copy meets one inner resource half?
- **Understanding target:** Derive the amplitude factor $1/d$ multiplying $U|\psi\rangle$, and hence the $1/d^2$ probability of that isolated Bell outcome.
- **Dependencies and story role:** M03–M05 and M08. Establishes the local operation from which the collective mechanism is built.
- **Conceptual connection:** Known teleportation algebra converts a stored unitary program into action on quantum data, but a single selected contraction rarely succeeds.
- **Source pointers:** Watrous §§2.2.2, 6.3.1; [contraction identity](../science/construction.md#2-symmetry-gives-one-common-polar-output); [worked example](anchor.md#one-complete-small-example).

### M14 — Combine choices without treating them as independent trials

- **Central question:** How can the protocol use all port-and-input choices together?
- **Understanding target:** Define the Bell-sum operator $G$ and explain why its overlapping projectors need a collective normalization.
- **Dependencies and story role:** M05, M11 and M13. Replaces isolated attempts by the actual collective instrument.
- **Conceptual connection:** Sharing a specimen or port creates operator overlaps; multiplying independent success probabilities would describe a different protocol.
- **Source pointers:** Watrous §§1.1.3, 2.3.1; [Bell-sum instrument](../science/construction.md#1-an-alice-only-bell-sum-instrument).

### M15 — Include the kernel outcome physically

- **Central question:** Why is the protocol valid on the whole input space and in every branch?
- **Understanding target:** Check that the useful effects sum to the support projector of $G$ and that the complementary branch selects an existing Bob port.
- **Dependencies and story role:** M05, M08 and M14. Turns the formal collective expression into a complete permitted protocol.
- **Conceptual connection:** A proof cannot discard an inconvenient kernel outcome or repair it by an operation forbidden to the receiver.
- **Source pointers:** Watrous §§2.2.2, 2.3.1; [kernel completion](../science/construction.md#1-an-alice-only-bell-sum-instrument).

### M16 — Route every useful branch to the same target

- **Central question:** Why do different selected pairs lead to the same polar output after known ordering?
- **Understanding target:** Use separate whole-pair and input-copy symmetries to justify the common contraction map on the symmetric input sector.
- **Dependencies and story role:** M09 and M13–M15. Explains why a single global fidelity calculation covers all useful outcomes.
- **Conceptual connection:** Relabeling makes branch outputs comparable; it does not introduce an unknown-state correction at Bob.
- **Source pointers:** Watrous §7.1.1; [common polar output](../science/construction.md#2-symmetry-gives-one-common-polar-output).

### M17 — Express global fidelity as one spectral moment

- **Central question:** How does the physical instrument become a scalar expression involving $\sqrt G$?
- **Understanding target:** Follow $M^{\dagger}M=G$ on the relevant sector and obtain the unconditional useful contribution $\langle\sqrt G\rangle^2/\mu$.
- **Dependencies and story role:** M07, M11 and M16. Joins the target state, physical branches and polar normalization.
- **Conceptual connection:** The polar map removes the singular-value distortion of the contraction; its fidelity is still evaluated on the supplied input state.
- **Source pointers:** Watrous §§1.1.3, 3.2; [polar fidelity identity](../science/construction.md#2-symmetry-gives-one-common-polar-output).

### M18 — Find the exceptional shared-port moment

- **Central question:** Which overlap distinguishes repeated pure inputs from a second pool of Choi programs?
- **Understanding target:** Separate diagonal, shared-inner-half and other pair products, identifying the exceptional expectation $1/d$ instead of $1/d^2$.
- **Dependencies and story role:** M11, M14 and M17. Locates the calculation responsible for the one-sided port floor.
- **Conceptual connection:** The pure repeated-input marginal changes the variance of $G$; a familiar measurement construction need not have the same resource law in a different input model.
- **Source pointers:** Watrous §§1.1.2, 2.1.3; [exact two moments](../science/construction.md#3-the-two-moments-that-determine-the-bound).

### M19 — Turn variance into a return guarantee

- **Central question:** Why do two moments suffice to prove the constructive bound?
- **Understanding target:** Normalize $G$ to mean one, apply the displayed Hölder step, and identify the resulting global fidelity as a lower bound rather than an exact optimum.
- **Dependencies and story role:** M07, M17 and M18. Completes the analytical construction and its simultaneous return statement.
- **Conceptual connection:** Moment control limits polar distortion on the supplied family, including all returned systems together.
- **Source pointers:** Watrous §§1.1.3, 1.2.2, 3.2; [fidelity bound](../science/construction.md#4-from-moments-to-fidelity).

### M20 — Let Alice use every possible strategy

- **Central question:** How can a converse cover adaptive collective processing rather than one chosen circuit?
- **Understanding target:** Coarse-grain all histories selecting a given port into one POVM effect and explain why Alice's retained outputs disappear from Bob's output-only score.
- **Dependencies and story role:** M05, M08 and M12. Opens the necessity proof without artificially restricting the sender.
- **Conceptual connection:** The receiver's output rule compresses a general local protocol into a measurement optimization.
- **Source pointers:** Watrous §§2.2–2.3; [port POVM reduction](../science/converse.md#1-every-alice-protocol-gives-a-port-povm).

### M21 — Build the exact positive score operator

- **Central question:** What does the Haar average of the fidelity score look like?
- **Understanding target:** Connect the symmetric projector on $n+1$ copies, its partial transpose and the positive sum of Bell terms in the score identity.
- **Dependencies and story role:** M09–M10, M13 and M20. Supplies the task-specific operator against which every Alice measurement is tested.
- **Conceptual connection:** Permutation symmetry makes an infinite input average finite and explicit; the resulting decomposition allows a positivity bound.
- **Source pointers:** Watrous §§7.1.1, 7.2.1–7.2.2; [Haar score proof](../science/converse.md#2-the-haar-score-identity).

### M22 — Extract the unavoidable port and copy costs

- **Central question:** How do completeness, positivity and no-signalling constrain the score?
- **Understanding target:** Explain the baseline contribution $1/(d+n)$, the bound on each positive Bell term, and the separate ceiling $m/d$.
- **Dependencies and story role:** M03, M20 and M21. Converts the score identity into exact finite necessary inequalities.
- **Conceptual connection:** The lower bound uses all of Alice's freedom while retaining the fixed resource and Bob-only-selection assumptions.
- **Source pointers:** Watrous §§2.3.1, 2.1.3; [score bound](../science/converse.md#3-bounding-the-entire-port-measurement); [no-signalling ceiling](../science/converse.md#4-the-no-signalling-ceiling).

### M23 — Match the frontier at fixed fidelity

- **Central question:** When do the upper and lower results establish the same resource order?
- **Understanding target:** Hold $F_0\in(1/2,1)$ fixed and recover a port budget of order $d+d^2/n$, with constants depending on $F_0$.
- **Dependencies and story role:** M19 and M22. Unifies sufficiency and necessity into the central theorem.
- **Conceptual connection:** Matching an asymptotic order differs from finding the exact finite-budget fidelity or optimal vanishing-error dependence.
- **Source pointers:** Watrous §§1.1–1.2 for the underlying algebra; [fixed-error statement](../science/model.md#matched-order-at-fixed-error); [matched frontier](../science/converse.md#5-the-matched-fixed-fidelity-frontier).

### M24 — Locate the useful intermediate regime

- **Central question:** What changes before enough input copies exist for accurate input estimation?
- **Understanding target:** Follow $n=\Theta(d^\alpha)$ with $0\lt\alpha\lt1$ to $m=\Theta(d^{2-\alpha})$ and explain why the balanced point alone is not the whole contribution.
- **Dependencies and story role:** M02 and M23. Gives the resource law its operational meaning.
- **Conceptual connection:** Coherently supplied quantum data can reduce stored-port cost before an estimate-then-prepare route learns an accurate classical input description.
- **Source pointers:** Watrous §2.3 for measurements; [unequal-budget examples](../science/examples.md#the-intermediate-regime); [input-estimation comparison](../science/examples.md#why-learning-the-input-first-does-not-explain-every-regime); research attribution in [related work](../references/RELATED_WORK.md).

### M25 — Find the exact success probability with one pair spent

- **Central question:** Can combining all ports with all specimens help when each accepted branch must return every spare pair?
- **Understanding target:** Explain why an exact Bell-pair return removes the spare half from the branch effect, and why covariance leaves separate weights for a canonical contraction subspace and its complement. State $`p_0=\max(m,n)/[d(\max(m,n)+d-1)]`$ and recover the single-port and one-specimen endpoints.
- **Dependencies and story role:** M06–M09, M13–M14 and M20–M22. Brings the return requirement into the converse and identifies the attaining endpoint protocol.
- **Conceptual connection:** Completeness constrains the sum over possible selected ports. With exact spare returns and one pair spent, the larger supply determines the optimum. The same norm can be tracked into the exact-return laws for composition and purification by identifying the different output maps.
- **Source pointers:** Watrous §§2.2.2, 2.3.1 and 7.2.1, [endpoint checks](../science/construction.md#5-the-two-endpoint-checks), [exact-return proof](../science/exact-return.md), and [three-project comparison](../science/exact-return.md#how-exact-return-compares-across-three-tasks).

### M26 — Retrieve a noisy stored channel

- **Central question:** Why does the same construction work when each outer half has passed through an arbitrary channel?
- **Understanding target:** Move the same CPTP map through Alice's operations and port routing, then apply fidelity monotonicity to the complete returned-resource target.
- **Dependencies and story role:** M04, M07 and M19. Connects the teleportation theorem to action on quantum data.
- **Conceptual connection:** Equivariance supplies a constructive extension, including nonunital channels, without extending the converse to unrestricted programmable processors.
- **Source pointers:** Watrous §§2.2.2, 3.2.3; [stored-channel proof](../science/construction.md#6-stored-channel-retrieval); [noisy example](../science/examples.md#a-noisy-stored-operation).

### M27 — Keep the compiler inside Alice's laboratory

- **Central question:** How is the collective contraction encoded by known gates without touching Bob's ports?
- **Understanding target:** Follow label preparation, stable register selection and Bell unpreparation, and identify the input/output projectors of the rectangular encoding.
- **Dependencies and story role:** M08, M14–M16 and M19. Bridges the abstract instrument to a finite circuit with the same operational boundary.
- **Conceptual connection:** Whole-pair symmetry belongs to the proof; coherent routing and signal tests in the implementation act only on Alice's registers.
- **Source pointers:** Watrous §§1.1.3, 2.2.2 for operator representations; [projected encoding](../science/implementation.md#2-an-alice-only-projected-encoding). Singular-value transformation is a separately cited research ingredient there.

### M28 — Pay for cutoff, precision and workspace

- **Central question:** How can a finite circuit approximate the polar operation without a promised minimum nonzero singular value?
- **Understanding target:** Explain the state-dependent small-spectrum bound, polynomial cutoff and synthesis error budget, and identify the charged gates, storage and ancillas.
- **Dependencies and story role:** M11, M18–M19 and M27. Completes the algorithmic resource account without treating the POVM as free.
- **Conceptual connection:** Spectral weight on the promised input controls approximation loss; whole-circuit finite precision is a different bound and must also be paid.
- **Source pointers:** Watrous §§1.1.3, 1.2.2; [cutoff argument](../science/implementation.md#4-why-a-state-dependent-cutoff-preserves-the-global-target); [routing and precision](../science/implementation.md#5-routing-padding-and-finite-precision).

### M29 — Charge all the pairs spent on an accepted branch

- **Central question:** How much can success probability grow if Alice may spend up to $`\ell`$ pairs, counting the selected pair?
- **Understanding target:** Explain the upper bound $`p\le\min(1,e\ell/d)`$ and how $`\ell`$ independent one-port protocols using $`d`$ specimens each attain its order when the supplies suffice. Include pairs from failed trials in the accepted branch's budget and allow the trials to consume input specimens.
- **Dependencies and story role:** M07, M13, M20–M22 and M25. Extends the exact-output result to a budget with several pairs spent.
- **Conceptual connection:** An accepted branch can preserve many spares while the pairs used along the way still count. At constant exact success the number spent has order at least $`d`$, even with many supplied pairs.
- **Source pointers:** [Pair spending and exact success](../science/exact-return.md), [related work](../references/RELATED_WORK.md), and the [worked examples](../science/examples.md).

### M30 — Reconcile success probability, fidelity and return

- **Central question:** How does the best heralding probability change if the selected output may be approximate while spare returns stay exact?
- **Understanding target:** Explain the optimal tradeoff $`P=p_0(1-1/d)/[F-1/d+p_0(1-F)]`$ for conditional squared fidelity $`F`$ from $`1/d`$ to $`1`$. Compare its endpoints with the deterministic fixed-fidelity resource frontier and the exact-output spending law. State which guarantees the finite checks test.
- **Dependencies and story role:** M12–M29. Synthesizes the three return guarantees, the conditions under which they apply and the physical operations they charge.
- **Conceptual connection:** Accepting more branches can lower conditional fidelity. The exact-return requirement keeps the operation on spare pairs fixed as Alice adjusts her acceptance rule.
- **Source pointers:** [Conditional fidelity and exact return](../science/exact-return.md), [worked example](anchor.md#what-exact-return-changes), [deterministic resource frontier](../science/model.md), [finite implementation](../science/implementation.md), and [verification](../verification/README.md).
