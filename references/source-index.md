# Inspected sources and claim dependencies

The comparison below was checked on 16 November 2026. It records the scope of inspection rather than asserting an exhaustive priority search. The all-dimensional resource proofs are in this repository; imported algorithmic theorems and inherited measurement ideas are credited separately.

| Source | Inspected scope | Role and boundary |
|---|---|---|
| [Grosshans et al., arXiv:2409.10393v2](https://arxiv.org/html/2409.10393v2), 27 April 2026, Quantum 10, 2105 | Full primary HTML setup, main result, construction and discussion; exact one-port formula and simultaneous multicopy/multiport future direction checked | Closest task antecedent. Its exact heralded single-port theorem is recovered as an endpoint. Its future-direction statement is not a proof of our deterministic approximate frontier. |
| [Muguruza–Speelman, Quantum 8, 1573](https://quantum-journal.org/papers/q-2024-12-18-1573/), arXiv:2402.18356v2 | Primary task, stated performance and program application; known-state promise checked | Known-classical-input port preparation. Fixed-error endpoint and estimate-then-prepare comparison; its sharp vanishing-error behavior is not claimed here. |
| [Ishizaka–Hiroshima, PRL 101, 240501](https://doi.org/10.1103/PhysRevLett.101.240501), and PRA 79, 042306 | Established protocol and fixed-resource setting, cross-checked against the primary multicopy paper | Port selection and correction-free retrieval are inherited. The present one-input bound is a sufficient approximate-global-fidelity bound, not a new exact single-input optimum. |
| [Strelchuk–Horodecki–Oppenheim, PRL 110, 010505](https://doi.org/10.1103/PhysRevLett.110.010505) | Measurement, signal-moment and recycling framework; source also identified by arXiv:1209.2683 | General moment/recycling machinery is credited. Our displayed constants are derived here rather than imported from this source. |
| [Quantum Program Composition, pinned construction](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/8ae6b6b0e04c9507d148911ac0c58c7bf0670682/science/construction.md) | README, complete construction and implementation at commit 8ae6b6b0e04c9507d148911ac0c58c7bf0670682 | Direct polar/routing/moment predecessor. Two Choi pools have a different inner marginal. Its whole-program symmetry compiler is not an allowed Alice-only gate here. |
| [Gilyén–Su–Low–Wiebe, arXiv:1806.01838v1](https://arxiv.org/abs/1806.01838v1) | Projected singular-value transformation and sign approximation: Corollary 18, Lemma 25, Theorem 26 | Imported finite polynomial/transform theorem. The Alice-only encoding, state-weighted cutoff and complete error accounting are supplied here. |
| [Haah, arXiv:1806.10236](https://arxiv.org/abs/1806.10236), Quantum 3, 190 | Primary preprocessing statement and algorithmic scope | Known classical QSP phase preprocessing; no unknown-data loading or program inversion. |
| [Bruß–Macchiavello, quant-ph/9812016](https://arxiv.org/abs/quant-ph/9812016) | Primary full short HTML, universal pure-state estimation fidelity | Establishes the estimate-then-prepare input-loss baseline. This is a statistical comparison, not a classical runtime lower bound. |
| [Mafi–Moghaddam, arXiv:2611.00874v1](https://arxiv.org/html/2611.00874v1), 31 October 2026 | Full primary HTML, resource diagram, single- and multi-qubit experiments, noise and circuit discussion | Latest nearby experiment remains one program port; a multi-qubit program is not multiple independent alternative ports. |
| [Mozrzymas–Studziński–Kopszak, Quantum 5, 477](https://quantum-journal.org/papers/q-2021-06-17-477/) | Primary abstract and task description | Several distinct teleported subsystems and several outputs. This comparison does not claim a full independent reconstruction of its optimization formulas. |
| [Okada–Kato–Buscemi, arXiv:2501.16878v2](https://arxiv.org/abs/2501.16878v2), 10 May 2025 | Primary metadata and abstract/task | Port telecloning has one input and multiple approximate outputs, not repeated identical inputs for one output. |
| [Brzić et al., arXiv:2510.20530v2](https://arxiv.org/html/2510.20530v2), 16 November 2025 | Primary setup, summary, Sections 8–9 and discussion of copies as partial input knowledge | Known-state higher-order computation and flexible storage stage. Conceptual connection is inherited; no finite-copy frontier is inferred from that stronger promise. |

Related internal purification and thermal-teleportation accounts were checked for task overlap. Their inputs, target outputs and receiver control differ. They are not proof dependencies of the frontier here.

The comparison covers current accessible versions of the closest identified accounts and targeted searches for multicopy/multiport combinations. An unavailable or subsequently revised source may require an update. The reader-facing claims do not rely on a claim of exhaustive novelty certification.

## Exact Bell-return comparisons

| Source and inspected scope | Role in this project |
| --- | --- |
| [Grosshans et al., arXiv:2409.10393v2](https://arxiv.org/html/2409.10393v2), main theorem and §6 | Exact single-port endpoint and the explicit question of multiple inputs and ports |
| [Kopszak et al., arXiv:2504.00710v2](https://arxiv.org/html/2504.00710v2), §§2.1 and 4.1.1 | Conditional degradation of unused Bell pairs after a standard successful probabilistic protocol |
| [Christandl et al., Theorem 1.3](https://doi.org/10.1007/s00220-020-03884-0) | Exact-output probabilistic port teleportation approaches unit success at fixed dimension when spectator return is unrestricted |
| [Canonical Purification Cost, exact frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/fc4651999bff3c65ab7992cda015751ae8b5715f/science/exact_frontier.md), pure-output rigidity and unequal harmonic sectors | Polynomial exactness and symmetric contraction methods for a different supplied-state model |

The [exact-return proof](../science/exact-return.md) gives the model and deductions these works are compared against.
