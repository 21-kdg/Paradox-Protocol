import { useState } from "react";

export default function ConsentToggle() {
  const [consent, setConsent] = useState(true);

  return (
    <div className="bg-white p-6 rounded-xl shadow">
      <p className="mb-4 text-lg">
        Data Sharing Consent: 
        <span className={consent ? "text-green-600" : "text-red-600"}>
          {consent ? " ALLOWED" : " BLOCKED"}
        </span>
      </p>

      <button
        onClick={() => setConsent(!consent)}
        className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Toggle Consent
      </button>

      <p className="mt-4 text-sm text-gray-500">
        🔍 Demo Tip: Turn OFF → trigger violation alerts
      </p>
    </div>
  );
}
