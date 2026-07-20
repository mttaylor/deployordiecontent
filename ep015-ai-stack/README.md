# EP015 — The AI Stack I Actually Use

From Deploy or Die Episode 15: "The AI Stack I Actually Use Every Day (And What I Dropped)"

## The Filter

Before adding any tool, three questions:
1. Does it save >30 min/week?
2. Is it reliable enough that I don't have to babysit it?
3. Does it fit where I already work (terminal, browser, phone)?

## What Stayed

| Tool | Use Case | Cost |
|------|----------|------|
| [Claude](https://claude.ai) | Writing, reasoning, code review | ~$20/month |
| [Cursor](https://cursor.sh) | VS Code + Claude in the editor | ~$20/month |
| [OpenClaw](https://github.com/openclaw/openclaw) | Background agent, workflow automation | Free |
| [edge-tts](https://github.com/rany2/edge-tts) | TTS for video narration | Free |

**Total: ~$40/month**

## edge-tts Quick Start

```bash
pip install edge-tts

# Basic usage
edge-tts --voice en-US-AndrewNeural --rate=-5% \
  --text "Your narration text here" \
  --write-media output.mp3

# List available voices
edge-tts --list-voices
```

No API key needed. Wraps Microsoft's accessibility TTS engine.

## What Got Dropped

| Tool | Reason |
|------|--------|
| GitHub Copilot | Replaced by Cursor — autocomplete vs conversation |
| Jasper | Generic output, slow, cost more than Claude |
| Chrome AI extensions | Replaced by Claude tab + paste |
| Midjourney | Output didn't fit the aesthetic |

## Links
- Newsletter: https://deployordie.io
- EP008 (OpenClaw setup): https://github.com/mttaylor/deployordiecontent/tree/main/ep008-openclaw-content-automation
- EP011 (Claude code review): https://github.com/mttaylor/deployordiecontent/tree/main/ep011-claude-code-review
