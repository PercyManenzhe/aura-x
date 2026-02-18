from datetime import datetime

class ContextEngine:
    def enrich(self, inputs: dict) -> dict:
        # placeholder enrichment: time + simple weather hint + derived risk flags
        enriched = dict(inputs)
        enriched["timestamp_utc"] = datetime.utcnow().isoformat()

        service = (inputs.get("service") or "").lower()
        issue = (inputs.get("issue") or "").lower()

        risk = []
        if service in ["streetlights", "electricity"] and issue in ["outage", "no_signal"]:
            risk.append("public_safety_risk")
        if issue in ["tamper", "theft", "cable_theft"]:
            risk.append("security_risk")

        enriched["risk_flags"] = risk
        enriched["enrichment"] = {
            "weather": inputs.get("weather_hint") or "unknown (ready to integrate)",
            "map_ready": True
        }
        return enriched
