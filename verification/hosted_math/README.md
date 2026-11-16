# Hosted mathematics verification

These read-only helpers compare every mathematical expression in the commit-pinned GitHub Markdown with its source at wide and narrow viewport widths. They retain source inventories, accessible MathML, comparison reports and screenshots for human inspection. A structural pass does not establish scientific correctness or replace visual review.

The helper set is copied unchanged from [Guinevere](https://github.com/GoGoKo699/Guinevere/tree/5731b136156e426c2adf10fb5b09fdbccc8c9de4/plugins/merlin-arthur-research/skills/merlin-arthur-research/scripts), commit `5731b136156e426c2adf10fb5b09fdbccc8c9de4`.

The workflow uses a fresh anonymous Chromium context, reads this public repository at the proposed commit, and has `contents: read` only. It uses no secrets or persisted checkout credentials. Reports and captures are retained temporarily as workflow artifacts. For local use, provide Node.js 18+, Python 3.10+, Git, Playwright and MathJax; the dependency directory and output belong outside the scientific source.

```bash
node verification/hosted_math/probe_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Multicopy-Teleportation --revision COMMIT --page README.md --output /tmp/multicopy-probe
node verification/hosted_math/capture_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Multicopy-Teleportation --revision COMMIT --output /tmp/multicopy-hosted
```

Replace `COMMIT` with the full inspected Git commit. Use a new empty output directory for each run. The full collector inventories every tracked Markdown page; the probe checks only one representative page and is not a full repository review.
