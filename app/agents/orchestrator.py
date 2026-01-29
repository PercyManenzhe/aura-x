

# app/agents/orchestrator.py
# app/agents/orchestrator.py

import yaml
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.tourism_agent import TourismAgent, DecisionAgent, ResponseAgent
from app.agents.reasoning_agent import ReasoningAgent


class AuraXOrchestrator:
    def __init__(self, yaml_path="config.yaml"):
        # Load workflow
        self.workflow = self.load_workflow(yaml_path)

        # Register all agents
        self.agent_map = {
            "TourismAgent": TourismAgent(),
            "DecisionAgent": DecisionAgent(),
            "ResponseAgent": ResponseAgent(),
            "ReasoningAgent": ReasoningAgent(),
            "RecommendationAgent": RecommendationAgent(),
        }

    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def run(self):
        results = {}

        for step in self.workflow["steps"]:
            step_name = step["name"]
            agent_name = step["agent"]
            task = step["task"]

            agent = self.agent_map.get(agent_name)

            if agent:
                output = agent.run(task)
                results[step_name] = output
                print(f"{step_name.upper()}: {output}")
            else:
                results[step_name] = f"Agent {agent_name} not found!"
                print(f"{step_name.upper()}: Agent {agent_name} not found!")


        return results

 


