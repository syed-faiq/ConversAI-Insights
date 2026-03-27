from pydantic import BaseModel
from typing import List, Dict, Any


class AIAnalysis(BaseModel):
    summary: str
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]


class ProductivityResult(BaseModel):
    productivity_score: int
    productivity_level: str
    ai_analysis: AIAnalysis


class ProductivityResponse(BaseModel):
    message: str
    productivity_analysis: ProductivityResult