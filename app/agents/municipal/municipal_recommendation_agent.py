from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent


class MunicipalRecommendationAgent(BaseMunicipalAgent):

    def __init__(self):
        super().__init__("MunicipalRecommendationAgent")

    def run(self, task: str, context=None):
        context = context or {}

        brain = self.get_brain(context)

        recommendations = [
            "Dispatch electrical maintenance team immediately",
            "Prioritize repair for street lights",
            "Coordinate with Eskom"
        ]

        if brain:
            brain.add_event("recommendations_generated", "electricity")

        return {
            "agent": self.name,
            "recommendations": recommendations
        }