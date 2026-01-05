from fastapi import FastAPI
from routes.access_request import router as access_router


app = FastAPI(
    title="Consent Firewall Backend",
    description="Backend enforcement layer for AI-powered consent firewall",
    version="1.0"
)

# Register routes
app.include_router(access_router)

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Consent Firewall Backend is live"
    }
