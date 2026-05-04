class MunicipalSafetyAgent:
    def run(self, task: str, context=None):
        context = context or {}
        reasoning = context.get("reasoning", {})

        risks = reasoning.get("risks", [])

        safety_measures = []

        for risk in risks:
            if "accident" in risk.lower():
                safety_measures.append("Deploy warning signage and traffic control")
            if "water" in risk.lower():
                safety_measures.append("Provide emergency water supply to affected areas")
            if "electricity" in risk.lower():
                safety_measures.append("Ensure backup power for critical facilities")

        return {
            "agent": "MunicipalSafetyAgent",
            "safety_measures": safety_measures
        }