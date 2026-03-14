 ---

# 🧠 RosterIQ

### Memory-Driven Provider Roster Intelligence Agent

![AI](https://img.shields.io/badge/AI-Agent-blue)
![Memory Architecture](https://img.shields.io/badge/Architecture-Memory--Driven-purple)
![Hackathon](https://img.shields.io/badge/Event-HiLabs%20Cognizance%202026-green)
![Python](https://img.shields.io/badge/Built%20With-Python-yellow)

---

## 📌 Overview

**RosterIQ** is an **AI-powered intelligence system** designed to analyze healthcare **provider roster operations**.

It processes:

* pipeline processing data
* market transaction data

to automatically:

🔍 detect operational problems
📊 analyze market performance
🧠 explain root causes
⚡ help operations teams respond faster

The system was built for the **HiLabs Cognizance 2026 Hackathon**.

---

# 🚨 Problem Statement

Healthcare organizations process **thousands of provider roster files every month**.

Each file goes through **multiple pipeline stages**.

When something goes wrong, operations teams must manually investigate:

❌ Which stage failed
❌ Which organization caused the issue
❌ Whether the issue affects market success rates

This investigation process is:

🔴 Slow
🔴 Manual
🔴 Difficult to scale

---

# 💡 Our Solution

RosterIQ acts like an **AI Operations Analyst**.

Instead of a simple dashboard, we built a **Memory-Driven AI System** that can:

🧠 remember past investigations
📚 understand pipeline knowledge
⚙ follow investigation procedures
🔎 detect patterns across data

The system uses:

* **AI Agents**
* **Tool-based analysis**
* **Layered memory architecture**

---

# 🧭 High Level System Flow

```
User Query
   │
   ▼
Supervisor Agent
   │
   ▼
Memory Manager
   │
   ▼
Agent Selection
   │
   ▼
Analysis Tools
   │
   ▼
Alerts • Charts • Reports
```

---

# 🏗 System Architecture

```
User
 │
 ▼
Supervisor Agent
 │
 ▼
Memory Manager
 │
 ├ Episodic Memory
 ├ Procedural Memory
 ├ Semantic Memory
 └ RAG Memory
 │
 ▼
Operational Agents
 │
 ├ Pipeline Agent
 ├ Market Agent
 └ Monitoring Agent
 │
 ▼
Tool Layer
 │
 ├ Data Tool
 ├ Visualization Tool
 ├ Alert System
 ├ Reasoning Engine
 ├ Report Generator
 └ Web Search Tool
 │
 ▼
Insights & Visual Reports
```

---

# 🧠 Memory Architecture

Memory is the **core intelligence layer** of RosterIQ.

The system uses **four types of memory**.

---

## 🧠 Episodic Memory

Stores **past investigations** and user interactions.

Example:

```
Query: Analyze CA market
Result: Found 3 stuck roster operations
Time: 2026-03-10
```

This helps the system answer:

➡ Have we seen this issue before?

---

## ⚙ Procedural Memory

Stores **investigation workflows** as JSON procedures.

Example procedures:

* `triage_stuck_ros`
* `market_health_report`
* `retry_effectiveness_analysis`

Example JSON structure:

```json
{
  "procedure": "triage_stuck_ros",
  "steps": [
    "load pipeline data",
    "identify stuck operations",
    "group by organization",
    "generate report"
  ]
}
```

This allows agents to follow **standard diagnostic steps**.

---

## 📚 Semantic Memory

Stores **domain knowledge about the pipeline system**.

Examples:

* meaning of **DART generation**
* explanation of **health flags**
* definition of **failure statuses**

This helps agents **explain problems clearly**.

---

## 🔎 RAG Memory

RAG memory stores **insights discovered during analysis**.

Example insight:

```
Repeated DART generation delays detected in CA market
```

This allows the system to **learn patterns and reuse insights** later.

---

# 🔗 How Memory Works Together

```
User Query
   │
   ▼
Memory Manager
 │
 ├ Episodic Memory → Past investigations
 ├ Procedural Memory → Workflows
 ├ Semantic Memory → Knowledge
 └ RAG Memory → Learned insights
 │
 ▼
Provide context to agents
```

---

# 🤖 Agents in the System

RosterIQ uses **multiple specialized agents**.

### 🧠 Supervisor Agent

Controls the system and routes queries.

### ⚙ Pipeline Agent

Analyzes pipeline stages and detects stuck processes.

### 📊 Market Agent

Analyzes market success rates and retry performance.

### 📡 Monitoring Agent

Continuously monitors for operational risks.

---

# 🧰 Tool Layer

Agents use different tools to perform analysis.

| Tool                   | Purpose                               |
| ---------------------- | ------------------------------------- |
| **Data Tool**          | Reads and processes CSV datasets      |
| **Visualization Tool** | Generates charts and graphs           |
| **Alert System**       | Detects operational risks             |
| **Reasoning Engine**   | Explains root causes                  |
| **Report Generator**   | Creates structured reports            |
| **Web Search Tool**    | Fetches external healthcare knowledge |

---

# 📊 Visualizations Generated

RosterIQ can generate multiple visual reports.

### 📈 Market Success Trend

```
X-axis → Month
Y-axis → Success Percentage
Lines → Different Markets
```

---

### 📊 Retry Effectiveness Chart

```
X-axis → Market
Y-axis → Retry Lift
```

---

### 🔥 Pipeline Health Heatmap

```
Organization × Pipeline Stage
```

This helps identify **bottlenecks in the pipeline**.

---

# 📂 Project Structure

```
rosterIQ
│
├ agents
├ memory
├ tools
├ procedures
├ data
│
├ main.py
├ config.py
├ requirements.txt
└ README.md
```

Each folder represents a **different system component**.

---

# ⚙ Installation

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run the system

```bash
python main.py
```

---

# 🧪 Example Demo Queries

Try the system with these queries:

```
Analyze market success
Show market chart
Find stuck roster operations
Why are transactions failing?
Search CMS provider validation rules
```

These queries demonstrate:

✔ memory retrieval
✔ reasoning capability
✔ automated analysis
✔ chart generation

---

# 🎥 Demo Video
```
https://youtu.be/k_oLevckMfA?si=1fzu5wV7sHNNSZq5

```

# 🏁 Conclusion

RosterIQ demonstrates how **AI agents with layered memory architecture** can analyze complex operational pipelines.

By combining:

🧠 Episodic Memory
⚙ Procedural Workflows
📚 Semantic Knowledge
🔎 RAG Insights

the system becomes a **powerful operational intelligence assistant** for healthcare data pipelines.


## Team Vastavikta
Members Name : Naman jain, Riya jain, Shreya Pandey, Ashutosh kumar
Email address: namanjain82670@gmail.com

---

