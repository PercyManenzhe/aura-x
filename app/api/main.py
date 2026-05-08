from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.workflows import router as workflow_router
from app.api.routes.incidents import router as incident_router

app = FastAPI(
    title="Aura-X Municipal Intelligence API",
    version="2.0.0"
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    workflow_router,
    prefix="/workflows",
    tags=["Workflows"]
)

app.include_router(
    incident_router,
    prefix="/incidents",
    tags=["Citizen Incidents"]
)


