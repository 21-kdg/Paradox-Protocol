export default function AlertCard({ alert }) {
  return (
    <div className="bg-white p-4 rounded-lg shadow border-l-4 border-red-500">
      <h3 className="font-semibold">{alert.type}</h3>
      <p className="text-sm text-gray-600">{alert.message}</p>
      <span className="text-xs text-gray-400">{alert.time}</span>
    </div>
  );
}
