from app.agents.tourism_agent import TourismAgent
from app.agents.safety_agent import SafetyAgent

class AuraXOrchestrator:
    def __init__(self):
        self.tourism_agent = TourismAgent()
        self.safety_agent = SafetyAgent()

    def start_experience(self, mode, location, level):
        print(f"🎮 Mode: {mode} | Location: {location} | Level: {level}")

        if mode == "tourism":
            self.tourism_agent.run(location, level)
        elif mode == "safety":
            self.safety_agent.run(location, level)
        else:
            print("❌ Unknown mode")

