class ContextEngine:

    @staticmethod
    def build_context(inputs: dict):

        return {
            "location": {
                "province": inputs.get("province"),
                "municipality": inputs.get("municipality"),
                "ward": inputs.get("ward")
            },
            "issue": inputs.get("issue"),
            "priority": inputs.get("priority", "medium")
        }