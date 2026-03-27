export default function Card({ title, children }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-5 mb-4">
      {title && <h2 className="text-xl font-semibold mb-2">{title}</h2>}
      <div>{children}</div>
    </div>
  );
}