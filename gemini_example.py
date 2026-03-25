# gemini_chat_interface.py
# Refactored version using Google GenAI SDK

import os
from dotenv import load_dotenv
from google import genai


def fetch_api_key():
    """Retrieve API key from environment variables."""
    load_dotenv()
    key = os.getenv("GOOGLE_API_KEY")

    if not key:
        raise RuntimeError("GOOGLE_API_KEY is missing. Add it to your .env file.")
    
    return key


def create_genai_client(key):
    """Initialize Gemini client."""
    return genai.Client(api_key=key)


def generate_reply(client, query):
    """Generate response from Gemini model."""
    try:
        result = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=query,
            config={
                "temperature": 0.7,
                "top_p": 0.9,
                "max_output_tokens": 500,
            }
        )

        return result.text or "⚠️ Empty response received."

    except Exception as err:
        message = str(err).lower()

        if "api_key_invalid" in message:
            return "❌ Invalid API key. Please verify your credentials."

        elif "quota" in message:
            return "⚠️ API usage limit reached. Try later."

        elif "not found" in message:
            return "⚠️ Model unavailable. Consider using 'gemini-1.5-pro'."

        return f"Unexpected error: {err}"


def run_chat():
    """Main execution flow."""
    print("=" * 50)
    print("   Gemini AI Console")
    print("=" * 50)

    user_input = input("\nAsk something: ").strip()

    if not user_input:
        print("⚠️ No input provided. Please try again.")
        return

    print("\nGenerating response...\n")

    api_key = fetch_api_key()
    gemini_client = create_genai_client(api_key)

    output = generate_reply(gemini_client, user_input)

    print("Result:")
    print("-" * 40)
    print(output)
    print("-" * 40)


if __name__ == "__main__":
    run_chat()