# app/agents/reasoning_agent.py





# app/agents/reasoning_agent.py

import app.services.llm_adapter as llm_service

llm_available = llm_service.llm_available
call_openai = llm_service.call_openai


class GenericReasoningAgent:
    def run(self, task, context=None):
        context = context or {}

        # If OpenAI key exists, use LLM path
        if llm_available():
            prompt = f"""
You are an AI reasoning agent for Aura-X.
Task: {task}

Context keys available: {list(context.keys())}

Return a short structured reasoning response with:
- understanding
- analysis
- decision
- response
"""
            try:
                llm_text = call_openai(prompt)
                return {
                    "agent": "GenericReasoningAgent",
                    "mode": "llm",
                    "task": task,
                    "llm_output": llm_text
                }
            except Exception as e:
                # If OpenAI fails, fall back safely
                return {
                    "agent": "GenericReasoningAgent",
                    "mode": "fallback",
                    "error": str(e),
                    "understanding": f"Task understood as: '{task}'",
                    "analysis": f"Analyzing task with context keys: {list(context.keys())}",
                    "decision": "Proceed with structured response generation",
                    "response": "Response generated based on decision: Proceed with structured response generation"
                }

        # Default fallback path (no key)
        return {
            "agent": "GenericReasoningAgent",
            "mode": "local",
            "understanding": f"Task understood as: '{task}'",
            "analysis": f"Analyzing task with context keys: {list(context.keys())}",
            "decision": "Proceed with structured response generation",
            "response": "Response generated based on decision: Proceed with structured response generation"
        }
