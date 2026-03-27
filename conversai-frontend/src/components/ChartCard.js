export default function ChartCard({ title, children }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-5 mb-4">
      <h3 className="text-xl font-semibold mb-4">{title}</h3>
      {children}
    </div>
  );
}