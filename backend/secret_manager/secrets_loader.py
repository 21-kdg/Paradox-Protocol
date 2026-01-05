import os

def get_secret(key_name: str):
    """
    Placeholder for Google Secret Manager
    """
    return os.getenv(key_name, "SECRET_NOT_SET")
