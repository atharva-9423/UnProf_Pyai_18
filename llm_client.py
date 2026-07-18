import os
import sys

from google import genai
from google.genai import errors
from google.genai.types import GenerateContentConfig

MODEL_NAME = "gemini-3.5-flash"


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable is not set.")
        print("   export GEMINI_API_KEY='your-key-here'      (macOS/Linux)")
        print("   setx GEMINI_API_KEY \"your-key-here\"        (Windows — reopen terminal after)")
        sys.exit(1)
    return genai.Client(api_key=api_key)


def ask(client, user_prompt, system_prompt=None, temperature=0.7):
    config_kwargs = {"temperature": temperature}
    if system_prompt:
        config_kwargs["system_instruction"] = system_prompt

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_prompt,
            config=GenerateContentConfig(**config_kwargs),
        )
        return response.text

    except errors.ClientError as e:
        return f"[ERROR] Request error: {e}"
    except errors.ServerError as e:
        return f"[ERROR] Gemini API unavailable: {e}"
    except errors.APIError as e:
        return f"[ERROR] API error: {e}"
    except Exception as e:
        return f"[ERROR] Unexpected error: {e}"
