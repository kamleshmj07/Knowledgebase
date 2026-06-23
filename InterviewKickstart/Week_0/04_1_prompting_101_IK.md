
## Prompt Components
* **Instruction:** A specific task or instruction you want the model to perform.
* **Context:** External information or additional context that can steer the model to better responses.
* **Input Data:** The input or question that we are interested to find a response for.

---

## N-Shot Prompting
*Note: "Shot" refers to an example (e.g., Zero example, one example, few examples).*

LLMs are instruction-tuned (LLMIT), meaning they are trained to expect an instruction, context, and input.

### 1. Zero-Shot or One-Shot
* Capable of performing some tasks in a "zero-shot" manner.
* The prompt won't contain examples or demonstrations.
* Instructs the model to perform a task without any additional examples to steer it.

### 2. Few-Shot Prompt
* For complex tasks, zero-shot may not be enough.
* Few-shot enables **in-context learning** where we provide demonstrations in the prompt.
* This steers the model to better performance.

---

## Chain-of-Thought (CoT) Prompting

**Example:**
> **Prompt:**
> The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
> A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
> 
> The odd numbers in this group add up to an even number: 17, 10, 19, 4, 8, 12, 24.
> A: Adding all the odd numbers (17, 19) gives 36. The answer is True.
> 
> The odd numbers in this group add up to an even number: 16, 11, 14, 4, 8, 13, 24.
> A: Adding all the odd numbers (11, 13) gives 24. The answer is True.
> 
> The odd numbers in this group add up to an even number: 17, 9, 10, 12, 13, 4, 2.
> A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.
> 
> The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
> A:

> **Model Answer:**
> Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.

---

## Zero-Shot CoT Prompting

### (a) Standard Zero-Shot
> **Q:** A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?
> **A:** The answer (arabic numerals) is
> ----------------
> **(Output)** 8 ❌

### (b) Zero-Shot CoT Activation
> **Q:** A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?
> **A:** Let's think step by step.
> ----------------
> **(Output)** There are 16 balls in total. Half of the balls are golf balls. That means that there are 8 golf balls. Half of the golf balls are blue. That means that there are 4 blue golf balls. ✅

---

## ReAct: Reason + Act

### CoT (Chain-of-Thought)
* **Pros:** Has shown that LLMs have reasoning capabilities.
* **Cons:**
  * Still lacks access to the external world.
  * Unable to update its knowledge, which can lead to issues like fact hallucination and error propagation.

### ReAct
* LLMs generate verbal reasoning traces **and** actions for a task.
* Allows the model to perform dynamic reasoning to create, maintain, and adjust plans for acting.
* Enables interaction with external environments (e.g., Wikipedia) to incorporate additional information into the reasoning process.

---

## References
* [Introduction to RAG (Prompting Guide)](https://www.promptingguide.ai/research/rag.en#introduction-to-rag)
* [Techniques, Challenges, and Future of Augmented Language Models (Gradient Flow)](https://gradientflow.com/techniques-challenges-and-future-of-augmented-language-models/)
* [LangChain Quickstart](https://python.langchain.com/v0.1/docs/get_started/quickstart/)
* [Bing Chat Data Exfiltration PoC and Fix (Embrace The Red)](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/)
* [LLM Agents (Prompting Guide)](https://www.promptingguide.ai/research/llm-agents)
* [Introduction to LLM Agents (NVIDIA Developer Blog)](https://developer.nvidia.com/blog/introduction-to-llm-agents/)
