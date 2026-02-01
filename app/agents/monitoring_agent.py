from datetime import datetime

class MonitoringAgent:
    def run(self, task: str, context=None):
        context = context or {}

        workflow = context.get("workflow", "unknown")
        run_id = context.get("run_id", "unknown")
        steps = context.get("steps", [])
        confidence = context.get("confidence", {})

        total_steps = len(steps)
        failed_steps = [s for s in steps if s.get("status") != "success"]

        monitoring_payload = {
            "agent": "MonitoringAgent",
            "task": task,
            "timestamp": datetime.now().isoformat(),
            "workflow": workflow,
            "run_id": run_id,
            "total_steps": total_steps,
            "failed_steps": len(failed_steps),
            "confidence_score": confidence.get("score"),
            "notes": [
                "Ready for Huawei LTS log shipping",
                "Ready for OBS run archive (JSON)",
                "Ready for Cloud Eye metrics (future)"
            ]
        }

        return monitoring_payload
