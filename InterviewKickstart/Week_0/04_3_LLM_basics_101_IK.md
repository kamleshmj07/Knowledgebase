## Behind most Generative AI systems is a Large Language Model (LLM)

> The LLM is both **the Engine** and **the Brain**

---

## What are LLMs?

**L**arge · **L**anguage · **M**odel

| Term | Meaning |
|---|---|
| **Large** | Trained on a large dataset (terabytes of text, hundreds of billions of tokens) |
| **Language** | Works with human languages |
| **Model** | Relies on AI models |

---

## Key Characteristics

- Trained on **massive datasets** to learn patterns, meaning, and reasoning
- **Understand and generate** language and other modalities (text, code, images, audio)
- Built on **transformer architectures that scale** to billions of parameters and long context

---

## Under the Hood

- **Architecture:** Transformer Architecture
- **Landmark paper:** *"Attention is All You Need"* (2017)

---

## Examples

> GPT · Claude · Gemini

---

## What is a Token?

- A **token** is the basic unit of text an LLM processes
- **~4 characters = 1 token**
- **1 token ≈ 0.75 words**

### Example: Tokenizing a sentence

`"Hello, How Are You?"` → `"Hello"` `"How"` `"Are"` `"You"` `"?"`

---

## How Tokenization Works

| Input | Tokens |
|---|---|
| `Cat` | `Cat` |
| `Cats` | `Cat` + `s` |
| `ChatGPT` | `Chat` + `G` + `pt` |

---

## Token Scale in Practice

| Scope | Token Count |
|---|---|
| English language vocabulary | ~170k tokens |
| ChatGPT context window | ~50k tokens |
