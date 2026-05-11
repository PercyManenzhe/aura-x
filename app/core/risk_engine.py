from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class RiskWeights:
    infrastructure: float = 0.35
    crime: float = 0.25
    environment: float = 0.20
    service_failure: float = 0.20


class RiskEngine:
    """
    Aura-X Risk Engine v2 (Stable Unified Model)
    Works ONLY with UnifiedProvinceIntelligence objects
    """

    def __init__(self):
        self.weights = RiskWeights()

    # ---------------- MAIN ENTRY ----------------
    def compute(self, ctx) -> Dict[str, Any]:

        infra_score = self._infra_risk(ctx)
        crime_score = self._crime_risk(ctx)
        env_score = self._environment_risk(ctx)
        service_score = self._service_risk(ctx)

        risk_score = (
            infra_score * self.weights.infrastructure +
            crime_score * self.weights.crime +
            env_score * self.weights.environment +
            service_score * self.weights.service_failure
        )

        risk_level = self._classify(risk_score)
        early_warning = self._early_warning(risk_score, ctx)

        return {
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "early_warning": early_warning,

            "breakdown": {
                "infrastructure": infra_score,
                "crime": crime_score,
                "environment": env_score,
                "service_failure": service_score,
            },

            "intelligence": {
                "signals": self._risk_signals(ctx, risk_score),
                "drivers": {
                    "infrastructure": infra_score,
                    "crime": crime_score,
                    "environment": env_score,
                    "service_failure": service_score
                }
            },

            "gis_ready": True,
            "simulation_ready": True
        }

    # ---------------- INFRASTRUCTURE ----------------
        # ---------------- INFRASTRUCTURE ----------------
    def _infra_risk(self, ctx):

        infra = ctx.infrastructure

        score = 0.0

        if infra.get("electricity") == "outage":
            score += 0.6

        if infra.get("water") == "failure":
            score += 0.4

        if infra.get("roads") == "damaged":
            score += 0.3

        return min(score, 1.0)

    # ---------------- CRIME ----------------
    def _crime_risk(self, ctx):

        issue = " ".join(ctx.active_issues).lower()

        score = 0.2

        if "outage" in issue:
            score += 0.5

        if "dark" in issue:
            score += 0.3

        if "violent" in issue:
            score += 0.6

        return min(score, 1.0)

    # ---------------- ENVIRONMENT ----------------
    def _environment_risk(self, ctx):

        weather = ctx.environment.get("weather", "normal")

        mapping = {
            "normal": 0.1,
            "rain": 0.4,
            "storm": 0.7,
            "flood": 1.0
        }

        return mapping.get(weather, 0.1)

    # ---------------- SERVICE FAILURE ----------------
    def _service_risk(self, ctx):

        issue = " ".join(ctx.active_issues).lower()

        score = 0.1

        if "outage" in issue:
            score += 0.5

        if "failure" in issue:
            score += 0.4

        if "delay" in issue:
            score += 0.3

        return min(score, 1.0)

    # ---------------- CLASSIFICATION ----------------
    def _classify(self, score: float) -> str:

        if score >= 0.75:
            return "CRITICAL"

        elif score >= 0.5:
            return "HIGH"

        elif score >= 0.25:
            return "MEDIUM"

        return "LOW"

    # ---------------- EARLY WARNING ----------------
    def _early_warning(self, score: float, ctx) -> bool:

        infra = ctx.infrastructure

        return any([
            score >= 0.6,
            "outage" in " ".join(ctx.active_issues).lower(),
            infra.get("electricity") == "outage"
        ])

    # ---------------- SIGNALS ----------------
    def _risk_signals(self, ctx, score: float) -> List[str]:

        infra = ctx.infrastructure
        issue = " ".join(ctx.active_issues).lower()

        signals = []

        if score > 0.5:
            signals.append("high_risk_zone")

        if infra.get("electricity") == "outage":
            signals.append("power_failure_zone")

        if "outage" in issue:
            signals.append("service_disruption")

        return signals