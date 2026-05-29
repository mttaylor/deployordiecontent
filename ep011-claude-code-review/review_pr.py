#!/usr/bin/env python3
"""
Claude Code Review Bot
Deploy or Die EP011 — github.com/mttaylor/deployordiecontent
"""

import subprocess
import anthropic
import sys

SYSTEM_PROMPT = """You are a senior software engineer reviewing a pull request. Your job is to identify:
- Logic errors that could cause incorrect behavior
- Security vulnerabilities (auth bypasses, injection risks, insecure defaults)
- Missing error handling
- Race conditions or concurrency issues
- Missing or inadequate tests

For each issue found, state the file and line, describe the problem, and suggest a fix.
Be direct. If the code looks correct, say so.
Do not summarize what the code does unless it helps explain a problem."""


def review_pr(base_branch="main"):
    diff = subprocess.check_output(
        ["git", "diff", f"{base_branch}...HEAD"],
        text=True
    )
    if not diff.strip():
        print("No changes to review.")
        return

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Review this diff:\n\n{diff}"}]
    )
    print(message.content[0].text)


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "main"
    review_pr(base)
