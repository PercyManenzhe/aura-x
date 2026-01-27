from app.agents.orchestrator import AuraXOrchestrator

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


