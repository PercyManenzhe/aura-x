class GISEngine:
    """
    Converts Province Intelligence into GIS-ready data
    """

    def generate_map_data(self, province):
        return {
            "location": {
                "province": province.location.province,
                "municipality": province.location.municipality,
                "ward": province.location.ward,
            },
            "risk": {
                "score": province.risk_score,
                "level": province.risk_level,
            },
            "infrastructure": province.infrastructure,
            "environment": {
                "weather": province.environment.weather,
                "flood_risk": province.environment.flood_risk,
            }
        }