from collections import defaultdict
from datetime import datetime
from router_utils import nlp_utils
from router_utils import behaviour_utils
from router_utils import trend_utils
def compute_metrics(messages, total_conversations):

    total_messages = len(messages)

    user_messages = 0
    assistant_messages = 0

    timestamps = []

    code_messages = 0

    CODE_KEYWORDS = [
        "python","code","function","api","sql",
        "javascript","class","debug","error"
    ]

    for msg in messages:

        role = msg.get("role")
        text = str(msg.get("text","")).lower()
        time = msg.get("time")

        if role == "user":
            user_messages += 1

        if role == "assistant":
            assistant_messages += 1

        if time:
            timestamps.append(time)

        if any(k in text for k in CODE_KEYWORDS):
            code_messages += 1


    timestamps.sort()

    # active days
    days = set()
    hours = defaultdict(int)

    for ts in timestamps:

        dt = datetime.fromtimestamp(ts)

        days.add(dt.date())
        hours[dt.hour] += 1


    active_days = len(days)

    most_active_hour = None

    if hours:
        most_active_hour = max(hours, key=hours.get)


    # total time spent
    total_seconds = 0

    for i in range(1, len(timestamps)):

        gap = timestamps[i] - timestamps[i-1]

        if 0 < gap < 600:
            total_seconds += gap


    total_time_minutes = round(total_seconds / 60,2)


    # average session duration
    avg_session_duration = 0

    if total_conversations:
        avg_session_duration = round(total_time_minutes / total_conversations,2)


    # messages per day
    messages_per_day = 0

    if active_days:
        messages_per_day = round(total_messages / active_days,2)


    # code ratio
    code_ratio = 0

    if total_messages:
        code_ratio = round(code_messages / total_messages,2)


    # consistency score
    consistency_score = 0

    if timestamps:

        first = datetime.fromtimestamp(timestamps[0])
        last = datetime.fromtimestamp(timestamps[-1])

        span_days = (last - first).days + 1

        if span_days:
            consistency_score = round((active_days / span_days) * 100,2)
    topic_data = nlp_utils.categorize_topics(messages)

    dominant_topics = topic_data.get("dominant_topics", [])
    topic_metrics = topic_data.get("topic_metrics", {})

    # Behavior analysis
    behavior = behaviour_utils.analyze_learning_behavior(
        {
            "total_messages": total_messages,
            "messages_per_day": messages_per_day,
            "consistency_score": consistency_score,
            "code_vs_noncode_ratio": code_ratio,
            "avg_messages_per_conversation": round(total_messages/total_conversations,2)
        },
        topic_metrics,
        dominant_topics
    )
    trend = trend_utils.analyze_learning_trend(messages)
    return {

        "total_messages": total_messages,
        "user_messages": user_messages,
        "assistant_messages": assistant_messages,

        "avg_messages_per_conversation": round(total_messages/total_conversations,2),

        "active_days": active_days,
        "most_active_hour": most_active_hour,

        "estimated_time_spent_minutes": total_time_minutes,

        "average_session_duration_minutes": avg_session_duration,

        "messages_per_day": messages_per_day,

        "code_vs_noncode_ratio": code_ratio,

        "consistency_score": consistency_score,

        "dominant_topics": dominant_topics,
        "topic_metrics": topic_metrics,

        "learning_behavior": behavior,
        "learning_growth_trend": trend
    }