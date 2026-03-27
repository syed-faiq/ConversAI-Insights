"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";  // ✅ import router
import { useMetrics } from "../../context/MetricsContext";
import { generateQuiz, submitQuiz } from "../../services/quizService";

export default function QuizPage() {
  const { metrics } = useMetrics();
  const router = useRouter();  // ✅ router

  const [quiz, setQuiz] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);

  // Generate quiz
  useEffect(() => {
    const fetchQuiz = async () => {
      if (!metrics) return;
      setLoading(true);
      try {
        const res = await generateQuiz(metrics);
        const quizWithIds = (res.quiz || []).map((q, index) => ({
          ...q,
          id: `q${index + 1}`,
          correct_answer: q.answer,  // 🔥 correct_answer mapping
        }));
        setQuiz(quizWithIds);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchQuiz();
  }, [metrics]);

  // Handle answers
  const handleAnswer = (qid, value) => {
    setAnswers((prev) => ({ ...prev, [qid]: value }));
  };

  // Submit quiz
  const handleSubmit = async () => {
    if (!quiz.length) return;

    const answersArray = Object.keys(answers).map((qid) => ({
      question_id: qid,
      answer: answers[qid],
    }));

    setLoading(true);
    try {
      const submitRes = await submitQuiz({ quiz, answers: answersArray });

      // Save submission in localStorage (for Evaluate page)
      localStorage.setItem("quiz_submission", JSON.stringify(submitRes.submission));

      // ✅ Redirect to evaluation page
      router.push("/evaluate");
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (!metrics) return <p>Please upload data first.</p>;

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Quiz</h1>
      {loading && <p>Generating quiz...</p>}

      {quiz.map((q, index) => (
        <div key={q.id} className="bg-white p-5 rounded shadow">
          <p className="font-semibold mb-2">{index + 1}. {q.question}</p>

          {q.type === "mcq" && (
            <div className="space-y-2">
              {q.options.map((opt, i) => (
                <label key={i} className="block">
                  <input
                    type="radio"
                    name={q.id}
                    value={opt.charAt(0)}
                    onChange={(e) => handleAnswer(q.id, e.target.value)}
                    className="mr-2"
                  />
                  {opt}
                </label>
              ))}
            </div>
          )}

          {q.type === "short" && (
            <textarea
              className="w-full border p-2 mt-2 rounded"
              rows={3}
              onChange={(e) => handleAnswer(q.id, e.target.value)}
            />
          )}

          <p className="text-sm text-gray-500 mt-2">
            Topic: {q.topic} | Marks: {q.marks}
          </p>
        </div>
      ))}

      {quiz.length > 0 && (
        <button
          onClick={handleSubmit}
          className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700"
        >
          Submit Quiz
        </button>
      )}
    </div>
  );
}