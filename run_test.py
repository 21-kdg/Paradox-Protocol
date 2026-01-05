import json
from policy_parser import PolicyParser
from behavior_monitor import BehaviorMonitor
from anomaly_detector import AnomalyDetector
from decision_engine import DecisionEngine

# LOAD POLICY
with open("test_cases/normal_usage.json") as f:
    policy_json = json.load(f)

policy = PolicyParser(policy_json)

# INIT COMPONENTS
monitor = BehaviorMonitor()
detector = AnomalyDetector(policy)
decision_engine = DecisionEngine()

# SIMULATE APP BEHAVIOR
monitor.log_request(
    purpose="login",
    allowed_purposes=policy_json["allowed_purposes"],
    destination="internal-db"
)

monitor.log_request(
    purpose="ads",
    allowed_purposes=policy_json["allowed_purposes"],
    destination="external-ad-server"
)

# ANALYZE
snapshot = monitor.snapshot()
violations = detector.detect(snapshot)
decision = decision_engine.decide(violations)

print("Behavior Snapshot:", snapshot)
print("Violations Detected:", violations)
print("FINAL DECISION:", decision)
