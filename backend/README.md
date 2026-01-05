## 🔐 Encryption & Key Management (Phase 2)

This backend implements a KMS-compatible encryption layer to protect sensitive data.

### Current Mode
- Local mock KMS used for development
- Encryption applied to consent logs and incident records

### Production Mode
- Compatible with Google Cloud KMS
- Provider can be switched via `KMS_PROVIDER=gcp`
- Keys managed externally, no plaintext storage

### Security Guarantees
- Encryption at rest
- Separation of duties
- Audit-ready logs
