
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
