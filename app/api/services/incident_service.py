from datetime import datetime
import uuid


class IncidentService:

    @staticmethod
    def create_incident(data: dict):

        incident = {
            "incident_id": f"INC-{uuid.uuid4().hex[:8].upper()}",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "reported",
            "data": data
        }

        return incident