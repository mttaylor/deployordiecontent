# EP017 — Making AI Coding Agents More Reliable with Fable5

From Deploy or Die Episode 17: "How to Make Your AI Coding Agent 10x More Reliable"

## The Problem

AI coding agents fail in predictable ways:
- Claims tests pass without running them
- Hallucinating API signatures from stale training data
- Silently dropping requirements that proved difficult
- Fixing symptoms instead of root causes

You can't fix this by asking nicely — the prompt is what decays.

## The Solution: Fable5 Methodology

A self-enforcing methodology extracted from one of Anthropic's most capable models (above Opus tier).

**Repo:** https://github.com/UnpaidAttention/fable5-methodology

## Install (Claude Code)

```bash
claude plugin marketplace add UnpaidAttention/fable5-methodology
claude plugin install fable5-methodology
# restart Claude Code
```

Or script install:
```bash
git clone https://github.com/UnpaidAttention/fable5-methodology.git
cd fable5-methodology
./install.sh
```

## The 4 Enforcement Layers

### 1. Hooks (strongest)
Deterministic scripts at lifecycle events. Don't ask the model to remember — block the action.

| Hook | Enforces |
|------|----------|
| `pre-tool-guard` | Blocks force push, DROP/TRUNCATE, curl\|sh, secret commits |
| `post-edit-verify` | Lints every touched file; flags test skip markers |
| `delivery-gate` | Blocks "done" if no test ran since last edit |
| `evidence-log` | Appends every tool call to an objective log |
| `pre-compact-handoff` | Snapshots state before context compaction |
| `session-loader` | Injects git status + notes at session start |

### 2. Agents (independent review)
| Agent | Role |
|-------|------|
| `builder` | Implements one scoped change; refuses without acceptance criteria |
| `qa-verifier` | Runs tests independently; no edit tools (can only verify) |
| `code-reviewer` | Adversarial cold review — hunts fake progress, dropped requirements |
| `research-scout` | Checks installed environment first, not training data |

**Rule:** Builder output is never accepted without qa-verifier evidence.

### 3. Context
26 on-demand skills covering: debugging, security review, code review, architecture decisions, uncertainty management, and more.

### 4. Evals
Behavioral regression tests. Each recurring failure becomes an eval. Catches drift when you swap models.

## The Honest Claim

It doesn't make a weaker model as capable as the model the methodology was extracted from. It makes whatever model you're running significantly more reliable than the same model running without it.

## Links
- Fable5 repo: https://github.com/UnpaidAttention/fable5-methodology
- Newsletter: https://deployordie.io
- EP011 (Claude code review bot): https://github.com/mttaylor/deployordiecontent/tree/main/ep011-claude-code-review
