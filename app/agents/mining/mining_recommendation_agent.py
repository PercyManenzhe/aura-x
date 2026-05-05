class MiningRecommendationAgent:
    def run(self, task: str, context=None):
        context = context or {}
        inputs = context.get("inputs", {})

        mine_type = inputs.get("mine_type", "underground")
        risk_level = inputs.get("risk_level", "medium")

        recommendations = [
            "Update and verify hazard identification & risk assessment (HIRA)",
            "Run refresher training for emergency response procedures",
            "Daily pre-shift inspections checklist and logging",
            "PPE compliance verification and incident reporting workflow"
        ]

        if mine_type == "underground":
            recommendations.insert(0, "Ventilation and gas monitoring verification (underground focus)")

        if risk_level == "high":
            recommendations.insert(0, "Increase safety inspections frequency and supervisor sign-off")

        return {
            "agent": "MiningRecommendationAgent",
            "mine_type": mine_type,
            "risk_level": risk_level,
            "recommendations": recommendations
        }
# app/agents/mining_recommendation_agent.py