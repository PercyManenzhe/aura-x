class MunicipalRecommendationAgent:
    def run(self, task: str, context=None):
        context = context or {}
        inputs = context.get("inputs", {})
        reasoning = context.get("reasoning", {})

        service_area = inputs.get("service_area", "general")
        priority = reasoning.get("priority", "medium")

        recommendations = []

        if service_area == "water":
            recommendations += [
                "Deploy emergency water tankers within 24 hours",
                "Dispatch repair team for leak or pipe damage",
                "Communicate outage updates to residents via SMS/WhatsApp"
            ]

        elif service_area == "electricity":
            recommendations += [
                "Dispatch electrical maintenance team immediately",
                "Prioritize repair for street lights in high-risk areas",
                "Coordinate with Eskom or local grid operators"
            ]

        elif service_area == "roads":
            recommendations += [
                "Deploy road maintenance teams for pothole repairs",
                "Place warning signage for dangerous areas",
                "Schedule structural inspection for affected roads/bridges"
            ]

        elif service_area == "waste":
            recommendations += [
                "Reroute waste collection to affected areas",
                "Deploy additional waste bins in high-accumulation zones",
                "Increase monitoring for illegal dumping hotspots"
            ]

        elif service_area == "climate":
            recommendations += [
                "Activate flood response teams and resources",
                "Coordinate with disaster management authorities",
                "Communicate safety guidelines to residents in affected areas"
            ]

        elif service_area == "Building":
            recommendations += [
                "Conduct safety inspections for reported buildings",
                "Coordinate with emergency services for evacuation if needed",
                "Prioritize repairs for critical infrastructure"
            ]

        else:
            recommendations += [
                "Initiate general service response team",
                "Log issue into municipal ticketing system"
            ]

        if priority == "high":
            recommendations.insert(0, "Activate emergency response protocol (24–48 hrs)")

        return {
            "agent": "MunicipalRecommendationAgent",
            "service_area": service_area,
            "priority": priority,
            "recommendations": recommendations
        }