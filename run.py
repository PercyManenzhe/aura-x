from app.agents.orchestrator import AuraXOrchestrator
reasoning_output = self.reasoning_agent.run(task, context)
results["reasoning"] = reasoning_output


def main():
    print("🚀 Starting Aura-X Virtual Tourism AI System")

    system = AuraXOrchestrator()
    system.start_experience(
        mode="tourism",
        location="Mpumalanga Panorama Route",
        level="4D"
    )

if __name__ == "__main__":
    main()



