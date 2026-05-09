class WardMapper:

    def map(self, province, risk_result=None):
        return {
            "ward": getattr(province.location, "ward", None),
            "municipality": province.location.municipality,
            "province": province.location.province,

            "risk": {
                "score": risk_result.get("risk_score", 0.0) if risk_result else 0.0,
                "level": risk_result.get("risk_level", "LOW") if risk_result else "LOW",
                "signals": risk_result.get("intelligence", {}).get("signals", []) if risk_result else []
            },

            "gis_layer": "ward_intelligence"
        }