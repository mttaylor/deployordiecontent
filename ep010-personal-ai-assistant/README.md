# EP010 — Personal AI Assistant Setup

From Deploy or Die Episode 10: "How I Built a Personal AI Assistant That Runs My Content Business"

## The Stack
- **OpenClaw** — open-source AI agent runtime (runs locally)
- **Telegram** — mobile interface (BotFather → token → connect)
- **Anthropic Claude** — the model (swap for OpenAI if preferred)
- **Workspace files** — markdown config that defines the agent

## Install
```bash
npm install -g openclaw
openclaw setup        # connects your AI provider + Telegram
openclaw gateway start
```

Then message your bot. That's it.

## The 4 Workspace Files

### AGENTS.md
Agent behavior — startup checklist, memory rules, when to reach out proactively.
[See template →](AGENTS_template.md)

### SOUL.md  
Voice and personality — no filler phrases, direct, has opinions.
[See template →](SOUL_template.md)

### USER.md
Context about you — name, timezone, goals, projects, content plan.
[See template →](USER_template.md)

### MEMORY.md
Long-term memory — decisions, lessons, context that survives restarts.
Start empty. The agent fills it over time.

## The Skills System
Skills are markdown files with instructions for repeatable tasks.
Drop them in your OpenClaw skills directory.
The agent follows them exactly every time.

## Links
- OpenClaw: https://github.com/openclaw/openclaw
- OpenClaw docs: https://docs.openclaw.ai
- Newsletter: https://deployordie.io
