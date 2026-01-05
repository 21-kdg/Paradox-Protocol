from security.kms_encryptor import encrypt_data

def log_incident(event: dict):
    encrypted_event = encrypt_data(str(event))
    print("Encrypted Log Stored:", encrypted_event)
