from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent


class MunicipalOpsAgent(BaseMunicipalAgent):

    def __init__(self):
        super().__init__("MunicipalOpsAgent")

    def run(self, task: str, context=None):
        context = context or {}

        brain = self.get_brain(context)
        inputs = self.get_inputs(context)

        issue = inputs.get("issue", "")
        municipality = inputs.get("municipality", "")

        if brain:
            brain.set_issue(issue)

        return {
            "agent": self.name,
            "classified_service_area": "electricity",
            "inputs": inputs
        }
    
    