from fastapi import APIRouter
from pydantic import BaseModel

# Consent evaluation (Phase 1 + Phase 2)
from middleware.consent_check import evaluate_request

# Enforcement layer (Phase 3)
from enforcement.enforce_action import enforce

# Encrypted logging (Phase 2)
from logs.logger import log_incident


router = APIRouter()


# 🔹 Request schema
class AccessRequest(BaseModel):
    app_id: str
    user_id: str
    data_type: str
    purpose: str
    destination: str
    timestamp: str


# 🔥 Consent Firewall Gate
@router.post("/request-access")
def request_access(request: AccessRequest):
    # Convert request to dictionary
    request_data = request.dict()

    # Step 1: Evaluate consent / AI decision
    decision = evaluate_request(request_data)

    # Step 2: Automated enforcement
    enforcement_result = enforce(decision, request_data)

    # Step 3: Encrypted audit logging
    log_incident({
        "app_id": request_data["app_id"],
        "user_id": request_data["user_id"],
        "data_type": request_data["data_type"],
        "purpose": request_data["purpose"],
        "destination": request_data["destination"],
        "decision": decision["action"],
        "reason": decision["reason"],
        "enforcement": enforcement_result,
        "timestamp": request_data["timestamp"]
    })

    # Step 4: API response
    return {
        "decision": decision["action"],
        "reason": decision["reason"],
        "enforcement": enforcement_result
    }
