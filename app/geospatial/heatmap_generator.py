class HeatmapGenerator:

    def generate(self, province, risk_result=None):
        location = getattr(province, "location", None) or province

        return {
            "ward": getattr(location, "ward", None),
            "municipality": getattr(location, "municipality", ""),
            "province": getattr(location, "province", ""),
            "risk_score": risk_result.get("risk_score", 0.0) if risk_result else 0.0,
            "risk_level": risk_result.get("risk_level", "LOW") if risk_result else "LOW",

            "heat": self._compute_heat(risk_result)
        }

    def _compute_heat(self, risk_result):
        if not risk_result:
            return "green"

        score = risk_result.get("risk_score", 0)

        if score >= 0.75:
            return "red"
        elif score >= 0.5:
            return "orange"
        elif score >= 0.25:
            return "yellow"
        return "green"