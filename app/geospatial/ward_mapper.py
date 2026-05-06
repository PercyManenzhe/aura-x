# app/geospatial/ward_mapper.py

class WardMapper:

    def map_ward_risk(self, province):
        """
        Break risk into ward-level structure
        """

        ward = province.location.ward or "Unknown"

        return {
            "ward": ward,
            "risk_score": province.risk_score,
            "risk_level": province.risk_level,
            "issues": province.active_issues,
            "alerts": getattr(province, "alerts", [])
        }