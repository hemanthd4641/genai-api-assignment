# hf_llm_chat.py
# Refactored Hugging Face Inference API example

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


def get_hf_api_key():
    """Load Hugging Face API key from environment."""
    load_dotenv()
    key = os.getenv("HUGGINGFACE_API_KEY")

    if not key:
        raise RuntimeError("HUGGINGFACE_API_KEY is missing in .env file.")
    
    return key


def init_hf_client(token):
    """Initialize Hugging Face inference client."""
    return InferenceClient(token=token)


def generate_hf_response(client, user_input):
    """Send user input to Hugging Face model and return response."""
    try:
        result = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=300,
            temperature=0.7,
        )

        return result.choices[0].message.content.strip()

    except Exception as err:
        error_text = str(err).lower()

        if "token" in error_text or "unauthorized" in error_text:
            return "❌ Invalid Hugging Face API key."

        elif "rate" in error_text or "limit" in error_text:
            return "⚠️ Rate limit reached. Please try again later."

        elif "not found" in error_text:
            return "⚠️ Model not available. Check model name."

        return f"Unexpected error: {err}"


def run_hf_chat():
    """Main CLI interface."""
    print("=" * 50)
    print("   Hugging Face LLM Chat")
    print("=" * 50)

    user_query = input("\nEnter your query: ").strip()

    if not user_query:
        print("⚠️ No input detected. Please enter a prompt.")
        return

    print("\nGenerating response from Hugging Face...\n")

    api_key = get_hf_api_key()
    hf_client = init_hf_client(api_key)

    output = generate_hf_response(hf_client, user_query)

    print("Result:")
    print("-" * 40)
    print(output)
    print("-" * 40)


if __name__ == "__main__":
    run_hf_chat()