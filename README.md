# 🚀 Multi-Provider AI Integration System

A Python-based project that integrates **five leading AI platforms** — Groq, Ollama (local), Hugging Face, Google Gemini, and Cohere — into a unified and modular system.

This project demonstrates how different Large Language Model (LLM) APIs can be accessed individually as well as through a **centralized routing interface**, enabling flexible AI usage.

> 📘 Developed as part of the *CampusPe Generative AI Assignment (2026)*

---

## 📁 Project Structure

```
genai-api-assignment/
│
├── cohere_example.py        # Cohere API integration
├── gemini_example.py        # Google Gemini API
├── groq_example.py          # Groq (LLaMA models)
├── huggingface_example.py   # Hugging Face API
├── ollama_example.py        # Local LLM using Ollama
│
├── multi_api_query.py       # Unified multi-model router
│
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
├── .env                     # API keys (not uploaded)
├── .gitignore               # Ignore sensitive files
│
└── screenshots/
    ├── cohere.png
    ├── gemini.png
    ├── groq.png
    ├── hugging_face.png
    ├── llama.png
    └── multi.png
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd genai-api-assignment
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate:
venv\Scripts\activate           # Windows
source venv/bin/activate        # macOS / Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Keys

Create a `.env` file:

```
GROQ_API_KEY=your_groq_key
HUGGINGFACE_API_KEY=your_hf_key
GOOGLE_API_KEY=your_google_key
COHERE_API_KEY=your_cohere_key
```

⚠️ Never upload `.env` to GitHub.

---

## 🔑 API Key Sources

| Provider     | Link                                     | Free Tier |
| ------------ | ---------------------------------------- | --------- |
| Groq         | https://console.groq.com/                | ✅ Yes     |
| Hugging Face | https://huggingface.co/settings/tokens   | ✅ Yes     |
| Gemini       | https://makersuite.google.com/app/apikey | ✅ Yes     |
| Cohere       | https://dashboard.cohere.com/            | ✅ Yes     |
| Ollama       | https://ollama.ai/                       | ✅ Free    |

---

## ▶️ How to Run

### 🔹 Groq

```bash
python groq_example.py
```

---

### 🔹 Ollama (Local Model)

```bash
ollama pull tinyllama
python ollama_example.py
```

✔ Runs locally (offline after download)

---

### 🔹 Hugging Face

```bash
python huggingface_example.py
```

⏳ First run may be slow (cold start)

---

### 🔹 Google Gemini

```bash
python gemini_example.py
```

⚡ Fast and efficient responses

---

### 🔹 Cohere

```bash
python cohere_example.py
```

🧠 Strong for conversational tasks

---

### 🔹 Multi-Model System

```bash
python multi_api_query.py
```

Features:

* Select any model
* Auto mode (smart routing)
* Compare outputs

---

## 🧠 Key Features

* 🔄 Multi-LLM Integration (5 providers)
* ⚙️ Modular and clean architecture
* 🔐 Secure API key handling
* 🌐 Cloud + Local AI support
* 🤖 Smart routing system
* 🧪 Multi-model comparison

---

## 📊 Observations

* ⚡ Groq → fastest responses
* 🧠 Gemini → balanced performance
* 💻 Ollama → offline AI
* 🕒 Hugging Face → slower first response
* 🎯 Cohere → structured outputs

---

## ⚠️ Notes

* Ensure API keys are valid
* Ollama must be running locally
* Internet required for cloud APIs
* Free tiers may have limits

---

## 🎯 Conclusion

This project demonstrates how multiple AI providers can be integrated into a **single intelligent system**, enabling flexibility, scalability, and performance comparison.

---

## 👨‍💻 Author

Hemanth D
CampusPe — Generative AI Program (2026)

---
