# 🚀 Multi-Provider AI Integration System

A Python-based project that integrates **five leading AI platforms** — Groq, Ollama (local), Hugging Face, Google Gemini, and Cohere — into a unified and modular system.

This project demonstrates how different Large Language Model (LLM) APIs can be accessed individually as well as through a **centralized routing interface**, enabling flexible AI usage.

> 📘 Developed as part of the *CampusPe Generative AI Assignment (2026)*

---

## 📁 Project Structure

```
ai-api-integration/
│
├── groq_client.py           # Groq (LLaMA 3 - high speed inference)
├── ollama_local.py          # Ollama (local LLM execution)
├── hf_client.py             # Hugging Face (open-source models)
├── gemini_client.py         # Google Gemini (fast + multimodal)
├── cohere_client.py         # Cohere (command-based models)
│
├── multi_llm_router.py      # Unified interface (model selection + routing)
│
├── requirements.txt         # Dependencies
├── .env                     # API keys (excluded from version control)
├── .gitignore               # Prevents sensitive data leaks
│
└── screenshots/
    ├── groq.png
    ├── ollama.png
    ├── huggingface.png
    ├── gemini.png
    ├── cohere.png
    └── multi.png
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd ai-api-integration
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate:
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file and add your API keys:

```
GROQ_API_KEY=your_groq_key
HUGGINGFACE_API_KEY=your_hf_key
GOOGLE_API_KEY=your_google_key
COHERE_API_KEY=your_cohere_key
```

⚠️ **Important:**
Never upload `.env` to GitHub. It is already included in `.gitignore`.

---

## 🔑 API Key Sources

| Provider      | Link                                     | Free Tier |
| ------------- | ---------------------------------------- | --------- |
| Groq          | https://console.groq.com/                | ✅ Yes     |
| Hugging Face  | https://huggingface.co/settings/tokens   | ✅ Yes     |
| Google Gemini | https://makersuite.google.com/app/apikey | ✅ Yes     |
| Cohere        | https://dashboard.cohere.com/            | ✅ Yes     |
| Ollama        | Local installation (https://ollama.ai/)  | ✅ Free    |

---

## ▶️ Usage Guide

### 🔹 Groq (Ultra-fast inference)

```bash
python groq_client.py
```

---

### 🔹 Ollama (Local LLM Execution)

```bash
ollama pull llama3
python ollama_local.py
```

✔ Runs fully offline after model download

---

### 🔹 Hugging Face (Open Models)

```bash
python hf_client.py
```

⏳ First response may be slow due to cold start

---

### 🔹 Google Gemini

```bash
python gemini_client.py
```

⚡ Optimized for speed and efficiency

---

### 🔹 Cohere

```bash
python cohere_client.py
```

🧠 Strong performance for conversational tasks

---

### 🔹 Unified Multi-Model Interface

```bash
python multi_llm_router.py
```

Features:

* Select any provider dynamically
* Auto-routing based on input
* Compare multiple model outputs

---

## 🧠 Key Features

* 🔄 **Multi-LLM Integration** (5 providers in one system)
* ⚙️ **Modular Architecture** (easy to extend)
* 🔐 **Secure API Handling** via `.env`
* 🌐 **Cloud + Local AI Support**
* 🤖 **Smart Routing Logic**
* 🧪 **Side-by-side Model Comparison**

---

## 📊 Observations

* ⚡ Groq delivers fastest responses
* 🧠 Gemini provides balanced performance
* 💻 Ollama enables offline AI usage
* 🕒 Hugging Face may have cold-start latency
* 🎯 Cohere performs well in structured tasks

---

## ⚠️ Notes

* Ensure all API keys are valid before running scripts
* Ollama must be running locally before execution
* Internet is required for all cloud-based APIs
* Free tiers may have usage limits

---

## 🎯 Conclusion

This project showcases how multiple AI services can be combined into a **single intelligent system**, enabling flexibility, performance comparison, and efficient usage of different LLM providers.

---

## 👨‍💻 Author

Hemanth D
CampusPe — Generative AI Program (2026)

---
