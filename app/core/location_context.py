from dataclasses import dataclass
from typing import Optional

@dataclass
class LocationContext:
    country: str = "South Africa"
    province: str = ""
    municipality: str = ""
    ward: Optional[str] = None
    area_type: str = "township"