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
