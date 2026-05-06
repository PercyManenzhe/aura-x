class HeatmapGenerator:
    

    def generate(self, province):
        """
        Convert risk into color zones
        """

        risk_score = province.risk_score

        if risk_score >= 0.75:
            color = "red"
        elif risk_score >= 0.4:
            color = "orange"
        else:
            color = "green"

        return {
            "ward": province.location.ward,
            "risk_score": risk_score,
            "color": color
        }