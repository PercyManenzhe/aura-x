class ResponseAgent:
    def run(self, task: str, context: dict = None):
        """
        Orchestrator calls agent.run(task) (sometimes with context).
        We build a structured 'report' based on previous step outputs.
        """
        context = context or {}
        inputs = context.get("inputs", {})

        # The orchestrator stores previous step outputs by step name: context["recommend"], etc.
        recommend_output = context.get("recommend", {})
        recommendations = []
        if isinstance(recommend_output, dict):
            recommendations = recommend_output.get("recommendations", []) or []

        duration_days = int(inputs.get("duration_days", 2) or 2)
        if duration_days < 1:
            duration_days = 1

        # Simple day-by-day allocation
        day_by_day = []
        for day in range(1, duration_days + 1):
            idx = day - 1
            activities = [recommendations[idx]] if idx < len(recommendations) else []
            day_by_day.append({"day": day, "activities": activities})

        report = {
            "highlights": recommendations[:2],
            "day_by_day_plan": day_by_day,
            "safety_notes": [
                "Check weather conditions before travel.",
                "Keep emergency contacts saved and share your route with someone.",
            ],
            "estimated_cost_notes": [
                "Mid-range accommodation recommended (based on budget_level).",
                "Budget for entry fees, fuel, and meals.",
            ],
        }

        return {
            "agent": "ResponseAgent",
            "task": task,
            "report": report,
            "status": "structured_report_generated",
        }
