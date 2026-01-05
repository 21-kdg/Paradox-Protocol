class AnomalyDetector:
    def __init__(self, policy):
        self.policy = policy

    def detect(self, behavior_snapshot):
        violations = []

        if behavior_snapshot["purpose_mismatch"]:
            violations.append("PURPOSE_MISMATCH")

        if behavior_snapshot["request_count"] > self.policy.max_frequency():
            violations.append("FREQUENCY_THRESHOLD_BREACH")

        for dest in behavior_snapshot["destinations"]:
            if dest not in self.policy.allowed_destinations():
                violations.append("THIRD_PARTY_DATA_EXFILTRATION")

        return violations
