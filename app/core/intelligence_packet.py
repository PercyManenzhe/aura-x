from dataclasses import dataclass, field
from typing import Dict, List, Any
from datetime import datetime


@dataclass
class IntelligencePacket:

    def __init__(
        self,
        run_id,
        workflow,
        province,
        municipality,
        ward,
        issue
    ):

        self.run_id = run_id
        self.workflow = workflow

        self.province = province
        self.municipality = municipality
        self.ward = ward

        self.issue = issue

        # ADD THIS
        self.active_issues = [issue] if issue else []

        self.infrastructure = {}
        self.environment = {}
        self.risk = {}
        self.gis = {}
        self.simulation = {}

            # ---------------- GIS ----------------
    def set_gis(self, gis_data):
        self.gis = gis_data

    # ---------------- SIMULATION ----------------
    def set_simulation(self, simulation_data):
        self.simulation = simulation_data

    # ---------------- SUMMARY ----------------
    def summary(self):

        return {
            "run_id": self.run_id,
            "workflow": self.workflow,
            "province": self.province,
            "municipality": self.municipality,
            "ward": self.ward,
            "issue": self.issue,
            "risk": self.risk,
            "gis": self.gis,
            "simulation": self.simulation,
            "active_issues": self.active_issues
        }