# EP011 — Claude Code Review Bot

From Deploy or Die Episode 11: "I Built a Code Review Bot With Claude. Here's the Prompt."

## What it does
Pipes your git diff to Claude with a system prompt tuned to find logic errors, security issues, missing error handling, race conditions, and missing tests. Posts the review as a PR comment via GitHub Actions.

## Files
- `review_pr.py` — run locally: `python3 review_pr.py main`
- Drop `claude-review.yml` in `.github/workflows/` for automatic PR reviews

## Setup
```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python3 review_pr.py main
```

For GitHub Actions: add `ANTHROPIC_API_KEY` as a repository secret.

## Cost
~$0.01 per review. Team of 10 shipping 10 PRs/day = ~$5/day for an always-on senior reviewer.

## Links
- Newsletter: https://deployordie.io
- Anthropic API docs: https://docs.anthropic.com
