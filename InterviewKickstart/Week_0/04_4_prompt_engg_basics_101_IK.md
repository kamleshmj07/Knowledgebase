## Prompt Engineering

> Key concept: **System Prompt**

---

## The 4 Elements of a Good Prompt

- **Context** — Set the stage: role, goal, plan, etc.
  - *e.g. "You are a senior SRE reviewing a post-mortem"*

- **Structure** — Use delimiters, Markdown, or XML-like tags
  - *Use `## Task`, `## Input`, `## Output` headers to organize your prompt*

- **Constraints** — Output format, tone, edge cases
  - *e.g. "Respond in JSON. Max 200 words. Use only the data provided."*

- **Iterate** — Draft, evaluate, review output, refine

---

## Example: System Prompt

```text
## Role
You are a senior SRE reviewing a post-mortem.

## Task
Summarize the root cause and recommend 3 action items.

## Input
{incident report}

## Constraints
- Max 200 words
- Respond in JSON
- Use only the data provided
```

---

## Prompt Engineering — Types

| Type | Description | Notes |
|---|---|---|
| **Zero Shot** | No examples provided. LLM is expected to know the answer. | No example |
| **One Shot** | One example provided to guide the LLM's response. | One example → `"Great product"` → `Label: Positive` |
| **Few Shot** | A few examples provided so the LLM understands the expected/ideal response. | Few examples |
| **Chain of Thought** | Provide reasoning through intermediate steps. Extension of few-shot with logical flow. | Step by step |
| **COT-SC** | Self-Consistency with Chain of Thought: construct multiple chains of thought, evaluate each, and select the most coherent one. | |
| **Tree of Thoughts** | Expands chains of thought into a tree format — allows backtracking and exploring multiple branches of reasoning from a single root idea. | |

---

## Complexity Spectrum

```
Zero Shot → One Shot → Few Shot → Chain of Thought → COT-SC → Tree of Thoughts
  (simple) ────────────────────────────────────────────────────────► (complex)
```

---


