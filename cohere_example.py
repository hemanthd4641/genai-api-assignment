import os
from dotenv import load_dotenv
import cohere


def load_api_key():
    """Load API key from environment variables."""
    load_dotenv()
    key = os.getenv("COHERE_API_KEY")

    if not key:
        raise RuntimeError("Missing COHERE_API_KEY in environment file.")
    
    return key


def initialize_client(api_key):
    """Create Cohere client instance."""
    return cohere.ClientV2(api_key)


def get_response(client, user_input):
    """Send prompt to Cohere and return response."""
    try:
        result = client.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7,
            max_tokens=500
        )

        return result.message.content[0].text.strip()

    except Exception as error:
        return f"Request failed: {error}"


def main():
    print("=" * 50)
    print("   Cohere AI Chat Interface")
    print("=" * 50)

    prompt_text = input("\nType your query: ").strip()

    if not prompt_text:
        print("⚠️ Please enter a valid prompt.")
        return

    print("\nProcessing request...\n")

    api_key = load_api_key()
    client = initialize_client(api_key)

    reply = get_response(client, prompt_text)

    print("Output:")
    print("-" * 40)
    print(reply)
    print("-" * 40)


if __name__ == "__main__":
    main()