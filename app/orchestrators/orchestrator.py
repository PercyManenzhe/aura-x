import yaml
import uuid
from datetime import datetime, timezone

# ================= GEOSPATIAL =================
from app.geospatial.gis_engine import GISEngine
from app.geospatial.heatmap_generator import HeatmapGenerator
from app.geospatial.ward_mapper import WardMapper

# ================= CORE =================
from app.core.risk_engine import RiskEngine
from app.core.simulation_engine import SimulationEngine
from app.core.intelligence_packet import IntelligencePacket

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


def build_workflow_output(
    workflow_name,
    run_id,
    inputs,
    steps,
    final,
    confidence
):
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

    # ================= LOAD WORKFLOW =================
    def load_workflow(self, path):

        with open(path, "r") as f:
            return yaml.safe_load(f)

        # ================= INITIALIZE PACKET =================
    def initialize_packet(self, inputs, run_id):

        packet = IntelligencePacket(
            run_id=run_id,
            workflow=self.workflow.get("workflow", "unknown"),
            province=inputs.get("province", ""),
            municipality=inputs.get("municipality", ""),
            ward=inputs.get("area", ""),
            issue=inputs.get("issue", "")
        )

        issue = packet.issue.lower()

        if "electricity" in issue:
            packet.infrastructure["electricity"] = "outage"

        if "water" in issue:
            packet.infrastructure["water"] = "failure"

        if "road" in issue:
            packet.infrastructure["roads"] = "damaged"

        if "storm" in issue or "rain" in issue:
            packet.environment["weather"] = "storm"

        return packet

    # ================= MAIN RUN =================
    def run(self, inputs=None):

        inputs = inputs or {}

        run_id = f"AX-{uuid.uuid4().hex[:8].upper()}"
        workflow_name = self.workflow.get("workflow", "unknown")

        # 1. Initialize Packet
        packet = self.initialize_packet(inputs, run_id)

        # 2. Risk Engine
        risk_engine = RiskEngine()
        risk_result = risk_engine.compute(packet)
        packet.risk = risk_result

        # 3. GIS
        gis_engine = GISEngine()
        heatmap = HeatmapGenerator()
        mapper = WardMapper()

        map_data = gis_engine.generate_map_data(
            packet,
            risk_result
        )

        packet.set_gis(map_data)

        heatmap_data = heatmap.generate(
            packet.province,
            risk_result
        )

        ward_data = mapper.map(
            packet.province,
            risk_result
        )

        # 4. Simulation
        simulation_engine = SimulationEngine()

        simulation_results = simulation_engine.run(
            packet,
            risk_result
        )

        packet.set_simulation(simulation_results)

        # 5. Context
        step_context = {
            "packet": packet,
            "risk": risk_result,
            "gis": map_data,
            "simulation": simulation_results,
            "run_id": run_id,
            "workflow": workflow_name,
            "inputs": inputs
        }

        steps_output = []

        # 6. Execute workflow agents
        for step in self.workflow.get("steps", []):

            step_name = step.get("name")
            agent_name = step.get("agent")
            task = step.get("task")

            agent = self.agent_map.get(agent_name)

            if not agent:
                output = {
                    "error": f"Missing agent {agent_name}"
                }
                status = "error"

            else:
                try:
                    output = agent.run(task, step_context)
                    status = "success"

                except Exception as e:
                    output = {
                        "exception": str(e)
                    }
                    status = "error"

            steps_output.append({
                "step": step_name,
                "agent": agent_name,
                "status": status,
                "output": output
            })

            step_context[step_name] = output

        # 7. Confidence
        errors = [
            s for s in steps_output
            if s["status"] == "error"
        ]

        confidence = {
            "score": 0.75 if not errors else 0.55,
            "notes": [
                f"Steps: {len(steps_output)}",
                f"Errors: {len(errors)}"
            ]
        }

        # 8. Monitoring
        monitoring = MunicipalMonitoringAgent().run(
            "monitor",
            {
                "workflow": workflow_name,
                "run_id": run_id,
                "steps": steps_output,
                "confidence": confidence
            }
        )

        # 9. Final Output
        final = {
            "summary": "Aura-X execution completed",

            "intelligence_packet": packet.summary(),

            "monitoring": monitoring,

            "gis": {
                "map_data": map_data,
                "heatmap": heatmap_data,
                "ward_data": ward_data
            },

            "simulation": simulation_results
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