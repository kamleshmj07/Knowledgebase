# Part 1: Template and Do's vs Don'ts

**“The only Agentic AI project template you should ever use.”**

**Part 1: Description**

**Part 2: Sample Readme Code**

**Part 1**

---

# **🧠 Agentic AI Project – Final Detailed Template**

**Goal:**  
Make it immediately clear **what problem the agent solves, why an agent is required, how it thinks, and how success is measured**.

---

## **1️⃣ Project Title & Value Proposition**

**Format:**

*Agent type \+ primary user \+ outcome*

**Example:**

Autonomous Incident Triage Agent for SRE teams, reducing MTTR by 30%

---

## **2️⃣ Background & Problem Context**

* Real-world context where this problem appears  
* Who experiences the pain and how frequently  
* Why this problem becomes hard at scale  
* What breaks with manual processes or simple automation

Avoid generic AI framing. This should read like a real operational problem.

---

## **3️⃣ Target User & Job To Be Done (JTBD)**

* **Primary user persona** (role, environment)  
* **Secondary users** (if any)  
* Clear Job To Be Done

**Example format:**

* **Primary User:** Support Operations Manager  
* **JTBD:** Accurately classify and route incoming tickets within SLA without manual intervention.

---

## **4️⃣ Why an Agentic Approach (Very Important)**

Explicitly justify:

* Why scripts, workflows, or chatbots are insufficient  
* Where reasoning, planning, or autonomy is required  
* What decisions the agent must make dynamically

This section is a hard requirement. If this is weak, the project is weak.

---

## **5️⃣ Agent Role, Scope & Autonomy Level**

Define clearly:

* What the agent owns end-to-end  
* Where humans intervene  
* What actions are restricted

**Example:**

* Agent autonomously plans and executes classification and routing  
* Human approval required for escalations and customer-facing actions

---

## **6️⃣ Agent Architecture & Components**

Break the system into **thinking and execution units**.

### **a) Planner / Decision Layer**

* How tasks are decomposed  
* Static vs dynamic planning

### **b) Executors / Sub-Agents**

* Individual responsibilities  
* Tools or APIs used

### **c) Memory**

* Short-term (conversation / session)  
* Long-term (vector DB, logs, history)

### **d) Orchestration Logic**

* Control flow  
* Retry logic  
* Failure handling

Diagrams are encouraged but not mandatory.

---

## **7️⃣ End-to-End Agent Workflow**

Describe the lifecycle **step-by-step**:

1. Input ingestion  
2. Context extraction  
3. Planning / decomposition  
4. Tool execution  
5. Validation or self-check  
6. Output generation  
7. Escalation or fallback (if needed)

This should read like a **trace of the agent’s thinking**.

---

## **8️⃣ Tools, Models & Stack (With Rationale)**

For each major component:

* What tool/model is used  
* Why it was chosen  
* What role it plays in the system

Listing tools without justification is considered incomplete.

---

## **9️⃣ Evaluation Strategy & Metrics**

Define how success is measured:

* Accuracy or task success rate  
* Latency  
* Cost per run  
* Human intervention rate  
* Known false positives / negatives

Even approximate metrics are acceptable if reasoning is clear.

---

## **🔟 Guardrails, Trust & Safety**

Explain:

* Where the agent is allowed to act  
* Where it must stop  
* How users can override decisions  
* Logging and observability

This section is critical for PMs and EMs.

---

## **1️⃣1️⃣ Failure Modes & Tradeoffs**

* Known edge cases  
* Where the agent fails or becomes unreliable  
* Tradeoffs between accuracy, cost, and speed  
* Constraints intentionally accepted

Honesty here increases credibility.

---

## **1️⃣2️⃣ Results, Learnings & Insights**

* What worked better than expected  
* What failed initially  
* Surprising agent behavior  
* Key system or product learnings

This should feel like a **postmortem**, not marketing.

---

## **1️⃣3️⃣ Future Improvements & Iteration Plan**

* What v2 would change  
* What would be needed to scale  
* Additional agents, tools, or controls planned

---

## **1️⃣4️⃣ Demo & Artifacts**

* Live demo link or video walkthrough  
* Architecture diagram (optional)  
* Sample logs or traces (optional)

---

## **1️⃣5️⃣ Role-Based Signal (Mandatory)**

Explicitly state what this project demonstrates:

* **For PMs:** problem framing, metrics, tradeoffs, trust  
* **For EMs:** system design, orchestration, scalability  
* **For SWEs:** correctness, modularity, robustness

---

# **✅ Do’s and ❌ Don’ts (Evaluation-Ready Table)**

| Area | ✅ Do | ❌ Don’t |
| ----- | ----- | ----- |
| Problem | Describe a real, scaled pain | Pick a toy or generic problem |
| Agent Justification | Explain why an agent is needed | Use agents “because AI” |
| Autonomy | Clearly define boundaries | Claim full autonomy blindly |
| Architecture | Decompose into planner/executor/memory | Treat agent as a single prompt |
| Workflow | Show step-by-step reasoning | Jump straight to output |
| Tools | Justify every major tool | List tools as buzzwords |
| Metrics | Define how success is measured | Say “works well” |
| Safety | Add guardrails and overrides | Ignore trust and control |
| Failure Modes | Admit limitations | Claim no failures |
| Learnings | Share insights and tradeoffs | Only highlight positives |
| PM Signal | Focus on decisions and impact | Over-index on code |
| EM Signal | Explain orchestration and scale | Stay at surface level |
| SWE Signal | Show robustness and structure | Rely on demos only |

---

# Part 2: Sample Code

---

Project Name  
(Replace this with your project’s name)

Overview  
This project provides a brief description of its purpose, the problem it addresses, and the reasons behind its existence. Keep this section concise and clear so that anyone visiting the repository immediately understands its purpose.

Key Features  
• Feature 1 – Short explanation of what it does  
• Feature 2 – Short explanation of what it does  
• Feature 3 – Short explanation of what it does

Tech Stack  
• Programming Language or Framework  
• Backend or Frontend framework (if applicable)  
• Database (if applicable)  
• Tools, libraries, or platforms used

Project Structure

project-root  
│── src  
│ ├── main file  
│ ├── utilities folder  
│── tests  
│── README file  
│── dependency file

Installation Steps

1. Clone the repository from GitHub  
2. Navigate to the project directory  
3. Install required dependencies

Usage Instructions  
Explain how to run or use the project after installation.  
Mention the main command or steps required to start the application.

Example Input  
Provide a sample input or action performed by the user.

Example Output  
Provide the expected output or result.

Running Tests  
Explain how to run tests for this project, if applicable.

Configuration  
If the project uses environment variables or configuration files, explain what needs to be set up before running the project.

Future Improvements  
• Planned feature or enhancement 1  
• Planned feature or enhancement 2  
• Planned feature or enhancement 3

Contributing Guidelines  
Explain how others can contribute to this project.  
Example: fork the repository, create a new branch, make changes, and submit a pull request.

License  
Specify the license under which the project is distributed.

Author  
Name  
GitHub profile link  
LinkedIn or other professional profile link

---

