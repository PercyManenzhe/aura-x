from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime


# ---------------------------
# LOCATION (PROVINCE-FIRST DESIGN)
# ---------------------------
@dataclass
class LocationContext:
    country: str = "South Africa"
    province: str = ""              #  CORE LAYER
    municipality: str = ""
    ward: Optional[str] = None
    area_type: str = "township"     # informal_settlement, urban, rural


# ---------------------------
# ENVIRONMENT
# ---------------------------
@dataclass
class EnvironmentalState:
    weather: str = "normal"
    rainfall_level: str = "low"
    flood_risk: str = "low"
    temperature: Optional[float] = None


# ---------------------------
# INFRASTRUCTURE SYSTEMS
# ---------------------------
@dataclass
class InfrastructureState:
    electricity: str = "stable"
    water: str = "stable"
    sewage: str = "stable"
    roads: str = "stable"
    telecoms: str = "stable"


# ---------------------------
# RISK SIGNALS (CORE INTELLIGENCE INPUT)
# ---------------------------
@dataclass
class RiskSignals:
    crime_risk: str = "low"
    fire_risk: str = "low"
    flood_risk: str = "low"
    infrastructure_failure_risk: str = "low"


# ---------------------------
# EVENT MEMORY (AI MEMORY LAYER)
# ---------------------------
@dataclass
class EventLog:
    event_type: str
    description: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


# ---------------------------
# AURA-X PROVINCE INTELLIGENCE CORE
# ---------------------------
@dataclass
class UnifiedProvinceIntelligence:

    # Identity layer
    location: LocationContext

    # System state
    environment: EnvironmentalState = field(default_factory=EnvironmentalState)
    infrastructure: InfrastructureState = field(default_factory=InfrastructureState)
    risks: RiskSignals = field(default_factory=RiskSignals)

    # Dynamic context
    population_density: str = "medium"
    active_issues: List[str] = field(default_factory=list)

    # Metadata
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    confidence: float = 1.0

    # Memory layer
    event_log: List[EventLog] = field(default_factory=list)

    # Computed intelligence
    risk_score: float = 0.0

    # ---------------------------
    # CORE METHODS
    # ---------------------------

    def add_event(self, event_type: str, description: str):
        self.event_log.append(EventLog(event_type, description))

    def update_infrastructure(self, service: str, status: str):
        if hasattr(self.infrastructure, service):
            setattr(self.infrastructure, service, status)
            self.add_event("infrastructure_update", f"{service} -> {status}")

    def update_risk(self, risk_type: str, level: str):
        if hasattr(self.risks, risk_type):
            setattr(self.risks, risk_type, level)
            self.add_event("risk_update", f"{risk_type} -> {level}")

    def set_issue(self, issue: str):
        self.active_issues.append(issue)
        self.add_event("new_issue", issue)

    def summary(self) -> Dict[str, Any]:
        return {
            "location": self.location.__dict__,
            "environment": self.environment.__dict__,
            "infrastructure": self.infrastructure.__dict__,
            "risks": self.risks.__dict__,
            "risk_score": self.risk_score,
            "active_issues": self.active_issues,
            "event_count": len(self.event_log),
            "timestamp": self.timestamp,
            "confidence": self.confidence
        }