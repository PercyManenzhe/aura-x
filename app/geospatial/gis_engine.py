class GISEngine:

    def generate_map_data(self, province, risk_result=None):

        # -----------------------------
        # SAFE LOCATION EXTRACTION
        # -----------------------------
        location = getattr(province, "location", province)

        # -----------------------------
        # RISK SAFE FALLBACK
        # -----------------------------
        risk_result = risk_result or {}

        # -----------------------------
        # BUILD MAP OUTPUT
        # -----------------------------
        return {
            "location": {
                "country": getattr(location, "country", "South Africa"),
                "province": getattr(location, "province", ""),
                "municipality": getattr(location, "municipality", ""),
                "ward": getattr(location, "ward", None),
            },

            "risk": {
                "score": risk_result.get("risk_score", 0.0),
                "level": risk_result.get("risk_level", "LOW"),
                "signals": risk_result.get("intelligence", {}).get("signals", []),
            },

            "infrastructure": {
                "electricity": getattr(getattr(province, "infrastructure", None), "electricity", "unknown"),
                "water": getattr(getattr(province, "infrastructure", None), "water", "unknown"),
                "roads": getattr(getattr(province, "infrastructure", None), "roads", "unknown"),
                "telecoms": getattr(getattr(province, "infrastructure", None), "telecoms", "unknown"),
            },

            "environment": {
                "weather": getattr(getattr(province, "environment", None), "weather", "normal"),
                "flood_risk": getattr(getattr(province, "environment", None), "flood_risk", "low"),
            },

            "gis_ready": True
        }