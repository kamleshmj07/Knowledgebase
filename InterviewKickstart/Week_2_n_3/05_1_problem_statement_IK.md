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
