# EP008 — OpenClaw Content Automation Workflow

From Deploy or Die Episode 8: "How I Set Up OpenClaw to Automate My Content Workflow"

## The Setup

OpenClaw is an open-source AI agent runtime that runs locally. Configure it with markdown context files and connect to Telegram for a mobile interface to your workflow.

### Workspace files that drive the content pipeline:
- `AGENTS.md` — agent behavior and conventions
- `SOUL.md` — voice and personality  
- `USER.md` — context about you and your projects
- `STATUS.md` — current episode pipeline status (the agent updates this)

### How it works
Send one message: "work on episode X"

The agent:
1. Reads the content plan + STATUS.md
2. Writes narration script
3. Generates audio (`edge-tts --voice en-US-AndrewNeural --rate=-5%`)
4. Renders video (`python3 render_ep00X_v1.py`)
5. Writes newsletter (AI Tool | Money Move | Crypto Signal | 3 Links)
6. Drafts tweet + LinkedIn post
7. Pushes code to GitHub

## Install OpenClaw

```bash
npm i -g openclaw
openclaw setup
openclaw gateway start
```

Docs: https://docs.openclaw.ai

## Links
- OpenClaw: https://github.com/openclaw/openclaw
- Newsletter: https://deployordie.io
