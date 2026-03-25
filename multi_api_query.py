# multi_llm_router.py
# Unified AI Router with multiple LLM providers

import os
from dotenv import load_dotenv

from google.genai import Client
from groq import Groq
import cohere
from huggingface_hub import InferenceClient


# ── Setup ─────────────────────────────────────────────
def load_keys():
    """Load all API keys from environment."""
    load_dotenv()

    return {
        "gemini": os.getenv("GOOGLE_API_KEY"),
        "groq": os.getenv("GROQ_API_KEY"),
        "cohere": os.getenv("COHERE_API_KEY"),
        "hf": os.getenv("HUGGINGFACE_API_KEY"),
    }


def initialize_clients(keys):
    """Initialize all AI clients."""
    return {
        "gemini": Client(api_key=keys["gemini"]),
        "groq": Groq(api_key=keys["groq"]),
        "cohere": cohere.ClientV2(keys["cohere"]),
        "hf": InferenceClient(token=keys["hf"]),
    }


# ── Model Handlers ────────────────────────────────────
def handle_gemini(client, text):
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text
    )
    return res.text


def handle_groq(client, text):
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": text}]
    )
    return res.choices[0].message.content.strip()


def handle_cohere(client, text):
    res = client.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": text}]
    )
    return res.message.content[0].text.strip()


def handle_hf(client, text):
    res = client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": text}]
    )
    return res.choices[0].message.content.strip()


# ── Router Logic ──────────────────────────────────────
def route_request(prompt, option, clients):
    """Route request to selected or automatic model."""
    try:
        if option == "1":
            return handle_gemini(clients["gemini"], prompt)

        elif option == "2":
            return handle_groq(clients["groq"], prompt)

        elif option == "3":
            return handle_cohere(clients["cohere"], prompt)

        elif option == "4":
            return handle_hf(clients["hf"], prompt)

        elif option == "5":
            # Smart routing logic
            if len(prompt) < 60:
                return handle_groq(clients["groq"], prompt)
            else:
                return handle_gemini(clients["gemini"], prompt)

        else:
            return "⚠️ Invalid selection."

    except Exception as err:
        return f"❌ Error processing request: {err}"


# ── CLI Interface ─────────────────────────────────────
def main():
    print("=" * 55)
    print("   Multi-LLM Router System")
    print("=" * 55)

    print("""
Choose Model:
1. Gemini (Balanced)
2. Groq (Fast)
3. Cohere (Creative)
4. HuggingFace (Open Models)
5. Auto Select (Smart Routing)
""")

    user_choice = input("Enter option (1–5): ").strip()
    user_prompt = input("\nEnter your query: ").strip()

    if not user_prompt:
        print("⚠️ Prompt cannot be empty.")
        return

    print("\nProcessing...\n")

    keys = load_keys()
    clients = initialize_clients(keys)

    result = route_request(user_prompt, user_choice, clients)

    print("Response:")
    print("-" * 45)
    print(result)
    print("-" * 45)


if __name__ == "__main__":
    main()