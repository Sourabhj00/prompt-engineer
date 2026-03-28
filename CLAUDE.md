# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Claude Code skill (not a traditional software project). It provides an expert prompt refinement engine that transforms user prompts into production-ready, one-shot-optimized Master Prompts through a structured 6-step process.

## Repository Structure

- `prompt-engineer/SKILL.md` — Main skill definition (frontmatter + prompt instructions)
- `prompt-engineer/references/checklist.md` — 19-item prompt quality checklist (loaded only when skill is active)
- `prompt-engineer/examples/before-after.md` — Complete transformation example (loaded only when skill is active)
- `prompt-engineer/evals/evals.json` — 20 trigger test cases (10 should-trigger, 10 should-not)
- `prompt-engineer/scripts/` — Python tooling for validation and description optimization
- `README.md` — Installation and usage docs.
- `LICENSE` — MIT license.

## Scripts

All scripts live in `prompt-engineer/scripts/` and should be run from the repo root with `python -m scripts.<name>` or from the `prompt-engineer/` directory.

| Script | Purpose | Example |
|--------|---------|---------|
| `quick_validate.py` | Validate SKILL.md structure and frontmatter | `python scripts/quick_validate.py .` |
| `run_eval.py` | Test trigger accuracy against evals.json | `python -m scripts.run_eval --eval-set evals/evals.json --skill-path . --verbose` |
| `improve_description.py` | Use Claude to improve description from eval failures | `python -m scripts.improve_description --eval-results results.json --skill-path . --model claude-sonnet-4-6` |
| `run_loop.py` | Iterative optimization: eval → improve → repeat | `python -m scripts.run_loop --eval-set evals/evals.json --skill-path . --model claude-sonnet-4-6 --verbose` |
| `generate_report.py` | Generate HTML report from optimization results | `python -m scripts.generate_report results.json -o report.html` |

### Iterative optimization workflow

`run_loop.py` automates description improvement without manual intervention:
1. Splits evals into train/test sets (40% holdout by default)
2. Runs eval on current description
3. Calls Claude to improve description based on failures
4. Repeats until all train cases pass or max iterations reached
5. Opens a live-updating HTML report in the browser
6. Returns the best-scoring description (by test score)

## How the Skill Works

The skill follows a strict 6-step sequential process defined in `SKILL.md`:

1. **Critical Analysis** — Applies golden-rule litmus test, flags vague language, missing roles, unclear expectations
2. **Context Gap Questions** — Asks targeted questions (including large-context identification); proceeds with labeled `[ASSUMPTION: ...]` if unanswered. Also identifies prompt type (system / user-turn / both)
3. **Checklist Review** — Evaluates against the 19-item checklist in `references/checklist.md`
4. **Master Prompt Generation** — Produces XML-tagged structured prompt: `<role>`, `<task>`, `<context>` (with motivation), `<instructions>`, `<output_format>`, `<constraints>` (with uncertainty permission), `<examples>` (with typed `<example>` tags). Branches output format based on prompt type identified in Step 2
5. **Reasoning Summary** — Explains every change in `- [Change] → [Reason]` format, plus self-evaluation verification checks
6. **Iterative Refinement** — Handles user feedback by patching the Master Prompt without restarting from Step 1

**Hard rule**: Steps 1-3 must complete before generating the Master Prompt in Step 4.

## Installation

```bash
claude skill add Sourabhj00/prompt-engineer
```

Or manually copy the `prompt-engineer/` directory into the Claude Code skills directory.
