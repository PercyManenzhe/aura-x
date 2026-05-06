from app.agents.base_agent import BaseAgent
from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent
from app.core.unified_province_intelligence import UnifiedProvinceIntelligence

class MunicipalSafetyAgent(BaseMunicipalAgent):
    def __init__(self):
        super().__init__("MunicipalSafetyAgent")

    def run(self, task: str, context=None):
        context = context or {}

        reasoning = context.get("reasoning", {})
        if hasattr(reasoning, "risks"):
            risks = reasoning.risks
        elif isinstance(reasoning, dict):
            risks = reasoning.get("risks", [])
        else:
            risks = []

        return {
            "agent": "MunicipalSafetyAgent",
            "task": task,
            "safety_risks": risks,
            "status": "checked"
        }