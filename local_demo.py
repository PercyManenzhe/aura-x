


# instantiate orchestrator before use
from app.agents.orchestrator import AuraXOrchestrator
import json

def main():
    orchestrator = AuraXOrchestrator()

    result = orchestrator.run(
        inputs={
            "location": "Mpumalanga",
            "season": "All-year",
            "visitor_type": "General"
        }
    )

    print("\n🧠 Aura-X Structured Output:\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()




