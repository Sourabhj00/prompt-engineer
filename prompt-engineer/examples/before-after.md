# Example Transformation

## BEFORE (user-submitted prompt)

```
Tell me about the best practices for error handling in Python.
```

## Analysis Summary

- No role defined — who is Claude being? A tutor? A senior engineer? A docs writer?
- No audience — beginner? intermediate? someone debugging a specific issue?
- No output format — essay? bullet list? code examples?
- No scope — all of Python error handling is enormous (try/except, custom exceptions, logging, error hierarchies, async error handling, etc.)
- No constraints — length, depth, what to skip

## AFTER (Master Prompt)

```xml
<role>Senior Python engineer with 10+ years of production experience, explaining concepts to an intermediate developer who knows basic try/except but wants to write more robust code</role>

<task>Explain Python error handling best practices with emphasis on patterns used in production applications</task>

<context>
The reader is an intermediate Python developer working on a production web application.
Motivation: Poor error handling in production causes silent failures, data corruption, and undebuggable incidents. Getting this right prevents 3 AM pages.
</context>

<instructions>
1. Start with the most important principle (be specific about what to catch)
2. Cover these topics in order: exception hierarchy design, custom exceptions, context managers for cleanup, logging best practices, and error propagation patterns
3. For each topic, provide one concise code example showing the recommended pattern
4. After each code example, briefly explain WHY this pattern matters in production (not just what it does)
</instructions>

<output_format>
For each topic:
### Topic Name
Brief explanation (2-3 sentences)
```python
# code example
```
**Why this matters:** one sentence connecting to production impact
</output_format>

<constraints>
- Skip basic try/except syntax — the reader already knows this
- Focus on patterns, not exhaustive API reference
- Use realistic variable/function names, not foo/bar
- If any recommendation is contested or context-dependent, say so rather than presenting it as universal
</constraints>

<reasoning_depth>step-by-step</reasoning_depth>

<examples>
<example type="ideal">
### Custom Exception Hierarchies
Define a base exception for your application, then subclass for specific error categories...
[code example with AppError → ValidationError, DatabaseError]
**Why this matters:** Callers can catch broadly (AppError) or narrowly (ValidationError) — gives your team granular control over error recovery without catching unrelated exceptions.
</example>
</examples>
```
