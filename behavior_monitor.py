class BehaviorMonitor:
    def __init__(self):
        self.request_count = 0
        self.destinations = set()
        self.purpose_mismatch = False

    def log_request(self, purpose, allowed_purposes, destination):
        self.request_count += 1

        if purpose not in allowed_purposes:
            self.purpose_mismatch = True

        self.destinations.add(destination)

    def snapshot(self):
        return {
            "request_count": self.request_count,
            "purpose_mismatch": self.purpose_mismatch,
            "destinations": list(self.destinations)
        }
