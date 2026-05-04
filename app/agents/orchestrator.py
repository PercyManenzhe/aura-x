


# app/agents/orchestrator.py

import yaml
from datetime import datetime
import uuid


# --- Import ALL agents (modular) ---
from app.agents.core.monitoring_agent import MonitoringAgent

# Municipal
from app.agents.municipal.municipal_ops_agent import MunicipalOpsAgent
from app.agents.municipal.municipal_reasoning_agent import MunicipalReasoningAgent
from app.agents.municipal.municipal_recommendation_agent import MunicipalRecommendationAgent
from app.agents.municipal.municipal_response_agent import MunicipalResponseAgent
from app.agents.municipal.municipal_decision_agent import MunicipalDecisionAgent
from app.agents.municipal.municipal_safety_agent import MunicipalSafetyAgent
from app.agents.municipal.municipal_monitoring_agent import MunicipalMonitoringAgent

# Mining (example)
from app.agents.mining.mining_safety_agent import MiningSafetyAgent
from app.agents.mining.mining_recommendation_agent import MiningRecommendationAgent


def build_workflow_output(workflow_name, run_id, inputs, step_results, final_summary, confidence):
    return {
        "schema_version": "2.0",
        "project": "Aura-X",
        "workflow": workflow_name,
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "inputs": inputs,
        "steps": step_results,
        "final": final_summary,
        "confidence": confidence
    }


class AuraXOrchestrator:
    def __init__(self, yaml_path):
        self.workflow = self.load_workflow(yaml_path)

        # 🔥 CLEAN modular agent registry
        self.agent_map = {
            # --- Core ---
            "MonitoringAgent": MonitoringAgent(),

            # --- Municipal ---
            "MunicipalOpsAgent": MunicipalOpsAgent(),
            "MunicipalReasoningAgent": MunicipalReasoningAgent(),
            "MunicipalDecisionAgent": MunicipalDecisionAgent(),
            "MunicipalRecommendationAgent": MunicipalRecommendationAgent(),
            "MunicipalSafetyAgent": MunicipalSafetyAgent(),
            "MunicipalResponseAgent": MunicipalResponseAgent(),
            "MunicipalMonitoringAgent": MunicipalMonitoringAgent(),

            # --- Mining ---
            "MiningSafetyAgent": MiningSafetyAgent(),
            "MiningRecommendationAgent": MiningRecommendationAgent(),
        }

    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def run(self, inputs=None):
        inputs = inputs or {}

        run_id = f"AX-{uuid.uuid4().hex[:8].upper()}"
        workflow_name = self.workflow.get("workflow", "unknown")

        step_context = {
            "inputs": inputs,
            "run_id": run_id,
            "workflow": workflow_name,
        }

        ordered_steps = []

        for step in self.workflow["steps"]:
            step_name = step["name"]
            agent_name = step["agent"]
            task = step["task"]

            agent = self.agent_map.get(agent_name)

            if not agent:
                output = f"Agent {agent_name} not found"
                status = "error"
            else:
                try:
                    output = agent.run(task, step_context)
                    status = "success"
                except Exception as e:
                    output = str(e)
                    status = "error"

            step_record = {
                "step": step_name,
                "agent": agent_name,
                "task": task,
                "status": status,
                "output": output,
            }

            ordered_steps.append(step_record)
            step_context[step_name] = output

            print(f"{step_name.upper()}: {output}")

        # ---- Confidence ----
        input_count = len(inputs.keys())
        score = 0.65 + min(0.25, input_count * 0.03)

        errors = [s for s in ordered_steps if s["status"] == "error"]
        if errors:
            score -= 0.2

        confidence = {
            "score": round(max(0.4, score), 2),
            "notes": [
                "Workflow executed",
                f"Inputs provided: {input_count}",
                "Errors detected" if errors else "No errors detected"
            ]
        }

        # ---- Monitoring (AUTO DETECT DOMAIN) ----
        monitoring_agent_name = next(
            (s["agent"] for s in self.workflow["steps"] if "MonitoringAgent" in s["agent"]),
            "MonitoringAgent"
        )

        monitoring = self.agent_map[monitoring_agent_name].run(
            "Capture metrics",
            {
                "workflow": workflow_name,
                "run_id": run_id,
                "steps": ordered_steps,
                "confidence": confidence,
            }
        )

        print(f"MONITOR: {monitoring}")

        final_summary = {
            "summary": f"Aura-X completed workflow: {workflow_name}",
            "top_actions": step_context.get("recommend", {}).get("recommendations", []),
            "decision": step_context.get("decision", {}),
            "monitoring": monitoring,
        }

        return build_workflow_output(
            workflow_name,
            run_id,
            inputs,
            ordered_steps,
            final_summary,
            confidence
        )