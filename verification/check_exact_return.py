#!/usr/bin/env python3
"""Check exact Bell return and partial port spending in small ordered registers."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

import numpy as np

from verify import (
    alice_contraction,
    basis_tuples,
    bell_gram,
    checked,
    kron_all,
    pure,
    relative_error,
    target_vector,
)

TOL = 2e-10
SEED = 20261124


def symmetric_isometry(d: int, n: int) -> np.ndarray:
    """Columns are normalized uniform superpositions of words of one occupation."""
    occupations = [tuple(sorted(word)) for word in basis_tuples(d, n)]
    counts = Counter(occupations)
    columns = {word: index for index, word in enumerate(sorted(counts))}
    isometry = np.zeros((d**n, len(counts)))
    for row, word in enumerate(occupations):
        isometry[row, columns[word]] = 1 / np.sqrt(counts[word])
    return isometry


def ordered_bell_maps(d: int, m: int, n: int, copies: np.ndarray) -> list[np.ndarray]:
    """Scale the direct first-copy Bell contraction to the symmetric annihilator."""
    basis = np.kron(np.eye(d**m), copies)
    return [
        np.sqrt(d * n) * alice_contraction(d, m, n, j, 0) @ basis
        for j in range(m)
    ]


def routed_output(post: np.ndarray, d: int, m: int, n: int, port: int) -> np.ndarray:
    """Put Bob's output first, then the returned AB pairs and input copies."""
    residual_alice = m + n - 2
    order = [residual_alice + port]
    for alice_axis, returned in enumerate(k for k in range(m) if k != port):
        order.extend([residual_alice + returned, alice_axis])
    order.extend(range(m - 1, residual_alice))
    return post.reshape((d,) * (residual_alice + m)).transpose(order).ravel()


def test_exact_return(d: int, m: int, n: int, rng: np.random.Generator) -> dict:
    copies = symmetric_isometry(d, n)
    basis = np.kron(np.eye(d**m), copies)
    maps = ordered_bell_maps(d, m, n, copies)
    gram = sum(k.conj().T @ k for k in maps)
    # The earlier test suite constructs every physical port-copy projector separately.
    projected = basis.conj().T @ bell_gram(d, m, n) @ basis
    gram_error = relative_error(gram, projected)
    checked(gram_error < TOL, "the first-copy maps do not reproduce the full Bell sum")

    spectrum = np.linalg.eigvalsh(gram)
    predicted = min(m, n) * (max(m, n) + d - 1)
    computed = float(spectrum[-1])
    checked(abs(computed - predicted) < TOL, "incorrect top norm on the ordered ports")
    failure_min = float((1 - spectrum / predicted).min())
    checked(failure_min > -TOL, "the exact-return instrument exceeds identity")
    checked(abs(failure_min) < TOL, "the exact-return coefficient is not saturated")
    excess_failure_min = float((1 - 1.01 * spectrum / predicted).min())
    checked(excess_failure_min < -0.009, "larger identical branch coefficients remained feasible")

    expected_branch_probability = n / (d * predicted)
    expected_total_probability = max(m, n) / (d * (max(m, n) + d - 1))
    vector_error = 0.0
    probability_error = 0.0
    for _ in range(3):
        psi = pure(rng, d)
        # Columns are Bob's computational port labels, and rows are Alice's
        # ordered Bell halves and her compressed symmetric input.
        stock = copies.conj().T @ kron_all([psi] * n)
        source = np.kron(np.eye(d**m) / np.sqrt(d**m), stock[:, None])
        target = target_vector(np.eye(d), psi, m, n)
        success_probability = 0.0
        for port, bell_map in enumerate(maps):
            output = routed_output(bell_map @ source / np.sqrt(predicted), d, m, n, port)
            vector_error = max(
                vector_error,
                float(np.linalg.norm(output - np.sqrt(expected_branch_probability) * target)),
            )
            success_probability += float(np.vdot(output, output).real)
        probability_error = max(
            probability_error, abs(success_probability - expected_total_probability)
        )
    checked(vector_error < TOL, "output or returned specimen differs from the exact joint target")
    checked(probability_error < TOL, "complex promise states do not achieve the frontier")
    checked(expected_total_probability < 1 / d, "finite full return must have success below 1/d")

    return {
        "d": d,
        "ports": m,
        "copies": n,
        "compressed_input_dimension": len(gram),
        "projected_gram_error": gram_error,
        "ordered_gram_top_eigenvalue": computed,
        "frontier_top_eigenvalue": predicted,
        "failure_min_eigenvalue": failure_min,
        "failure_min_eigenvalue_above_frontier": excess_failure_min,
        "joint_output_vector_error": vector_error,
        "success_probability_error": probability_error,
        "frontier_success_probability": expected_total_probability,
    }


def spending_effect(
    bell_map: np.ndarray,
    d: int,
    m: int,
    copy_dimension: int,
    selected: int,
    spent: tuple[int, ...],
    rng: np.random.Generator,
) -> np.ndarray:
    """Build a nontrivial positive effect with identity on every returned half."""
    remaining = [port for port in range(m) if port != selected]
    active = [index for index, port in enumerate(remaining) if port in spent]
    returned = [index for index, port in enumerate(remaining) if port not in spent]
    active_dimension = copy_dimension * d ** len(active)
    matrix = rng.normal(size=(active_dimension, active_dimension))
    matrix = matrix + 1j * rng.normal(size=matrix.shape)
    positive = matrix.conj().T @ matrix / active_dimension
    dims = (d,) * (m - 1) + (copy_dimension,)
    order = active + [m - 1] + returned
    indices = np.arange(len(bell_map)).reshape(dims).transpose(order).ravel()
    ordered_map = bell_map[indices]
    return ordered_map.conj().T @ np.kron(positive, np.eye(d ** len(returned))) @ ordered_map


def test_spending(d: int, m: int, n: int, budget: int, rng: np.random.Generator) -> dict:
    copies = symmetric_isometry(d, n)
    residual = symmetric_isometry(d, n - 1)
    to_symmetric = np.kron(np.eye(d ** (m - 1)), residual).conj().T
    maps = [to_symmetric @ k for k in ordered_bell_maps(d, m, n, copies)]
    terms = []
    for size in range(1, budget + 1):
        for spent in combinations(range(m), size):
            for selected in spent:
                effect = spending_effect(maps[selected], d, m, residual.shape[1], selected, spent, rng)
                terms.append((size, effect))

    total = sum(effect for _, effect in terms)
    scale = float(np.linalg.eigvalsh(total)[-1])
    checked(scale > 0, "the spending fixture must have nonzero success effects")

    psi = pure(rng, d)
    stock = copies.conj().T @ kron_all([psi] * n)
    mixed = np.eye(d) / d
    stock_rho = np.outer(stock, stock.conj())
    physical = np.kron(kron_all([mixed] * m), stock_rho)
    t = (d - budget) / (budget * (d - 1))
    tilted_state = (1 - t) * mixed + t * np.outer(psi.conj(), psi)
    tilted = np.kron(kron_all([tilted_state] * m), stock_rho)

    factor = 1 + (d - 1) * t
    worst_case_factor = factor * (1 - t)**(budget - 1)
    min_branch_slack = float("inf")
    physical_success = 0.0
    tilted_success = 0.0
    for size, effect in terms:
        physical_term = float(np.einsum("ij,ji->", effect, physical).real / scale)
        tilted_term = float(np.einsum("ij,ji->", effect, tilted).real / scale)
        slack = tilted_term - factor * (1 - t)**(size - 1) * physical_term
        min_branch_slack = min(min_branch_slack, slack)
        physical_success += physical_term
        tilted_success += tilted_term
    worst_case_slack = tilted_success - worst_case_factor * physical_success
    checked(min_branch_slack > -TOL, "tilted test failed for a branchwise spending set")
    checked(worst_case_slack > -TOL, "the spending cap did not bound the aggregate")
    checked(tilted_success <= 1 + TOL, "normalized spending effects are infeasible")
    ceiling = 1 / worst_case_factor
    checked(ceiling <= np.e * budget / d + TOL, "optimized tilt misses the spending law")
    constructive_success = -np.expm1(budget * np.log1p(-1 / (2 * d - 1)))
    checked(constructive_success <= ceiling + TOL, "sequential witness exceeds the converse")
    return {
        "d": d,
        "ports": m,
        "copies": n,
        "spending_budget": budget,
        "branch_count": len(terms),
        "tilt": t,
        "minimum_branch_slack": min_branch_slack,
        "aggregate_slack": worst_case_slack,
        "tilted_success": tilted_success,
        "physical_success": physical_success,
        "tilted_converse_ceiling": ceiling,
        "sequential_success_when_enough_copies": float(constructive_success),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path.")
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    exact = [(2, 1, 1), (2, 1, 4), (2, 4, 1), (2, 2, 3), (2, 3, 2), (2, 3, 3),
             (3, 1, 3), (3, 3, 1), (3, 2, 2), (3, 2, 3), (3, 3, 2), (4, 2, 2)]
    spending = [(2, 2, 2, 1), (3, 3, 2, 2), (4, 2, 2, 2)]
    report = {
        "schema_version": 1,
        "seed": SEED,
        "numpy_version": np.__version__,
        "tolerance": TOL,
        "scope": "finite ordered-register checks for exact Bell return and tilted spending effects",
        "exact_return": [test_exact_return(*case, rng) for case in exact],
        "partial_spending": [test_spending(*case, rng) for case in spending],
    }
    print(f"PASS: {len(exact)} exact-return cases and {len(spending)} spending cases")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
        print(f"Report: {args.output}")


if __name__ == "__main__":
    main()
