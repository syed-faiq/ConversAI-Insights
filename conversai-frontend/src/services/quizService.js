const BASE_URL = "http://127.0.0.1:8080";

export async function generateQuiz(metrics) {
  const res = await fetch(`${BASE_URL}/ai/generate-quiz`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(metrics),
  });

  return await res.json();
}

export async function submitQuiz(data) {
  const res = await fetch(`${BASE_URL}/ai/submit-quiz`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data),
  });

  return await res.json();
}

export async function evaluateQuiz(data) {
  const res = await fetch(`${BASE_URL}/ai/evaluate-quiz`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data),
  });

  return await res.json();
}