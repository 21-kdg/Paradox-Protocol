import base64
import os

KMS_PROVIDER = os.getenv("KMS_PROVIDER", "mock")

def encrypt_data(plain_text: str) -> str:
    if KMS_PROVIDER == "gcp":
        # placeholder for real GCP KMS call
        raise NotImplementedError("GCP KMS not configured yet")
    else:
        return base64.b64encode(plain_text.encode()).decode()

def decrypt_data(cipher_text: str) -> str:
    if KMS_PROVIDER == "gcp":
        raise NotImplementedError("GCP KMS not configured yet")
    else:
        return base64.b64decode(cipher_text.encode()).decode()
