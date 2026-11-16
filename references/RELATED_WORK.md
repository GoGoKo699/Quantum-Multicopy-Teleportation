# Attribution and comparison

The task studied here is deterministic approximate **multicopy port teleportation**: $n$ identical unknown pure input specimens, $m$ independent maximally entangled resource pairs, one output, and no receiver correction beyond port selection. Its [fixed-fidelity frontier](../science/model.md) is established within this contract. Exact heralded teleportation, general programmable processors, and sending several independent inputs are different tasks.

## What is inherited

Port-based teleportation and the absence of receiver corrections are due to Ishizaka and Hiroshima [1,2]. Pretty-good/square-root measurements, signal-operator moment bounds and resource recycling are established machinery [3,4]. Quantum singular value transformation, bounded sign approximations and stable phase preprocessing are imported algorithmic tools [8,9]. We do not claim any of these general constructions as new.

The public [Quantum Program Composition construction](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/8ae6b6b0e04c9507d148911ac0c58c7bf0670682/science/construction.md) supplies the closest methodological antecedent: a whole-space normalized Bell-contraction instrument, common routed branches on symmetric copy pools, a polar map, and a Hölder bound using two moments. Its theorem consumes two pools of unitary Choi specimens and produces a Choi specimen for their product. Both inner marginals are maximally mixed.

Here the second pool consists of repeated pure input states. Distinct Bell terms sharing one resource half have expectation $1/d$, rather than $1/d^2$. The resulting covariance changes the resource law and imposes a one-sided port floor. The new [converse](../science/converse.md) is an output-score argument for port teleportation; it is not a consequence of the two-program composition converse.

The present [compiler](../science/implementation.md) also respects a different spatial contract. A reflection exchanging whole Choi programs would act on the receiver's registers and cannot be imported as an Alice-only measurement. The labelled Bell-contraction encoding avoids that operation. The symmetry argument in the fidelity proof is an analytical identity, not an uncharged gate.

## Single-port multicopy teleportation

Grosshans, Horodecki, Murao, Młynik, Quintino, Studziński and Yoshida [5] prove that exact correction-free teleportation using one Bell port and $n$ input copies has optimal heralded success probability

```math
p(d,n)=\frac{n}{d(d+n-1)}.
```

The useful polar branch here reproduces that endpoint. Their April 2026 version identifies the simultaneous multicopy/multiport scenario as a future direction in Section 6. Our result establishes a deterministic approximate fixed-fidelity resource frontier, with a stronger joint-return construction. It does not claim their exact-heralded objective is solved for arbitrary port and input budgets.

Mafi and Moghaddam [10] implement small-copy single-port teleportation and program retrieval on superconducting hardware. In their generalized multi-qubit illustration, several Bell pairs encode one higher-dimensional operation; they are not independent alternative program ports. Their experimental circuit and noise study do not establish the finite-input/multiport frontier proved here.

## Known-state port preparation and input estimation

Muguruza and Speelman [6] study port-based state preparation when the sender has a complete classical description of the input. They obtain an exponential error dependence on the number of Bell ports and applications to hybrid programmable processors. That known-state promise is stronger than a finite supply of unknown quantum specimens.

The optimal universal pure-state estimation fidelity from $n$ specimens is $(n+1)/(n+d)$ [7]. Consequently, input estimation followed by known-state port preparation explains the balanced order $n,m=\Theta(d)$ for output-only fixed fidelity. This is credited as a baseline. It does not supply the intermediate regime $1\ll n\ll d$ at high uniform fidelity, nor the present joint return of input specimens.

Brzić, Yoshida, Murao and Quintino [13] analyze higher-order computation and storage/retrieval when the input is classically known. Their discussion explicitly interprets finite input specimens as partial input knowledge and cites the multicopy proposal. We credit that conceptual connection. Their known-state transformation and repeat-until-success theorems do not provide a finite-specimen port-budget law.

The consequential allocation established here is

```math
1\ll n\ll d,
\qquad m=\Theta(d^2/n),
```

followed by saturation at $m=\Theta(d)$. The construction reaches the whole regime and the port-selection converse matches its order. No claimed benefit rests solely on the balanced point.

## Boundaries with other teleportation and programming results

Multi-port teleportation of several different subsystems [11] has several outputs; repeated copies of one input used to produce one output have a different permutation symmetry and score operator. Port-based telecloning [12] goes from one input to multiple approximate outputs. Neither direction of conversion can be inferred merely by exchanging input and output labels.

General storage-and-retrieval and universal-programming results may allow optimized program states, a different storage stage, or arbitrary receiver processing. This project fixes independent normalized Choi specimens for its retrieval construction, and its matching lower theorem concerns correction-free port selection. It does not assert that every globally acting programmable processor has the same port-resource frontier.

Likewise, applying an arbitrary CPTP channel to the outer resource halves is inherited teleportation equivariance and fidelity monotonicity. This extends the constructive result to stored noisy/nonunital channels, but does not make a new lower bound for arbitrary program processors or certify recovery of an ideal operation from unknown noise.

## Sources

1. S. Ishizaka and T. Hiroshima, *Asymptotic teleportation scheme as a universal programmable quantum processor*, Physical Review Letters **101**, 240501 (2008). [DOI](https://doi.org/10.1103/PhysRevLett.101.240501), [arXiv:0807.4568](https://arxiv.org/abs/0807.4568).
2. S. Ishizaka and T. Hiroshima, *Quantum teleportation scheme by selecting one of multiple output ports*, Physical Review A **79**, 042306 (2009). [DOI](https://doi.org/10.1103/PhysRevA.79.042306).
3. P. Hausladen and W. K. Wootters, *A “Pretty Good” Measurement for Distinguishing Quantum States*, Journal of Modern Optics **41**, 2385–2390 (1994). [DOI](https://doi.org/10.1080/09500349414552221).
4. S. Strelchuk, M. Horodecki and J. Oppenheim, *Generalized Teleportation and Entanglement Recycling*, Physical Review Letters **110**, 010505 (2013). [DOI](https://doi.org/10.1103/PhysRevLett.110.010505), [arXiv:1209.2683](https://arxiv.org/abs/1209.2683). The moment/pretty-good-measurement and recycling machinery is credited; no asymptotic theorem here depends on importing their numerical constants.
5. F. Grosshans, M. Horodecki, M. Murao, T. Młynik, M. T. Quintino, M. Studziński and S. Yoshida, *Multicopy quantum state teleportation with application to storage and retrieval of quantum programs*, Quantum **10**, 2105 (2026). [DOI](https://doi.org/10.22331/q-2026-05-13-2105), [arXiv:2409.10393v2](https://arxiv.org/html/2409.10393v2), inspected version dated 27 April 2026; main theorem and Section 6.
6. G. Muguruza and F. Speelman, *Port-Based State Preparation and Applications*, Quantum **8**, 1573 (2024). [DOI](https://doi.org/10.22331/q-2024-12-18-1573), [arXiv:2402.18356v2](https://arxiv.org/abs/2402.18356v2).
7. D. Bruß and C. Macchiavello, *Optimal state estimation for d-dimensional quantum systems*, Physics Letters A **253**, 249–251 (1999). [DOI](https://doi.org/10.1016/S0375-9601(99)00099-7), [arXiv:quant-ph/9812016](https://arxiv.org/abs/quant-ph/9812016).
8. A. Gilyén, Y. Su, G. H. Low and N. Wiebe, *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*, STOC 2019, 193–204. [arXiv:1806.01838v1](https://arxiv.org/abs/1806.01838v1). Numbered implementation statements refer to Corollary 18, Lemma 25 and Theorem 26 of this version.
9. J. Haah, *Product Decomposition of Periodic Functions in Quantum Signal Processing*, Quantum **3**, 190 (2019). [DOI](https://doi.org/10.22331/q-2019-10-07-190), [arXiv:1806.10236](https://arxiv.org/abs/1806.10236).
10. Y. Mafi and A. G. Moghaddam, *Multicopy teleportation and quantum program retrieval on superconducting quantum hardware*, [arXiv:2611.00874v1](https://arxiv.org/html/2611.00874v1), 31 October 2026. Inspected full HTML: single-port protocol, experimental implementation and discussion.
11. M. Mozrzymas, M. Studziński and P. Kopszak, *Optimal Multi-port-based Teleportation Schemes*, Quantum **5**, 477 (2021). [DOI](https://doi.org/10.22331/q-2021-06-17-477), [arXiv:2011.09256v3](https://arxiv.org/abs/2011.09256v3).
12. R. Okada, K. Kato and F. Buscemi, *Port-based telecloning of an unknown quantum state*, Physical Review A **111**, 052408 (2025). [DOI](https://doi.org/10.1103/PhysRevA.111.052408), [arXiv:2501.16878v2](https://arxiv.org/abs/2501.16878v2). This comparator concerns multiple outputs; its inspected scope is recorded in the source index.
13. V. Brzić, S. Yoshida, M. Murao and M. T. Quintino, *Higher-order quantum computing with known input states*, [arXiv:2510.20530v2](https://arxiv.org/html/2510.20530v2), 16 November 2025. Sections 8–9 and the setup distinguish classical input knowledge from a finite specimen supply.
