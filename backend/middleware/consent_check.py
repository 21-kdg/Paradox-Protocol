def evaluate_request(request_data: dict):
    """
    Temporary rule-based consent evaluation.
    Later this will call the AI engine.
    """

    # Simple example rule
    if request_data["purpose"] == "ads":
        return {
            "action": "BLOCK",
            "reason": "Purpose not allowed by user consent"
        }

    return {
        "action": "ALLOW",
        "reason": "Request complies with consent policy"
    }
