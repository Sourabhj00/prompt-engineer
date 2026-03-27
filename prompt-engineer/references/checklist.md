# Prompt Quality Checklist

Evaluate the submitted prompt against every item below. For each item, state the status
(**present / missing / partial**) and provide a specific, actionable fix — not just that
something is missing.

```
[ ] Role/Persona defined? (who is Claude being — tutor, engineer, analyst, etc.)
[ ] Task stated clearly? (single unambiguous objective)
[ ] Output format specified? (headers, JSON, markdown, bullet list, etc.)
[ ] Tone/voice defined? (formal, casual, technical, empathetic, etc.)
[ ] Constraints stated? (scope limits, what to avoid, length bounds)
[ ] Examples provided? (at least one ideal output, mistake, or edge case)
[ ] Chain-of-thought triggered? (explicit reasoning depth instruction)
[ ] Edge cases handled? (what to do with ambiguous or unusual inputs)
[ ] Ambiguous pronouns or references? (every "it", "this", "they" resolves clearly)
[ ] Overly broad or vague scope? (could be narrowed without losing intent)
[ ] Length/depth guidance given? (brief overview vs. deep dive vs. exhaustive)
[ ] Model-specific optimization applied? (XML tags for Claude, etc.)
[ ] Prompt type identified? (system prompt, user-turn prompt, or both)
[ ] Golden rule applied? (Would a colleague with no context understand this prompt?)
[ ] Context/motivation provided for key instructions? (explains WHY, not just WHAT)
[ ] Instructions framed positively? (what to DO, not just what to avoid)
[ ] Long-context placement correct? (data/documents at top, query/instructions at bottom)
[ ] Uncertainty permission granted? (Claude explicitly told it can say "I don't know")
[ ] Grounding instructions present? (for tasks involving document/data/code analysis — require Claude to reference source before claiming)
```
