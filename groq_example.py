# groq_chat_client.py
# Refactored implementation for Groq LLaMA API

import os
from dotenv import load_dotenv
from groq import Groq


def load_api_credentials():
    """Load GROQ API key from environment."""
    load_dotenv()
    key = os.getenv("GROQ_API_KEY")

    if not key:
        raise RuntimeError("GROQ_API_KEY is not set in the environment.")
    
    return key


def setup_client(api_key):
    """Initialize Groq client."""
    return Groq(api_key=api_key)


def fetch_chat_response(client, user_query):
    """Send request to Groq model and return output."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_query}],
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content.strip()

    except Exception as err:
        error_text = str(err).lower()

        if "api" in error_text and "key" in error_text:
            return "❌ Invalid or missing API key."

        elif "rate" in error_text or "limit" in error_text:
            return "⚠️ Rate limit exceeded. Please wait and retry."

        return f"Unexpected error occurred: {err}"


def start_chat():
    """Main CLI interaction."""
    print("=" * 50)
    print("   Gemini Chat Interface")
    print("=" * 50)

    user_input = input("\nAsk your question: ").strip()

    if not user_input:
        print("⚠️ Empty input detected. Try again.")
        return

    print("\nFetching response from Groq...\n")

    api_key = load_api_credentials()
    groq_client = setup_client(api_key)

    answer = fetch_chat_response(groq_client, user_input)

    print("Output:")
    print("-" * 40)
    print(answer)
    print("-" * 40)


if __name__ == "__main__":
    start_chat()