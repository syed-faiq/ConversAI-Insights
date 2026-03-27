const BASE_URL = "http://127.0.0.1:8080";

export async function getProductivityAnalysis(metrics) {

  const response = await fetch(
    `${BASE_URL}/productivity-analysis`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(metrics)
    }
  );

  if (!response.ok) {
    throw new Error("Failed to analyze productivity");
  }

  return await response.json();
}