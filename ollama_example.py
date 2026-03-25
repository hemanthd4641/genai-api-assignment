# local_llm_chat.py
# Lightweight local AI chat using Ollama API

import requests

BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "tinyllama"


# ── API FUNCTIONS ─────────────────────────────────────
def fetch_available_models():
    """Retrieve list of installed Ollama models."""
    try:
        response = requests.get(f"{BASE_URL}/api/tags", timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item["name"] for item in data.get("models", [])]

    except Exception:
        return []


def generate_response(prompt_text, model_name):
    """Send prompt to Ollama model and return generated output."""
    endpoint = f"{BASE_URL}/api/generate"

    payload = {
        "model": model_name,
        "prompt": prompt_text,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 200
        }
    }

    try:
        res = requests.post(endpoint, json=payload, timeout=60)
        res.raise_for_status()
        return res.json().get("response", "").strip() or "⚠️ Empty reply"

    except requests.exceptions.Timeout:
        return "⚠️ Request timed out. Try again."

    except requests.exceptions.ConnectionError:
        return "❌ Cannot connect to Ollama. Is it running?"

    except Exception as err:
        return f"Unexpected error: {err}"


# ── CLI LOOP ──────────────────────────────────────────
def start_local_chat():
    print("\n" + "=" * 50)
    print("   Local LLM Chat (Ollama)")
    print("=" * 50)

    models = fetch_available_models()

    if models:
        print(f"\nAvailable Models: {models}")
    else:
        print("\n⚠️ No models found. Run: ollama pull tinyllama")

    model = DEFAULT_MODEL
    print(f"Active Model: {model}\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Session ended.")
            break

        if not user_input:
            print("⚠️ Please enter a prompt.")
            continue

        print("\nThinking...\n")

        output = generate_response(user_input, model)

        print("AI:", output)
        print("-" * 40)


# ── ENTRY POINT ───────────────────────────────────────
if __name__ == "__main__":
    start_local_chat()