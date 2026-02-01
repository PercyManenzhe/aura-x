import json

from app.agents.orchestrator import AuraXOrchestrator

def main():
    orchestrator = AuraXOrchestrator(yaml_path="workflows/municipal_ops.yaml")
    result = orchestrator.run(inputs={
        "municipality": "Example Local Municipality",
        "service": "streetlights",
        "issue": "outage",
        "area": "Ward 12",
        "priority": "high",
        "constraints": ["limited budget", "cable theft risk"]
    })


if __name__ == "__main__":
    main()
