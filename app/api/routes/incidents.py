from fastapi import APIRouter

from app.api.models.incident_models import IncidentRequest
from app.api.services.orchestration_service import (
    OrchestrationService
)

router = APIRouter()

service = OrchestrationService()


@router.post("/")
def create_incident(request: IncidentRequest):

    result = service.process_incident(
        request.dict()
    )

    return result