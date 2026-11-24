# Exact return of unused Bell ports

[Model](model.md) · [Approximate joint return](construction.md) · [Output-only converse](converse.md) · [Related work](../references/RELATED_WORK.md)

Returning unused Bell pairs exactly changes the teleportation task. A protocol that always accepts and returns every unselected pair delivers a maximally mixed qudit. Heralding allows useful output, but the probability of exact teleportation still stays below the single-port ceiling $`1/d`$, however many ports and input copies are supplied.

## Task and sharp frontier

Alice holds $`n\ge1`$ identical copies of an unknown pure state $`|\psi\rangle\in\mathbb C^d`$, with $`d\ge2`$. Alice and Bob share $`m\ge1`$ independent maximally entangled pairs $`|\Phi_d\rangle_{A_jB_j}`$. Bob holds the $`A`$ halves. An accepted outcome names a port $`j`$. Bob selects $`A_j`$ and may reorder the unselected ports as agreed. Alice may use any local instrument, private ancillas and classical processing. The task uses no correction at Bob and no extra shared entangled resource.

On each accepted outcome all $`m-1`$ unselected pairs must be returned in their original joint Bell state, with their pairing specified by the port label. The fidelity requirement concerns the selected qudit averaged over accepted outcomes, for every $`\psi`$. Write $`p_\psi`$ for the success probability and $`f_\psi`$ for the squared pure-state overlap of the **unnormalized** accepted output with $`|\psi\rangle`$, so the requirement is $`f_\psi\ge Fp_\psi`$. There is no condition on rejected branches. The converse permits discarding any or all input specimens.

**Theorem.** Let $`M=\max(m,n)`$ and $`p_0=M/[d(M+d-1)]`$. For $`1/d\le F\le1`$, the optimal guarantee on $`\inf_\psi p_\psi`$ is

```math
P_{\max}(F)=\frac{p_0(1-1/d)}{F-1/d+p_0(1-F)}.
```

At $`F=1`$ the optimum is $`p_0`$. For $`F\le1/d`$ a protocol that always accepts is feasible. The entire frontier is attained while also returning $`n-1`$ exact copies to Alice on each accepted outcome. When acceptance is deterministic and Bell return is exact, the selected Bob register is maximally mixed for every input.

## Why exact Bell return restricts Alice's instruments

Work on the supplied input support $`\mathcal H_n\otimes V^{\otimes m}`$, where $`V=\mathbb C^d`$ is the Bell basis space and $`\mathcal H_n=\mathrm{Sym}^n(V)`$ contains the input specimens. The vectors $`|\psi\rangle^{\otimes n}`$ span $`\mathcal H_n`$. For a given accepted outcome choosing $`j`$, refine Alice's map into Kraus operators. The returned Bell state is pure. Positivity implies that each nonzero Kraus contribution has the same pure Bell marginal. This holds also when the accepted outcome contains a mixture of different selected-qudit states.

For one such Kraus operator, expand all supplied Bell pairs in their computational bases. The term with Bob's basis labels $`i_1,\ldots,i_m`$ has Alice input $`|\psi\rangle^{\otimes n}|i_1,\ldots,i_m\rangle`$ and initial amplitude $`d^{-m/2}`$. By exact return, its Alice output must be $`|i_{-j}\rangle`$ on the unselected Bell halves, tensored with a vector depending on $`\psi`$ and $`i_j`$ but independent of $`i_{-j}`$. Independence follows by comparing the coefficients of the known product Bell state with those of the Kraus output. Thus on every coherent input, and then by linear span on $`\mathcal H_n`$, each successful Kraus operator is the identity on the unselected halves tensored with a map on the specimens and the selected half. Known permutations are absorbed into the designated output ordering.

The accepted effects consequently have the form

```math
E_j=X_j\otimes I_{-j},\qquad
X_j\ge0\text{ on }\mathcal H_n\otimes B_j,\qquad
\sum_j E_j\le I .
```

Any finer outcomes have been summed at this point. With $`\bar\psi`$ the complex conjugate in the Bell basis, the contribution from port $`j`$ to success and unnormalized fidelity is

```math
\begin{aligned}
p_{\psi,j}
 &=\mathrm{Tr}\!\left[
     X_j\left(|\psi\rangle\langle\psi|^{\otimes n}\otimes I/d\right)
   \right],\\
f_{\psi,j}
 &=\frac{1}{d}
   \langle\psi^{\otimes n},\bar\psi|X_j|
           \psi^{\otimes n},\bar\psi\rangle .
\end{aligned}
```

The second identity follows by projecting Bob's Bell half onto $`|\psi\rangle`$ before evaluating the probability of the Alice outcome. These expressions use effects only and allow arbitrary discarded Alice registers.

For deterministic acceptance, positivity of the failure effect and the strictly positive port marginal $`I/d^m`$ imply that the failure effect annihilates every vector $`|\psi\rangle^{\otimes n}|i_1,\ldots,i_m\rangle`$. It therefore vanishes on the whole supplied support. In the identity $`\sum_jX_j\otimes I_{-j}=I`$, expand in a product operator basis with an identity and traceless operators on each port. The only term that can carry a traceless operator on $`B_j`$ is the $`j`$ term, so its traceless coefficients vanish. Then each $`X_j=Y_j\otimes I_{B_j}`$. Steering the selected half with this effect yields a scalar multiple of $`I/d`$, which proves the pointwise deterministic statement.

## The two covariant effects and their joint norm

Let $`a_i:\mathcal H_n\to\mathcal H_{n-1}`$ be the normalized symmetric-tensor annihilation map for basis label $`i`$. It sends an occupation vector with $`k_i`$ particles of type $`i`$ to the decremented vector with coefficient $`\sqrt{k_i}`$. Define the selected-port contraction and its support projector by

```math
D_j=\sum_{i=1}^d a_i\otimes\langle i|_{B_j},
\qquad
Q_j=\frac{D_j^\dagger D_j}{n+d-1}.
```

Here and below the effects act as the identity on the other ports. Since $`D_j D_j^\dagger=\sum_i a_i a_i^\dagger=(n+d-1)I_{\mathcal H_{n-1}}`$, $`Q_j`$ is a projector. Two identities used below are

```math
D_j\bigl(|\psi\rangle^{\otimes n}|i\rangle\bigr)
=\sqrt n\,\psi_i|\psi\rangle^{\otimes(n-1)},
\qquad
\mathrm{Tr}_{B_j}Q_j=\frac{n}{n+d-1}I_{\mathcal H_n}.
```

To prove the converse, Haar average the effects under $`U^{\otimes n}\otimes\bar U^{\otimes m}`$ and then average over permutations of the ports. Both operations preserve feasibility. The Haar-mean success and score before averaging equal the corresponding values on each input after averaging. It is enough to bound these means because $`\inf_\psi p_\psi\le\mathbb E_\psi p_\psi`$ and the uniform constraint implies $`\mathbb E_\psi f_\psi\ge F\mathbb E_\psi p_\psi`$. This averaging is a calculation on Alice's effects.

The commutant of $`U^{\otimes n}\otimes\bar U`$ on $`\mathcal H_n\otimes B_j`$ is spanned by $`I`$ and $`Q_j`$. To see this, extend an invariant operator by zero to the full ordered tensor space and partially transpose the port. The resulting operator commutes with $`U^{\otimes(n+1)}`$, so Schur–Weyl duality puts it in the span of permutation operators. Compress the first $`n`$ factors to $`\mathcal H_n`$. The partial transpose commutes with that compression. There are two double cosets of the permutations of the first $`n`$ positions inside the permutations of all $`n+1`$: those fixing the port and those exchanging it with a specimen, up to permutations of the specimens on either side. They give the identity and the compression of the partial transpose of a port–specimen swap. The latter compression equals $`D_j^\dagger D_j/n`$. The partial transpose of the swap is $`d|\Phi_d\rangle\langle\Phi_d|`$ on the selected two registers. Its matrix element between $`|\psi\rangle^{\otimes n}|i\rangle`$ and $`|\varphi\rangle^{\otimes n}|k\rangle`$ is $`\overline{\psi_i}\varphi_k\langle\psi|\varphi\rangle^{n-1}`$, the same as for $`D_j^\dagger D_j/n`$ on these spanning vectors. Thus the averaged effects take the form $`aQ_j+b(I-Q_j)`$, with identical nonnegative $`a,b`$ at each port.

The largest eigenvalue used by these effects is

```math
L:=\left\|\sum_jQ_j\right\|
=\frac{\min(m,n)\bigl(\max(m,n)+d-1\bigr)}{n+d-1}.
```

For the norm proof, set $`S=\sum_j D_j^\dagger D_j`$. In the occupation basis of the specimens and the ordered computational basis of the ports, $`S`$ has entrywise nonnegative real coefficients. A maximizing vector can be taken with nonnegative coefficients, since replacing each entry by its modulus cannot decrease the Rayleigh quotient. Averaging that vector over port permutations is nonzero and gives another largest-eigenvalue vector, now in the symmetric port sector. This step addresses the full ordered port space.

On $`\mathrm{Sym}^n(V)\otimes\mathrm{Sym}^m(\bar V)`$ let $`b_i`$ denote the annihilation maps on the port occupations and $`C=\sum_i a_i b_i`$. The sum over all ports of $`|i\rangle\langle k|`$ is $`b_i^\dagger b_k`$ on that sector, so $`S=C^\dagger C`$ there. On the two graded occupation spaces the commutator is

```math
[C,C^\dagger]=d+N_a+N_b,
```

where $`N_a,N_b`$ count the two degrees. Put $`\Lambda(n,m)=\|C^\dagger C\|`$ on the degree $`(n,m)`$ sector. The largest eigenvalue of $`C^\dagger C`$ equals that of $`CC^\dagger`$ on $`(n-1,m-1)`$ for positive $`n,m`$. Thus

```math
\Lambda(n,m)=\Lambda(n-1,m-1)+d+n+m-2,
\qquad \Lambda(0,m)=\Lambda(n,0)=0.
```

Summing the recurrence and dividing by $`n+d-1`$ gives $`L`$. The operator $`\sum_jQ_j`$ also has eigenvalue zero: fix $`\psi`$ and choose a unit vector in each port orthogonal to $`\bar\psi`$ in its local space.

## Converse and attainment

For the averaged effects set $`u=ma`$, $`v=mb`$, $`s=n/[d(n+d-1)]`$, $`r=1/d`$, and $`x=L/m`$. The two extreme eigenspaces of $`\sum_jQ_j`$ imply

```math
v\le1,\qquad xu+(1-x)v\le1.
```

The contraction identities give uniform accepted probability $`p`$ and reward $`f`$,

```math
p=su+(1-s)v,\qquad
f=su+(r-s)v=p-(1-r)v.
```

In particular $`s/x=p_0`$. Feasibility and the fidelity constraint give

```math
p\le p_0+(1-p_0)v,\qquad v\le\frac{(1-F)p}{1-r}.
```

Eliminating $`v`$ proves the stated upper bound.

An exact-output instrument uses accepted Kraus maps $`D_j/\sqrt{(n+d-1)L}`$, each acting trivially on unselected Alice ports, and completes the failure outcome with the positive residual effect. Alice implements the instrument on the symmetric support and can use failure on its orthogonal complement. On port $`j`$, applying this contraction to the input qudits and Alice half of its Bell state leaves

```math
\sqrt{\frac{n}{d(n+d-1)L}}\,
|\psi\rangle_{A_j}|\psi\rangle^{\otimes(n-1)}
|\Phi_d\rangle^{\otimes(m-1)}
```

in the agreed output order. Each branch has success probability $`s/L`$, totaling $`ms/L=p_0`$. All registers in the target on success are exact. The other protocol always accepts, selects a uniformly random port, discards the corresponding Alice half and one input, and returns the other systems. Its selected output is $`I/d`$. A classical mixture of these two protocols preserves all return promises. Both choices have a uniform port label on acceptance, so the attained fidelity also holds conditional on each reported port. With $`\theta`$ the probability of choosing the exact herald, its accepted probability is $`p=\theta p_0+(1-\theta)`$ and its accepted score is $`f=\theta p_0+(1-\theta)r`$. As $`\theta`$ runs from zero to one, the conditional fidelity runs from $`r`$ to one, and this mixture saturates the converse on the full interval.

## How many pairs must an exact-output protocol spend?

Allow each accepted outcome to name a set $`S`$ of at most $`\ell`$ spent Bell pairs, including the selected pair $`j`$, for $`1\le\ell\le m`$. Every original pair outside $`S`$ is returned exactly and the selected output must be exact. The set can depend on the accepted outcome. For every $`\psi`$ the total success obeys

```math
p_\psi\le
\inf_{0\le t<1}
\frac{1}{[1+(d-1)t](1-t)^{\ell-1}},
```

For $`2\le\ell\le d`$ this gives

```math
p_\psi\le
\frac{\ell}{d}
\left[\frac{1-1/d}{1-1/\ell}\right]^{\ell-1}
\le\frac{e\ell}{d}.
```

At $`\ell=1`$ it gives the simpler ceiling $`1/d`$, while the sharp finite result is $`p_0`$. For $`\ell\ge d`$ the bound from $`t=0`$ is just one.

To prove the bound, exact return implies that the effect of each outcome is $`X_{j,S}\otimes I_{S^c}`$ by the Bell-basis argument above. Fix $`\psi`$, evaluate the copies in $`|\psi\rangle^{\otimes n}`$, and denote the resulting positive operator on the spent Alice ports by $`Z_{j,S}`$. Under the physical input all port marginals are maximally mixed. The reduced accepted output is proportional to the transpose of $`\mathrm{Tr}_{S\setminus\{j\}}Z_{j,S}`$. Exactness makes this partial trace proportional to $`|\bar\psi\rangle\langle\bar\psi|`$. Positivity implies that $`Z_{j,S}`$ has support on that ray at port $`j`$, and hence factors as $`|\bar\psi\rangle\langle\bar\psi|\otimes W_{j,S}`$ with $`W_{j,S}\ge0`$. This reasoning includes zero-probability branches.

Test completeness on the same specimen input but replace each Alice port marginal by the normalized state

```math
R_\psi(t)=(1-t)I/d+t|\bar\psi\rangle\langle\bar\psi|.
```

Relative to the physical input, the expectation of the accepted effect is multiplied by $`1+(d-1)t`$ on the selected port. On every other spent port the test marginal dominates $`(1-t)I/d`$, while identity effects on returned ports are unaffected. Thus the branch expectation under the test is at least $`[1+(d-1)t](1-t)^{|S|-1}`$ times its physical probability, and this factor is at least $`[1+(d-1)t](1-t)^{\ell-1}`$. Summing over accepted effects gives the bound because they sum to at most the identity. For $`2\le\ell\le d`$ the denominator is maximized at $`t=(d-\ell)/[\ell(d-1)]`$, and $`(1+1/(\ell-1))^{\ell-1}\le e`$ gives the simpler estimate.

For $`m\ge\ell`$ and $`n\ge\ell d`$, the order $`\min\{1,\ell/d\}`$ is attained. Allocate $`d`$ specimens and one Bell pair to each of $`\ell`$ independent one-port heralds. Each succeeds with probability $`1/(2d-1)`$. Choose any successful port, spending at most the $`\ell`$ pairs reserved for those attempts and returning all other pairs. The probability of at least one success is $`1-(1-1/(2d-1))^\ell=\Theta(\min\{1,\ell/d\})`$ with numerical constants. A success probability bounded away from zero therefore requires spending order $`d`$ Bell pairs under this exact-output and exact-return contract, even with arbitrary supplies.

## Exact return versus approximate return and port consumption

With $`m=n=d^2`$, independent ordinary Bell contractions give an exact selected output with probability $`1-(1-1/d^2)^{d^2}>1-e^{-1}`$ when every used pair can be spent. The same budgets give success below $`1/d`$ when all unselected pairs must return exactly. The output requirement is exact in both cases. For deterministic approximate **joint** return, the [collective construction](construction.md) instead gives joint squared fidelity at least $`mn/[mn+(d-1)(d+n)]`$. Its normalization depends on the contraction's singular directions. A single scalar normalization preserves the target vector exactly and without spectator disturbance, but pays the largest singular value on the entire input space. At $`m=1`$ the sharp heralding rate reduces to $`n/[d(n+d-1)]`$.

The comparison concerns independent maximally entangled ports, designated returned pairs and acceptance. The optimum for exact selected output with unrestricted spectator disturbance remains open here at general $`(m,n)`$. The success frontier allows failure to consume the resource. Repeated use requires an account of those failures. Receiver-side quantum recovery and different shared entangled resource states are outside this model.

The one-port endpoint is the theorem of Grosshans and coauthors, [*Quantum* **10**, 2105 (2026)](https://doi.org/10.22331/q-2026-05-13-2105), whose Section 6 also identifies simultaneous multiple ports and copies as a future direction. Studziński and coauthors' [standard probabilistic PBT](https://doi.org/10.1038/s41598-017-10051-4) optimizes exact output from one specimen with unselected ports discarded. Its success tends to one for fixed $`d`$ and large $`m`$, as shown by Christandl and coauthors, [Theorem 1.3](https://doi.org/10.1007/s00220-020-03884-0). Strelchuk, Horodecki and Oppenheim [develop approximate entanglement recycling](https://doi.org/10.1103/PhysRevLett.110.010505). Kopszak and coauthors [calculate successful-branch recycling fidelity](https://doi.org/10.1109/TIT.2026.3656762) for specified probabilistic measurements, including the standard one-specimen protocol with EPR ports. Their [Theorem 11](https://arxiv.org/pdf/2504.00710) evaluates degradation under that instrument. The optimization here constrains every returned Bell pair to fidelity one and treats all eligible Alice instruments.

The [Canonical Purification Cost exact frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/fc4651999bff3c65ab7992cda015751ae8b5715f/science/exact_frontier.md) already uses the same bosonic contraction commutator on independent state and conjugate specimens. The present input consists of ordered halves of shared Bell pairs. The step from the full ordered port norm to its symmetric sector, the spectator-return constraint on the accepted effects, and the composition of exactness with the expenditure cap are specific to this setting.
