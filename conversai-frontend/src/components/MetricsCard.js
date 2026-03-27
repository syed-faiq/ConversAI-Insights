export default function MetricsCard({ title, value, description }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-5 flex flex-col justify-between">
      <h3 className="text-gray-500 text-sm">{title}</h3>
      <p className="text-2xl font-bold mt-2">{value}</p>
      {description && <p className="text-gray-400 text-sm mt-1">{description}</p>}
    </div>
  );
}