# Prompt Engineer — Claude Code Skill

An expert prompt refinement engine that analyzes, interrogates, and rewrites any prompt into a production-ready, XML-structured **Master Prompt** — with full reasoning for every change.

## What It Does

The skill transforms your prompt through a structured 6-step process:

1. **Critical Analysis** — Applies a "golden rule" litmus test, flags vague language, missing roles, unclear output expectations, and unstated constraints
2. **Context Gap Questions** — Asks targeted questions to fill missing context before rewriting; identifies whether the prompt is a system prompt, user-turn prompt, or both
3. **Checklist Review** — Evaluates your prompt against 19 quality criteria (role, output format, tone, constraints, grounding instructions, uncertainty permission, long-context placement, and more)
4. **Master Prompt Generation** — Rewrites using XML-tagged structure (`<role>`, `<task>`, `<context>`, `<instructions>`, `<output_format>`, `<constraints>`, `<examples>`) with typed example tags and explicit motivation
5. **Reasoning Summary** — Explains every significant change with a `[Change] → [Reason]` format, plus a self-evaluation pass against the checklist
6. **Iterative Refinement** — If you provide feedback on the output, the skill patches the Master Prompt without restarting from Step 1

The skill will not generate a Master Prompt until Steps 1–3 are complete.

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

The skill triggers when you have a prompt artifact you want improved — not for general advice about prompting, but for actual rewriting of a specific prompt:

- `"Improve this prompt: ..."`
- `"This prompt isn't working well, can you fix it?"`
- `"Refine my system prompt for a customer support chatbot"`
- `"Optimize this for Claude"`
- `"Rewrite this to be clearer"` + paste your prompt
- Or just paste a raw prompt without explanation — the skill triggers automatically

## Example

**Input prompt:**
```
Tell me about the best practices for error handling in Python.
```

**What the skill flags:**
- No role — who is Claude being? A tutor? A senior engineer?
- No audience — beginner? someone debugging a production incident?
- No output format — essay? bullet list? code examples?
- No scope — Python error handling spans try/except, custom exceptions, logging, async, and more
- No constraints — length, depth, what to skip

**Output (Master Prompt):**
```xml
<role>Senior Python engineer with 10+ years of production experience, explaining concepts to an intermediate developer who knows basic try/except but wants to write more robust code</role>

<task>Explain Python error handling best practices with emphasis on patterns used in production applications</task>

<context>
The reader is an intermediate Python developer working on a production web application.
Motivation: Poor error handling in production causes silent failures, data corruption, and undebuggable incidents. Getting this right prevents 3 AM pages.
</context>

<instructions>
1. Start with the most important principle (be specific about what to catch)
2. Cover: exception hierarchy design, custom exceptions, context managers, logging best practices, error propagation
3. For each topic, provide one concise code example showing the recommended pattern
4. After each example, explain WHY this pattern matters in production
</instructions>

<output_format>
### Topic Name
Brief explanation (2-3 sentences)
[code example]
**Why this matters:** one sentence on production impact
</output_format>

<constraints>
- Skip basic try/except syntax — the reader already knows this
- Focus on patterns, not exhaustive API reference
- If any recommendation is context-dependent, say so explicitly rather than presenting it as universal
- If you are unsure about any claim, say so explicitly rather than generating a plausible-sounding answer.
</constraints>
```

## Repository Structure

```
prompt-engineer/
├── SKILL.md                        Main skill definition and 6-step process
├── references/
│   └── checklist.md                19-item prompt quality checklist
├── examples/
│   └── before-after.md             Complete before/after transformation example
├── evals/
│   └── evals.json                  20 trigger test cases (10 should-trigger, 10 should-not)
└── scripts/                        Description optimization tooling
    ├── utils.py                    Shared parse_skill_md() utility
    ├── quick_validate.py           Validates SKILL.md structure and frontmatter
    ├── run_eval.py                 Tests trigger accuracy against Claude CLI
    ├── improve_description.py      Uses Claude to improve description from eval failures
    ├── run_loop.py                 Iterative optimization: eval → improve → repeat
    └── generate_report.py          Generates HTML report of optimization progress
```

The checklist and examples are bundled as separate files to reduce context cost — they are only loaded when the skill is active.

## Development

### Validate the skill

```bash
cd prompt-engineer
python scripts/quick_validate.py .
```

Checks that SKILL.md has valid frontmatter, the name is kebab-case, the description is under 1024 characters, and all referenced files exist.

### Optimize the trigger description

The `run_loop.py` script iteratively improves the `description` field in SKILL.md frontmatter — the field Claude uses to decide whether to invoke the skill. It splits the 20 eval cases into train/test sets, evaluates the current description, uses Claude to propose improvements based on failures, and repeats until all training cases pass or the iteration limit is reached. A live HTML report opens in the browser showing results per iteration.

```bash
cd prompt-engineer
python -m scripts.run_loop \
  --eval-set evals/evals.json \
  --skill-path . \
  --model claude-sonnet-4-6 \
  --verbose
```

When done, the script prints the best-scoring description (selected by held-out test score, not training score). Update the `description` field in `SKILL.md` manually with the result.

### Scripts reference

| Script | Purpose | Key flags |
|--------|---------|-----------|
| `quick_validate.py <path>` | Validate SKILL.md | — |
| `run_eval.py` | Test trigger accuracy once | `--eval-set`, `--skill-path`, `--description` (to test a description without editing the file) |
| `run_loop.py` | Full iterative optimization | `--max-iterations`, `--holdout`, `--report none` (skip browser) |
| `generate_report.py <results.json>` | Render HTML from saved results | `-o <output.html>` |

## License

MIT
