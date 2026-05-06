import yaml

import uuid
from datetime import datetime, timezone

#================== APP ==================
from app.geospatial.gis_engine import GISEngine
from app.geospatial.ward_mapper import WardMapper
from app.geospatial.heatmap_generator import HeatmapGenerator

# ================= CORE =================
from app.core.unified_province_intelligence import UnifiedProvinceIntelligence
from app.core.risk_engine import RiskEngine
from app.core.location_context import LocationContext
from app.core.simulation_engine import SimulationEngine
# ================= MUNICIPAL =================
from app.agents.municipal.municipal_ops_agent import MunicipalOpsAgent
from app.agents.municipal.municipal_reasoning_agent import MunicipalReasoningAgent
from app.agents.municipal.municipal_recommendation_agent import MunicipalRecommendationAgent
from app.agents.municipal.municipal_response_agent import MunicipalResponseAgent
from app.agents.municipal.municipal_decision_agent import MunicipalDecisionAgent
from app.agents.municipal.municipal_safety_agent import MunicipalSafetyAgent
from app.agents.municipal.municipal_monitoring_agent import MunicipalMonitoringAgent

# ================= MINING =================
from app.agents.mining.mining_safety_agent import MiningSafetyAgent
from app.agents.mining.mining_recommendation_agent import MiningRecommendationAgent

# ================= TOURISM =================
from app.agents.tourism.tourism_safety_agent import TourismSafetyAgent
from app.agents.tourism.tourism_recommendation_agent import TourismRecommendationAgent



def build_workflow_output(workflow_name, run_id, inputs, steps, final, confidence):
    return {
        "schema_version": "2.0",
        "project": "Aura-X",
        "workflow": workflow_name,
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "inputs": inputs,
        "steps": steps,
        "final": final,
        "confidence": confidence,
    }



class AuraXOrchestrator:
    def __init__(self, yaml_path):
        self.workflow = self.load_workflow(yaml_path)       
        
        
        
        self.agent_map = {
            "MunicipalOpsAgent": MunicipalOpsAgent(),
            "MunicipalReasoningAgent": MunicipalReasoningAgent(),
            "MunicipalRecommendationAgent": MunicipalRecommendationAgent(),
            "MunicipalResponseAgent": MunicipalResponseAgent(),
            "MunicipalDecisionAgent": MunicipalDecisionAgent(),
            "MunicipalSafetyAgent": MunicipalSafetyAgent(),
            "MunicipalMonitoringAgent": MunicipalMonitoringAgent(),
 
            "MiningSafetyAgent": MiningSafetyAgent(),
            "MiningRecommendationAgent": MiningRecommendationAgent(),


            "TourismSafetyAgent": TourismSafetyAgent(),
            "TourismRecommendationAgent": TourismRecommendationAgent(),
        }


    def load_workflow(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)


    def initialize_province(self, inputs):
        province = UnifiedProvinceIntelligence(
            location=LocationContext(
                province=inputs.get("province", ""),
                municipality=inputs.get("municipality", ""),
                ward=inputs.get("area"),
                area_type="township"
            ),
            population_density="high"
        )

        issue = inputs.get("issue", "")
        if issue:
            province.set_issue(issue)

            issue_lower = issue.lower()

            if "electricity" in issue_lower:
                province.update_infrastructure("electricity", "outage")

            if "water" in issue_lower:
                province.update_infrastructure("water", "critical")

            if "road" in issue_lower:
                province.update_infrastructure("roads", "damaged")

            if "storm" in issue_lower or "rain" in issue_lower:
                province.environment.weather = "storm"

        return province

    def run(self, inputs=None):
        inputs = inputs or {}

        run_id = f"AX-{uuid.uuid4().hex[:8].upper()}"
        workflow_name = self.workflow.get("workflow", "unknown")

        province = self.initialize_province(inputs)

        risk_engine = RiskEngine()
        risk_engine.compute(province)

        step_context = {
            "province": province,
            "run_id": run_id,
            "workflow": workflow_name,
            "inputs": inputs
        }

        steps_output = []

        for step in self.workflow.get("steps", []):
            step_name = step.get("name")
            agent_name = step.get("agent")
            task = step.get("task")

            agent = self.agent_map.get(agent_name)

            if not agent:
                output = {"error": f"Missing agent {agent_name}"}
                status = "error"
            else:
                try:
                    output = agent.run(task, step_context)
                    status = "success"
                except Exception as e:
                    output = {"exception": str(e)}
                    status = "error"

            steps_output.append({
                "step": step_name,
                "agent": agent_name,
                "status": status,
                "output": output
            })

            step_context[step_name] = output

        errors = [s for s in steps_output if s["status"] == "error"]

        confidence = {
            "score": 0.75 if not errors else 0.55,
            "notes": [
                f"Steps: {len(steps_output)}",
                f"Errors: {len(errors)}"
            ]
        }

        monitoring = MunicipalMonitoringAgent().run("monitor", {
            "workflow": workflow_name,
            "run_id": run_id,
            "steps": steps_output,
            "confidence": confidence
        })

        final = {
            "summary": "Aura-X execution completed",
            "province_intelligence": province.summary(),
            "monitoring": monitoring
        }

        return build_workflow_output(
            workflow_name,
            run_id,
            inputs,
            steps_output,
            final,
            confidence
        )


if __name__ == "__main__":
    orch = AuraXOrchestrator("workflows/municipal_ops.yaml")

    result = orch.run({
        "province": "Mpumalanga",
        "municipality": "Gert Sibande",
        "issue": "electricity outage in township",
        "area": "Ward 12"
    })


    print(result)