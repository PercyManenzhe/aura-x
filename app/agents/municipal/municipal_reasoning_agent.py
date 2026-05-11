class MunicipalReasoningAgent:

    def run(self, task, context):

        packet = context["packet"]

        province = packet.province
        municipality = packet.municipality
        issue = packet.issue

        infrastructure = packet.infrastructure
        risk = packet.risk

        reasoning = []

        if infrastructure.get("electricity") == "outage":
            reasoning.append(
                "Electricity infrastructure failure detected."
            )

        if risk.get("risk_level") == "HIGH":
            reasoning.append(
                "High-risk escalation possible."
            )

        return {
            "agent": "MunicipalReasoningAgent",
            "province": province,
            "municipality": municipality,
            "issue": issue,
            "reasoning": reasoning
        }