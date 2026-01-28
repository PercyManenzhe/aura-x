

from app.agents.orchestrator import AuraXOrchestrator






def main():
    orchestrator = AuraXOrchestrator("config.yaml")
    results = orchestrator.run()
    print("\n🧠 Aura-X Output:")
    for step, output in results.items():
        print(f"{step.upper()}: {output}")

if __name__ == "__main__":
    main()




