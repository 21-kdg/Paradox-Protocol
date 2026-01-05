import base64

def encrypt_data(plain_text: str) -> str:
    """
    Mock encryption simulating Cloud KMS behavior.
    """
    encoded_bytes = base64.b64encode(plain_text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decrypt_data(cipher_text: str) -> str:
    """
    Mock decryption simulating Cloud KMS behavior.
    """
    decoded_bytes = base64.b64decode(cipher_text.encode("utf-8"))
    return decoded_bytes.decode("utf-8")
