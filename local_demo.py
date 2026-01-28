
from app.agents.orchestrator import AuraXOrchestrator






def main():
    print("🚀 Starting Aura-X Local Demo")

    orchestrator = AuraXOrchestrator()
    result = orchestrator.run("Assess system readiness")

    print("\n🧠 Aura-X Output:")
    print(result)

if __name__ == "__main__":
    main()


