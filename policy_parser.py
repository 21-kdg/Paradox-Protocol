class PolicyParser:
    def __init__(self, policy_json):
        self.policy = policy_json

    def is_purpose_allowed(self, purpose):
        return purpose in self.policy.get("allowed_purposes", [])

    def is_within_time(self, access_time):
        start = self.policy.get("time_window", {}).get("start")
        end = self.policy.get("time_window", {}).get("end")
        return start <= access_time <= end

    def max_frequency(self):
        return self.policy.get("max_requests_per_hour", 10)

    def allowed_destinations(self):
        return self.policy.get("allowed_destinations", [])
