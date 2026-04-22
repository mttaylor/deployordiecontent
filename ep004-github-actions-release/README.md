# EP004 — GitHub Actions Release Automation

Full workflow from Deploy or Die Episode 4.

Push a tag → Claude generates release notes → GitHub release created → Slack notified.

## Setup

1. Copy `.github/workflows/release.yml` into your repo
2. Add secrets to your GitHub repo:
   - `ANTHROPIC_API_KEY` — from console.anthropic.com
   - `SLACK_WEBHOOK` — from your Slack app settings
3. Add `scripts/generate_notes.py` (from EP001 — link below)
4. Push a tag: `git tag v1.0.0 && git push origin v1.0.0`

## Links
- EP001 (generate_notes.py): https://github.com/mttaylor/deployordiecontent/tree/main/ep001-release-notes-automation
- Video: https://youtube.com/@deployordie
- Newsletter: https://deployordie.io
