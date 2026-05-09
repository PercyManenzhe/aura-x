class SimulationEngine:

    def run(self, province, risk_result=None):
        return {
            "total_scenarios": 1,
            "scenarios": [
                {
                    "scenario": "Electricity Outage Escalation",
                    "timeline": [
                        {"time": "1 hour", "impact": "Service disruption continues"},
                        {"time": "3 hours", "impact": "Increased crime risk"},
                        {"time": "6 hours", "impact": "Public safety risk increases"},
                        {"time": "12 hours", "impact": "Critical infrastructure strain"}
                    ],
                    "risk_trend": "increasing"
                }
            ]
        }