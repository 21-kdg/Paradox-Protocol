export default function handler(req, res) {
  res.status(200).json([
    { type: "Consent Breach", message: "Data used without consent", time: "2 mins ago" },
    { type: "API Misuse", message: "Unauthorized request detected", time: "5 mins ago" }
  ]);
}
