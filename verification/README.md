# Verification and tested boundaries

The scientific proofs are in [the construction](../science/construction.md), [the converse](../science/converse.md), and [the finite circuit account](../science/implementation.md). The checks here examine the load-bearing register maps, normalizations, shared-copy moments, Haar identity, and channel extension in small dimensions.

From the repository root, using Python 3.10 or later:

```bash
python3 -m pip install -r requirements.txt
python3 verification/verify.py
```

The command writes [results.json](results.json) only after every check passes. To preserve a previous report, choose a different path:

```bash
python3 verification/verify.py --output /tmp/multicopy-teleportation-results.json
```

The only dependency is NumPy. Random input states and unitaries use the fixed seed `20261116`. The report records the NumPy version and numerical tolerance; small floating differences between supported versions are expected. No unknown unitary or input-state description is used to construct the tested processor. Those descriptions enter only the generated source and comparison target.

## What is checked

| Check | Actual observation |
| --- | --- |
| Bell-sum moments | Direct matrices give the first and second moments, including the enhanced correlation between different input copies using the same port. A deliberately independent-copy variance formula fails as expected. |
| Ordered physical instrument | Every successful Bell contraction and port permutation produces the prescribed target. The complete success and fixed-port failure Kraus operators are trace preserving on the entire ordered input space. |
| Reference and returned specimens | A reference-entangled input outside the identical-copy promise preserves its reference marginal. Random complex promise inputs reproduce the formula for the joint target fidelity, including every returned program and input copy. |
| Alice-only measurement | Alice's effects sum to the identity, and Bob's unconditional state before reading the port label remains maximally mixed. No Bob correction is included. |
| Haar score | A partial transpose of the full symmetric projector agrees with a separately constructed sum of Bell operators. Exact finite designs independently reproduce the Haar operator for the listed qubit cases and the qutrit one-input case. |
| Converse score on a physical POVM | The actual completed polar POVM obeys both the Haar-score and no-signalling bounds. For the qubit cases, evaluating the physical protocol on an exact design agrees with the Haar-score calculation. This does not optimize over all POVMs. |
| Known projected encoding | Explicit uniform-label preparation, controlled stable routing, and Bell unpreparation give the projected contraction and its Gram operator with normalization `G/(d*m*n)`. The exact polar block agrees with the instrument's Kraus operators. Its finite-dimensional success/failure flag dilation is unitary. |
| Stored channels | Nonunital amplitude damping and depolarization commute through the complete Alice-only protocol, including failure. The resulting squared Uhlmann fidelity obeys data processing for the mixed global target. |

## Dimensions and limitations

The ordered physical fixtures use `(d,m,n)` equal to `(2,1,1)`, `(2,1,2)`, `(2,2,1)`, `(2,2,2)`, `(2,2,3)`, `(2,3,2)`, `(3,1,2)`, and `(3,2,1)`. There are three random complex promise trials per fixture. The largest full input dimension is 256. Moment checks additionally include `(3,2,2)`, whose Alice-space dimension is 81. Dense projected-encoding fixtures are capped at dimension 256.

The code uses ordered physical tensor factors and does not replace Alice's circuit by a projection onto the symmetry of whole shared pairs. The proof may use that symmetry; it is not an allowed Alice gate. Bob's only operations are the specified port selection and relabeling.

The flag-dilation check uses exact dense matrix functions. It does **not** synthesize or execute a finite-precision QSVT phase sequence, compile an elementary-gate circuit, measure physical runtime, or establish a hardware advantage. The implementation theorem's polynomial degree, small-spectrum estimate, and synthesis error rest on its analytical argument and cited primary results. The finite checks do not certify arbitrary dimensions, optimality, priority, a vanishing-error frontier, or repeated reuse of the approximately returned specimens.

The converse is for the correction-free port model. These checks provide no lower bound for an unrestricted processor that can apply arbitrary operations to both halves of the stored programs.
