from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime


@dataclass
class LocationContext:
    country: str = "South Africa"
    province: str = ""
    municipality: str = ""
    ward: Optional[str] = None
    area_type: str = "township"


@dataclass
class EnvironmentalState:
    weather: str = "normal"
    weather_risk: str = "low"
    rainfall_level: str = "low"
    flood_risk: str = "low"
    temperature: Optional[float] = None


@dataclass
class InfrastructureState:
    electricity: str = "stable"
    water: str = "stable"
    sewage: str = "stable"
    roads: str = "stable"
    telecoms: str = "stable"
    infrastructure_status: str = "stable"


@dataclass
class RiskSignals:
    crime_risk: str = "low"
    fire_risk: str = "low"
    flood_risk: str = "low"
    infrastructure_failure_risk: str = "low"


@dataclass
class EventLog:
    event_type: str
    description: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class UnifiedProvinceIntelligence:
    location: LocationContext
    population_density: str = "medium"

    
    environment: EnvironmentalState = field(default_factory=EnvironmentalState)
    
    infrastructure: InfrastructureState = field(default_factory=InfrastructureState)
    
    risks: RiskSignals = field(default_factory=RiskSignals)

    
    service_area: str = ""
    service_failures: List[str] = field(default_factory=list)
    
    active_issues: List[str] = field(default_factory=list)

    
    event_log: List[EventLog] = field(default_factory=list)

    
    risk_score: float = 0.0
    risk_level: str = "LOW"
    risk_signals: List[str] = field(default_factory=list)
    alerts: list = field(default_factory=list)

    early_warning: bool = False
    emergency: bool = False

    
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    confidence: float = 1.0

    # ---------------- METHODS ----------------

    def update_infrastructure(self, service: str, status: str):
        if hasattr(self.infrastructure, service):
            setattr(self.infrastructure, service, status)


    
    def set_issue(self, issue: str):
        self.active_issues.append(issue)

    def add_event(self, event_type: str, description: str):
        self.event_log.append(EventLog(event_type=event_type, description=description))

    def set_risk_data(self, risk_data: Dict[str, Any]):
        self.risk_score = risk_data.get("risk_score", 0.0)
        self.risk_level = risk_data.get("risk_level", "LOW")
        self.early_warning = risk_data.get("early_warning", False)

        intelligence = risk_data.get("intelligence", {})
        self.risk_signals = intelligence.get("signals", [])

   
    def summary(self) -> Dict[str, Any]:
        return {
            "location": self.location.__dict__,
            "environment": self.environment.__dict__,
            "infrastructure": self.infrastructure.__dict__,
            "risks": self.risks.__dict__,
            "risk_score": self.risk_score,
            "risk_level": self.risk_level,
            "risk_signals": self.risk_signals,
            "active_issues": self.active_issues,
        
            "event_count": len(self.event_log),
        
        }