import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    if len(sys.argv) < 2:
        print("usage: agent <prompt text> [--verbose]")
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    prompt = sys.argv[1]
    response = client.models.generate_content(model='gemini-2.0-flash-001',
                                              contents=prompt)
    print(response.text)
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        usage_metadata = response.usage_metadata
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
