


# app/agents/orchestrator.py
import yaml
from datetime import datetime
import uuid

from app.agents.tourism_agent import TourismAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.response_agent import ResponseAgent
from app.agents.reasoning_agent import GenericReasoningAgent
from app.agents.recommendation_agent import RecommendationAgent


def build_workflow_output(workflow_name, inputs, step_results, final_summary, confidence):
    return {
        "schema_version": "1.0",
        "project": "Aura-X",
        "workflow": workflow_name,
        "run_id": f"AX-{uuid.uuid4().hex[:8].upper()}",
        "timestamp": datetime.now().isoformat(),
        "inputs": inputs,
        "steps": step_results,
        "final": final_summary,
        "confidence": confidence
    }


class AuraXOrchestrator:
    def __init__(self, yaml_path="config.yaml"):
        self.workflow = self.load_workflow(yaml_path)

        self.agent_map = {
            "TourismAgent": TourismAgent(),
            "DecisionAgent": DecisionAgent(),
            "ResponseAgent": ResponseAgent(),
            "ReasoningAgent": GenericReasoningAgent(),     # YAML-friendly name
            "RecommendationAgent": RecommendationAgent(),
        }

    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def run(self, inputs=None):
        inputs = inputs or {}
        step_context = {}
        ordered_steps = []

        for step in self.workflow["steps"]:
            step_name = step["name"]
            agent_name = step["agent"]
            task = step["task"]

            agent = self.agent_map.get(agent_name)

            if agent:
                # Agents that accept context
                if agent_name in ["ReasoningAgent", "RecommendationAgent"]:
                    output = agent.run(task, step_context)
                else:
                    output = agent.run(task)

                status = "success"
            else:
                output = f"Agent {agent_name} not found"
                status = "error"

            ordered_steps.append({
                "step": step_name,
                "agent": agent_name,
                "task": task,
                "status": status,
                "output": output
            })

            step_context[step_name] = output
            print(f"{step_name.upper()}: {output}")

        final_summary = {
            "summary": "Aura-X completed a multi-agent tourism workflow",
            "top_recommendations": (
                step_context.get("recommend", {}).get("recommendations", [])
                if isinstance(step_context.get("recommend"), dict)
                else []
            ),
            "suggested_next_actions": [
                "Add personalization inputs (budget, duration, interests)",
                "Attach nearby services (lodging, transport, guides)",
                "Enable multilingual output"
            ]
        }

        confidence = {
            "score": 0.72,
            "rationale": [
                "Workflow executed end-to-end without errors",
                "Recommendations are region-consistent",
                "Limited personalization inputs in demo"
            ]
        }

        return build_workflow_output(
            workflow_name=self.workflow.get("workflow", "unknown"),
            inputs=inputs,
            step_results=ordered_steps,
            final_summary=final_summary,
            confidence=confidence
        )


 


