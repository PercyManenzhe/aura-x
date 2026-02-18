from typing import Optional, Dict, Any
from app.services.context_engine import ContextEngine

class MunicipalOpsAgent:
    def __init__(self):
        self.ctx = ContextEngine()

    def run(self, task: str, step_context: Optional[Dict[str, Any]] = None) -> str:
        step_context = step_context or {}
        inputs = step_context.get("inputs", {})
        enriched_inputs = self.ctx.enrich(inputs)
        step_context["inputs"] = enriched_inputs

        # ...existing code...
        return f"MunicipalOpsAgent: Completed '{task}'"
    
    