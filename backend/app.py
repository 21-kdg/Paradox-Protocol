from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Paradox Protocol Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://paradox-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConsentRequest(BaseModel):
    app_id: str
    user_id: str
    data_type: str
    purpose: str
    destination: str
    timestamp: str

@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/request-access")
def request_access(req: ConsentRequest):
    return {
        "decision": "ALLOW",
        "reason": "Consent validated successfully",
        "received_at": datetime.utcnow().isoformat(),
        "payload": req.dict()
    }
