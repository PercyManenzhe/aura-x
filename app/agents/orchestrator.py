


# app/agents/orchestrator.py
import yaml
from datetime import datetime
import uuid


from app.agents.monitoring_agent import MonitoringAgent
from app.agents.tourism_agent import TourismAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.response_agent import ResponseAgent
from app.agents.reasoning_agent import GenericReasoningAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.mining_safety_agent import MiningSafetyAgent
from app.agents.mining_recommendation_agent import MiningRecommendationAgent
from app.agents.municipal_ops_agent import MunicipalOpsAgent
from app.agents.municipal_recommendation_agent import MunicipalRecommendationAgent



def build_workflow_output(workflow_name, run_id, inputs, step_results, final_summary, confidence):
    return {
        "schema_version": "1.0",
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
    def __init__(self, yaml_path="config.yaml"):
        self.yaml_path = yaml_path
        self.workflow = self.load_workflow(yaml_path)

        self.agent_map = {
            "TourismAgent": TourismAgent(),
            "DecisionAgent": DecisionAgent(),
            "ResponseAgent": ResponseAgent(),
            "ReasoningAgent": GenericReasoningAgent(),
            "RecommendationAgent": RecommendationAgent(),
            "MonitoringAgent": MonitoringAgent(),

            "MiningSafetyAgent": MiningSafetyAgent(),
            "MiningRecommendationAgent": MiningRecommendationAgent(),

            "MunicipalOpsAgent": MunicipalOpsAgent(),
            "MunicipalRecommendationAgent": MunicipalRecommendationAgent(),
        }


    def main():
        orchestrator = AuraXOrchestrator(yaml_path="workflows/mining_safety.yaml")
        result = orchestrator.run(inputs={
            "site": "Underground Section A",
            "hazards": ["poor ventilation", "slippery walkway"],
            "incident_type": "near_miss",
            "shift": "night",
            "compliance_focus": ["PPE", "ventilation", "emergency_response"],
        })
        print("\n🧠 Aura-X Mining Output:\n")
        print(result)
    
        # Example second run (municipal) — keeps variable scoped separately
        orchestrator2 = AuraXOrchestrator(yaml_path="workflows/municipal_ops.yaml")
        result2 = orchestrator2.run(inputs={
            "municipality": "Example Local Municipality",
            "service": "streetlights",
            "issue": "outage",
            "area": "Ward 12",
            "priority": "high",
            "constraints": ["limited budget", "cable theft risk"],
        })
        print("\n🧠 Aura-X Municipal Output:\n")
        print(result2)
    
    if __name__ == "__main__":
        main()


    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def run(self, inputs=None):
        inputs = inputs or {}

        # One run_id per execution (DO NOT generate inside loop)
        run_id = f"AX-{uuid.uuid4().hex[:8].upper()}"
        workflow_name = self.workflow.get("workflow", "unknown")

        step_context = {
            "inputs": inputs,
            "run_id": run_id,
            "workflow": workflow_name,
        }

        ordered_steps = []

        # Execute each step defined in YAML (skip MonitoringAgent if present)
        for step in self.workflow["steps"]:
            step_name = step["name"]
            agent_name = step["agent"]
            task = step["task"]

            # Skip monitor if you accidentally left it in YAML
            if agent_name == "MonitoringAgent" or step_name == "monitor":
                continue

            agent = self.agent_map.get(agent_name)

            if agent:
                if agent_name in [
                    "ReasoningAgent",
                    "RecommendationAgent",
                    "MiningRecommendationAgent",
                    "MunicipalRecommendationAgent",
                ]:
                    output = agent.run(task, step_context)
                else:
                    output = agent.run(task)

                status = "success"
            else:
                output = f"Agent {agent_name} not found"
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

        # ---- Confidence scoring (simple + explainable) ----
        input_count = len(inputs.keys())
        score = 0.60 + min(0.30, input_count * 0.03)

        errors = [s for s in ordered_steps if s["status"] == "error"]
        if errors:
            score = max(0.40, score - 0.20)

        confidence = {
            "score": round(score, 2),
            "rationale": [
                "Workflow executed end-to-end without errors"
                if not errors else "Workflow completed with missing agent(s)",
                "Recommendations aligned to user inputs where provided",
                f"Personalization inputs provided: {input_count}",
            ],
        }

        # ---- Monitoring (run AFTER loop so it sees steps + confidence) ----
        monitoring = self.agent_map["MonitoringAgent"].run(
            "Capture run metrics and audit trail",
            {
                "workflow": workflow_name,
                "run_id": run_id,
                "steps": ordered_steps,
                "confidence": confidence,
            }
        )

        print(f"MONITOR: {monitoring}")

        # ---- Summary ----
        final_summary = {
            "summary": f"Aura-X completed workflow: {workflow_name}",
            "top_recommendations": (
                step_context.get("recommend", {}).get("recommendations", [])
                if isinstance(step_context.get("recommend"), dict)
                else []
            ),
            "suggested_next_actions": [
                "Add richer inputs for higher personalization",
                "Enable multilingual output",
                "Connect to Huawei Cloud storage and logging (OBS/LTS)",
            ],
            "monitoring": monitoring,  
        }

        return build_workflow_output(
            workflow_name=workflow_name,
            run_id=run_id,
            inputs=inputs,
            step_results=ordered_steps,
            final_summary=final_summary,
            confidence=confidence,
        )
