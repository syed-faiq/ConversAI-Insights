export default function ProductivityReport({ report }) {
  if (!report || !report.ai_analysis) {
    return <p className="text-gray-500">Productivity data is not available.</p>;
  }

  const { ai_analysis, productivity_score, productivity_level } = report;

  // Safely convert arrays into plain text
  const strengthsText = Array.isArray(ai_analysis.strengths)
    ? ai_analysis.strengths.join(". ")
    : "";
  const weaknessesText = Array.isArray(ai_analysis.weaknesses)
    ? ai_analysis.weaknesses.join(". ")
    : "";
  const recommendationsText = Array.isArray(ai_analysis.recommendations)
    ? ai_analysis.recommendations.join(". ")
    : "";

  return (
    <div className="space-y-6">

      <div className="bg-white shadow-md rounded-lg p-5">
        <h2 className="text-xl font-semibold mb-2">Productivity Score</h2>
        <p className="text-4xl font-bold text-blue-600">{productivity_score}</p>
        <p className="text-gray-600">{productivity_level}</p>
      </div>

      <div className="bg-white shadow-md rounded-lg p-5">
        <h2 className="text-xl font-semibold mb-2">AI Summary</h2>
        <p>{ai_analysis.summary || "No summary available."}</p>
      </div>

      <div className="bg-white shadow-md rounded-lg p-5">
        <h2 className="text-xl font-semibold mb-2">Strengths</h2>
        <p>{strengthsText || "No strengths data available."}</p>
      </div>

      <div className="bg-white shadow-md rounded-lg p-5">
        <h2 className="text-xl font-semibold mb-2">Weaknesses</h2>
        <p>{weaknessesText || "No weaknesses data available."}</p>
      </div>

      <div className="bg-white shadow-md rounded-lg p-5">
        <h2 className="text-xl font-semibold mb-2">Recommendations</h2>
        <p>{recommendationsText || "No recommendations available."}</p>
      </div>

    </div>
  );
}