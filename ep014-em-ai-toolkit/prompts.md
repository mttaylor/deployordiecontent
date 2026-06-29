# EP014 — Engineering Manager AI Prompt Toolkit

From Deploy or Die Episode 14: "The Engineering Manager's AI Toolkit: 5 Problems AI Solves Better Than Spreadsheets"

Every prompt follows the same structure: **raw context + what you need + format.**

---

## Prompt 1 — Weekly Status Report

```
Here is a list of Jira tickets closed this week, pull requests merged,
and incidents resolved:

[PASTE YOUR DATA HERE]

Write a concise engineering status report for non-technical stakeholders.
Use plain language. Flag anything that was blocked or is at risk.
Format: three sections — Shipped, Blocked, Watch List.
Keep each section to bullet points. No more than 2 sentences per bullet.
```

**Input:** JIRA export / GitHub PR list / incident log
**Output:** Structured stakeholder report
**Time saved:** ~40 minutes/week

---

## Prompt 2 — Dependency Mapping

```
Here is a list of project tickets with descriptions:

[PASTE TICKET LIST HERE]

Identify all dependencies between these tickets.
For each dependency, state:
- Which ticket blocks which
- Why (based on the descriptions)

Flag any circular dependencies.
Flag any critical path risks — tickets that, if delayed, would block
the most other work.
```

**Input:** Ticket list with descriptions
**Output:** Dependency map with critical path flags
**Time saved:** Hours of manual analysis

---

## Prompt 3 — Incident Timeline Reconstruction

```
Here are the raw Slack messages and log excerpts from our incident
on [DATE]:

[PASTE SLACK MESSAGES AND LOG EXCERPTS HERE]

Construct a chronological timeline of events.
For each event: timestamp, actor (if known), action taken, observed effect.
Flag any gaps in the timeline where information is missing or unclear.
Note any points where the response could have been faster.
```

**Input:** Slack export + log excerpts
**Output:** Structured incident timeline
**Time saved:** 1.5–2 hours of manual reconstruction

---

## Prompt 4 — Retrospective Summary

```
Here are the notes from our engineering retrospective:

[PASTE RETRO NOTES / MIRO EXPORT / FIGJAM EXPORT]

Summarize into three sections:
1. What Went Well
2. What Didn't Go Well
3. Action Items

For each action item:
- State the specific action (not vague — be concrete)
- Suggest an owner based on who raised the issue
- Suggest a timeline (this sprint / next sprint / next quarter)

Be direct. Skip feel-good filler. If something was clearly a problem, say so.
```

**Input:** Miro / FigJam export or raw notes
**Output:** Structured retro summary with draft owners
**Time saved:** 30–45 minutes of post-retro synthesis

---

## Prompt 5 — Pre-Release Risk Surface

```
Here is the architecture of our upcoming release:

System overview: [describe the system]
New components being introduced: [list them]
External dependencies: [list third-party services, APIs, databases]
Rollback plan: [describe it, or note if none exists]
Known risks already identified: [list any you already know about]

Identify the top 10 risk areas for this release.
For each risk:
1. Describe the failure mode (what specifically could go wrong)
2. Estimate the likely impact (user-facing / data / revenue / SLA)
3. Suggest one specific mitigation action to take before release

Be systematic. Include risks that are unlikely but high-impact.
```

**Input:** Release architecture description
**Output:** Prioritized risk register with mitigations
**Time saved:** Full pre-mortem meeting, or the risks you'd have missed

---

## The Pattern

Every prompt above follows the same structure:

1. **Raw context** — paste in the messy data you already have
2. **What you need** — specific output, not vague
3. **Format** — sections, bullet points, ownership

The skill isn't learning to use AI. The skill is knowing which 45-minute manual task to hand off first.

---

## Links
- Newsletter: https://deployordie.io
- EP011 (Claude code review bot): https://github.com/mttaylor/deployordiecontent/tree/main/ep011-claude-code-review
- EP010 (OpenClaw workflow automation): https://github.com/mttaylor/deployordiecontent/tree/main/ep010-personal-ai-assistant
