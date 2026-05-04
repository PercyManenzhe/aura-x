class MunicipalDecisionAgent:
    def run(self, task: str, context=None):
        context = context or {}
        reasoning = context.get("reasoning", {})

        risks = reasoning.get("risks", [])
        impact = reasoning.get("impact", [])

        if len(risks) >= 2:
            decision = "Immediate intervention required (24-48 hrs)"
            priority = "critical"
        else:
            decision = "Schedule intervention within standard SLA"
            priority = "medium"

        return {
            "agent": "MunicipalDecisionAgent",
            "decision": decision,
            "priority": priority,
            "justification": impact
        }