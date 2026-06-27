## RAG Indexing & Query Routing

---

## 1. Why Indexing is Required in RAG

- **RAG needs fast retrieval** — Indexing converts documents into retrievable units (chunks/nodes) with embeddings + metadata.
- **Without indexing, retrieval is too slow at scale** — every query would require a full scan over all chunks (high latency, high cost).

> 💡 Good indexing (chunking + metadata) makes it more likely that the retriever returns the right context, **reducing hallucinations**.

Rough Diagram of RAG Architecture
```
╔══════════════════════════════════ RAG ARCHITECTURE ══════════════════════════════════╗
║                                                                                      ║
║  ┌─────────────────────────────── OFFLINE (Indexing) ────────────────────────────┐   ║
║  │                                                                               │   ║
║  │  Documents ──chunking──► Chunks ──vectorize──► {...} ──indexing──► VectorDB   │   ║
║  │                                                                  (Node 1/2/3) │   ║
║  └────────────────────────────────────────────────────────────────────┬──────────┘   ║
║                                                                        │ retrieve    ║
║  ┌─────────────────────────────── ONLINE (Query Time) ───────────────▼───────────┐   ║
║  │                                                                               │   ║
║  │  User ──► Query ──► Embedding Model ──vectorize──► {...} ──search──► VectorDB │   ║
║  │                                                                        │      │   ║
║  │                                                            Relevant Contexts  │   ║
║  │                                                                 │             │   ║
║  │  User ◄──── Response ◄──── LLM ◄──── Augment (Query + Prompts + Context)      │   ║
║  └───────────────────────────────────────────────────────────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

  Indexing happens OFFLINE · Retrieval happens ONLINE at query time
```

---

## 2. Why Multiple Indexes Exist in Production RAG

```
                      ┌─────────────────────────┐
                      │  Production RAG System  │
                      └────────────┬────────────┘
                                   │
                          ◆ Why Multiple Indexes? ◆
                                   │
      ┌─────────────┬──────────────┼──────────────┬──────────────┐
      │             │              │              │              │
      ▼             ▼              ▼              ▼              ▼
  [Reason 1]    [Reason 2]    [Reason 3]    [Reason 4]    [Reason 5]
 Different      Search        Domain        Update        Security
 Data Types     Strategy      Separation    Frequency     & Access
      │             │              │              │              │
      ▼             ▼              ▼              ▼              ▼
 PDFs: large    Dense Vector   HR Policies   Weekly:        PII/Sensitive:
 chunks         (semantic)     Index         Policy docs    Isolated
                               ─────────     Batch proc.   ─────────
 FAQs: small    BM25/Keyword   Engineering   ─────────     Legal Docs:
 Q&A chunks     (exact terms)  Runbooks      Hourly:        Restricted
                               Index         Incidents     ─────────
 Code:          Hybrid         ─────────     Mini-batches  Multi-tenant:
 syntax-aware   (both)         Product       ─────────     Team A/B
                               Specs Index   Real-time:    ─────────
 Tables:                       ─────────     Logs/events   Routing +
 structured     ✓ Reduces      Streaming     metadata
 queries          noise        ingestion     filters
                ✓ Better
 Tickets:         top-k
 metadata-rich    relevance
      │             │              │              │              │
      └─────────────┴──────────────┴──────────────┴──────────────┘
                                   │
                                   ▼
                    ╔══════════════════════════════╗
                    ║  Better Retrieval Quality    ║
                    ║       & Performance          ║
                    ╚══════════════════════════════╝
```

---

## 3. Why Route Queries Differently Based on Intent

```
                             [ User Query ]
                                   │
                      ◆ Intent Classification ◆
                                   │
      ┌──────────┬─────────┬───────┼───────┬──────────┬──────────┐
      │          │         │       │       │          │          │
      ▼          ▼         ▼       ▼       ▼          ▼          ▼
  Fact       Trouble-   How-to  Latest  Code       Metrics
  Lookup     shooting           Status  Question
      │          │         │       │       │          │
  "PTO       "Error     "Explain "Current "Where   "Q4
  carryover   504 on    indexing  outage  is retry  churn?"
  limit?"    service X" in RAG"  status?" logic?"
      │          │         │       │       │          │
      ▼          ▼         ▼       ▼       ▼          ▼
  FAQ/Policy  Runbooks  Knowledge Incident  Code     Table/SQL
  Index       +Tickets  Base      Index     Index    Backend
  ─────────   ────────  ────────  ────────  ──────   ─────────
  Keyword+    Recent+   Semantic  Time-     Code-    Structured
  Hybrid      Exact     +Reranker sliced    aware    Query
  Precision   Match              7-30d     Embeddings NOT Vector
              Bias to            Recency   Symbol    Search
              Latest             Weighted  Filters
      └──────────┴─────────┴───────┴───────┴──────────┘
                                   │
                                   ▼
                         ╔═══════════════════╗
                         ║ Optimized         ║
                         ║ Retrieval         ║
                         ╚═══════════════════╝
```

---

## 4. Intent-Based Query Routing — Full Production Detail

| # | Intent | Example Query | Routes To | Data | Search | Update | Why |
|---|---|---|---|---|---|---|---|
| 1 | **Fact Lookup** | "PTO carryover limit?" | FAQ/Policy Index | Small chunks, FAQs | Keyword + Hybrid | Weekly batch | Data types + Search strategy |
| 2 | **Troubleshooting** | "Error 504 on service X?" | Runbooks/Tickets Index | Metadata-rich tickets | Exact + Recency bias | Hourly | Update freq + Domain separation |
| 3 | **How-to/Conceptual** | "Explain RAG indexing" | Knowledge Base Index | Long docs, PDFs | Semantic + Dense | Weekly batch | Data types + Search strategy |
| 4 | **Latest Status** | "Current outage status?" | Incident Index | Time-sliced 7-30d | Recency weighted | Real-time stream | Update freq + Recency needs |
| 5 | **Code Question** | "Where is retry logic?" | Code Index | Syntax-aware code | Symbol filters | On commit | Data types + Specialized search |
| 6 | **Structured Metrics** | "What was Q4 churn?" | SQL/Structured Backend | Tables, metrics | SQL queries | ETL pipeline | Search strategy + Structured data |

> 💡 **Key Insight:** Not all queries are equal. A single vector index is a bottleneck —
> intent-based routing ensures each query hits the right index with the right search strategy.
