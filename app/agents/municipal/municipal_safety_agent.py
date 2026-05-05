class MunicipalSafetyAgent:
    def run(self, task: str, context=None):
        context = context or {}

        reasoning = context.get("reasoning", {})
        analyze = context.get("analyze", {})

        risks = reasoning.get("risks", [])
        service_area = analyze.get("service_area", "")
        area_context = analyze.get("inputs", {}).get("context", {})

        population_density = area_context.get("population_density", "unknown")

        safety_measures = []

        # ----------------------------------------
        # ELECTRICITY RISKS
        # ----------------------------------------
        if service_area == "electricity":
            safety_measures.extend([
                "Deploy backup generators to clinics and critical facilities",
                "Provide temporary lighting in high-risk zones",
                "Increase patrol visibility in affected areas",
                "Coordinate with SAPS and community policing forums",
            ])

        # ----------------------------------------
        # CRIME / GENERAL SAFETY RISKS
        # ----------------------------------------
        for risk in risks:
            if "crime" in risk.lower():
                safety_measures.extend([
                    "Increase visible policing in affected areas",
                    "Activate community safety patrols",
                ])

        # ----------------------------------------
        # STORMS / WEATHER RISKS
        # ----------------------------------------
        if "storm" in str(risks).lower():
            safety_measures.extend([
                "Issue severe weather alerts",
                "Deploy emergency response teams",
                "Inspect and secure infrastructure",
            ])

        # ----------------------------------------
        # WATER / DRAINAGE / FLOODING
        # ----------------------------------------
        if "water" in service_area or "flood" in str(risks).lower():
            safety_measures.extend([
                "Clear blocked drainage systems",
                "Deploy water pumps in flooded areas",
                "Restrict access to high-risk zones",
            ])

        # ----------------------------------------
        # SEWAGE / HEALTH RISKS
        # ----------------------------------------
        if "sewage" in str(risks).lower():
            safety_measures.extend([
                "Isolate contaminated areas",
                "Deploy sanitation teams immediately",
                "Provide temporary sanitation facilities",
                "Issue public health warnings",
            ])

        # ----------------------------------------
        # FIRE RISKS (Informal settlements)
        # ----------------------------------------
        if "fire" in str(risks).lower():
            safety_measures.extend([
                "Deploy fire response units urgently",
                "Create firebreak zones in informal settlements",
                "Educate community on fire prevention",
            ])

        # ----------------------------------------
        # HIGH DENSITY AREAS (Townships / informal)
        # ----------------------------------------
        if population_density == "high":
            safety_measures.append(
                "Prioritize rapid response due to high population density"
            )

        # remove duplicates
        safety_measures = list(set(safety_measures))

        return {
            "agent": "MunicipalSafetyAgent",
            "safety_measures": safety_measures
        }