"use client";

import { useState, useEffect } from "react";
import { evaluateQuiz } from "../../services/quizService";

export default function EvaluatePage() {
  const [submission, setSubmission] = useState(null);
  const [evaluation, setEvaluation] = useState(null);
  const [loading, setLoading] = useState(false);

  // On page load, fetch submission and evaluate automatically
  useEffect(() => {
    const savedSubmission = localStorage.getItem("quiz_submission");
    if (!savedSubmission) return;

    const submissionData = JSON.parse(savedSubmission);
    setSubmission(submissionData);

    const evaluate = async () => {
      setLoading(true);
      try {
        const res = await evaluateQuiz({ submission: submissionData });
        setEvaluation(res.evaluation);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    evaluate();
  }, []);

  if (!submission) return <p>No quiz submission found. Please complete the quiz first.</p>;

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Quiz Evaluation</h1>
      {loading && <p>Evaluating quiz...</p>}

      {evaluation && (
        <div className="bg-white p-6 rounded shadow mt-6">
          <h2 className="text-2xl font-bold mb-4">Evaluation Result</h2>

          <p><b>Total Marks:</b> {evaluation.total_marks}</p>
          <p><b>Obtained:</b> {evaluation.obtained_marks}</p>
          <p><b>Percentage:</b> {evaluation.percentage}%</p>
          <p><b>Knowledge Level:</b> {evaluation.knowledge_level}</p>

          <hr className="my-4" />

          <h3 className="text-xl font-semibold mb-2">Feedback</h3>
          <p>{evaluation.feedback_summary.summary}</p>

          <div className="mt-4">
            <h4 className="font-semibold">Strengths:</h4>
            <ul className="list-disc list-inside">
              {evaluation.feedback_summary.strengths.map((s, i) => <li key={i}>{s}</li>)}
            </ul>

            <h4 className="font-semibold mt-2">Weaknesses:</h4>
            <ul className="list-disc list-inside">
              {evaluation.feedback_summary.weaknesses.map((w, i) => <li key={i}>{w}</li>)}
            </ul>

            <h4 className="font-semibold mt-2">Recommendations:</h4>
            <ul className="list-disc list-inside">
              {evaluation.feedback_summary.recommendations.map((r, i) => <li key={i}>{r}</li>)}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}