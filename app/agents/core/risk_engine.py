class RiskEngineV1:
    """
    Aura-X Risk Engine v1
    Computes multi-factor risk score for South African provinces
    """

    def calculate(self, province: dict):
        """
        province = UnifiedCityProvince (or simplified dict)
        """

        weather = province.get("weather_risk", "low")
        infra = province.get("infrastructure_status", "stable")
        population = province.get("population_density", "medium")
        service_failures = province.get("service_failures", [])

        score = 0
        signals = []

        # Weather Risk
        if weather == "severe":
            score += 30
            signals.append("Severe weather conditions")

        elif weather == "moderate":
            score += 15
            signals.append("Moderate weather risk")

        # Infrastructure Risk
        if infra == "critical":
            score += 30
            signals.append("Critical infrastructure stress")

        elif infra == "unstable":
            score += 20
            signals.append("Unstable infrastructure conditions")

        # Population density
        if population == "high":
            score += 20
            signals.append("High population exposure risk")

        elif population == "medium":
            score += 10

        # Service failures (electricity, water, roads, sewage)
        if len(service_failures) >= 2:
            score += 25
            signals.append("Multiple service failures detected")

        elif len(service_failures) == 1:
            score += 10
            signals.append("Single service failure detected")

        # Risk classification
        if score >= 70:
            level = "CRITICAL"
        elif score >= 40:
            level = "HIGH"
        elif score >= 20:
            level = "MEDIUM"
        else:
            level = "LOW"

        # Early warning logic
        warning = None
        if level in ["HIGH", "CRITICAL"]:
            warning = "Activate emergency readiness protocols"

        return {
            "province_risk_score": score,
            "risk_level": level,
            "signals": signals,
            "early_warning": warning
        }