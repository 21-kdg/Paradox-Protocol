import Navbar from "../components/Navbar";
import ConsentToggle from "../components/ConsentToggle";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <div className="max-w-3xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-4">Consent Configuration</h1>
        <ConsentToggle />
      </div>
    </div>
  );
}
