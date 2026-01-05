export default function handler(req, res) {
  res.status(200).json([
    "User data accessed without permission",
    "Third-party API violation detected",
    "Consent revoked but request continued"
  ]);
}
