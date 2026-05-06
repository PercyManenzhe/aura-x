class RiskEngine:
    """
    Aura-X Risk Engine v1
    Computes multi-factor risk score for South African provinces
    """

    def compute(self, province):
        if hasattr(province, "summary"):
            province = province.summary()
        return self.compute_risk_score(province)

    def compute_risk_score(self, province: dict):
        ...