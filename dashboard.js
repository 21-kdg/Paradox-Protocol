import Navbar from "../components/Navbar";
import AlertsDashboard from "../dashboards/AlertsDashboard";

export default function Dashboard() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />
      <AlertsDashboard />
    </div>
  );
}
