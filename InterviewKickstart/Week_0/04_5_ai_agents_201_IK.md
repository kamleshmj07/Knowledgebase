## The Cognitive Engine — More Than Just Text

> Domain + Data → AI/w

In an agentic system, the LLM stops being a simple chatbot and becomes the **Reasoning Core**.
It acts as the central controller that:

- **Parses** user intent from ambiguous natural language → *Intent Parsing*
- **Decomposes** complex problems into steps → *Problem Decomposition*
- **Synthesizes** data returned from those tools → *Synthesis*

---

## LLM as Reasoning Core & Controller
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

**Re**asoning + **Act**ing

The standard loop for modern agents is **ReAct**:

- **Thought** — The agent analyzes the request → *Which tool to call?*
- **Action** — It decides which tool to call → *Execute the tool*
- **Observation** — It reads the tool's output → *Observe*
- **Repeat** — It updates its thought process and loops

> This cycle continues until the final answer is found.

---

## ReAct Agent Loop — Flow

```
                [ User Query ]
                      │
          ┌───────────▼────────────┐
          │      ReAct Agent Loop  │
          │                        │
          │     [ Reason (think) ] ◄──────────────┐
          │             │                         │
          │   [ Decide if tool needed ]            │
          │        │            │                  │
          │       yes           no                 │
          │        │            │                  │
          │ [ Call Tool via  [ Compose        │
          │   Tool Executor ]  Final Answer ] │
          │        │            │                  │
          │ [ Observe tool     [ Done ]            │
          │    output ]                            │
          │        │                               │
          │ [ Accumulate evidence / update state ] │
          │        └───────────────────────────────┘
          └────────────────────────┐
                                   │
                            [ Final Answer ]
```

---

## Single Agent Model

> A single agent owns:
> - Model + policy
> - Airline tools
> - Iterates: **think → act → observe** until it can answer confidently

---

## Memory: Short vs. Long Term

| | **Short-Term (Context)** | **Long-Term (Vector Store)** |
|---|---|---|
| **Analogy** | RAM | Hard Drive |
| **Description** | Holds immediate conversation history, current prompt, and recent tool outputs | Uses Vector Databases (RAG) to store vast amounts of information |
| **Retrieval** | Everything in context window | Only relevant "memories" via semantic similarity to current task |
| **Limit** | Context window size (e.g., 128k tokens) | Infinite persistence |
| **Limitation** | Cleared when the session ends | — |

---

## Long-Term Memory: Vector Store Options

> Weaviate · Chroma · pgvector · Pinecone

---
## Planning & Reasoning

### Breaking Down Complexity

Agents cannot solve complex tasks in one shot.
They use planning techniques to improve reliability.

| Technique | Description |
|---|---|
| **Chain of Thought** | Stepping through logic explicitly |
| **Tree of Thoughts** | Exploring multiple possibilities before committing |
| **Reflection** | Reviewing past actions to catch errors |

---
## The Future: Multi-Agent Systems

| **Specialization** | **Orchestration** | **Autonomy** |
|---|---|---|
| Instead of one generalist, swarms of specialized agents (Coder, Designer, Writer) will collaborate. | "Manager" agents break down huge projects and assign tasks to "worker" agents. | Agents run continuously in the background, optimizing workflows without human input. |
| *Sub-agents* | *Manager* | |

---

## Flow

```
[ Specialization ] ──► [ Orchestration ] ──► [ Autonomy ]

(Sub-agents)            (Manager)            (Always-on)
```

---

## Frameworks

> CrewAI · Google ADK · LangGraph · AutoGen
---

## Agentic Design Patterns

- Agentic Design Patterns are the **building blocks for LLM systems** that go beyond single prompt-response interactions.
- They use composable structures to orchestrate reasoning, decisions, tools, and control flow.
- By replacing hard-coded logic with system structure, these patterns enable reliable adaptation and scaling — from simple assistants to autonomous, goal-driven agents.

---

## Pattern Taxonomy

```
                        ┌─────────────────┐
                        │ Design Patterns │
                        └────────┬────────┘
                                 │
          ┌──────────┬───────────┼───────────┬──────────────┐
          │          │           │           │              │
          ▼          ▼           ▼           ▼              ▼
   ┌────────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐
   │ Reflection │ │ Routing │ │ Tool Use │ │ Planning │ │ Multi- Agent  │
   │  Pattern   │ │ Pattern │ │ Pattern  │ │ Pattern  │ │ Pattern       │
   └────────────┘ └─────────┘ └──────────┘ └──────────┘ └───────────────┘

```
---



---
## References

- [Customize agent workflows with advanced orchestration techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [ReAct: Synergizing Reasoning and Acting in Language Models — arXiv](https://arxiv.org/abs/2210.03629)
- [Intro to LLM agents](https://developer.nvidia.com/blog/introduction-to-llm-agents/)

