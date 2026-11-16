#!/usr/bin/env python3
"""Small dense checks of the multicopy, multiport teleportation account.

These are finite-dimensional diagnostics, not proofs of the asymptotic claims.
Only NumPy is required. No oracle calls or unknown-state descriptions are used by
the tested processor: U and psi enter the input and the expected target only.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

TOL = 2e-8
SEED = 20261116


def checked(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def relative_error(actual: np.ndarray, expected: np.ndarray) -> float:
    return float(np.linalg.norm(actual - expected) / max(1.0, np.linalg.norm(expected)))


def psd_function(a: np.ndarray, function, *, cutoff: float = 1e-10) -> np.ndarray:
    values, vectors = np.linalg.eigh((a + a.conj().T) / 2)
    checked(float(values.min()) > -TOL, "operator expected to be positive")
    transformed = np.zeros_like(values)
    positive = values > cutoff
    transformed[positive] = function(values[positive])
    return (vectors * transformed) @ vectors.conj().T


def sqrt_psd(a: np.ndarray) -> np.ndarray:
    return psd_function(a, np.sqrt)


def inverse_sqrt(a: np.ndarray) -> np.ndarray:
    return psd_function(a, lambda x: 1 / np.sqrt(x))


def support(a: np.ndarray) -> np.ndarray:
    return psd_function(a, lambda x: np.ones_like(x))


def kron_all(items) -> np.ndarray:
    result = np.array([1.0 + 0j])
    for item in items:
        result = np.kron(result, item)
    return result


def basis_tuples(d: int, count: int):
    return itertools.product(range(d), repeat=count)


def flat_index(values, d: int) -> int:
    result = 0
    for value in values:
        result = result * d + int(value)
    return result


def permutation_operator(d: int, count: int, order: list[int]) -> np.ndarray:
    dimension = d**count
    indices = np.arange(dimension).reshape((d,) * count).transpose(order).ravel()
    operator = np.zeros((dimension, dimension), complex)
    operator[np.arange(dimension), indices] = 1
    return operator


def embed(operator: np.ndarray, axes: list[int], d: int, count: int) -> np.ndarray:
    """Embed an operator in ordered physical registers, without symmetry reduction."""
    rest = [i for i in range(count) if i not in axes]
    order = axes + rest
    dimension = d**count
    indices = np.arange(dimension).reshape((d,) * count).transpose(order).ravel()
    result = np.zeros((dimension, dimension), complex)
    result[np.ix_(indices, indices)] = np.kron(operator, np.eye(d ** len(rest)))
    return result


def partial_trace(rho: np.ndarray, keep: list[int], d: int, count: int) -> np.ndarray:
    rest = [i for i in range(count) if i not in keep]
    order = keep + rest + [count + i for i in keep] + [count + i for i in rest]
    a = d ** len(keep)
    b = d ** len(rest)
    tensor = rho.reshape((d,) * (2 * count)).transpose(order).reshape(a, b, a, b)
    return np.einsum("arbr->ab", tensor)


def pure(rng: np.random.Generator, d: int) -> np.ndarray:
    vector = rng.normal(size=d) + 1j * rng.normal(size=d)
    return vector / np.linalg.norm(vector)


def haar_unitary(rng: np.random.Generator, d: int) -> np.ndarray:
    matrix = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(matrix)
    diagonal = np.diag(r)
    return q * (diagonal / np.abs(diagonal)).conj()


def choi_vector(unitary: np.ndarray) -> np.ndarray:
    """Physical order outer A, inner B; U acts on A."""
    d = len(unitary)
    bell = np.eye(d).reshape(-1) / np.sqrt(d)
    return np.kron(unitary, np.eye(d)) @ bell


def promise_vector(unitary: np.ndarray, psi: np.ndarray, m: int, n: int) -> np.ndarray:
    return kron_all([choi_vector(unitary)] * m + [psi] * n)


def target_vector(unitary: np.ndarray, psi: np.ndarray, m: int, n: int) -> np.ndarray:
    return kron_all([unitary @ psi] + [choi_vector(unitary)] * (m - 1) + [psi] * (n - 1))


def bell_gram(d: int, m: int, n: int) -> np.ndarray:
    """Direct index formula for G=d sum Phi on Alice's B pools and C pools."""
    size = d ** (m + n)
    result = np.zeros((size, size), complex)
    for values in basis_tuples(d, m + n):
        column = flat_index(values, d)
        for r in range(m):
            for s in range(n):
                if values[r] != values[m + s]:
                    continue
                for a in range(d):
                    changed = list(values)
                    changed[r] = changed[m + s] = a
                    result[flat_index(changed, d), column] += 1
    return result


def alice_contraction(d: int, m: int, n: int, r: int, s: int) -> np.ndarray:
    result = np.zeros((d ** (m + n - 2), d ** (m + n)), complex)
    rest_b = [i for i in range(m) if i != r]
    rest_c = [m + i for i in range(n) if i != s]
    for values in basis_tuples(d, m + n):
        if values[r] == values[m + s]:
            remaining = [values[i] for i in rest_b + rest_c]
            result[flat_index(remaining, d), flat_index(values, d)] = 1 / np.sqrt(d)
    return result


def full_contraction(d: int, m: int, n: int, r: int, s: int) -> np.ndarray:
    """Bell contraction and allowed port routing in A1,B1,...,Am,Bm,C1,... order."""
    count = 2 * m + n
    result = np.zeros((d ** (count - 2), d**count), complex)
    order = [2 * r]
    for i in range(m):
        if i != r:
            order.extend([2 * i, 2 * i + 1])
    order.extend(2 * m + j for j in range(n) if j != s)
    for values in basis_tuples(d, count):
        if values[2 * r + 1] == values[2 * m + s]:
            output = [values[i] for i in order]
            result[flat_index(output, d), flat_index(values, d)] = 1 / np.sqrt(d)
    return result


def discard_fixed_port(d: int, m: int, n: int, b: int, c: int) -> np.ndarray:
    """Failure Kraus: retain A1, discard B1 and C1, reorder remaining registers."""
    count = 2 * m + n
    result = np.zeros((d ** (count - 2), d**count), complex)
    order = [0] + list(range(2, 2 * m)) + list(range(2 * m + 1, count))
    for values in basis_tuples(d, count):
        if values[1] == b and values[2 * m] == c:
            result[flat_index([values[i] for i in order], d), flat_index(values, d)] = 1
    return result


def build_instrument(d: int, m: int, n: int):
    g = bell_gram(d, m, n)
    g_inverse = inverse_sqrt(g)
    g_support = support(g)
    alice_axes = [2 * i + 1 for i in range(m)] + list(range(2 * m, 2 * m + n))
    inverse_full = embed(g_inverse, alice_axes, d, 2 * m + n)
    failure_alice = np.eye(len(g)) - g_support
    failure_full = embed(failure_alice, alice_axes, d, 2 * m + n)
    successes = []
    alice_successes = []
    contractions = []
    for r in range(m):
        for s in range(n):
            contraction = full_contraction(d, m, n, r, s)
            contractions.append(contraction)
            successes.append(np.sqrt(d) * contraction @ inverse_full)
            alice_successes.append(np.sqrt(d) * alice_contraction(d, m, n, r, s) @ g_inverse)
    failures = [discard_fixed_port(d, m, n, b, c) @ failure_full for b in range(d) for c in range(d)]
    return g, successes, failures, alice_successes, failure_alice, contractions


def channel_output(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum((k @ rho @ k.conj().T for k in kraus), np.zeros((kraus[0].shape[0],) * 2, complex))


def fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
    root = sqrt_psd(rho)
    value = float(np.trace(sqrt_psd(root @ sigma @ root)).real) ** 2
    return min(1.0, max(0.0, value))


def test_instrument(d: int, m: int, n: int, rng: np.random.Generator) -> dict:
    count = 2 * m + n
    checked(d**count <= 256, "physical fixture exceeds explicit 256-dimensional cap")
    g, successes, failures, alice_successes, failure_alice, contractions = build_instrument(d, m, n)
    kraus = successes + failures
    identity = np.eye(d**count)
    complete = sum(k.conj().T @ k for k in kraus)
    completion_error = relative_error(complete, identity)
    checked(completion_error < TOL, "full ordered-register channel is not trace preserving")

    alice_axes = [2 * i + 1 for i in range(m)] + list(range(2 * m, count))
    gram_full = d * sum(l.conj().T @ l for l in contractions)
    gram_embedding_error = relative_error(gram_full, embed(g, alice_axes, d, count))
    checked(gram_embedding_error < TOL, "Bell contractions disagree with independently indexed Gram")

    alice_effects = [a.conj().T @ a for a in alice_successes]
    alice_completion_error = relative_error(sum(alice_effects) + failure_alice, np.eye(len(g)))
    checked(alice_completion_error < TOL, "Alice-only POVM does not complete")

    # A reference-entangled input outside the identical-specimen promise checks
    # the entire channel, not just its advertised source family.
    entangled = pure(rng, 2 * d**count).reshape(2, d**count)
    reference_before = entangled @ entangled.conj().T
    reference_after = np.zeros((2, 2), complex)
    for k in kraus:
        branch = entangled @ k.T
        reference_after += branch @ branch.conj().T
    reference_error = relative_error(reference_after, reference_before)
    checked(reference_error < TOL, "reference marginal changed under completed channel")

    roots = sqrt_psd(g)
    minimum_margin = 1.0
    maximum_formula_error = 0.0
    maximum_branch_mismatch = 0.0
    maximum_no_signalling_error = 0.0
    observed = []
    for _ in range(3):
        psi = pure(rng, d)
        unitary = haar_unitary(rng, d)
        v = promise_vector(unitary, psi, m, n)
        w = target_vector(unitary, psi, m, n)
        checked(abs(np.linalg.norm(v) - 1) < TOL, "promise input not normalized")
        for l in contractions:
            checked(np.linalg.norm(l @ v - w / d) < TOL, "Bell contraction/routing target is wrong")
        branches = [k @ v for k in successes]
        mismatch = max(float(np.linalg.norm(branch - branches[0])) for branch in branches)
        maximum_branch_mismatch = max(maximum_branch_mismatch, mismatch)
        checked(mismatch < TOL, "successful routed branches fail to coincide")
        global_success_fidelity = sum(abs(np.vdot(w, b)) ** 2 for b in branches)
        reduced_alice = np.kron(np.eye(d**m) / d**m, np.outer(kron_all([psi] * n), kron_all([psi] * n).conj()))
        mu = float(np.trace(g @ reduced_alice).real)
        formula = float(np.trace(roots @ reduced_alice).real) ** 2 / mu
        formula_error = abs(global_success_fidelity - formula)
        maximum_formula_error = max(maximum_formula_error, formula_error)
        checked(formula_error < TOL, "physical global fidelity disagrees with moment formula")
        bound = m * n / (m * n + (d - 1) * (d + n))
        minimum_margin = min(minimum_margin, global_success_fidelity - bound)
        checked(global_success_fidelity + TOL >= bound, "global-return lower bound violated")
        rho = channel_output(kraus, np.outer(v, v.conj()))
        global_fidelity = float(np.vdot(w, rho @ w).real)
        output_rho = partial_trace(rho, [0], d, count - 2)
        output_fidelity = float(np.vdot(unitary @ psi, output_rho @ (unitary @ psi)).real)
        checked(global_fidelity + TOL >= global_success_fidelity, "failure completion reduced fidelity")
        checked(output_fidelity + TOL >= global_fidelity, "tracing returns decreased target fidelity")
        checked(output_fidelity <= min(1.0, m / d) + TOL, "no-correction port bound violated")
        observed.append({"successful_global_fidelity": float(global_success_fidelity), "completed_global_fidelity": global_fidelity, "output_only_fidelity": output_fidelity})

        # Apply Alice's un-routed POVM by square-root Kraus operators. Bob's
        # unconditional marginal must remain I/d^m before reading the port label.
        unselected = np.zeros((d**m, d**m), complex)
        for effect in alice_effects + [failure_alice]:
            local_root = sqrt_psd(effect)
            physical_root = embed(local_root, alice_axes, d, count)
            branch = physical_root @ v
            unselected += partial_trace(np.outer(branch, branch.conj()), [2 * r for r in range(m)], d, count)
        no_signalling_error = relative_error(unselected, np.eye(d**m) / d**m)
        maximum_no_signalling_error = max(maximum_no_signalling_error, no_signalling_error)
        checked(no_signalling_error < TOL, "Alice's measurement signalled to Bob before port selection")

    return {"d": d, "m": m, "n": n, "full_input_dimension": d**count, "alice_dimension": len(g), "completion_error": completion_error, "gram_embedding_error": gram_embedding_error, "alice_completion_error": alice_completion_error, "reference_error": reference_error, "max_branch_mismatch": maximum_branch_mismatch, "max_formula_error": maximum_formula_error, "max_no_signalling_error": maximum_no_signalling_error, "minimum_lower_bound_margin": float(minimum_margin), "random_promise_trials": observed}


def symmetric_projector(d: int, n: int) -> np.ndarray:
    result = np.zeros((d**n, d**n), complex)
    for perm in itertools.permutations(range(n)):
        result += permutation_operator(d, n, list(perm)) / math.factorial(n)
    return result


def score_operator(d: int, n: int) -> np.ndarray:
    projector = symmetric_projector(d, n + 1) / math.comb(d + n, n + 1)
    axes = list(range(2 * (n + 1)))
    axes[n], axes[2 * n + 1] = axes[2 * n + 1], axes[n]
    return projector.reshape((d,) * (2 * (n + 1))).transpose(axes).reshape(d ** (n + 1), d ** (n + 1))


def qubit_icosahedron() -> list[np.ndarray]:
    golden = (1 + np.sqrt(5)) / 2
    bloch = []
    for a in [-1, 1]:
        for b in [-1, 1]:
            bloch += [(0, a, b * golden), (a, b * golden, 0), (b * golden, 0, a)]
    result = []
    pauli = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    for point in bloch:
        point = np.array(point) / np.linalg.norm(point)
        rho = (np.eye(2) + sum(x * s for x, s in zip(point, pauli))) / 2
        _, vectors = np.linalg.eigh(rho)
        result.append(vectors[:, -1])
    return result


def qutrit_mubs() -> list[np.ndarray]:
    result = [np.eye(3, dtype=complex)[:, i] for i in range(3)]
    x = np.arange(3)
    for a in range(3):
        for b in range(3):
            result.append(np.exp(2j * np.pi * (a * x * x + b * x) / 3) / np.sqrt(3))
    return result


def test_haar_score(d: int, n: int) -> dict:
    p = symmetric_projector(d, n)
    wide = np.kron(p, np.eye(d))
    # Construct the Bell terms separately, not by transposing the larger
    # symmetric projector used for the left side.
    bell = np.eye(d).reshape(-1) / np.sqrt(d)
    q = d * np.outer(bell, bell.conj())
    summation = sum(embed(q, [s, n], d, n + 1) for s in range(n))
    dn = math.comb(d + n - 1, n)
    rhs = (wide + wide @ summation @ wide) / ((d + n) * dn)
    score = score_operator(d, n)
    identity_error = relative_error(score, rhs)
    checked(identity_error < TOL, "Haar score identity failed")
    checked(float(np.linalg.eigvalsh(score).min()) > -TOL, "Haar score is not positive")
    checked(abs(np.trace(score) - 1) < TOL, "Haar score not normalized")
    result = {"d": d, "n": n, "symmetric_dimension": dn, "identity_error": identity_error}
    design = qubit_icosahedron() if d == 2 and n <= 3 else qutrit_mubs() if (d, n) == (3, 1) else None
    if design is not None:
        quadrature = sum(np.outer(v, v.conj()) for v in (kron_all([psi] * n + [psi.conj()]) for psi in design)) / len(design)
        error = relative_error(score, quadrature)
        checked(error < TOL, "independent exact-design Haar fixture failed")
        result.update({"exact_design_points": len(design), "exact_design_error": error})
    return result


def test_moments(d: int, m: int, n: int) -> dict:
    """Trace products on the actual marginal, including shared-port terms."""
    g = bell_gram(d, m, n)
    psi = np.eye(d, dtype=complex)[:, 0]
    psi_pool = kron_all([psi] * n)
    rho = np.kron(np.eye(d**m) / d**m, np.outer(psi_pool, psi_pool.conj()))
    mu = float(np.trace(rho @ g).real)
    second = float(np.trace(rho @ g @ g).real)
    expected_mu = m * n / d
    expected_variance = m * n * (1 + (n - 1) / d - n / d**2)
    checked(abs(mu - expected_mu) < TOL, "first Bell-sum moment failed")
    checked(abs(second - mu**2 - expected_variance) < TOL, "shared-port second moment failed")
    eigenvalues, eigenvectors = np.linalg.eigh(g)
    weights = np.diag(eigenvectors.conj().T @ rho @ eigenvectors).real
    x = np.maximum(eigenvalues, 0) / mu
    tail = float(weights[x < 0.25 - TOL].sum())
    relative_variance = expected_variance / mu**2
    checked(tail <= 16 * relative_variance / 9 + TOL, "state-dependent small-spectrum tail bound failed")
    mean_root = float(np.sum(weights * np.sqrt(x)))
    holder_bound = 1 / (1 + relative_variance)
    checked(mean_root**2 + TOL >= holder_bound, "Holder fidelity inequality failed")
    # The deliberate incorrect formula treats different input copies at the
    # same port as independent. This is a consequential negative control.
    independent_variance = m * n * (1 - 1 / d**2)
    omitted_correlation = second - mu**2 - independent_variance
    if n > 1:
        checked(omitted_correlation > 0.01, "shared-copy negative control did not separate")
    return {"d": d, "m": m, "n": n, "alice_dimension": len(g), "mean": mu, "second_moment": second, "variance": second - mu**2, "expected_variance": expected_variance, "polar_global_fidelity": mean_root**2, "holder_lower_bound": holder_bound, "small_spectrum_mass": tail, "chebyshev_mass_upper_bound": min(1.0, 16 * relative_variance / 9), "incorrect_independent_variance_discrepancy": float(omitted_correlation)}


def test_actual_povm_score(d: int, m: int, n: int) -> dict:
    g = bell_gram(d, m, n)
    inv = inverse_sqrt(g)
    effects = [np.zeros_like(g) for _ in range(m)]
    for r in range(m):
        for s in range(n):
            j = np.sqrt(d) * alice_contraction(d, m, n, r, s) @ inv
            effects[r] += j.conj().T @ j
    effects[0] += np.eye(len(g)) - support(g)
    score = score_operator(d, n)
    average = 0.0
    for r in range(m):
        score_full = embed(score, list(range(m, m + n)) + [r], d, m + n)
        average += float(np.trace(effects[r] @ score_full).real) / d**m
    score_bound = (d + m * n) / (d * (d + n))
    checked(average <= min(1.0, score_bound, m / d) + TOL, "actual POVM exceeded a converse bound")
    result = {"d": d, "m": m, "n": n, "exact_haar_output_fidelity": average, "haar_score_bound": score_bound, "no_signalling_bound": m / d}
    if d == 2 and n <= 3:
        _, success, failure, _, _, _ = build_instrument(d, m, n)
        scores = []
        for psi in qubit_icosahedron():
            v = promise_vector(np.eye(d), psi, m, n)
            rho = channel_output(success + failure, np.outer(v, v.conj()))
            output = partial_trace(rho, [0], d, 2 * m + n - 2)
            scores.append(float(np.vdot(psi, output @ psi).real))
        error = abs(average - np.mean(scores))
        checked(error < TOL, "Haar score disagrees with physical port protocol on exact design")
        result["physical_design_error"] = float(error)
    return result


def bell_unprepare(d: int) -> np.ndarray:
    x = np.arange(d)
    fourier = np.exp(2j * np.pi * np.outer(x, x) / d) / np.sqrt(d)
    summation = np.zeros((d * d, d * d), complex)
    for a in range(d):
        for b in range(d):
            summation[flat_index([a, (a + b) % d], d), flat_index([a, b], d)] = 1
    return (summation @ np.kron(fourier, np.eye(d))).conj().T


def uniform_prepare(size: int) -> np.ndarray:
    e0 = np.eye(size, dtype=complex)[:, 0]
    target = np.ones(size, complex) / np.sqrt(size)
    if size == 1:
        return np.eye(1)
    vector = (e0 - target) / np.linalg.norm(e0 - target)
    return np.eye(size) - 2 * np.outer(vector, vector.conj())


def test_alice_block_encoding(d: int, m: int, n: int) -> dict:
    count = m + n
    dimension = d**count
    labels = m * n
    total = labels * dimension
    checked(total <= 256, "dense Alice compiler fixture exceeds 256-dimensional cap")
    select = np.zeros((total, total), complex)
    for r in range(m):
        for s in range(n):
            label = r * n + s
            order = [r] + [i for i in range(m) if i != r] + [m + s] + [m + j for j in range(n) if j != s]
            select[label * dimension:(label + 1) * dimension, label * dimension:(label + 1) * dimension] = permutation_operator(d, count, order)
    unprepare = embed(bell_unprepare(d), [0, m], d, count)
    w = np.kron(np.eye(labels), unprepare) @ select @ np.kron(uniform_prepare(labels), np.eye(dimension))
    unitary_error = relative_error(w.conj().T @ w, np.eye(total))
    checked(unitary_error < TOL, "PREP/SELECT/Bell-unprepare is not unitary")
    selected_rows = []
    for label in range(labels):
        for values in basis_tuples(d, count):
            if values[0] == 0 and values[m] == 0:
                selected_rows.append(label * dimension + flat_index(values, d))
    encoded = w[np.ix_(selected_rows, range(dimension))]
    direct = np.concatenate([alice_contraction(d, m, n, r, s) for r in range(m) for s in range(n)], axis=0) / np.sqrt(labels)
    contraction_error = relative_error(encoded, direct)
    checked(contraction_error < TOL, "projected Alice encoding has wrong contraction or routing")
    g = bell_gram(d, m, n)
    gram_error = relative_error(encoded.conj().T @ encoded, g / (d * m * n))
    checked(gram_error < TOL, "Alice projected Gram normalization is wrong")
    polar = encoded @ inverse_sqrt(encoded.conj().T @ encoded)
    ideal = np.concatenate([np.sqrt(d) * alice_contraction(d, m, n, r, s) @ inverse_sqrt(g) for r in range(m) for s in range(n)], axis=0)
    polar_error = relative_error(polar, ideal)
    checked(polar_error < TOL, "projected polar map has wrong Kraus normalization")
    # Exact finite-dimensional flag dilation checks both input and output
    # complements. It does not compile a finite-precision QSVT polynomial.
    out_dim = len(polar)
    flag_unitary = np.block([[polar, sqrt_psd(np.eye(out_dim) - polar @ polar.conj().T)], [sqrt_psd(np.eye(dimension) - polar.conj().T @ polar), -polar.conj().T]])
    flag_error = relative_error(flag_unitary.conj().T @ flag_unitary, np.eye(out_dim + dimension))
    checked(flag_error < TOL, "polar success/failure flag dilation is not unitary")
    return {"d": d, "m": m, "n": n, "alice_dimension": dimension, "encoding_dimension": total, "unitary_error": unitary_error, "projected_contraction_error": contraction_error, "projected_gram_error": gram_error, "polar_kraus_error": polar_error, "polar_flag_unitary_error": flag_error, "outer_program_registers_in_encoding": 0}


def local_channel(rho: np.ndarray, kraus: list[np.ndarray], axes: list[int], d: int, count: int) -> np.ndarray:
    result = rho
    for axis in axes:
        full_kraus = [embed(k, [axis], d, count) for k in kraus]
        result = channel_output(full_kraus, result)
    return result


def test_channel_data_processing(rng: np.random.Generator) -> list[dict]:
    d, m, n = 2, 2, 2
    _, success, failure, _, _, _ = build_instrument(d, m, n)
    processor = success + failure
    psi = pure(rng, d)
    source = promise_vector(np.eye(d), psi, m, n)
    target = target_vector(np.eye(d), psi, m, n)
    rho_source = np.outer(source, source.conj())
    rho_target = np.outer(target, target.conj())
    ideal_output = channel_output(processor, rho_source)
    ideal_fidelity = float(np.vdot(target, ideal_output @ target).real)
    gamma = 0.37
    amplitude_damping = [np.diag([1, np.sqrt(1 - gamma)]), np.array([[0, np.sqrt(gamma)], [0, 0]], complex)]
    p = 0.31
    paulis = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.diag([1, -1]).astype(complex)]
    depolarizing = [np.sqrt(1 - p) * np.eye(2)] + [np.sqrt(p / 3) * x for x in paulis]
    reports = []
    for name, channel in [("nonunital_amplitude_damping", amplitude_damping), ("depolarizing", depolarizing)]:
        checked(relative_error(sum(k.conj().T @ k for k in channel), np.eye(d)) < TOL, "test channel is not trace preserving")
        actual_source = local_channel(rho_source, channel, [2 * r for r in range(m)], d, 2 * m + n)
        actual_output = channel_output(processor, actual_source)
        output_outer_axes = [0] + [1 + 2 * r for r in range(m - 1)]
        transported_output = local_channel(ideal_output, channel, output_outer_axes, d, 2 * m + n - 2)
        transported_target = local_channel(rho_target, channel, output_outer_axes, d, 2 * m + n - 2)
        covariance_error = relative_error(actual_output, transported_output)
        checked(covariance_error < TOL, "identical program channels do not commute through Alice-only processor")
        mixed_fidelity = fidelity(actual_output, transported_target)
        checked(mixed_fidelity + TOL >= ideal_fidelity, "channel data-processing fidelity decreased")
        reports.append({"channel": name, "d": d, "m": m, "n": n, "commutation_error": covariance_error, "ideal_global_fidelity": ideal_fidelity, "mixed_global_squared_fidelity": mixed_fidelity, "data_processing_margin": mixed_fidelity - ideal_fidelity})
    return reports


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    physical_cases = [(2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 2), (3, 1, 2), (3, 2, 1)]
    report = {"schema_version": 1, "seed": SEED, "numpy_version": np.__version__, "tolerance": TOL, "scope": "finite dense scientific diagnostics; no theorem certification, runtime benchmark or finite-precision QSVT compilation", "moments": [test_moments(d, m, n) for d, m, n in physical_cases + [(3, 2, 2)]], "physical_instrument": [test_instrument(d, m, n, rng) for d, m, n in physical_cases], "haar_score": [test_haar_score(d, n) for d, n in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]], "actual_povm_score": [test_actual_povm_score(d, m, n) for d, m, n in [(2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2), (2, 2, 3), (3, 2, 1)]], "alice_block_encoding": [test_alice_block_encoding(d, m, n) for d, m, n in [(2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2), (2, 2, 3), (3, 2, 1)]], "channel_data_processing": test_channel_data_processing(rng)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(report['moments'])} moment cases, {len(report['physical_instrument'])} physical cases, {len(report['haar_score'])} Haar identities, {len(report['actual_povm_score'])} POVM scores, {len(report['alice_block_encoding'])} Alice encodings, {len(report['channel_data_processing'])} channel transports")
    print(f"Report: {args.output}")


if __name__ == "__main__":
    main()
