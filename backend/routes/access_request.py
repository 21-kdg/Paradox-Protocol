from fastapi import APIRouter
from pydantic import BaseModel
from backend.middleware.consent_check import evaluate_request


router = APIRouter()

class AccessRequest(BaseModel):
    app_id: str
    user_id: str
    data_type: str
    purpose: str
    destination: str
    timestamp: str

@router.post("/request-access")
def request_access(request: AccessRequest):
    decision = evaluate_request(request.dict())

    return {
        "decision": decision["action"],
        "reason": decision["reason"]
    }
