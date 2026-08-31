# AI Agent Architecture: Agents as Distributed Systems (Reference: https://www.youtube.com/watch?v=hD9-V56FNRI)

**Core thesis:** Once an AI agent can call tools, hit APIs, and write to databases, it stops being "just a model" and starts behaving like a distributed system. It needs the same engineering discipline backend teams already use for microservices — idempotency, retries, circuit breakers, scoped permissions, observability — layered around the model's probabilistic decision-making.

---

## 1. Why Agents Became Distributed Systems

| Chatbot era | Agentic era |
|---|---|
| Prompt in → text out | Prompt in → plan → tool calls → real side effects |
| No side effects | Can write to DBs, call APIs, trigger workflows |
| Worst case: wrong answer | Worst case: wrong **action** (deleted data, bad refund) |
| Boundary = the model | Boundary = every system the agent can reach |

The failure surface moved from "the model said something wrong" to "the model *did* something wrong" — which is a systems problem, not just a model-quality problem.

## 2. Cautionary Tales (Why This Matters)

- **Replit agent deleted a production database** → missing scoped authority + no robust, easy rollback/backup.
- **Air Canada chatbot issued an incorrect refund** → no authoritative source-of-truth retrieval; the agent acted on stale/incorrect policy data.

Both are systems-design failures that good architecture would have contained.

## 3. The Agent as a Probabilistic Coordinator

Traditional backend orchestrators coordinate multi-step workflows **deterministically** — the paths are known in advance (a fixed decision tree). An AI agent coordinates the same kind of multi-step workflow, but **probabilistically** — the space of possible actions is much larger and less predictable.

**Implication:** you can't rely on the agent's own judgment as the safety mechanism. You need deterministic guardrails wrapped around a probabilistic core.

## 4. The Agent Loop & Where It Breaks

```
        ┌───────────────────────────────────────────────┐
        │                  AGENT LOOP                    │
        └───────────────────────────────────────────────┘
                │
                ▼
        ╔═══════════════╗   pulls context — risk: stale/wrong data
        ║     PLAN      ║
        ╚═══════════════╝
                │
                ▼
        ╔═══════════════╗   calls tools/APIs/DBs — risk: real side effects
        ║      ACT      ║
        ╚═══════════════╝
                │
                ▼
        ╔═══════════════╗   reads results — risk: partial/misread results
        ║    OBSERVE    ║
        ╚═══════════════╝
                │
                ▼
        ╔═══════════════╗   writes state — risk: persists bad data
        ║    PERSIST    ║
        ╚═══════════════╝
                │
                ▼
        ╔═══════════════╗   chooses next step — risk: wrong action / retry storm
        ║     DECIDE    ║
        ╚═══════════════╝
                │
                └────────────► back to PLAN
```

**Design rule:** persist every step (plan, action, observation, decision). Without a full record, you can't diagnose *where* an agent went wrong, and you can't build a safe "undo."

## 5. Tool Calls Are Just RPCs

A tool call is a thin wrapper around an API, database, or queue — so it inherits every classic remote-call failure mode:

- Network delay / timeout
- Duplicate delivery (the request gets sent twice)
- "Phantom success" — the server actually wrote the data, but the client received an error

**Key insight:** a timeout means *unknown*, not *failed*. If an agent treats every timeout as "it didn't happen" and retries blindly, you get duplicate side effects (e.g., a customer refunded twice).

## 6. Idempotency Is Non-Negotiable

- Every mutating tool call should carry a **request ID / idempotency key**.
- Tools should support a **status lookup** so the agent can check "did this already succeed?" before retrying.
- This single pattern prevents most duplicate-side-effect incidents.

## 7. Controlling Retries (No Retry Storms)

Agents default to retrying on failure. Left unbounded, this becomes a retry storm that can cascade into a downstream outage. Guardrails:

- Max turn budget
- Max spend / cost ceiling
- Max parallel calls (limit fan-out)
- Exponential backoff between retries

## 8. Memory Is State, Not Just "Context"

- **Short-term memory:** the current thread — scoped to a single execution.
- **Long-term memory:** project files, system prompt, databases, cache layers.

The moment "context" can influence an action, it stops being harmless context and becomes **state** — and state can go stale, conflict with the source of truth, or corrupt future actions.

**Treat memory like a cache:** attach provenance to it, and invalidate it whenever the underlying source of truth changes.

## 9. Multi-Step Transactions Need Compensation

Agents often chain actions across system boundaries — e.g., update a ticket → email a customer → update the CRM. Partial failure is the norm in distributed workflows, not the exception.

**You need a compensating action defined in advance for every irreversible step** — similar to the saga pattern used in distributed transactions. Example: if the agent sends an incorrect email, the defined compensation might be an automatic correction/apology email.

## 10. Circuit Breakers

When a downstream dependency is unhealthy or saturated, a circuit breaker should stop the agent from calling it further. This protects the dependency and prevents cascading failure across the system.

## 11. Least-Privilege Access

The default instinct is to over-grant permissions ("just give it full read/write on the table so it can finish the task"). This is exactly backwards:

- Separate **read** and **write** credentials.
- Maintain an explicit **allow-list** of tools the agent may call.
- A capable model with excessive privilege is what turns a small mistake into a large incident.

## 12. Scoped Human Approvals

An approval should never be a blanket yes. Bind every approval to:

- The specific **action** and **parameters**
- **Timestamp**
- **Actor** (who approved)
- **Expiration**

Example: approval for a $30 refund must never silently cover a later $300 refund.

## 13. Observability

Logs alone can't reconstruct *why* an agent did something. Full traces should capture:

- Model/version invoked
- Prompt sent
- Tool calls and parameters
- Tool responses and errors
- Retrieved context
- Writes/state changes made
- Approvals obtained

## Key Takeaway

Better models reduce the *frequency* of mistakes — but they can't eliminate network failures, stale data, or adversarial input. Real safety comes from systems design:

- Tool contracts (clear schemas + idempotency)
- Defined source-of-truth rules for conflicting state
- Rate limits and retry policies
- Least-privilege permissions
- End-to-end tracing
- Defined recovery/compensation paths

**The question to ask when designing any agent:** *What does the system let it do when it's wrong?*
