# app/agents/municipal/municipal_monitoring_agent.py
from app.agents.municipal.base_municipal_agent import BaseMunicipalAgent
from datetime import datetime
from app.core.unified_province_intelligence import UnifiedProvinceIntelligence

class MunicipalMonitoringAgent(BaseMunicipalAgent):
    def __init__(self):
        super().__init__("MunicipalMonitoringAgent")

    def run(self, task: str, context=None):
        context = context or {}
        province = context.get("province")

        event_count = 0
        if province is not None and hasattr(province, "event_log"):
            event_count = len(province.event_log)

        return {
            "agent": "MunicipalMonitoringAgent",
            "task": task,
            "workflow": context.get("workflow"),
            "run_id": context.get("run_id"),
            "steps": context.get("steps", []),
            "confidence": context.get("confidence", {}),
            "event_count": event_count,
        }