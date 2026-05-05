class MunicipalResponseAgent:
    def run(self, task: str, context=None):
        context = context or {}

        reasoning = context.get("reasoning", {})
        safety = context.get("safety", {})           #  correct
        recommend = context.get("recommend", {})     #  correct

        safety_actions = safety.get("safety_measures", [])
        recommendations = recommend.get("recommendations", [])

        # Combine actions
        actions = safety_actions + recommendations

        return {
            "agent": "MunicipalResponseAgent",
            "report": {
                "summary": "Municipal service disruption detected and analyzed",
                "impact": reasoning.get("impact", []),
                "risks": reasoning.get("risks", []),
                "priority": reasoning.get("priority", "medium"),
                "actions": actions,   #  THIS will now be populated
                "citizen_message": "The municipality is aware of the issue and response teams are being deployed."
            }
        }