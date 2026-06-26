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
