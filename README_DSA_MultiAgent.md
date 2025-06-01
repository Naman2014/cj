
# 🤖 DSA Multi-Agent Learning Companion

---

## 📚 Problem Statement

Learning Data Structures and Algorithms (DSA) is challenging—not just due to complex theory, but because of several issues learners face:

- ❓ Not knowing where to start or what to study next  
- 🧩 Getting stuck solving problems  
- 📆 Lack of a structured practice plan  
- 😓 Losing motivation due to slow progress  
- 🔍 Wasting time Googling fragmented resources  

### 🎯 Our Solution

We're building a **DSA Multi-Agent Learning Companion** — an intelligent assistant powered by collaborative AI agents that support students at every step of their DSA journey.

---

## 🧠 Solution Overview

Our architecture consists of:

- ✅ **1 Central Agent** – Understands user intent  
- 🧠 **4 Specialized Side Agents** – Concept, Code, Planner, Motivation  
- 🤖 **1 Orchestrator Agent** – Directs queries to the right expert

### 🔁 User Flow

```text
User Query → Orchestrator → Central Agent (classifies) 
→ Orchestrator (routes) → Specialized Agent → Response → User
```

---

## 🧩 Agent Roles & LLMs

| Agent              | Role                                             | Model Used                    | Why This Model? |
|-------------------|--------------------------------------------------|-------------------------------|------------------|
| **Central Agent**  | Classify user input                              | Gemini 2.0 Flash              | Fast and structured intent classification |
| **Concept Agent**  | Explain theory and DSA concepts                  | DeepSeek LLaMA 70B (distill)  | Great for teaching complex topics |
| **Code Agent**     | Code writing, debugging, and explanations        | DeepSeek LLaMA 70B (distill)  | Balanced code and reasoning |
| **Planner Agent**  | Create study plans based on topics & timeline    | DeepSeek LLaMA 70B (distill)  | Strong structured generation |
| **Motivation Agent** | Encourage and support users                   | Gemma 2 9B IT                 | Friendly and emotionally supportive |
| **Orchestrator Agent** | Routes queries to the correct agent         | Logic-based                   | Lightweight and crucial to system |

---

## 🧠 Suggested Model Alternatives

| Agent              | Alternative LLMs                               |
|-------------------|------------------------------------------------|
| **Concept Agent**  | Claude 3 Opus                                 |
| **Code Agent**     | GPT-4.5 Turbo, Code LLaMA 70B                 |
| **Planner Agent**  | Claude 3 Sonnet                               |
| **Motivation Agent** | Gemini 1.5 Pro                            |

---

## 💻 How to Run Locally

### 1️⃣ Create and Activate Virtual Environment

**For Windows:**

```bash
python -m venv new_env
new_env\Scripts\activate
```

**For macOS/Linux:**

```bash
python3 -m venv new_env
source new_env/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup API Keys

Create a `.env` file in the root directory with the following format:

```env
GEMINI_KEY='your_gemini_api_key'
GROQ_API_KEY='your_groq_api_key'
```

> 🔐 These are used for accessing models like Gemini and DeepSeek via APIs.

---

### 4️⃣ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

---

## 🧪 Features

- ✅ Intelligent query classification
- 📘 Conceptual explanations of DSA topics
- 💻 Code generation, fixing, and debugging
- 🗓️ Custom study plan generation
- 🌈 Motivational support

---

## 🌱 Example Use-Cases

- "What is a segment tree?" → 📘 Concept Agent  
- "Fix this binary search code" → 💻 Code Agent  
- "Give me a 15-day DSA roadmap" → 🗓️ Planner Agent  
- "I feel like giving up..." → 🌈 Motivation Agent  

---
