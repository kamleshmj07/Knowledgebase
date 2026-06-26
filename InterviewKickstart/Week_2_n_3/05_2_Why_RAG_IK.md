## Why RAG? Three Core Problems

---

### ❌ Problem 1: LLMs Don't Know Your Data

```
User: "Login fails after password reset"
            │
            ▼
    [ LLM: Generic Answer ]
            │
            ▼
        FAILS:
        - No access to YOUR tickets
        - Can't cite real solutions
        - May hallucinate
```

---

### ❌ Problem 2: Keyword Search Misses Synonyms

Same issue, described in different words:

| Query | Found? |
|---|---|
| `can't login` | ✅ |
| `authentication failed` | ❌ |
| `invalid credentials` | ❌ |
| `access denied` | ❌ |
| `SSO not working` | ❌ |

> **Result: 80% missed!**

---

### ❌ Problem 3: Context is Scattered

Tickets have many fields: `Title` · `Description` · `Resolution` · `Category` · `Priority` · `Date`

- Can't search smartly — no filtering by priority/category
- Title-only search misses details buried in description/resolution

---

## Key Challenges

- **LLM-only approach** — can sound correct but may **guess/hallucinate**;
  it doesn't know your ticket history by default.
- **Context limits** — we can't paste all tickets into the prompt;
  we must retrieve only the best few.
- **Noise vs precision trade-off** — without chunking + indexing choices,
  retrieval becomes inconsistent.

---

## ✅ The Solution: Semantic Retrieval (RAG Pipeline)

```
[ Embeddings ]      [ Vector Store ]     [ Metadata ]       [ Grounded ]
Text → Vectors  ──► Index all tickets ──► Filter by     ──► Cite real
Capture meaning     Fast search           category/priority  solutions
```

### What Semantic Retrieval Does

- Finds `auth failed` when searching `can't login`
- Returns full context with resolution
- Filters by category and priority
- Backs answers with real past tickets
