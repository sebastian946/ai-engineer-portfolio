# Learning Log

Short, dated entries. What I did, what I learned, what is next. Newest first.

## 2026-11-05

**Did**

- Set up the `ai-engineer-portfolio` hub: README with project table, `CONVENTIONS.md`, project README template, PR template, `.env.example`.
- Wrote `scripts/check_readme.py` to enforce the README contract and wired it into GitHub Actions (`readme-check.yml`) on every push and PR.

**Learned**

- A README contract is only useful if something enforces it. A 60-line script plus a CI job turns a "please remember to" into a hard gate.
- Deciding the evaluation and cost/latency sections up front forces every future project to be measured, not just demoed.
- Conventional Commits and `<type>/<description>` branches cost nothing now and make the history readable to a recruiter or reviewer later.

**Next**

- First project: a RAG system over a public document set with a golden eval set of at least 30 questions, faithfulness and recall@k metrics, and a cost table.
- Add the project to the hub table with its key result once the first eval run is in.
