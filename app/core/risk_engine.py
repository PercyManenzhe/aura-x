from typing import List


class RiskEngine:

    def __init__(self):
        # -----------------------------
        # WEIGHTS (tunable later via YAML)
        # -----------------------------
        self.weights = {
            "infrastructure": 0.4,
            "environment": 0.2,
            "population": 0.2,
            "active_issues": 0.2
        }

    # =====================================================
    # MAIN ENTRY
    # =====================================================
    def compute(self, province):
        """
        Main intelligence computation
        """

        infra_score = self._score_infrastructure(province)
        env_score = self._score_environment(province)
        pop_score = self._score_population(province)
        issue_score = self._score_issues(province)

        # -----------------------------
        # FINAL SCORE (0 → 1)
        # -----------------------------
        total_score = (
            infra_score * self.weights["infrastructure"] +
            env_score * self.weights["environment"] +
            pop_score * self.weights["population"] +
            issue_score * self.weights["active_issues"]
        )

        province.risk_score = round(total_score, 2)

        # -----------------------------
        # RISK LEVEL
        # -----------------------------
        province.risk_level = self._get_risk_level(province.risk_score)

        # -----------------------------
        # ALERTS
        # -----------------------------
        province.alerts = self._generate_alerts(province)

        # -----------------------------
        # EARLY WARNING / EMERGENCY
        # -----------------------------
        province.early_warning = province.risk_score >= 0.6
        province.emergency = province.risk_score >= 0.8

        return province

    # =====================================================
    # INFRASTRUCTURE SCORING
    # =====================================================
    def _score_infrastructure(self, province):
        score = 0.0

        infra = province.infrastructure

        if infra.electricity == "outage":
            score += 0.4

        if infra.water in ["critical", "outage"]:
            score += 0.3

        if infra.sewage in ["overflow", "critical"]:
            score += 0.3

        if infra.roads in ["damaged", "blocked"]:
            score += 0.2

        return min(score, 1.0)

    # =====================================================
    # ENVIRONMENT SCORING
    # =====================================================
    def _score_environment(self, province):
        env = province.environment
        score = 0.0

        if env.weather == "storm":
            score += 0.3

        if env.flood_risk == "high":
            score += 0.5

        if env.rainfall_level == "high":
            score += 0.2

        return min(score, 1.0)

    # =====================================================
    # POPULATION SCORING
    # =====================================================
    def _score_population(self, province):
        density = province.population_density

        if density == "high":
            return 0.7
        elif density == "medium":
            return 0.4
        else:
            return 0.2

    # =====================================================
    # ISSUE SCORING
    # =====================================================
    def _score_issues(self, province):
        issues = province.active_issues

        if not issues:
            return 0.0

        score = 0.0

        for issue in issues:
            issue_lower = issue.lower()

            if "electricity" in issue_lower:
                score += 0.4

            if "water" in issue_lower:
                score += 0.3

            if "flood" in issue_lower:
                score += 0.5

            if "fire" in issue_lower:
                score += 0.6

        return min(score, 1.0)

    # =====================================================
    # RISK LEVEL
    # =====================================================
    def _get_risk_level(self, score):
        if score >= 0.8:
            return "CRITICAL"
        elif score >= 0.6:
            return "HIGH"
        elif score >= 0.4:
            return "MEDIUM"
        else:
            return "LOW"

    # =====================================================
    # ALERT GENERATION
    # =====================================================
    def _generate_alerts(self, province) -> List[str]:
        alerts = []

        infra = province.infrastructure
        env = province.environment

        # -----------------------------
        # INFRA ALERTS
        # -----------------------------
        if infra.electricity == "outage":
            alerts.append("Power outage detected — increased crime and safety risk")

        if infra.water in ["critical", "outage"]:
            alerts.append("Water supply disruption — public health risk")

        if infra.sewage == "overflow":
            alerts.append("Sewage overflow — environmental hazard")

        if infra.roads == "blocked":
            alerts.append("Road blockage — emergency response delays")

        # -----------------------------
        # ENVIRONMENT ALERTS
        # -----------------------------
        if env.flood_risk == "high":
            alerts.append("Flood risk high — evacuation may be required")

        if env.weather == "storm":
            alerts.append("Severe weather — infrastructure instability risk")

        # -----------------------------
        # POPULATION AMPLIFIER
        # -----------------------------
        if province.population_density == "high":
            alerts.append("High population density — risk impact amplified")

        return alerts