import os
from dotenv import load_dotenv
from openai import OpenAI

# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# =========================================================
# OPENAI CLIENT
# =========================================================
client = None

if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)

# =========================================================
# AVAILABILITY CHECK
# =========================================================
def llm_available() -> bool:
    return client is not None

# =========================================================
# GENERATE RESPONSE
# =========================================================
def generate_response(
    prompt: str,
    system_prompt: str = "You are Aura-X Municipal Intelligence AI.",
    model: str = "gpt-4.1-mini",
    temperature: float = 0.3,
    max_tokens: int = 500,
):
    """
    Production-ready LLM wrapper for Aura-X.
    """

    if not llm_available():
        return {
            "status": "offline",
            "response": "LLM unavailable. OPENAI_API_KEY missing."
        }

    try:
        completion = client.chat.completions.create(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = completion.choices[0].message.content

        return {
            "status": "success",
            "model": model,
            "response": response_text
        }

    except Exception as e:
        return {
            "status": "error",
            "response": str(e)
        }

# =========================================================
# MUNICIPAL ANALYSIS HELPER
# =========================================================
def municipal_analysis(issue: str, municipality: str):
    """
    Specialized municipal reasoning helper.
    """

    prompt = f"""
    Municipality: {municipality}

    Incident:
    {issue}

    Analyze:
    - public safety risks
    - infrastructure risks
    - likely escalation
    - recommended response
    - municipal departments involved
    """

    return generate_response(prompt)

# =========================================================
# INCIDENT CLASSIFICATION
# =========================================================
def classify_incident(issue: str):

    prompt = f"""
    Classify the following municipal issue:

    {issue}

    Return:
    - category
    - severity
    - urgency
    - recommended department
    """

    return generate_response(prompt)

# =========================================================
# EARLY WARNING ENGINE
# =========================================================
def early_warning_prediction(context: dict):

    prompt = f"""
    Analyze the following municipal intelligence context
    and determine if early warning risks exist.

    Context:
    {context}

    Determine:
    - escalation likelihood
    - emergency risk
    - infrastructure instability
    - social unrest probability
    """

    return generate_response(prompt)

