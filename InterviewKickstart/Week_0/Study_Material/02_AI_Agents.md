# AI Agents

---

## What is an AI Agent?

An AI Agent is an autonomous system built on an LLM that can **sense**, **plan**, and **act**
to achieve a goal — with minimal human intervention.

```
Agent = (Prompt + Tools + Memory) × LLM
```

**Core Capabilities:**

| Capability | What it does |
|---|---|
| **Understand** | Reads a high-level goal and breaks it into steps |
| **Call Functions** | Converts intent into structured inputs (e.g. JSON) to trigger APIs or tools |
| **Take Actions** | Runs searches, writes files, updates DBs, sends messages |
| **Adapt** | Reads feedback (errors, logs) and adjusts its plan on the fly |

---

## Agentic AI System Flow

```
Goal → Agent (LLM) → Reason → Act (APIs · DB · Code) → Observe → Adapt & Re-plan
                                       ↑
                               MCP Toolbox
```

MCP Toolbox sits under **Act** — MCP servers expose APIs, DBs, and code execution tools that agents invoke during the action phase.

---

## Agentic Workflows vs. Autonomous Agents

| | **Autonomous** | **Workflow** |
|---|---|---|
| **Orchestration** | LLM (dynamic) | Code (fixed pipeline) |
| **Flexibility** | High — adapts on the fly | Low — predefined steps |
| **Predictability** | Lower → lower observability | Higher |
| **Error Handling** | LLM reasons about it | Developer codes it |
| **LLM Calls** | N (unknown ahead of time) | Fixed (known in advance) |
| **Best For** | Open-ended tasks | Well-defined processes |

**Agentic Workflow** — developer defines the flow; LLM & tool control is programmatically set:
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

**Autonomous Agent** — the model decides what to do next at runtime:
```
              ┌──────────────────────────┐
              │                          │
In ──► [ LLM Call ] ──action──► [ Tool ] ──► Out
          ▲                        │
          └──────── feedback ──────┘
```

> In practice, most production systems are **hybrids**: a workflow defines the high-level stages, but individual stages may use autonomous reasoning within a bounded scope.

---

## LLM as Reasoning Core

In an agentic system, the LLM stops being a chatbot and becomes the **Reasoning Core** — the central controller that:

- **Parses** user intent from ambiguous natural language → *Intent Parsing*
- **Decomposes** complex problems into steps → *Problem Decomposition*
- **Synthesizes** data returned from tools → *Synthesis*

```
          INPUTS & PERCEPTION
  Audio · Vision · Text · Data Feeds
                   │
  ┌────────────────▼─────────────────┐
  │         MEMORY & CONTEXT         │
  │  Knowledge Base                  │
  │  Conversation History            │
  │  Long-Term Memory                │
  └────────────────┬─────────────────┘
                   │
            ┌──────▼──────┐
            │     LLM     │
            │  Reasoning  │
            │    Core &   │
            │ Controller  │
            └──────┬──────┘
                   │
  ┌────────────────▼─────────────────┐
  │         TOOLS & ACTIONS          │
  │  Actuation · Web Search          │
  │  Code Execution · Communication  │
  └────────────────┬─────────────────┘
                   │
       PLANNING & DECISIONING
  ┌─────────────────────────────────┐
  │  Goal Setting → Strategy Gen    │
  │  Task Decomposition ← Self-     │
  │                      Correction │
  └─────────────────────────────────┘
```

---

## The ReAct Loop

**Re**asoning + **Act**ing — the standard loop for modern agents:

- **Thought** — Analyze the request → *Which tool to call?*
- **Action** — Call the tool → *Execute*
- **Observation** — Read the tool's output → *Observe*
- **Repeat** — Update thought process and loop until final answer

```
            [ User Query ]
                  │
      ┌───────────▼────────────┐
      │      ReAct Agent Loop  │
      │                        │
      │     [ Reason (think) ] ◄──────────────┐
      │             │                         │
      │   [ Decide if tool needed ]           │
      │        │            │                 │
      │       yes           no                │
      │        │            │                 │
      │ [ Call Tool ]  [ Compose Final Answer]│
      │        │            │                 │
      │ [ Observe output ]  [ Done ]          │
      │        │                              │
      │ [ Accumulate evidence / update state ]│
      │        └──────────────────────────────┘
      └────────────────────────┐
                               │
                        [ Final Answer ]
```

---

## Memory

| | **Short-Term (Context)** | **Long-Term (Vector Store)** |
|---|---|---|
| **Analogy** | RAM | Hard Drive |
| **Holds** | Conversation history, current prompt, recent tool outputs | Vast information via Vector DB (RAG) |
| **Retrieval** | Everything in context window | Only relevant "memories" via semantic similarity |
| **Limit** | Context window size (e.g., 128k tokens) | Infinite persistence |
| **Cleared** | When session ends | Persists |

**Vector Store options:** Weaviate · Chroma · pgvector · Pinecone

---

## Planning & Reasoning

Agents use planning techniques to break down complexity and improve reliability:

| Technique | Description |
|---|---|
| **Chain of Thought** | Stepping through logic explicitly |
| **Tree of Thoughts** | Exploring multiple possibilities before committing |
| **Reflection** | Reviewing past actions to catch errors |

---

## Multi-Agent Systems

| **Specialization** | **Orchestration** | **Autonomy** |
|---|---|---|
| Swarms of specialized agents (Coder, Designer, Writer) collaborate | "Manager" agents break down projects and assign tasks to "worker" agents | Agents run continuously in the background |

```
[ Specialization ] ──► [ Orchestration ] ──► [ Autonomy ]
  (Sub-agents)            (Manager)            (Always-on)
```

**Frameworks:** CrewAI · Google ADK · LangGraph · AutoGen

---

## Agentic Design Patterns

Building blocks for LLM systems that go beyond single prompt-response interactions — composable structures to orchestrate reasoning, decisions, tools, and control flow.

```
                    ┌─────────────────┐
                    │ Design Patterns │
                    └────────┬────────┘
                             │
      ┌──────────┬───────────┼───────────┬──────────────┐
      ▼          ▼           ▼           ▼              ▼
┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐
│Reflection│ │ Routing │ │ Tool Use │ │ Planning │ │ Multi-Agent │
└──────────┘ └─────────┘ └──────────┘ └──────────┘ └─────────────┘
```

---

## Worked Examples

### Example 1: Meeting Scheduling Agent

**System Prompt:** *"You are a scheduling assistant helping user book meetings"*  
**Tools:** `find_next_free_slot(from_date)`, `book_slot(start_time, duration)`

**User:** `"book 30 mins on Feb 16"`

```
THINK:  I need to find next available slot for Feb 16.
ACT:    find_next_free_slot("Feb 16") → 9am
OBSERVE: Next available slot is 9am.

THINK:  Now I need to book the 9am slot for 30 mins.
ACT:    book_slot(9am, 30 mins) → true
OBSERVE: Meeting booked, task is complete.
```

---

### Example 2: Travel Assistant Agent

**System Prompt:** *"You are a travel assistant helping user with their questions"*  
**Tools:** `get_weather(location)`

```
User  ──① "I am flying to Paris today. Should I carry an umbrella?"
         │
Agent ──② prompt + tool definitions + user message ──► LLM
         │
LLM   ──③ get_weather("Paris") ──► Agent
         │
Agent ──④ prompt + message history + tool result: "Paris, 14°C, rain expected" ──► LLM
         │
LLM   ──⑤ "Yes, bring an umbrella! Rain is expected today." ──► Agent
         │
Agent ──⑥ "Yes, bring an umbrella! ☂️" ──► User
```

> **LLM as Judge** — The LLM evaluates tool results and decides whether the answer is sufficient or another tool call is needed.

---

## References
- [LangGraph — Workflows vs Agents](https://docs.langchain.com/oss/javascript/langgraph/workflows-agents)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- [ReAct: Synergizing Reasoning and Acting in Language Models — arXiv](https://arxiv.org/abs/2210.03629)
- [AWS — Customize agent workflows with Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [NVIDIA — Introduction to LLM Agents](https://developer.nvidia.com/blog/introduction-to-llm-agents/)
