class RecommendationAgent:
    def run(self, task: str, context: dict | None = None):
        context = context or {}
        inputs = context.get("inputs", {})

        location = inputs.get("location", "Mpumalanga")
        season = inputs.get("season", "All-year")
        budget = inputs.get("budget_level", "mid")
        group = inputs.get("group_type", "general")
        duration = inputs.get("duration_days", 2)
        interests = inputs.get("interests", ["nature"])

        # Base pool (demo-safe)
        pool = [
            {"name": "Kruger National Park", "type": "nature", "budget": ["mid", "high"]},
            {"name": "Blyde River Canyon", "type": "nature", "budget": ["low", "mid", "high"]},
            {"name": "Pilgrim’s Rest", "type": "culture", "budget": ["low", "mid"]},
            {"name": "God’s Window", "type": "nature", "budget": ["low", "mid", "high"]},
            {"name": "Sudwala Caves", "type": "adventure", "budget": ["mid", "high"]},
        ]

        # Filter by interest + budget
        filtered = [
            p for p in pool
            if p["type"] in interests and budget in p["budget"]
        ]

        # If nothing matched, fall back to top picks
        if not filtered:
            filtered = pool[:4]

        # Limit by duration (simple heuristic)
        max_items = 3 if duration <= 2 else 5
        picks = filtered[:max_items]

        recommendations = [f"{p['name']} – {p['type'].title()} experience" for p in picks]

        return {
            "agent": "RecommendationAgent",
            "location": location,
            "season": season,
            "budget_level": budget,
            "group_type": group,
            "duration_days": duration,
            "interests": interests,
            "recommendations": recommendations,
        }
