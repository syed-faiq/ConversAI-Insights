from pydantic import BaseModel
from typing import List, Optional


class QuizAnswer(BaseModel):
    question_id: str
    answer: str


class QuizQuestion(BaseModel):
    id: str
    type: str
    question: str
    topic: str
    marks: int
    correct_answer: Optional[str] = None
    reference_answer: Optional[str] = None


class QuizSubmissionRequest(BaseModel):
    quiz: List[QuizQuestion]
    answers: List[QuizAnswer]


class SubmissionItem(BaseModel):
    id: str
    type: str
    question: str
    topic: str
    marks: int
    correct_answer: Optional[str] = None
    reference_answer: Optional[str] = None
    user_answer: Optional[str]


class QuizSubmissionResponse(BaseModel):
    message: str
    submission: List[SubmissionItem]