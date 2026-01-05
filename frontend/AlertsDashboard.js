import { useEffect, useState } from "react";
import AlertCard from "../components/AlertCard";
import LineChart from "../components/LineChart";

export default function AlertsDashboard() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("/api/alerts")
      .then(res => res.json())
      .then(data => setAlerts(data));
  }, []);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">Real-Time Violation Alerts</h2>

      <div className="grid md:grid-cols-3 gap-4">
        {alerts.map((a, i) => (
          <AlertCard key={i} alert={a} />
        ))}
      </div>

      <div className="mt-8 bg-white p-4 rounded-xl shadow">
        <LineChart />
      </div>
    </div>
  );
}
