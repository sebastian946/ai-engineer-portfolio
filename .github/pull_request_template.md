## Summary

<!-- What does this PR change and why? One or two sentences. Link the issue if there is one. -->

## Type of change

- [ ] `feat` new capability
- [ ] `fix` bug fix
- [ ] `eval` evaluation dataset / metric / run
- [ ] `perf` cost or latency improvement
- [ ] `docs` documentation only
- [ ] `chore` / `refactor` / `test`

## Eval results (before / after)

<!-- Required if prompts, models, retrieval, chunking or tools changed. Command: python evals/run_eval.py -->

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| | | | |

## Cost & latency impact

<!-- Cost per request and p50/p95 latency before vs after. Write "No impact" if nothing in the request path changed. -->

| | Before | After |
|---|--------|-------|
| Cost / request | | |
| p50 latency | | |
| p95 latency | | |

## Test evidence

<!-- Paste the command and the relevant output: pytest summary, eval table, screenshot or GIF. -->

```
```

## Checklist

- [ ] Branch name and commits follow [CONVENTIONS.md](../CONVENTIONS.md)
- [ ] No secrets, keys or customer data in the diff or history
- [ ] `.env.example` updated if a new variable was added
- [ ] README updated and `python scripts/check_readme.py` passes
- [ ] Tests added or updated and passing locally
- [ ] Eval results included when behavior changed
