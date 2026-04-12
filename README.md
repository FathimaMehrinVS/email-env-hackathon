---
title: Meta x Scaler OpenEnv Hackathon - Email Triage
emoji: 📧
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
app_port: 7860
---

# 📧 OpenEnv Hackathon: Email Triage AI
**Entry for the Meta x SCALER School of Technology AI Hackathon**

[![OpenEnv Compatible](https://img.shields.io/badge/OpenEnv-Compatible-blue)](https://github.com/OpenEnv-AI)
[![Sponsored by Meta](https://img.shields.io/badge/Sponsored%20by-Meta-blue)](https://meta.com)
[![Scaler School](https://img.shields.io/badge/Powered%20by-Scaler-blue)](https://scaler.com)


A robust, multi-task AI environment for evaluating email triage agents. This project simulates realistic email management scenarios with structured metadata and varying difficulty levels.

## 🚀 Overview
The **Smart Email Triage Agent** is designed to process incoming emails and classify them into three critical categories using a combination of LLM reasoning and rule-based fallbacks:

*   **🗑️ Delete**: Spam, phishing, and unwanted marketing.
*   **⭐ Mark Important**: Work-related syncs, urgent security alerts, and stakeholder messages.
*   **📥 Ignore**: Generic notifications, receipts, and neutral updates.

## 🧠 Key Features
*   **Multi-Task Difficulty**: Supports `easy`, `medium`, and `hard` task sets with increasing ambiguity.
*   **Rich Observations**: Agents receive `sender`, `subject`, and `body` fields for deep contextual analysis.
*   **Robust Inference**: Uses a Chain-of-Thought style prompting strategy with high-accuracy fallbacks.
*   **Pydantic Validated**: All API interactions are strictly typed for reliability.

## 🛠️ Environment Specification
| Feature | Details |
| :--- | :--- |
| **Action Space** | `delete`, `mark_important`, `ignore` |
| **Observation Space** | `sender`, `subject`, `text` |
| **Reward Function** | `+1.0` for correct, `-1.0` for incorrect |
| **Dataset Size** | 18+ unique curated email scenarios |

## 📦 Deployment
This environment is built as a **Dockerized API** compatible with Hugging Face Spaces and OpenEnv benchmarks.

```bash
# To run locally via Docker
docker build -t email-triage .
docker run -p 7860:7860 email-triage
```

## 📊 Benchmark results
The baseline agent achieves **100% accuracy** on the `easy` set and handles high-ambiguity cases in the `hard` set using advanced context mapping.

---
*Developed for the Meta x SCALER OpenEnv AI Hackathon 2026. Powered by PyTorch & Hugging Face.*