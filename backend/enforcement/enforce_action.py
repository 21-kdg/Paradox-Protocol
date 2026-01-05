def enforce(decision: dict, request_data: dict):
    """
    Automated incident response logic.
    Designed to run as a Cloud Function in production.
    """

    action = decision.get("action")

    if action == "BLOCK":
        print(f"[ENFORCEMENT] App {request_data['app_id']} BLOCKED due to consent violation")
        return "ACCESS_REVOKED"

    if action == "ALLOW":
        print(f"[ENFORCEMENT] Access allowed for app {request_data['app_id']}")
        return "ACCESS_GRANTED"

    print("[ENFORCEMENT] No action taken")
    return "NO_ACTION"
