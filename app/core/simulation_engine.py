from typing import Dict, Any, List


class SimulationEngine:

    def simulate(self, province) -> Dict[str, Any]:
        """
        Runs future scenario simulations based on current province state
        """

        simulations = []

        # -----------------------------
        # ELECTRICITY OUTAGE SCENARIO
        # -----------------------------
        if province.infrastructure.electricity == "outage":

            simulations.append({
                "scenario": "Electricity Outage Escalation",
                "timeline": [
                    {"time": "1 hour", "impact": "Service disruption continues"},
                    {"time": "3 hours", "impact": "Increased crime risk due to darkness"},
                    {"time": "6 hours", "impact": "Public safety risk increases"},
                    {"time": "12 hours", "impact": "Critical infrastructure strain"},
                ],
                "risk_trend": "increasing"
            })

        # -----------------------------
        # FLOOD SCENARIO
        # -----------------------------
        if province.environment.flood_risk == "high":

            simulations.append({
                "scenario": "Flood Escalation",
                "timeline": [
                    {"time": "1 hour", "impact": "Water levels rising"},
                    {"time": "3 hours", "impact": "Roads may become inaccessible"},
                    {"time": "6 hours", "impact": "Homes at risk"},
                    {"time": "12 hours", "impact": "Evacuations required"},
                ],
                "risk_trend": "critical"
            })

        # -----------------------------
        # WATER FAILURE SCENARIO
        # -----------------------------
        if province.infrastructure.water in ["critical", "outage"]:

            simulations.append({
                "scenario": "Water Supply Crisis",
                "timeline": [
                    {"time": "2 hours", "impact": "Residents begin water shortage"},
                    {"time": "6 hours", "impact": "Sanitation issues arise"},
                    {"time": "12 hours", "impact": "Public health risk increases"},
                ],
                "risk_trend": "increasing"
            })

        # -----------------------------
        # GLOBAL RISK ESCALATION
        # -----------------------------
        if province.risk_score >= 0.7:
            simulations.append({
                "scenario": "Multi-System Stress",
                "timeline": [
                    {"time": "1 hour", "impact": "Pressure on emergency services"},
                    {"time": "4 hours", "impact": "Service delivery delays"},
                    {"time": "8 hours", "impact": "System-wide instability"},
                ],
                "risk_trend": "critical"
            })

        return {
            "total_scenarios": len(simulations),
            "scenarios": simulations
        }