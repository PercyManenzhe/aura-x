from app.agents.orchestrator import AuraXOrchestrator
def run(self):
    results = {}
    context = {}

    for step in self.workflow["steps"]:
        step_name = step["name"]
        agent_name = step["agent"]
        task = step["task"]

        agent = self.agent_map.get(agent_name)

        if agent:
            if agent_name in ["ReasoningAgent", "RecommendationAgent"]:
                output = agent.run(task, context)
            else:
                output = agent.run(task)

            results[step_name] = output
            context[step_name] = output

            print(f"{step_name.upper()}: {output}")
        else:
            print(f"{step_name.upper()}: Agent {agent_name} not found")

    return results




