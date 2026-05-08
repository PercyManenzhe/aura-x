import os
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()


class LLMAdapterV2:
    """
    Aura-X Intelligence Layer (LLM Adapter V2)

    This is the central brain connector for:
    - reasoning
    - decision-making
    - risk interpretation
    - structured outputs
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    # -----------------------------------------------------
    # CORE CALL
    # -----------------------------------------------------
    def call_llm(self, prompt: str, mode: str = "reasoning") -> str:
        """
        Base LLM call (safe fallback ready)
        """

        if not self.api_key:
            return self._mock_response(prompt, mode)

        # IMPORTANT:
        # For now we keep safe fallback.
        # Later we plug OpenAI / Azure / local models here.

        return self._mock_response(prompt, mode)
    
    """
    We will replace it with this in the future when we enable real LLM calls. For now, it serves as a safe fallback to ensure the system always returns structured data.:

OpenAI
Azure OpenAI
local LLM (Ollama)
Huawei model APIs
    """

    # -----------------------------------------------------
    # STRUCTURED INTELLIGENCE CALL
    # -----------------------------------------------------
    def structured_call(
        self,
        system: str,
        user: str,
        schema: Optional[Dict[str, Any]] = None,
        mode: str = "reasoning"
    ) -> Dict[str, Any]:
        """
        Forces structured JSON output for agents
        """

        prompt = f"""
SYSTEM:
{system}

USER:
{user}

IMPORTANT:
Return ONLY valid JSON.
No explanation.
"""

        raw = self.call_llm(prompt, mode=mode)

        # Try parse JSON safely
        try:
            return json.loads(raw)
        except Exception:
            return {
                "raw_output": raw,
                "parsed": False,
                "mode": mode
            }

    # -----------------------------------------------------
    # INTELLIGENCE MODES
    # -----------------------------------------------------

    def reasoning(self, context: Dict) -> Dict:
        return self.structured_call(
            system="You are a municipal reasoning engine.",
            user=json.dumps(context),
            mode="reasoning"
        )

    def decision(self, context: Dict) -> Dict:
        return self.structured_call(
            system="You are a decision engine for municipal operations.",
            user=json.dumps(context),
            mode="decision"
        )

    def risk_analysis(self, context: Dict) -> Dict:
        return self.structured_call(
            system="You analyze risks in municipalities.",
            user=json.dumps(context),
            mode="risk"
        )

    def recommendations(self, context: Dict) -> Dict:
        return self.structured_call(
            system="You generate actionable municipal recommendations.",
            user=json.dumps(context),
            mode="recommendation"
        )

    # -----------------------------------------------------
    # MOCK ENGINE (until API is enabled)
    # -----------------------------------------------------
    def _mock_response(self, prompt: str, mode: str) -> str:
        """
        Deterministic fallback so system ALWAYS works
        """

        if mode == "risk":
            return json.dumps({
                "risk_score": 0.42,
                "risks": ["Service disruption", "Public safety risk"],
                "level": "MEDIUM"
            })

        if mode == "decision":
            return json.dumps({
                "decision": "Standard SLA intervention",
                "priority": "medium"
            })

        if mode == "recommendation":
            return json.dumps({
                "actions": [
                    "Deploy maintenance team",
                    "Notify municipal control room"
                ]
            })

        return json.dumps({
            "message": "Aura-X mock reasoning output",
            "status": "ok"
        })

