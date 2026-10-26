# LLMs & Prompting

---

## What are LLMs?

> The LLM is both **the Engine** and **the Brain** behind most Generative AI systems.

**L**arge · **L**anguage · **M**odel

| Term | Meaning |
|---|---|
| **Large** | Trained on a large dataset (terabytes of text, hundreds of billions of tokens) |
| **Language** | Works with human languages |
| **Model** | Relies on AI models |

**Key Characteristics**
- Trained on **massive datasets** to learn patterns, meaning, and reasoning
- **Understand and generate** language and other modalities (text, code, images, audio)
- Built on **transformer architectures** that scale to billions of parameters and long context
- Architecture: Transformer — landmark paper *"Attention is All You Need"* (2017)
- Examples: GPT · Claude · Gemini

---

## Tokens

- A **token** is the basic unit of text an LLM processes — **~4 characters = 1 token**, **1 token ≈ 0.75 words**

| Input | Tokens |
|---|---|
| `Cat` | `Cat` |
| `Cats` | `Cat` + `s` |
| `ChatGPT` | `Chat` + `G` + `pt` |

| Scope | Token Count |
|---|---|
| English vocabulary | ~170k tokens |
| ChatGPT context window | ~50k tokens |

---

## Limitations

| Limitation | Description |
|---|---|
| **No Fresh Knowledge** | Trained on a snapshot of the world — can't access your docs, databases, or today's events |
| **Hallucinations** | Confidently wrong; no built-in way to verify or say "I don't know" |
| **No Actions** | Generates text, not outcomes — can't call an API, run a query, or update a ticket |
| **No Memory** | Every conversation starts from zero |

> LLMs are powerful **text generators** — but without augmentation, they are stateless, actionless, and frozen in time.
> These limitations are exactly what **AI Agents** are designed to solve.

---

## Prompt Anatomy

**Components of a prompt:**
- **Instruction** — The specific task you want the model to perform
- **Context** — External information or role to steer the model
- **Input Data** — The question or data to process

LLMs are instruction-tuned (LLMIT) — trained to expect instruction, context, and input.

**What makes a good prompt:**

| Element | What it does | Example |
|---|---|---|
| **Context** | Set the stage: role, goal, plan | *"You are a senior SRE reviewing a post-mortem"* |
| **Structure** | Use delimiters, Markdown, or XML-like tags | `## Task`, `## Input`, `## Output` |
| **Constraints** | Output format, tone, edge cases | *"Respond in JSON. Max 200 words. Use only the data provided."* |
| **Iterate** | Draft → evaluate → refine | — |

**Example system prompt:**
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

## Prompting Techniques

| Technique | Description | Notes |
|---|---|---|
| **Zero-Shot** | No examples — LLM uses its training alone | Simple tasks |
| **One-Shot** | One example to guide the response | `"Great product"` → `Label: Positive` |
| **Few-Shot** | A few examples enabling **in-context learning** | Complex tasks where zero-shot falls short |
| **Chain of Thought (CoT)** | Provide reasoning through intermediate steps | Step by step |
| **COT-SC** | Self-Consistency: generate multiple CoT chains, pick the most coherent | More reliable than single CoT |
| **Tree of Thoughts** | Expands CoT into a tree — allows backtracking and exploring multiple branches | Open-ended reasoning |

**Complexity spectrum:**
```
Zero-Shot → One-Shot → Few-Shot → Chain of Thought → COT-SC → Tree of Thoughts
 (simple) ──────────────────────────────────────────────────────────► (complex)
```

---

### Chain-of-Thought Example

**Prompt (few-shot CoT):**
> The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
> A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
>
> The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
> A:

**Model answer:** Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.

---

### Zero-Shot CoT

Adding "Let's think step by step" unlocks reasoning without any examples:

| Approach | Prompt | Output |
|---|---|---|
| Standard | *"How many blue golf balls?"* → `A: The answer is` | 8 ❌ |
| Zero-Shot CoT | *"How many blue golf balls?"* → `A: Let's think step by step.` | 4 ✅ |

---

### ReAct: Reason + Act

CoT alone still lacks access to the external world — it can hallucinate and can't update knowledge.

**ReAct** extends CoT by generating both reasoning traces **and** actions, letting the model interact with external environments (APIs, search, databases) and incorporate real results into its reasoning.

> Full ReAct loop and agent architecture → see `02_AI_Agents.md`

---

## References
- [Prompting Guide — RAG Introduction](https://www.promptingguide.ai/research/rag.en#introduction-to-rag)
- [LangChain Quickstart](https://python.langchain.com/v0.1/docs/get_started/quickstart/)
- [Prompting Guide — LLM Agents](https://www.promptingguide.ai/research/llm-agents)
- [NVIDIA — Introduction to LLM Agents](https://developer.nvidia.com/blog/introduction-to-llm-agents/)
