

from app.agents.orchestrator import AuraXOrchestrator






def main():
    print("🚀 Starting Aura-X Local Demo with YAML workflow")

    orchestrator = AuraXOrchestrator()
    result = orchestrator.run()

    print("\n🧠 Aura-X Output:")
    for step, output in result.items():
        print(f"{step.upper()}: {output}")

if __name__ == "__main__":
    main()



