from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent


class MunicipalResponseAgent(BaseMunicipalAgent):

    def __init__(self):
        super().__init__("MunicipalResponseAgent")

    def run(self, task: str, context=None):
        context = context or {}

        brain = self.get_brain(context)

        # Pull previous outputs safely
        reasoning = context.get("reasoning", {})
        recommendations = context.get("recommend", {})

        report = {
            "summary": "Municipal service disruption detected and analyzed",
            "impact": reasoning.get("impact", []),
            "risks": reasoning.get("risks", []),
            "priority": reasoning.get("priority", "medium"),
            "actions": recommendations.get("recommendations", []),
            "citizen_message": "The municipality is aware of the issue and response teams are being deployed."
        }

        # Store intelligence in the brain
        if brain:
            brain.add_event("response_generated", "municipal report created")

        return {
            "agent": self.name,
            "report": report
        }