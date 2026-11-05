# Conventions

These rules apply to this hub repo and to every project repo linked from it.

## 1. Repository names

- Lowercase, kebab-case, ASCII only: `rag-support-bot`, `llm-eval-harness`.
- Pattern: `<domain>-<what-it-is>`. Avoid generic names like `project1` or `test`.
- No version numbers or dates in the name.

## 2. Branch names

- `main` is always deployable and protected. Work happens on short-lived branches.
- Pattern: `<type>/<short-kebab-description>` where `type` is one of
  `feat`, `fix`, `docs`, `chore`, `refactor`, `eval`, `exp`.
- Examples: `feat/hybrid-retrieval`, `eval/add-faithfulness-metric`, `exp/rerank-cohere`.
- Delete branches after merge.

## 3. Commits: Conventional Commits

Format: `<type>(<optional scope>): <imperative summary>`

| Type | Use for |
|------|---------|
| `feat` | New user-facing capability |
| `fix` | Bug fix |
| `docs` | README, docs, comments |
| `chore` | Tooling, CI, dependencies |
| `refactor` | Code change with no behavior change |
| `test` | Tests only |
| `eval` | Evaluation datasets, metrics, eval runs |
| `perf` | Latency or cost improvements |

Rules: summary under 72 characters, lowercase, no trailing period. Breaking changes use `!` after the type and a `BREAKING CHANGE:` footer.

## 4. Standard folder structure

```
<project>/
├── README.md              # follows the README contract (section 7)
├── .env.example           # every variable the app reads, with dummy values
├── .gitignore
├── pyproject.toml         # or requirements.txt
├── src/<package>/         # application code
├── evals/
│   ├── datasets/          # golden sets (small, versioned)
│   ├── run_eval.py        # reproducible entry point
│   └── results/           # committed summaries (JSON/MD), not raw dumps
├── tests/                 # unit and integration tests
├── scripts/               # one-off utilities
├── docs/                  # diagrams, demo GIFs, ADRs
└── .github/workflows/     # CI
```

## 5. Secrets policy

- Never commit API keys, tokens, connection strings or customer data. Not even in tests, notebooks or commit history.
- All secrets are read from environment variables. Every variable is documented in `.env.example` with a placeholder value (see [templates/.env.example](templates/.env.example)).
- `.env`, `*.pem`, `*.key` and credential files are gitignored by default (see [.gitignore](.gitignore)).
- Before pushing, run `git diff --cached` and scan for `sk-`, `AKIA`, `Bearer`, `password=`.
- If a secret leaks: rotate it immediately, then rewrite history. Rotation first, cleanup second.

## 6. Evaluation requirements

A project is not "done" until it has:

1. A versioned golden dataset (minimum 30 examples) under `evals/datasets/`.
2. At least one automated metric relevant to the task (e.g. exact match, faithfulness, retrieval recall@k, task success rate).
3. A single reproducible command (`python evals/run_eval.py`) that prints a results table.
4. A baseline to compare against (naive prompt, no retrieval, previous version).
5. Results, cost per run and p50/p95 latency recorded in the README with the date they were measured.

Any PR that changes prompts, models, retrieval or chunking must include before/after eval numbers.

## 7. README contract

Every project README must follow [templates/PROJECT_README.md](templates/PROJECT_README.md) and contain these headings, in this order:

1. Title + one-line pitch
2. Demo (GIF)
3. CI badge
4. `## Problem`
5. `## Architecture` with a Mermaid diagram
6. `## Evaluation` with a results table
7. `## Cost & latency` with a cost table and a "prices checked on" date
8. `## Trade-offs & decisions`
9. `## Run it`
10. `## Limitations & next steps`

[scripts/check_readme.py](scripts/check_readme.py) enforces the mandatory headings and runs in CI on every push and pull request.
