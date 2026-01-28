class ReasoningAgent:
    def __init__(self, name="GenericReasoningAgent"):
        self.name = name

    def run(self, task: str, context: dict = None) -> dict:
        context = context or {}

        understanding = self._understand(task)
        analysis = self._analyze(task, context)
        decision = self._decide(analysis)
        response = self._respond(decision)

        return {
            "agent": self.name,
            "understanding": understanding,
            "analysis": analysis,
            "decision": decision,
            "response": response
        }

    def _understand(self, task: str) -> str:
        return f"Task understood as: '{task}'"

    def _analyze(self, task: str, context: dict) -> str:
        return f"Analyzing task with context keys: {list(context.keys())}"

    def _decide(self, analysis: str) -> str:
        return "Proceed with structured response generation"

    def _respond(self, decision: str) -> str:
        return f"Response generated based on decision: {decision}"
