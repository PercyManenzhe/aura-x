class WardMapper:

    def map(self, province, risk_result):

        return {
            "province": province,
            "risk_level": risk_result.get("classification", "UNKNOWN"),
            "mapped": True,
            "zones": [
                {
                    "ward": "Ward 12",
                    "status": "HIGH RISK"
                },
                {
                    "ward": "Ward 8",
                    "status": "MEDIUM RISK"
                }
            ]
        }