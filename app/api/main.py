from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from app.api.routes.health import router as health_router
from app.api.routes.workflows import router as workflow_router
from app.api.routes.incidents import router as incident_router

app = FastAPI(
    title="Aura-X Municipal Intelligence API",
    version="2.0.0",
    description="Aura-X AI Intelligence Platform",

    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "docExpansion": "none",
        "syntaxHighlight.theme": "monokai",
    },
    swagger_ui_init_oauth=None,
    swagger_css_url="/static/swagger.css",
    swagger_favicon_url="/static/aura-x-logo.jpg"
)
from fastapi.openapi.docs import get_swagger_ui_html


@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
        return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Aura-X Municipal Intelligence API",
        swagger_css_url="/static/swagger.css",
        swagger_favicon_url="/static/aura-x-logo.jpg",
        swagger_ui_parameters={
            "docExpansion": "none"
        }
    )
# ---------------- STATIC FILES ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------------- ROUTERS ----------------
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

# ---------------- CUSTOM OPENAPI ----------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Aura-X Municipal Intelligence API",
        version="2.0.0",
        description="Aura-X AI Intelligence Platform",
        routes=app.routes,
    )

    # ENSURE VALID OPENAPI VERSION (THIS FIXES YOUR ERROR)
    openapi_schema["openapi"] = "3.0.2"

    # Logo injection (safe)
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/aura-x-logo.jpg"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema
