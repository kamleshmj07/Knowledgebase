## Text Embeddings

### What is an Embedding?

Text is converted into a **vector** (list of numbers) that captures semantic meaning.
Semantically similar texts produce numerically similar vectors.

text1 ──► [ Embedding Model ] ──► emb1 [ vector ]

text2 ──► [ Embedding Model ] ──► emb2 [ vector ]

> The same embedding model must be used for both indexing and querying
> to ensure vectors live in the same space.

---

### Measuring Similarity: Cosine Similarity

The angle **θ** between two vectors determines how similar they are.

```
emb1
    ↑
    │ θ
    │╱
    └──────► emb2
```

| Scenario | cos(θ) | Meaning |
|---|---|---|
| `cos(0°)` | **1** | Identical meaning — perfect match |
| `cos(90°)` | **0** | No relation — completely different |
| `cos(180°)` | **-1** | Opposite meaning |

### Formula
similarity = cos(θ) = (emb1 · emb2) / (|emb1| × |emb2|)

> In RAG, the top-k chunks with the **highest cosine similarity**
> to the query embedding are retrieved and passed to the LLM.


