from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent
from app.core.unified_province_intelligence import UnifiedProvinceIntelligence

class MunicipalDecisionAgent(BaseMunicipalAgent):
    def __init__(self):
        super().__init__("MunicipalDecisionAgent")

    def run(self, task: str, context=None):
        context = context or {}
        intel = context.get("province")

        if intel is None:
            intel = context.get("reasoning", {})

        if isinstance(intel, dict):
            score = intel.get("risk_score", 0)
        else:
            score = getattr(intel, "risk_score", 0)

        if score >= 7:
            decision = "Emergency response activation"
            priority = "critical"
        elif score >= 4:
            decision = "Schedule immediate intervention"
            priority = "high"
        else:
            decision = "Standard SLA intervention"
            priority = "medium"

        if not isinstance(intel, dict) and hasattr(intel, "add_event"):
            intel.add_event("decision_made", decision)

        return {
            "agent": "MunicipalDecisionAgent",
            "decision": decision,
            "priority": priority
        }