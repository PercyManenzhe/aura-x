from app.orchestrators.orchestrator import AuraXOrchestrator


class OrchestrationService:

    WORKFLOW_MAP = {
        "municipal": "workflows/municipal_ops.yaml",
        "mining": "workflows/mining_safety.yaml",
        "tourism": "workflows/tourism_safety_health.yaml",
    }

    @classmethod
    def execute(cls, workflow: str, inputs: dict):

        yaml_path = cls.WORKFLOW_MAP.get(workflow)

        if not yaml_path:
            return {
                "status": "error",
                "message": f"Unknown workflow: {workflow}"
            }

        orchestrator = AuraXOrchestrator(
            yaml_path=yaml_path
        )

        result = orchestrator.run(inputs=inputs)

        return {
            "status": "success",
            "workflow": workflow,
            "result": result
        }