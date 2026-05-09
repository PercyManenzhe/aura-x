import os
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()


class LLMAdapterV2:
    """
    Aura-X Cognitive Intelligence Layer (v2)

    This is the central brain of Aura-X:
    - Municipal reasoning
    - Risk intelligence
    - Decision support
    - Scenario understanding
    - Multi-domain routing (municipal, mining, tourism)
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    # =====================================================
    # CORE LLM CALL (SAFE MODE FIRST)
    # =====================================================
    def call_llm(self, prompt: str, system: Optional[str] = None) -> str:
        """
        Future-ready LLM connector.
        Right now: safe fallback (no external API dependency).
        """

        if not self.api_key:
            return self._fallback_response(prompt)

        # TODO (next phase):
        # - OpenAI / Azure OpenAI / local LLM / Huawei integration
        return self._fallback_response(prompt)

    # =====================================================
    # CORE INTELLIGENCE ENGINE (MUNICIPAL BRAIN)
    # =====================================================
    def reason(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts raw municipal input into structured intelligence
        """

        prompt = f"""
You are Aura-X Municipal Intelligence Engine.

Analyze the context and return STRICT JSON ONLY:

Context:
{json.dumps(context, indent=2)}

Output schema:
{{
  "risks": [],
  "impact": [],
  "priority": "low|medium|high|critical",
  "risk_score": 0.0,
  "recommendations": []
}}
"""

        response = self.call_llm(prompt)


        try:
            return json.loads(response)
        except Exception:
            return {
                "risks": ["fallback parsing used"],
                "impact": [],
                "priority": "medium",
                "risk_score": 0.5,
                "recommendations": []
            }

    # =====================================================
    # DECISION ENGINE (GOVERNMENT LOGIC LAYER)
    # =====================================================
    def decision(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts risk intelligence into action decisions
        """

        risks = context.get("risks", [])
        score = context.get("risk_score", 0.0)

        if score >= 0.7:
            return {
                "decision": "Emergency intervention",
                "priority": "critical"
            }
        elif score >= 0.4:
            return {
                "decision": "Standard SLA intervention",
                "priority": "medium"
            }
        else:
            return {
                "decision": "Monitor situation",
                "priority": "low"
            }

    # =====================================================
    # MULTI-DOMAIN ROUTER (FUTURE NATIONAL SYSTEM)
    # =====================================================
    def route_intelligence(self, domain: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expands Aura-X into national intelligence system
        """

        if domain == "municipal":
            return self.reason(payload)

        if domain == "mining":
            return {
                "status": "mining module placeholder",
                "risk": "not implemented yet"
            }

        if domain == "tourism":
            return {
                "status": "tourism module placeholder",
                "recommendation": "not implemented yet"
            }

        return {
            "error": f"Unsupported domain: {domain}"
        }

    # =====================================================
    # FALLBACK SAFETY ENGINE
    # =====================================================
    def _fallback_response(self, prompt: str) -> str:
        return json.dumps({
            "status": "offline_mode",
            "message": "Aura-X running in deterministic intelligence mode",
            "prompt_length": len(prompt)
        })
    
