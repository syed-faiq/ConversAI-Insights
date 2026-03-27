from pydantic import BaseModel
from typing import List, Optional


class MCQQuestion(BaseModel):
    type: str
    question: str
    options: List[str]
    answer: str
    topic: str
    marks: int


class ShortQuestion(BaseModel):
    type: str
    question: str
    topic: str
    reference_answer: str
    marks: int


class QuizItem(BaseModel):
    type: str
    question: str
    topic: str
    marks: int
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    reference_answer: Optional[str] = None


class QuizResponse(BaseModel):
    message: str
    quiz: List[QuizItem]