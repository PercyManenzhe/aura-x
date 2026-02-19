from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Literal, Union

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

# --- input schemas per workflow -------------------------------------------------

class TourismInputs(BaseModel):
    location: str
    season: Optional[str] = "All-year"
    visitor_type: Optional[str] = "General"
    budget_level: Optional[str] = "mid"
    group_type: Optional[str] = "general"
    duration_days: Optional[int] = 2
    interests: Optional[List[str]] = ["nature"]


class MiningInputs(BaseModel):
    site: str
    hazards: List[str]
    incident_type: Optional[str] = "near_miss"
    shift: Optional[str] = "day"
    compliance_focus: Optional[List[str]] = []


class GPS(BaseModel):
    lat: float
    lon: float


class MunicipalInputs(BaseModel):
    municipality: str
    ward: Optional[str] = None
    service: str
    asset_type: Optional[str] = None
    asset_id: Optional[str] = None
    issue: Optional[str] = None
    gps: Optional[GPS] = None
    sensor_status: Optional[str] = None
    last_seen: Optional[str] = None
    weather_hint: Optional[str] = None


class RunRequest(BaseModel):
    workflow: Literal["tourism", "mining", "municipal"]
    inputs: Union[TourismInputs, MiningInputs, MunicipalInputs]



@app.get("/")
def root():
    return {"message": "Aura-X API running. Visit /docs for Swagger UI."}


@app.get("/health")
def health():
    return {"status": "ok", "service": "Aura-X"}


@app.post("/run")
def run_aura_x(req: RunRequest):
    # req.inputs is already validated as one of the workflow models
    raw_inputs = req.inputs

    # convert input model to plain dict (Union members are BaseModel subclasses)
    if isinstance(raw_inputs, BaseModel):
        validated = raw_inputs.model_dump()
    else:
        validated = dict(raw_inputs)

    # --- filter out null/placeholder values ---
    def _clean(v):
        if v is None:
            return False
        if isinstance(v, str) and v.strip().lower() == "string":
            return False
        if isinstance(v, (list, dict)) and not v:
            return False
        return True

    cleaned_inputs = {k: v for k, v in validated.items() if _clean(v)}

    # select workflow-specific yaml and create orchestrator per request
    yaml_path = workflow_map.get(req.workflow, "config.yaml")
    orchestrator = AuraXOrchestrator(yaml_path=yaml_path)
    result = orchestrator.run(inputs=cleaned_inputs)
    return result


