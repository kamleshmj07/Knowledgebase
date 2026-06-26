
## What is an AI Agent?

An AI Agent is an autonomous system built on an LLM that can **sense**, **plan**, and **act**
to achieve a goal — with minimal human intervention.

---

## Core Capabilities

| Capability | What it does |
|---|---|
| **Understand** | Reads a high-level goal and breaks it into steps |
| **Call Functions** | Converts intent into structured inputs (e.g. JSON) to trigger APIs or tools |
| **Take Actions** | Runs searches, writes files, updates DBs, sends messages |
| **Adapt** | Reads feedback (errors, logs) and adjusts its plan on the fly |

---

## Agentic AI Systems (Goal-Driven)

**Goal** → **Agent (LLM)** → **Reason** → **Act (APIs · DB · Code)** → **Observe** → **Adapt & Re-plan**
                                                    ↑
                                            **MCP Toolbox**

MCP Toolbox is placed under the **Act** step since MCP servers expose APIs, DBs, and code execution tools that agents invoke during the action phase.
---

> With execution responsibility delegated to agents, the focus shifts to what they can automate.


Agent = (Prompt + Tools + Memory) * LLM


---

## Agentic Workflows vs Autonomous Agents

| | **Agentic Workflows** | **Autonomous Agents** |
|---|---|---|
| **Control** | LLM & tool control flow is programmatically defined | The model dynamically decides what to do next |
| **Nature** | Deterministic | Dynamic |

---

## Agentic Workflows

```
                        ┌─────────┐
                   ┌──► │ Agent A │──┐
                   │    └─────────┘  │
                   │    ┌─────────┐  │    ┌─────────────┐
In ──► Orchestrator├──► │ Agent B │──├──► │ Synthesizer │──► Out
                   │    └─────────┘  │    └─────────────┘
                   │    ┌─────────┐  │
                   └──► │ Agent C │──┘
                        └─────────┘
```

---

## Autonomous Agents

```
                  ┌──────────────────────────┐
                  │                          │
In ──► [ LLM Call ] ──action──► [ Tool ] ──► Out
              ▲                      │
              └──────── feedback ────┘
```

---

## Key Insight

> In **Agentic Workflows**, the developer defines the flow.
> In **Autonomous Agents**, the LLM decides the next step at runtime.

---

## Workflows vs. Autonomous Agents

| | **Autonomous** | **Workflow** |
|---|---|---|
| **Orchestration** | LLM (dynamic) | Code (fixed pipeline) |
| **Flexibility** | High (adapts on the fly) | Low (predefined steps) |
| **Predictability** | Lower → lower observability | Higher |
| **Error Handling** | LLM reasons about it | Developer codes it |
| **LLM Calls** | N (unknown ahead of time) | Fixed (known in advance) |
| **Best For** | Open-ended tasks | Well-defined processes |

---

> 💡 **In practice:** Most production systems are hybrids: a workflow defines the high-level stages,
> but individual stages may use autonomous reasoning within a bounded scope.

---

## Example 1: Meeting Scheduling Agent

### Agent Setup

**System Prompt**
> "You are a scheduling assistant helping user book meetings"

**Tool Definitions**
```python
find_next_free_slot(from_date)
book_slot(start_time, duration)
```

---

### Agent Loop

```
START ──► [ LLM ] ──── Request Tool Call ────► [ Tool Executor ]
              ▲                                        │
              └──────────── Observe Response ──────────┘
                                   │
                                  END
```

---

### Execution Trace

**User:** `"book 30 mins on Feb 16"`

```
// START

// THINK
1. I need to find next available slot for Feb 16.
// ACT
2. find_next_free_slot("Feb 16") -> 9am
// OBSERVE
3. Okay, next available slot is 9am.

// THINK
4. Now I need to book the 9am slot for 30 mins.
// ACT
5. book_slot(9am, 30 mins) -> true
// OBSERVE
6. Meeting booked, task is complete.

// END
```

---

## Example 2: Travel Assistant Agent

### Agent Setup

**1. System Prompt**
> "You are a travel assistant helping user with their questions"

**2. Tool Definitions**
```python
get_weather(location)
```

**3. Message History** — passed with every LLM call

---

### Sequence Flow

```
You                         Agent                              LLM
 │                            │                                 │
 │──① "I am flying to Paris   │                                 │
 │    today. Should I carry   │                                 │
 │    an umbrella?"           │                                 │
 │                            │                                 │
 │                            │──② prompt + tool definitions ──►│
 │                            │    + user message               │
 │                            │                                 │
 │                            │◄──③ get_weather("Paris") ───────│
 │                            │                                 │
 │                            │──④ prompt + tool definitions ──►│
 │                            │    + message history            │
 │                            │    + tool result:               │
 │                            │    "Paris, 14°C, rain expected" │
 │                            │                                 │
 │                            │◄──⑤ "Yes, bring an umbrella!   │
 │                            │       Rain is expected today."  │
 │                            │                                 │
 │◄──⑥ "Yes, bring an        │                                 │
 │       umbrella! ☂️"         │                                 │
```

---

> 💡 **LLM as Judge** — The LLM evaluates tool results and decides
> whether the answer is sufficient or another tool call is needed.


## Reference

- [LangGraph — Workflows vs Agents](https://docs.langchain.com/oss/javascript/langgraph/workflows-agents)
- [Anthropic - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
