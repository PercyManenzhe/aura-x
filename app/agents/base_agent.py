from app.core.unified_province_intelligence import UnifiedProvinceIntelligence


class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def get_inputs(self, context):
        return context.get("inputs", {})

    def get_brain(self, context) -> UnifiedProvinceIntelligence:
        return context.get("brain")

    def run(self, task: str, context=None):
        raise NotImplementedError("Each agent must implement run()")