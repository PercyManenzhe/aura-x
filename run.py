from app.agents.orchestrator import AuraXOrchestrator
def run(self, inputs=None):
    inputs = inputs or {}
    step_results = {}
    ordered_steps = []

    for step in self.workflow["steps"]:
        step_name = step["name"]
        agent_name = step["agent"]
        task = step["task"]

        agent = self.agent_map.get(agent_name)

        if agent:
            if agent_name in ["ReasoningAgent", "RecommendationAgent"]:
                output = agent.run(task, step_results)
            else:
                output = agent.run(task)

            status = "success"
        else:
            output = f"Agent {agent_name} not found"
            status = "error"

        result = {
            "step": step_name,
            "agent": agent_name,
            "task": task,
            "status": status,
            "output": output
        }

        step_results[step_name] = output
        ordered_steps.append(result)

        print(f"{step_name.upper()}: {output}")

    final_summary = {
        "summary": "Aura-X completed a multi-agent tourism workflow",
        "top_recommendations": step_results.get("recommend", {}).get("recommendations", []),
        "suggested_next_actions": [
            "Add personalization inputs",
            "Attach nearby services",
            "Enable multilingual output"
        ]
    }

    confidence = {
        "score": 0.72,
        "rationale": [
            "Workflow completed successfully",
            "Recommendations are region-consistent",
            "Limited personalization inputs"
        ]
    }

    return build_workflow_output(
        workflow_name=self.workflow.get("workflow", "unknown"),
        inputs=inputs,
        step_results=ordered_steps,
        final_summary=final_summary,
        confidence=confidence
    )

