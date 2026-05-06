# app/geospatial/gis_engine.py

class GISEngine:

    def map_province(self, province):
        """
        Convert intelligence into geo-visual data
        """

        return {
            "location": {
                "province": province.location.province,
                "municipality": province.location.municipality,
                "ward": province.location.ward
            },
            "risk_score": province.risk_score,
            "risk_level": province.risk_level,
            "coordinates": self._mock_coordinates(province)
        }

    def _mock_coordinates(self, province):
        # Replace later with real GIS lookup
        return {
            "lat": -26.2,
            "lng": 28.0
        }