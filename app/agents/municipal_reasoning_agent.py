class MunicipalReasoningAgent:
    def run(self, task: str, context=None):
        context = context or {}
        inputs = context.get("inputs", {})

        service_area = inputs.get("service_area")
        weather = inputs.get("weather", "normal")

        risks = []
        impact = []

        if service_area == "water":
            risks.append("Public health risk due to water shortage")
            impact.append("Households, schools, and clinics affected")

        if service_area == "electricity":
            risks.append("Crime and safety risk due to outages")
            impact.append("Street lighting and essential services disrupted")

        if service_area == "roads":
            risks.append("High accident probability")
            impact.append("Transport disruption and vehicle damage")

        if weather == "heavy rain":
            risks.append("Infrastructure damage escalation")

        priority = "high" if len(risks) >= 2 else "medium"

        return {
            "agent": "MunicipalReasoningAgent",
            "priority": priority,
            "risks": risks,
            "impact": impact
        }