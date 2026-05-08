from pydantic import BaseModel


class IncidentRequest(BaseModel):

    province: str
    municipality: str
    ward: str
    issue: str

    citizen: str | None = None
    channel: str | None = "mobile"