class MonitoringAgent:
    def run(self, task, context=None):
        return {
            "agent": "MonitoringAgent",
            "task": task,
            "status": "ok",
            "message": "Core monitoring active"
        }
