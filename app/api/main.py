from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from app.agents.orchestrator import AuraXOrchestrator

app = FastAPI(title="Aura-X API", version="1.0")

workflow_map = {
    # Core demos
    "tourism": "config.yaml",
    "mining": "workflows/mining_safety.yaml",
    "municipal": "workflows/municipal_ops.yaml",

    # Tourism deep-dive domains
    "tourism_safety_health": "workflows/tourism_safety_health.yaml",
    "tourism_culture_authority": "workflows/tourism_culture_authority.yaml",
    "tourism_logistics_ports": "workflows/tourism_logistics_ports.yaml",
    "tourism_economic_opportunity": "workflows/tourism_economic_opportunity.yaml",

    # Strategic infrastructure
    "rail_corridor_tourism": "workflows/rail_corridor_tourism.yaml",

    # Municipal & Eskom operations
    "municipal_smart_city": "workflows/municipal_smart_city.yaml",

}


class RunRequest(BaseModel):
    workflow: Optional[str] = "tourism"

    # existing tourism fields...
    location: Optional[str] = "Mpumalanga"
    season: Optional[str] = "All-year"
    visitor_type: Optional[str] = "General"
    budget_level: Optional[str] = "mid"
    group_type: Optional[str] = "general"
    duration_days: Optional[int] = 2
    interests: Optional[List[str]] = ["nature"]

    # municipal & Eskom pack fields
    municipality: Optional[str] = None
    ward: Optional[str] = None
    service: Optional[str] = None  # streetlights | electricity | water | waste
    asset_type: Optional[str] = None  # smart_meter | high_mast | pump_station
    asset_id: Optional[str] = None
    issue: Optional[str] = None  # outage | leak | tamper | no_signal
    gps: Optional[Dict[str, float]] = None  # {"lat":..., "lon":...}
    sensor_status: Optional[str] = None  # online | offline | intermittent
    last_seen: Optional[str] = None
    weather_hint: Optional[str] = None

    extra: Optional[Dict[str, Any]] = None


@app.get("/")
def root():
    return {"message": "Aura-X API running. Visit /docs for Swagger UI."}


@app.get("/health")
def health():
    return {"status": "ok", "service": "Aura-X"}


@app.post("/run")
def run_aura_x(req: RunRequest):
    inputs = req.model_dump(exclude={"workflow"})
    # keep extra optional, but merge if provided
    extra = inputs.pop("extra", None) or {}
    inputs.update(extra)

    # select workflow-specific yaml and create orchestrator per request
    yaml_path = workflow_map.get(req.workflow, "config.yaml")
    orchestrator = AuraXOrchestrator(yaml_path=yaml_path)
    result = orchestrator.run(inputs=inputs)
    return result
