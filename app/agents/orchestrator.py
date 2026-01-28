

import yaml
import yaml

from app.agents.tourism_agent import TourismAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.response_agent import ResponseAgent
from app.agents.reasoning_agent import ReasoningAgent


class AuraXOrchestrator:
    def __init__(self, yaml_path="config.yaml"):
        self.workflow = self.load_workflow(yaml_path)

        self.agent_map = {
            "TourismAgent": TourismAgent(),
            "DecisionAgent": DecisionAgent(),
            "ResponseAgent": ResponseAgent(),
            "ReasoningAgent": ReasoningAgent(),
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
                print(f"{step_name.upper()}: Agent {agent_name} not found!")
                results[step_name] = f"Agent {agent_name} not found!"

        return results




