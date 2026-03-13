# EP001 — Automated Release Notes with Claude AI

**As seen in:** [Deploy or Die — Episode 1](https://www.youtube.com/@deployordie)

Stop writing release notes by hand. This 30-line GitHub Actions workflow watches for a git tag, pulls your commit log, calls the Claude API, and posts polished release notes to your GitHub Release — automatically.

---

## Setup

### 1. Copy the workflow file

Copy `.github/workflows/release-notes.yml` into your repo.

### 2. Add your Anthropic API key

In your GitHub repo go to:
**Settings → Secrets and variables → Actions → New repository secret**

- Name: `ANTHROPIC_API_KEY`
- Value: your key from [console.anthropic.com](https://console.anthropic.com)

### 3. Ship it

```bash
git tag v1.0.0 -m "your message"
git push origin v1.0.0
```

The workflow fires automatically. Release notes appear in your GitHub Release within ~10 seconds.

---

## How it works

```
git push tag
    └── GitHub Action triggers
            └── git log since last tag
                    └── Claude API call
                            └── GitHub Release created
```

1. **Trigger** — fires on any tag matching `v*`
2. **Commit log** — fetches all commits since the previous tag (up to 50)
3. **Claude** — groups commits by feature / bugfix / breaking change, writes for developers, no marketing language
4. **Release** — creates a GitHub Release with the generated notes

---

## Customizing the prompt

Edit the `content` field in the workflow to change how Claude writes the notes:

```yaml
"content": "Summarize these commits into release notes for ${{ github.ref_name }}.
Group by feature, bugfix, and breaking change.
Write for developers. No marketing language. Under 200 words."
```

Some ideas:
- Add your product name for context
- Change the format (bullet points vs prose)
- Ask it to call out breaking changes more prominently
- Increase `max_tokens` for longer notes

---

## Requirements

- GitHub Actions enabled on your repo
- An [Anthropic API key](https://console.anthropic.com) (pay-per-use, very cheap for this use case)
- `jq` — available by default on `ubuntu-latest` runners

---

## More episodes

→ [deployordie.io](https://deployordie.io)
→ [x.com/deployordie_ai](https://x.com/deployordie_ai)
→ [linkedin.com/company/deployordie](https://www.linkedin.com/company/deployordie/)
