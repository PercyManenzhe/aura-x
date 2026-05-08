from app.orchestrators.orchestrator import AuraXOrchestrator


class OrchestrationService:

    def __init__(self):

        self.orchestrator = AuraXOrchestrator(
            yaml_path="workflows/municipal_ops.yaml"
        )

    def process_incident(self, payload):

        return self.orchestrator.run(payload)