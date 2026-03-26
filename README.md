# Prompt Engineer — Claude Code Skill

An expert prompt refinement engine that analyzes, interrogates, and rewrites any prompt into a production-ready, one-shot-optimized **Master Prompt**.

## What It Does

This skill takes any prompt you give it and transforms it through a structured 5-step process:

1. **Critical Analysis** — Identifies vague language, missing roles, unclear expectations, and unstated constraints
2. **Context Gap Questions** — Asks targeted questions to fill in missing context before rewriting
3. **Checklist Review** — Evaluates your prompt against 12 quality criteria with actionable fixes
4. **Master Prompt Generation** — Produces a fully structured, production-ready prompt
5. **Reasoning Summary** — Explains every significant change and why it improves the prompt

## Installation

### Install as a Claude Code skill

```bash
claude skill add Sourabhj00/prompt-engineer
```

### Manual installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Sourabhj00/prompt-engineer.git
   ```
2. Copy the `prompt-engineer/` folder into your Claude Code skills directory.

## Usage

Once installed, simply ask Claude Code to improve or refine a prompt:

- "Improve this prompt: ..."
- "Refine my prompt"
- "Optimize this for Claude"
- Or just paste a raw prompt — the skill triggers automatically

## Example

**Input:**
> Write a blog post about AI

**What the skill does:**
- Flags that the prompt lacks audience, tone, length, format, and topic constraints
- Asks targeted questions to fill gaps
- Produces a fully structured Master Prompt with role, task, context, instructions, output format, constraints, and examples

## License

MIT
