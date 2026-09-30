# LangChain Runnables

A hands-on repository for learning and understanding **Runnables in LangChain**.

This repository contains simple examples of different Runnable components and shows how they can be used to build structured LLM workflows with **OpenAI** and **Hugging Face** models.

---

## 📌 What are LangChain Runnables?

**Runnables** are the building blocks used to create workflows in modern LangChain applications.

A Runnable takes an input, performs some operation, and produces an output.

A simple workflow looks like:

```text
Input
  ↓
Runnable
  ↓
Output
```

Multiple Runnables can also be connected together:

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output Parser
  ↓
Final Output
```

Runnables make it easier to build, compose, and reuse different parts of an LLM application.

---

# 📂 Repository Structure

```text
Langchain-Runnables/
│
├── runnabe_lambda_HF.py
├── runnable_lambda_OA.py
│
├── runnable_parallel_HF.py
├── runnable_parallel_OA.py
│
├── runnable_passthrough_HF.py
├── runnable_passthrough_OA.py
│
├── runnable_sequence_HF.py
└── runnable_sequence_OA.py
```

> Note: `runnabe_lambda_HF.py` uses the existing filename in the repository.

---

# 🔹 Runnable Types Covered

This repository focuses on four important Runnable concepts:

1. RunnableLambda
2. RunnableParallel
3. RunnablePassthrough
4. RunnableSequence

Examples are provided using both **Hugging Face** and **OpenAI** integrations.

---

# 1. RunnableLambda

`RunnableLambda` allows you to turn a normal Python function into a Runnable.

For example:

```python
def process_text(text):
    return text.upper()
```

This function can be converted into a Runnable and used as part of a LangChain workflow.

### Flow

```text
Input
  ↓
RunnableLambda
  ↓
Python Function
  ↓
Output
```

### Files

```text
runnabe_lambda_HF.py
runnable_lambda_OA.py
```

### Use Cases

* Custom Python logic
* Data transformation
* Pre-processing
* Post-processing
* Connecting custom functions to LangChain workflows

---

# 2. RunnableParallel

`RunnableParallel` allows multiple Runnables to execute independently using the same input.

For example:

```text
                ┌──→ Runnable A ──→ Output A
Input ──────────┤
                └──→ Runnable B ──→ Output B
```

This is useful when multiple operations do not depend on each other.

### Files

```text
runnable_parallel_HF.py
runnable_parallel_OA.py
```

### Example Use Case

Given a topic, we might generate:

```text
              ┌──→ Summary
Topic ────────┤
              └──→ Key Points
```

Both operations can be performed independently.

---

# 3. RunnablePassthrough

`RunnablePassthrough` passes the input directly to the next step without modifying it.

```text
Input
  ↓
RunnablePassthrough
  ↓
Same Input
```

It is particularly useful when building dictionaries or combining multiple inputs inside a Runnable pipeline.

### Files

```text
runnable_passthrough_HF.py
runnable_passthrough_OA.py
```

### Example Concept

```text
Input
  │
  ├──────────────→ Original Input
  │
  └──→ Other Processing
```

This allows the original input to remain available while other operations are performed.

---

# 4. RunnableSequence

`RunnableSequence` connects multiple Runnables together so that the output of one step becomes the input of the next step.

```text
Input
  ↓
Runnable 1
  ↓
Runnable 2
  ↓
Runnable 3
  ↓
Output
```

For example:

```text
User Question
      ↓
Prompt Template
      ↓
LLM
      ↓
Output Parser
      ↓
Final Answer
```

### Files

```text
runnable_sequence_HF.py
runnable_sequence_OA.py
```

### Use Cases

* Multi-step LLM workflows
* Prompt → LLM pipelines
* Data transformation pipelines
* RAG pipelines
* Structured output workflows

---

# 🤖 OpenAI and Hugging Face Examples

The repository contains examples using two different model providers.

### OpenAI

```text
runnable_lambda_OA.py
runnable_parallel_OA.py
runnable_passthrough_OA.py
runnable_sequence_OA.py
```

### Hugging Face

```text
runnabe_lambda_HF.py
runnable_parallel_HF.py
runnable_passthrough_HF.py
runnable_sequence_HF.py
```

This makes it easier to understand that the **Runnable concepts remain similar even when the underlying LLM provider changes**.

---

# 🛠️ Technologies Used

* Python
* LangChain
* OpenAI
* Hugging Face
* LLMs
* Runnable Architecture

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/laxmankhedkar/Langchain-Runnables.git
```

### 2. Navigate to the project

```bash
cd Langchain-Runnables
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install LangChain

```bash
pip install langchain
```

Depending on the example, you may also need the appropriate provider/integration packages.

For example:

```bash
pip install langchain-openai
```

or:

```bash
pip install langchain-huggingface
```

---

# 🔑 API Keys

Some examples require an API key from the corresponding model provider.

Store API keys as environment variables rather than directly inside Python files.

For example:

```text
OPENAI_API_KEY=your_api_key
```

For Hugging Face:

```text
HUGGINGFACEHUB_API_TOKEN=your_token
```

> Never commit API keys or `.env` files to GitHub.

---

# ▶️ Running the Examples

### RunnableLambda

```bash
python runnable_lambda_OA.py
```

or:

```bash
python runnabe_lambda_HF.py
```

### RunnableParallel

```bash
python runnable_parallel_OA.py
```

or:

```bash
python runnable_parallel_HF.py
```

### RunnablePassthrough

```bash
python runnable_passthrough_OA.py
```

or:

```bash
python runnable_passthrough_HF.py
```

### RunnableSequence

```bash
python runnable_sequence_OA.py
```

or:

```bash
python runnable_sequence_HF.py
```

---

# 🎯 Learning Objectives

This repository is created to build a practical understanding of LangChain Runnables.

By working through these examples, you can understand:

* What Runnables are
* How Runnables work in LangChain
* `RunnableLambda`
* `RunnableParallel`
* `RunnablePassthrough`
* `RunnableSequence`
* How to compose multiple Runnables
* How inputs and outputs move through a pipeline
* How Runnables work with different LLM providers
* How Runnable concepts are used in real LLM applications

---

# 🔄 Runnable Workflow

A typical LangChain application can be built by combining different Runnables:

```text
                ┌──→ Parallel Processing
                │
Input → Lambda ──┤
                │
                └──→ Passthrough
                       ↓
                    Sequence
                       ↓
                      LLM
                       ↓
                    Output
```

The main advantage is that individual components can be combined into reusable workflows.

---

# 💡 Why Runnables Matter

Runnables are important because modern LangChain applications are often built as **composable pipelines**.

Instead of writing all application logic in one large function, we can break the workflow into smaller components:

```text
Prompt
   +
LLM
   +
Custom Logic
   +
Parser
   ↓
Complete Application
```

This makes applications easier to understand, modify, test, and extend.

---

# 🚀 Possible Future Improvements

Some useful additions to this repository could include:

* RunnableBranch
* RunnableMap
* RunnablePassthrough with practical examples
* RunnableConfig
* Streaming with Runnables
* Batch processing
* Async Runnables
* RAG using Runnables
* Output parsers with Runnables
* Tool calling with Runnable pipelines
* LangGraph workflows

---

# 👨‍💻 Author

**Laxman Khedkar**

Data Scientist & ML Engineer
Python | SQL | Machine Learning | NLP | LLMs | RAG | Generative AI

GitHub: [@laxmankhedkar](https://github.com/laxmankhedkar)

---

## ⭐ About This Repository

This repository is part of my hands-on learning journey with **LangChain and Generative AI**.

The goal is to understand LangChain concepts by implementing them through small and practical Python examples.

If you find this repository useful, feel free to ⭐ the repository and explore the examples.
