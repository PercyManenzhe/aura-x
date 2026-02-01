import os
from datetime import datetime
import json
import argparse
from unittest import result
from app.agents.orchestrator import AuraXOrchestrator

WORKFLOW_MAP = {
    "tourism": "config.yaml",
    "mining": "workflows/mining_safety.yaml",
    "municipal": "workflows/municipal_ops.yaml",
}
from app.services.storage_adapter import save_run_local

path = save_run_local(result)
print(f"\n✅ Saved run output to: {path}")

DEFAULT_INPUTS = {
    "tourism": {
        "location": "Mpumalanga",
        "season": "All-year",
        "visitor_type": "General",
        "budget_level": "mid",
        "group_type": "family",
        "duration_days": 3,
        "interests": ["nature", "culture"],
    },
    "mining": {
        "site": "Underground Section A",
        "hazards": ["poor ventilation", "slippery walkway"],
        "incident_type": "near_miss",
        "shift": "night",
        "compliance_focus": ["PPE", "ventilation", "emergency_response"],
    },
    "municipal": {
        "municipality": "Example Local Municipality",
        "service": "streetlights",
        "issue": "outage",
        "area": "Ward 12",
        "priority": "high",
        "constraints": ["limited budget", "cable theft risk"],
    },
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", choices=["tourism", "mining", "municipal"], default="tourism")
    args = parser.parse_args()

    yaml_path = WORKFLOW_MAP[args.workflow]
    inputs = DEFAULT_INPUTS[args.workflow]

    orchestrator = AuraXOrchestrator(yaml_path=yaml_path)
    result = orchestrator.run(inputs=inputs)
              # Save run to /runs folder
    os.makedirs("runs", exist_ok=True)

    run_id = result.get("run_id", "AX-UNKNOWN")
    workflow = result.get("workflow", args.workflow)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"runs/{workflow}_{run_id}_{ts}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved run output to: {filename}")


    print(f"\n🧠 Aura-X Output ({args.workflow.upper()}) (JSON):\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
