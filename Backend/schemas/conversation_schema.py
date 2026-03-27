from pydantic import BaseModel
from typing import Dict, List, Any


class TopicMetrics(BaseModel):
    messages: int
    conversations: int
    time_spent_minutes: float
    messages_per_conversation: float
    avg_session_duration_minutes: float
    active_days: int
    code_ratio: float


class LearningBehavior(BaseModel):
    primary_interest: str
    secondary_interest: str
    learning_intensity: str
    technical_usage: str
    learning_consistency: str
    engagement_depth: str
    ai_dependency_score: int


class LearningGrowthTrend(BaseModel):
    trend: str
    early_period_technical_ratio: float
    recent_period_technical_ratio: float


class MetricsSchema(BaseModel):

    total_conversations: int
    total_messages: int
    user_messages: int
    assistant_messages: int

    avg_messages_per_conversation: float
    active_days: int
    most_active_hour: int

    estimated_time_spent_minutes: float
    average_session_duration_minutes: float
    messages_per_day: float

    code_vs_noncode_ratio: float
    consistency_score: float

    dominant_topics: List[str]

    topic_metrics: Dict[str, TopicMetrics]

    learning_behavior: LearningBehavior

    learning_growth_trend: LearningGrowthTrend