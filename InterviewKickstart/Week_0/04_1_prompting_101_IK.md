## Prompt Components
An instruction-tuned LLM (sometimes called LLMIT) is fundamentally trained to expect three distinct core elements in a prompt structure:
* **Instruction:** A specific task or directive you want the model to execute.
* **Context:** External information or supplementary background that steers the model toward better, more relevant responses.
* **Input Data:** The specific query, question, or data payload we want a response for.

---

## N-Shot Prompting Framework
The term **"shot"** translates directly to **"example"** (e.g., zero examples, one example, few examples).

### 1. Zero-Shot & One-Shot Prompting
* **Zero-Shot:** Instructs the model to perform a task without providing any structural examples or demonstrations. The model relies entirely on its pre-trained instructions.
* **One-Shot:** Provides exactly one demonstration example within the prompt to align the expected output format before giving the actual input data.

### 2. Few-Shot Prompting
* When dealing with complex, highly structured, or nuanced tasks, zero-shot prompting often falls short.
* **Few-Shot Prompting** enables **in-context learning**. By feeding multiple demonstrations directly inside the prompt payload, you dramatically steer the model toward highly predictable and accurate performance.

---

## Chain-of-Thought (CoT) Prompting
Chain-of-Thought prompts force the model to display its intermediate reasoning steps before arriving at a final answer. 

### Few-Shot CoT Example
**Prompt:**
```text
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 17, 10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.

The odd numbers in this group add up to an even number: 16, 11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.

The odd numbers in this group add up to an even number: 17, 9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
A:
