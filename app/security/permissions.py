class Permissions:

    ROLE_PERMISSIONS = {
        "citizen": ["report_issue"],

        "technician": [
            "view_incidents",
            "update_incidents"
        ],

        "municipal_manager": [
            "view_dashboard",
            "manage_workflows",
            "view_reports"
        ],

        "system_admin": ["all"]
    }

    def has_permission(self, role, permission):

        allowed = self.ROLE_PERMISSIONS.get(role, [])

        return "all" in allowed or permission in allowed