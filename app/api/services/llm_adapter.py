import os
from dotenv import load_dotenv
from . import llm_adapter

# Load .env if present
load_dotenv()

def llm_available() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))

def call_openai(prompt: str) -> str:
    """
    Minimal LLM call wrapper. Returns a plain string response.
    Uses OpenAI API key from environment: OPENAI_API_KEY
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    # NOTE: We'll keep this wrapper minimal & safe.
    # We'll use the official OpenAI python client later if you want,
    # but for now this is a clean placeholder pattern.
    # If you want the official client immediately, say so.

    # Fallback response for now if you don't want API calls yet
    return "LLM placeholder: OpenAI integration ready. Provide official client code when required."

