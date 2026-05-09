from dataclasses import dataclass, field
from typing import Dict, List, Any
from datetime import datetime


@dataclass
class IntelligencePacket:

    # Identity
    run_id: str
    timestamp: str

    # Location
    country: str = "South Africa"
    province: str = ""
    municipality: str = ""
    ward: str = ""

    # Core issue
    issue: str = ""

    # Infrastructure
    infrastructure: Dict[str, Any] = field(default_factory=dict)

    # Environment
    environment: Dict[str, Any] = field(default_factory=dict)

    # Risk
    risk: Dict[str, Any] = field(default_factory=dict)

    # GIS
    gis: Dict[str, Any] = field(default_factory=dict)

    # Simulation
    simulation: Dict[str, Any] = field(default_factory=dict)

    # Agent outputs
    agents: Dict[str, Any] = field(default_factory=dict)

    # Monitoring
    monitoring: Dict[str, Any] = field(default_factory=dict)

    # Metadata
    confidence: float = 1.0