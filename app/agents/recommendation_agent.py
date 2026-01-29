class RecommendationAgent:
    def run(self, task: str, context: dict | None = None):
        """
        Generates tourism recommendations based on reasoning output
        """

        context = context or {}

        location = context.get("location", "Mpumalanga")
        season = context.get("season", "All-year")
        visitor_type = context.get("visitor_type", "General")

        recommendations = [
            "Kruger National Park – wildlife safaris",
            "Blyde River Canyon – scenic viewpoints",
            "Pilgrim’s Rest – cultural heritage",
            "God’s Window – panoramic nature views",
        ]

        return {
            "agent": "RecommendationAgent",
            "location": location,
            "season": season,
            "visitor_type": visitor_type,
            "recommendations": recommendations,
        }
