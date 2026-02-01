from app.agents.orchestrator import AuraXOrchestrator

def main():
    orchestrator = AuraXOrchestrator(yaml_path="workflows/mining_safety.yaml")
    result = orchestrator.run(inputs={
        "site": "Underground Section A",
        "hazards": ["poor ventilation", "slippery walkway"],
        "incident_type": "near_miss",
        "shift": "night",
        "compliance_focus": ["PPE", "ventilation", "emergency_response"]
    })
    print("\n🧠 Aura-X Mining Output:\n")
    print(result)

if __name__ == "__main__":
    main()
