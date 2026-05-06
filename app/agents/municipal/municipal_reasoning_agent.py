class MunicipalReasoningAgent:

    def run(self, task: str, context=None):
        province = context["province"]

        risks = []
        impact = []

        if province.infrastructure.electricity == "outage":
            risks.append("Crime risk due to power outage")
            impact.append("Street lighting failure")

        if province.infrastructure.sewage == "overflow":
            risks.append("Severe health hazard")
            impact.append("Children exposed to contamination")

        if province.environment.weather == "storm":
            risks.append("Flood and infrastructure damage risk")

        province.risks.infrastructure_failure_risk = "high" if risks else "low"

        return {
            "agent": "MunicipalReasoningAgent",
            "risks": risks,
            "impact": impact,
            "risk_score": province.risk_score
        } 