import yaml
from datetime import datetime
import uuid

# ---------------- CORE ----------------
from ..agents.core.monitoring_agent import MonitoringAgent as CoreMonitoringAgent

# ---------------- MUNICIPAL ----------------
from app.agents.municipal.municipal_ops_agent import MunicipalOpsAgent
from app.agents.municipal.municipal_reasoning_agent import MunicipalReasoningAgent
from app.agents.municipal.municipal_recommendation_agent import MunicipalRecommendationAgent
from app.agents.municipal.municipal_response_agent import MunicipalResponseAgent
from app.agents.municipal.municipal_decision_agent import MunicipalDecisionAgent
from app.agents.municipal.municipal_safety_agent import MunicipalSafetyAgent
from app.agents.municipal.municipal_monitoring_agent import MunicipalMonitoringAgent

# ---------------- MINING ----------------
from app.agents.mining.mining_safety_agent import MiningSafetyAgent
from app.agents.mining.mining_recommendation_agent import MiningRecommendationAgent

# --------------- TOURISM ----------------
from app.agents.tourism.tourism_safety_agent import TourismSafetyAgent
from app.agents.tourism.tourism_recommendation_agent import TourismRecommendationAgent


# =========================================================
# OUTPUT BUILDER
# =========================================================
def build_workflow_output(workflow_name, run_id, inputs, steps, final, confidence):
    return {
        "schema_version": "2.0",
        "project": "Aura-X",
        "workflow": workflow_name,
        "run_id": run_id,
        "timestamp": datetime.now().isoformat(),
        "inputs": inputs,
        "steps": steps,
        "final": final,
        "confidence": confidence,
    }


# =========================================================
# ORCHESTRATOR
# =========================================================
class AuraXOrchestrator:
    def __init__(self, yaml_path):
        self.workflow = self.load_workflow(yaml_path)

        # SAFE AGENT REGISTRY (NO BREAKS IF MISSING)
        self.agent_map = {
            # Core
            "MonitoringAgent": CoreMonitoringAgent(),

            # Municipal
            "MunicipalOpsAgent": MunicipalOpsAgent(),
            "MunicipalReasoningAgent": MunicipalReasoningAgent(),
            "MunicipalRecommendationAgent": MunicipalRecommendationAgent(),
            "MunicipalResponseAgent": MunicipalResponseAgent(),
            "MunicipalDecisionAgent": MunicipalDecisionAgent(),
            "MunicipalSafetyAgent": MunicipalSafetyAgent(),
            "MunicipalMonitoringAgent": MunicipalMonitoringAgent(),

            # Mining
            "MiningSafetyAgent": MiningSafetyAgent(),
            "MiningRecommendationAgent": MiningRecommendationAgent(),
        }

    # -----------------------------------------------------
    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    # -----------------------------------------------------
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

        # =====================================================
        # EXECUTE WORKFLOW STEPS
        # =====================================================
        for step in self.workflow.get("steps", []):
            step_name = step.get("name")
            agent_name = step.get("agent")
            task = step.get("task", "")

            agent = self.agent_map.get(agent_name)

            if not agent:
                output = f"[ERROR] Agent not found: {agent_name}"
                status = "error"
            else:
                try:
                    output = agent.run(task, step_context)
                    status = "success"
                except Exception as e:
                    output = f"[EXCEPTION] {str(e)}"
                    status = "error"

            step_result = {
                "step": step_name,
                "agent": agent_name,
                "task": task,
                "status": status,
                "output": output,
            }

            ordered_steps.append(step_result)

            # store in context for next agents
            step_context[step_name] = output

            print(f"{step_name.upper()}: {output}")

        # =====================================================
        # CONFIDENCE ENGINE
        # =====================================================
        input_count = len(inputs)

        base_score = 0.65
        bonus = min(0.25, input_count * 0.03)

        errors = [s for s in ordered_steps if s["status"] == "error"]

        if errors:
            base_score -= 0.2

        confidence = {
            "score": round(max(0.4, base_score + bonus), 2),
            "notes": [
                "Workflow executed successfully" if not errors else "Workflow completed with errors",
                f"Inputs provided: {input_count}",
                f"Steps executed: {len(ordered_steps)}",
            ],
        }

        # =====================================================
        # MONITORING (SAFE)
        # =====================================================
        monitoring_agent = self.agent_map.get("MunicipalMonitoringAgent") \
            or self.agent_map.get("MonitoringAgent")

        monitoring = None

        if monitoring_agent:
            monitoring = monitoring_agent.run(
                "Capture metrics",
                {
                    "workflow": workflow_name,
                    "run_id": run_id,
                    "steps": ordered_steps,
                    "confidence": confidence,
                },
            )

        print(f"MONITOR: {monitoring}")

        # =====================================================
        # FINAL SUMMARY
        # =====================================================
        recommendations = step_context.get("recommend", {})
        decision = step_context.get("decision", {})

        final_summary = {
            "summary": f"Aura-X completed workflow: {workflow_name}",
            "top_actions": recommendations.get("recommendations", [])
            if isinstance(recommendations, dict)
            else [],
            "decision": decision if isinstance(decision, dict) else {},
            "monitoring": monitoring,
        }

        return build_workflow_output(
            workflow_name,
            run_id,
            inputs,
            ordered_steps,
            final_summary,
            confidence,
        )


# =========================================================
# OPTIONAL LOCAL TEST
# =========================================================
if __name__ == "__main__":
    orchestrator = AuraXOrchestrator(
    yaml_path="workflows/municipal_ops.yaml"
)

    result = orchestrator.run(
        inputs={
            "municipality": "Gert Sibande",
            "issue": "electricity outage in township",
            "area": "Ward 12",
            "priority": "high",
        }
    )

    print("\nFINAL OUTPUT:\n")
    print(result)