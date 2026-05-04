from typing import Optional, Dict, Any
from app.services.context_engine import ContextEngine

ISSUE_MAP = {
    "water": ["no water", "burst pipe", "low pressure"],
    "electricity": ["outage", "power failure", "street lights"],
    "roads": ["potholes", "road damage", "bridge risk"],
    "waste": ["collection delay", "illegal dumping"],
    "climate": ["flood", "heavy rain", "drought"],
    "Building": ["Aged", "Destroyed", "unsafe", "dilapidated", "crumbling", "collapsed", "structural damage", "hazardous"]
}

class MunicipalOpsAgent:
    def __init__(self):
        self.ctx = ContextEngine()

    def classify_issue(self, issue: str):
        issue = issue.lower()
        for category, keywords in ISSUE_MAP.items():
            if any(k in issue for k in keywords):
                return category
        return "general"

    def run(self, task: str, step_context: Optional[Dict[str, Any]] = None):
        step_context = step_context or {}
        inputs = step_context.get("inputs", {})
        enriched_inputs = self.ctx.enrich(inputs)

        issue = enriched_inputs.get("issue", "")
        category = self.classify_issue(issue)

        enriched_inputs["service_area"] = category

        # Add SA context awareness
        enriched_inputs["context"] = {
            "area_type": enriched_inputs.get("area_type", "township"),
            "population_density": "high",
            "country": "South Africa"
        }

        step_context["inputs"] = enriched_inputs

        return {
            "agent": "MunicipalOpsAgent",
            "classified_service_area": category,
            "inputs": enriched_inputs
        }
    
    