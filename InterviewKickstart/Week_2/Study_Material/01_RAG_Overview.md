# RAG Overview: Problem, Motivation, Tech Stack & Vector Stores


## Problem Statement: What Exactly Are We Building?

In Week 2, we are building the retrieval layer for the **SupportDesk RAG** assistant —
the part of the system that can reliably find the most relevant past support tickets for any new issue.

---

### The Problem We're Solving (In the Real World)

Engineers and Support teams regularly face issues like:

- Users can't log in after password reset
- Database connection timeouts in production
- Payments failing for international cards
- Emails not being delivered

---

### The Challenge

The solution often already exists in past tickets, but finding it is slow because:

| Reason | Description |
|---|---|
| **Unstructured text** | Ticket data is free-form text, not clean tables |
| **Different words** | People describe the same issue in different ways |
| **Keyword-based search** | Misses semantically relevant results |
| **Volume** | Too many tickets to read manually |


---


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


---


## RAG System: Tech Stack & Data Schema

---

## Tech Stack

```
┌─────────────────────────┐   ┌──────────────────────────┐
│ Orchestration           │   │ Indexing (Advanced)      │
│ LangChain (LCEL)        │   │ LlamaIndex strategies    │
└────────────┬────────────┘   └────────────┬─────────────┘
             │                             │
             └──────────┬──────────────────┘
                        ▼
                  [ Retrieval ]
                        │
          ┌─────────────┴──────────────┐
          ▼                            ▼
┌──────────────────────┐     ┌──────────────────────┐
│ Embeddings           │     │ Vector DB            │
│ OpenAI               │────►│ Chroma / FAISS       │
│ text-embedding-3-    │     └──────────┬───────────┘
│ small                │               │
└──────────────────────┘               ▼
                               [ Generation ]
                                     ▲
                  ┌──────────────────┤
                  │                  │
        ┌─────────────────┐ ┌────────────────────────┐
        │ LLM             │ │ Evaluation             │
        │ gpt-4o-mini     │ │ retrieval + generation │
        └─────────────────┘ │ metrics                │
                            └────────────────────────┘
```

### Component Summary

| Component | Tool / Model |
|---|---|
| **Orchestration** | LangChain (LCEL) |
| **Indexing** | LlamaIndex strategies |
| **Embeddings** | OpenAI `text-embedding-3-small` |
| **Vector DB** | Chroma / FAISS |
| **LLM** | `gpt-4o-mini` |
| **Evaluation** | Retrieval + generation metrics |

---

## Data Schema (What the Model Sees)

```
┌──────────────┐  transform  ┌───────────────────┐  chunk/split  ┌───────────────┐  retrieve top-k  ┌─────────────────┐
│  TicketJSON  │ ──────────► │ LangChainDocument │ ────────────► │    Chunk      │ ───────────────► │ PromptPayload   │
└──────────────┘             └───────────────────┘               └───────────────┘                  └─────────────────┘
```

### TicketJSON

```
+string  ticket_id
+string  title
+string  description
+string  resolution
+string  category
+string  priority
+date    created_date
+date    resolved_date
```

### Metadata

```
+string  ticket_id
+string  title
+string  category
+string  priority
+string  source
+string  chunk_id
+int     chunk_index
```

### LangChainDocument

```
+string    page_content
+Metadata  metadata
```

### Chunk

```
+string    chunk_text
+Metadata  metadata
```

### PromptPayload

```
+string    system_rules
+Chunk[]   context_chunks
+string    question
```


---


## Vector Databases & Embedding Pipeline

---

## Multi-Modal Embeddings → Vector Database

Any data type can be embedded into vectors and stored for similarity search.

```
Document ──► [ Text Embedding Model  ] ──► [ text vectors  ] ──► Similarity Search ──┐
                                                                                       │
Image    ──► [ Image Embedding Model ] ──► [ image vectors ] ──► Similarity Search ──┼──► Vector Database
                                                                                       │
Audio    ──► [ Audio Embedding Model ] ──► [ audio vectors ] ──► Similarity Search ──┘
```

| Input | Embedding Model | Output |
|---|---|---|
| Document | Text embedding model | Text vector embeddings |
| Image | Image embedding model | Image vector embeddings |
| Audio | Audio embedding model | Audio vector embeddings |

---

## Offline vs Online Pipeline

### Offline (Indexing Phase)

```
[ Documents ]
      │
      ▼
[ Embedding Model ]          ← Cohere · OpenAI · HuggingFace · LlamaIndex
      │
      ▼
[ Vector Embeddings ]
  [0.5,  0.8, -0.3,  0.2]
  [0.8,  0.3, -0.1,  1.0]
  [0.7,  0.6,  0.2,  0.9]
      │
      ▼
[ Vector Database ]
```

### Online (Query Phase)

```
                [ Query ] ──► [ Embedding Model ] ──► [-0.9, -0.7, -1.0, -0.8]
                                                │
                                                ▼
                                    [ Vector Database ]
                                       KNN Search
                                                │
                                                ▼
                                      [ Query Results ]
```

> ⚠️ **Key Note:** The output of a vector DB query is **text** (the original chunks),
> not embeddings. The vectors are used only for search — results are returned as readable text.

---

## Embedding Model Options

| Provider | Models |
|---|---|
| **OpenAI** | `text-embedding-3-small`, `text-embedding-3-large` |
| **Cohere** | `embed-english-v3.0`, `embed-multilingual-v3.0` |
| **HuggingFace** | `sentence-transformers/all-MiniLM-L6-v2` |
| **LlamaIndex** | Supports local + remote embedding models |


---
