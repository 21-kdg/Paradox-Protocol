class DecisionEngine:
    def __init__(self):
        self.severity_map = {
            "PURPOSE_MISMATCH": 2,
            "FREQUENCY_THRESHOLD_BREACH": 3,
            "THIRD_PARTY_DATA_EXFILTRATION": 5
        }

    def decide(self, violations):
        risk_score = sum(self.severity_map.get(v, 0) for v in violations)

        if risk_score >= 5:
            return "BLOCK"
        elif risk_score >= 3:
            return "SANDBOX"
        else:
            return "ALLOW"
