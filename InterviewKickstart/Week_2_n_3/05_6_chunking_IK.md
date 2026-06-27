## Chunking Strategies for RAG

### What is Chunking?

Chunking is the process of breaking large documents into smaller, manageable pieces
before embedding and storing them in a vector database.

**Why it matters:**
- LLMs have a finite context window — you can't pass an entire knowledge base
- Smaller chunks = more precise retrieval (only relevant pieces are fetched)
- Chunk quality directly determines RAG answer quality

**Two key parameters to tune:**
- `chunk_size` — how large each chunk is (in tokens or characters)
- `chunk_overlap` — how much consecutive chunks share (~10–20%) to avoid losing context at boundaries

```
[ Raw Document ] ──► [ Chunker ] ──► [ Chunk 1 ][ Chunk 2 ][ Chunk 3 ] ──► [ Embeddings ] ──► [ Vector DB ]
```

---

## Chunking Strategies

---

### 1) Fixed-Size Chunking

Split text into uniform segments based on a pre-defined number of characters, words, or tokens.

```
|← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  chunk_size  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ →|

"Artificial intelligence is transforming technology and shaping the future."

┌──────────────────────────────┬──────────────────────────────────────┐
│          Chunk 1             │              Chunk 2                 │
│  "Artificial intelligence    │  overlap + "and shaping the future." │
│   is transforming"           │                                      │
└──────────────────────────────┴──────────────────────────────────────┘
                          ↑ Overlap region shared between chunks
```

**Parameters:** `chunk_size`, `chunk_overlap` (10–20%)

| Pros | Cons |
|---|---|
| Simple and fast | May split mid-sentence or mid-idea |
| Predictable output size | Ignores semantic meaning |

**LangChain:** `CharacterTextSplitter`, `TokenTextSplitter`

---

### 2) Semantic Chunking

Segment the document based on meaningful units (sentences, paragraphs), then group
segments together as long as cosine similarity stays high. Start a new chunk when
similarity drops drastically.

```
Document
   │
   ▼
Segment into sentences/paragraphs
   │
   ▼
[ Initial first chunk ]
   │
   ├──► Keep adding segments while cosine similarity is HIGH
   │
   └──► Cosine similarity drops? ──► Start new chunk
                                          │
                                          ▼
                                  [ Final chunks ]
```

**Example output:**
```
Chunk 1: "Artificial intelligence is transforming industries by automating
          processes, enhancing decision-making, and providing insights through data analysis."

Chunk 2: "Machine learning, a subset of AI, enables systems to learn and improve
          from experience without explicit programming."

Chunk 3: "Deep learning, a branch of machine learning, uses neural networks with
          multiple layers to model complex patterns in data."
```

| Pros | Cons |
|---|---|
| Respects semantic boundaries | Slower (requires embedding each sentence) |
| Higher retrieval precision | Variable chunk sizes |

**LangChain:** `SemanticChunker` (with OpenAI embeddings)

---

### 3) Recursive Chunking

First split by inherent separators (`\n\n`, `\n`, `.`, ` `). Then recursively
split any chunk that exceeds the `chunk_size` limit until all chunks fit.

```
Document
   │
   ▼
Segment by paragraphs / thematic sections
   │
   ▼
Select a segment ──► size > chunk_size limit?
                              │           │
                             YES          NO
                              │           │
                              ▼           └──► ✅ Keep as-is
                     Split further
                     recursively ──────────────────────────┐
                              │                            │
                              └──────────► Re-check size ──┘
```

**Example output:**
```
Paragraph 1 → Split into sentences if too large:
  Chunk 1: "Artificial intelligence is transforming industries..."
  Chunk 2: "Machine learning, a subset of AI..."
  Chunk 3: "Deep learning, a branch of machine learning..."

Paragraph 2 → Fits within limit, kept as-is:
  Chunk 4: "AI is also improving natural language processing..."
```

| Pros | Cons |
|---|---|
| Respects natural separators | More complex to configure |
| Avoids splitting mid-paragraph | Still size-based at leaf level |

**LangChain:** `RecursiveCharacterTextSplitter` ← most commonly used in practice

---

### 4) Document Structure-Based Chunking

Use the document's inherent structure (headings, sections, paragraphs) as chunk
boundaries. Maintains structural integrity by aligning with logical sections.

```
Document Structure                     Chunks
┌──────────────┐                ┌──────────────────────┐
│ Title        │                │ Chunk 1: Title       │
│ Introduction │  ──────────►   │ Chunk 2: Introduction│
│ Section #1   │                │ Chunk 3: Section #1  │
│ Section #2   │                │ Chunk 4: Section #2  │
│ Conclusion   │                │ Chunk 5: Conclusion  │
└──────────────┘                └──────────────────────┘
                   * Merge with recursive chunking if any section is too large
```

**Example output:**
```
Chunk 1: "Title: The Role of Artificial Intelligence in Modern Education"
Chunk 2: "Introduction — AI is reshaping education by providing personalized learning..."
Chunk 3: "Section 1: Personalized Learning — AI enables customization of educational content..."
Chunk 4: "Section 2: Administrative Automation — From grading to scheduling..."
Chunk 5: "Conclusion — The integration of AI in education holds the promise..."
```

| Pros | Cons |
|---|---|
| Preserves logical document flow | Requires structured input (Markdown, HTML, PDF with headers) |
| Great for manuals, docs, reports | Unstructured text has no headers to split on |

**LangChain:** `MarkdownHeaderTextSplitter`, `HTMLHeaderTextSplitter`

---

### 5) LLM-Based Chunking

Use an LLM itself to decide how to chunk the document into semantically isolated,
meaningful pieces — going beyond simple heuristics.

```
[ Document ] ──► [ LLM ] ──► [ Final Chunks ]
                  (prompted to generate
                   semantically isolated chunks)
```

- The LLM understands context and meaning, not just character counts
- Produces the most semantically accurate chunks
- Combines the best of all approaches above

| Pros | Cons |
|---|---|
| Highest semantic accuracy | Expensive (LLM call per document) |
| Context-aware boundaries | Slow for large corpora |
| No heuristics needed | Non-deterministic output |

---

## Strategy Comparison

| Strategy | Split By | Semantic Awareness | Speed | Best For |
|---|---|---|---|---|
| **Fixed-size** | Token/char count | ❌ | ⚡ Fast | Quick prototypes |
| **Semantic** | Embedding similarity | ✅ High | 🐢 Slow | Dense prose |
| **Recursive** | Separators + size | 🟡 Partial | ⚡ Fast | General purpose |
| **Structure-based** | Doc headers/sections | 🟡 Structural | ⚡ Fast | Docs, manuals, wikis |
| **LLM-based** | LLM reasoning | ✅ Highest | 🐢 Slowest | High-accuracy pipelines |

> 💡 **In practice:** `RecursiveCharacterTextSplitter` is the most common starting point.
> Upgrade to semantic or LLM-based chunking when retrieval precision matters most.
