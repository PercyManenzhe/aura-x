from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from app.agents.orchestrator import AuraXOrchestrator

app = FastAPI(title="Aura-X API", version="1.0")

orchestrator = AuraXOrchestrator()


class RunRequest(BaseModel):
    location: Optional[str] = "Mpumalanga"
    season: Optional[str] = "All-year"
    visitor_type: Optional[str] = "General"
    budget_level: Optional[str] = "mid"
    group_type: Optional[str] = "general"
    duration_days: Optional[int] = 2
    interests: Optional[List[str]] = ["nature"]
    extra: Optional[Dict[str, Any]] = None

    
@app.get("/")
def root():
    return {"message": "Aura-X API running. Visit /docs for Swagger UI."}


@app.get("/health")
def health():
    return {"status": "ok", "service": "Aura-X"}


@app.post("/run")
def run_aura_x(req: RunRequest):
    inputs = req.model_dump()
    # keep extra optional, but merge if provided
    extra = inputs.pop("extra", None) or {}
    inputs.update(extra)

    result = orchestrator.run(inputs=inputs)
    return result
