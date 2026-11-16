# What additional input copies buy

The [frontier](model.md) compares two physically different resources: stored Bell ports or Choi programs, and repeated specimens of the unknown input. The input specimens are quantum data, not classical descriptions of that data.

## The intermediate regime

Take $n$ of order $\sqrt d$. The fixed-error port budget is of order $d^{3/2}$. With only one input specimen it is of order $d^2$. More generally, for any fixed $0<\alpha<1$,

```math
n=\Theta(d^\alpha)
\quad\Longrightarrow\quad
m_{\mathrm{opt}}=\Theta(d^{2-\alpha}).
```

Thus input copies yield an unbounded factor of order $n$ in the resource-port budget while their number is still much smaller than the state dimension. Once $n$ is of order $d$, the port budget saturates at order $d$.

For a concrete conservative allocation, choose $d=1024$, $n=32$ and target global fidelity $0.9$. The exact polar bound is sufficient when

```math
m\ge
9\,\frac{1023\cdot1056}{32}
=303831.
```

At $n=1$, the same bound needs $m\ge9(1024^2-1)=9437175$. These are sufficient counts from the stated bound, not exact optimal counts or hardware costs. The compiled circuit uses its own conservative error allocation. Every copy and every known routing operation remains charged.

## Why learning the input first does not explain every regime

With order $d$ copies, pure-state estimation can produce a fixed-accuracy classical description. Combining that estimate with known-state port-based state preparation explains the balanced output-only order $m,n=\Theta(d)$. That point alone is not the new capability.

The same approach is inadequate for $n\ll d$ at high uniform output fidelity. The optimal Haar-average fidelity of pure-state estimation from $n$ identical specimens is $(n+1)/(n+d)$ [1]. Even perfect subsequent teleportation of the estimate cannot repair that estimation loss. The collective construction instead uses the supplied specimens coherently together with the Bell ports. It also controls the returned specimens under one joint fidelity guarantee, whereas input tomography consumes its training specimens.

This comparison concerns estimate-then-prepare strategies. It is not an unrestricted classical-computation lower bound or a claim about end-to-end application runtime.

## One port: exact success and deterministic output differ

With $m=1$, Bob has only one available output register. If every outcome is retained and he cannot correct or replace that register, no-signalling fixes his unconditional marginal to $I/d$. The output fidelity is exactly $1/d$ for every input, regardless of $n$.

This does not conflict with exact heralded multicopy teleportation. Grosshans and collaborators prove a successful branch of probability

```math
p_{\mathrm{exact}}(d,n)=\frac{n}{d(d+n-1)}.
```

At $m=1$, the useful polar branch reproduces this known probability. Failed outcomes complete the deterministic channel and need not have high fidelity. A conditional exact success probability and an unconditional approximate-output score answer different questions.

For $d=2,n=2$, the exact successful branch has probability $1/3$. The unconditional output fidelity remains $1/2$. A claim that the polar lower bound $1/3$ is the exact deterministic fidelity would therefore be incorrect.

## One input specimen

For $n=1$, the constructive bound becomes

```math
F_{\mathrm{global}}\ge\frac{m}{m+d^2-1}.
```

This is the familiar square-root-measurement resource scale in port-based teleportation. It is a lower bound on approximate global fidelity, not an expression for an optimal exact-heralded success probability.

## A noisy stored operation

Let $\mathcal A_\gamma$ be the qubit amplitude-damping channel, with

```math
K_0=|0\rangle\langle0|+\sqrt{1-\gamma}|1\rangle\langle1|,
\qquad
K_1=\sqrt\gamma|0\rangle\langle1|.
```

Its normalized Choi state can be supplied as a mixed program specimen. For an unknown input $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, the desired output is the mixed state

```math
\begin{pmatrix}
|\alpha|^2+\gamma|\beta|^2 &
\sqrt{1-\gamma}\alpha\overline\beta\\
\sqrt{1-\gamma}\overline\alpha\beta &
(1-\gamma)|\beta|^2
\end{pmatrix}.
```

The retrieval instrument needs no estimate of $\alpha,\beta$ or $\gamma$ to implement this supplied channel. Moving $\mathcal A_\gamma$ to the outer halves of the Bell construction proves the same fidelity lower bound relative to this channel output and the returned noisy programs. The theorem implements the stored noisy operation; it does not reconstruct an ideal noiseless unitary from arbitrary noise.

## Return and reuse

The joint-return target contains one output, $m-1$ remaining programs and $n-1$ remaining input specimens. If its squared fidelity is at least $1-\epsilon$, its half-trace distance from the ideal target is at most $\sqrt\epsilon$. Every marginal inherits that distance bound.

Subsequent known channels contract trace distance, so a finite sequence can be analysed by a telescoping error budget. The one-use theorem by itself does not guarantee a fixed per-round error indefinitely. The initial resource preparation, storage coherence and actual gate noise also remain separate physical costs.

## Reference

1. D. Bruß and C. Macchiavello, *Optimal state estimation for d-dimensional quantum systems*, Physics Letters A **253**, 249–251 (1999), [arXiv:quant-ph/9812016](https://arxiv.org/abs/quant-ph/9812016). The comparison is its universal pure-state estimation fidelity, not a gate-complexity theorem.
