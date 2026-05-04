class MunicipalResponseAgent:
    def run(self, task: str, context=None):
        context = context or {}

        reasoning = context.get("reasoning", {})
        recommendations = context.get("recommendations", {})

        return {
            "agent": "MunicipalResponseAgent",
            "report": {
                "summary": "Municipal service disruption detected and analyzed",
                "impact": reasoning.get("impact", []),
                "risks": reasoning.get("risks", []),
                "priority": reasoning.get("priority"),
                "actions": recommendations.get("recommendations", []),
                "citizen_message": "The municipality is aware of the issue and response teams are being deployed."
            }
        }