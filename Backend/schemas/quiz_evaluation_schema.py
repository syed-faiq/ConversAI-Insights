from pydantic import BaseModel
from typing import List, Dict, Any


class QuestionEvaluation(BaseModel):
    id: str
    score: int
    feedback: str


class FeedbackSummary(BaseModel):
    summary: str
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]


class EvaluationResult(BaseModel):
    total_marks: int
    obtained_marks: int
    percentage: float
    knowledge_level: str
    question_results: List[QuestionEvaluation]
    feedback_summary: FeedbackSummary


class QuizEvaluationRequest(BaseModel):
    submission: List[Dict[str, Any]]


class QuizEvaluationResponse(BaseModel):
    message: str
    evaluation: EvaluationResult