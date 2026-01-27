import yaml
from app.agents.orchestrator import AuraXOrchestrator
from app.services.llm_service import LLMService
from app.services.cloud_adapter import HuaweiCloudAdapter

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    print("🚀 Aura-X Local Demo Starting...")

    config = load_config()
    system = AuraXOrchestrator()
    llm = LLMService()
    cloud = HuaweiCloudAdapter()

    # Tourism demo
    location = config["tourism"]["default_location"]
    level = config["tourism"]["modes"][-1]  # Use highest mode, e.g., 4D
    print("\n🎮 Tourism Demo:")
    system.start_experience(mode="tourism", location=location, level=level)
    print(llm.generate_text(f"Describe {location} in immersive detail."))
    cloud.upload_data({"location": location, "mode": level})

    # Safety demo
    print("\n⛑ Safety Demo (Mine & Train):")
    for scenario, details in config["safety"].items():
        system.start_experience(mode="safety", location=scenario, level=details["risk_level"])
        print(llm.generate_text(f"Safety briefing for {scenario} with risk {details['risk_level']}"))
        cloud.upload_data({"scenario": scenario, "risk": details["risk_level"]})

    print("\n✅ Local demo completed successfully!")

if __name__ == "__main__":
    main()
