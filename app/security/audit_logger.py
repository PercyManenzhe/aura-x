from datetime import datetime

class AuditLogger:

    def log_event(self, user, action, target):
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "action": action,
            "target": target
        }

        print("[AUDIT]", event)

        return event