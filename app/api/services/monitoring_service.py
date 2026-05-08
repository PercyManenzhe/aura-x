from datetime import datetime


class MonitoringService:

    @staticmethod
    def generate_metrics(workflow, steps, confidence):

        return {
            "workflow": workflow,
            "timestamp": datetime.utcnow().isoformat(),
            "steps_executed": len(steps),
            "confidence_score": confidence.get("score", 0),
            "system_status": "operational"
        }