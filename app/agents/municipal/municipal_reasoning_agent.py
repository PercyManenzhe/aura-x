class MunicipalReasoningAgent:
    def run(self, task: str, context=None):
        context = context or {}
        inputs = context.get("inputs", {})

        # FIX: support multiple sources of truth
        service_area = (
            inputs.get("service_area")
            or context.get("classified_service_area")
            or context.get("service_area")
        )

        weather = inputs.get("weather", "normal")

        risks = []
        impact = []

        # -----------------------------
        # WATER SYSTEM
        # -----------------------------
        if service_area == "water":
            risks.append("Public health risk due to water shortage")
            impact.append("Households, schools, and clinics affected")

        # -----------------------------
        # ELECTRICITY SYSTEM
        # -----------------------------
        elif service_area == "electricity":
            risks.append("Crime and safety risk due to outages")
            impact.append("Street lighting and essential services disrupted")

        # -----------------------------
        # ROADS SYSTEM
        # -----------------------------
        elif service_area == "roads":
            risks.append("High accident probability")
            impact.append("Transport disruption and vehicle damage")

        # -----------------------------
        # WEATHER MULTIPLIER (IMPORTANT FOR SA)
        # -----------------------------
        if weather in ["heavy rain", "storm", "flood"]:
            risks.append("Infrastructure damage escalation")
            impact.append("Possible flooding and service interruptions")

        # -----------------------------
        # PRIORITY ENGINE
        # -----------------------------
        priority = "high" if len(risks) >= 2 else "medium"

        return {
            "agent": "MunicipalReasoningAgent",
            "priority": priority,
            "risks": risks,
            "impact": impact
        }