from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime


# ---------------------------
# LOCATION (PROVINCE-FIRST DESIGN)
# ---------------------------
@dataclass
class LocationContext:
    country: str = "South Africa"
    province: str = ""              # CORE INTELLIGENCE UNIT (NOT STATE)
    municipality: str = ""
    ward: Optional[str] = None
    area_type: str = "township"     # township, urban, rural, informal_settlement


# ---------------------------
# ENVIRONMENT
# ---------------------------
@dataclass
class EnvironmentalState:
    weather: str = "normal"
    weather_risk: str = "low"       # ADDED for Risk Engine compatibility
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

    # ADDED: global intelligence compatibility
    infrastructure_status: str = "stable"


# ---------------------------
# RISK SIGNALS (CORE INPUT LAYER)
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
# AURA-X CORE INTELLIGENCE BRAIN
# ---------------------------
@dataclass
class UnifiedProvinceIntelligence:

    # Identity layer
    location: LocationContext

    # Environment layer
    environment: EnvironmentalState = field(default_factory=EnvironmentalState)

    # Infrastructure layer
    infrastructure: InfrastructureState = field(default_factory=InfrastructureState)

    # Risk signals layer
    risks: RiskSignals = field(default_factory=RiskSignals)

    # Population intelligence
    population_density: str = "medium"

    # Service intelligence
    service_area: str = ""
    service_failures: List[str] = field(default_factory=list)

    # Operational context
    active_issues: List[str] = field(default_factory=list)

    # AI Memory layer
    event_log: List[EventLog] = field(default_factory=list)

    # Computed intelligence (from Risk Engine)
    risk_score: float = 0.0
    risk_level: str = "LOW"
    risk_signals: List[str] = field(default_factory=list)

    # Early warning system
    early_warning_triggered: bool = False
    emergency_flag: bool = False

    # System metadata
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    confidence: float = 1.0







    # ---------------------------
    # CORE METHODS (INTELLIGENCE LAYER)
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

    # Risk Engine integration hook
    def apply_risk_engine(self, score: float, level: str, signals: List[str]):
        self.risk_score = score
        self.risk_level = level
        self.risk_signals = signals

        if level in ["HIGH", "CRITICAL"]:
            self.early_warning_triggered = True
            self.emergency_flag = True

        self.add_event("risk_update", f"Risk={level}, Score={score}")

    # 📊 FULL SYSTEM SUMMARY
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
            "service_failures": self.service_failures,
            "event_count": len(self.event_log),
            "early_warning": self.early_warning_triggered,
            "emergency": self.emergency_flag,
            "timestamp": self.timestamp,
            "confidence": self.confidence
        }