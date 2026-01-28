

import yaml

# Example AI Agents (temporary stubs for now)
class TourismAgent:
    def run(self, task: str):
        return f"TourismAgent: Completed '{task}'"

class DecisionAgent:
    def run(self, task: str):
        return f"DecisionAgent: Completed '{task}'"

class ResponseAgent:
    def run(self, task: str):
        return f"ResponseAgent: Completed '{task}'"


class AuraXOrchestrator:
    def __init__(self, yaml_path="config.yaml"):
        self.workflow = self.load_workflow(yaml_path)
        self.agent_map = {
            "TourismAgent": TourismAgent(),
            "DecisionAgent": DecisionAgent(),
            "ResponseAgent": ResponseAgent(),
        }

    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def run(self):
        results = {}
        for step in self.workflow["steps"]:
            agent_name = step["agent"]
            task = step["task"]
            agent = self.agent_map.get(agent_name)
            if agent:
                results[step["name"]] = agent.run(task)
            else:
                results[step["name"]] = f"Agent {agent_name} not found!"
        return results



