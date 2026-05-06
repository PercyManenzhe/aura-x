# app/geospatial/heatmap_generator.py

class HeatmapGenerator:

    def generate(self, ward_data):
        """
        Convert risk into heatmap intensity
        """

        score = ward_data["risk_score"]

        if score >= 0.8:
            color = "red"
        elif score >= 0.6:
            color = "orange"
        elif score >= 0.4:
            color = "yellow"
        else:
            color = "green"

        return {
            "ward": ward_data["ward"],
            "intensity": score,
            "color": color,
            "alerts": ward_data["alerts"]
        }