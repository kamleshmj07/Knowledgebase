# 04_2_ai_agents_and_systems_IK.md

## Core Definition
An **AI Agent** is an autonomous system built on top of a foundational Large Language Model (LLM) that can sense its environment, interpret information, and execute a strategic sequence of actions to achieve a specific goal with minimal human intervention.

---

## Key Capabilities
To function effectively and autonomously, an AI agent relies on four foundational capabilities:

* **Understand Instructions:** Parses complex, high-level objectives expressed in natural language and translates them into a coherent execution plan.
* **Make a Function Call:** Converts human-readable intent into structured data inputs (such as JSON parameters) required to trigger external software, code blocks, or APIs.
* **Take Actions:** Directly interacts with its environmental tools—such as executing web searches, updating databases, writing files, or sending communications.
* **Adapt Behavior Based on Feedback:** Continuously evaluates the success or failure of its previous actions (via execution logs, error messages, or environmental responses) and recalibrates its strategy on the fly.

---


## Agentic AI Systems (Goal-Driven)

**Goal** → **Agent (LLM)** → **Reason** → **Act (APIs · DB · Code)** → **Observe** → **Adapt & Re-plan**
                                                    ↑
                                            **MCP Toolbox**

MCP Toolbox is placed under the **Act** step since MCP servers expose APIs, DBs, and code execution tools that agents invoke during the action phase.
---

> With execution responsibility delegated to agents, the focus shifts to what they can automate.

