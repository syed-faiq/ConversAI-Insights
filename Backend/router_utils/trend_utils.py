from datetime import datetime


TECH_KEYWORDS = [
    "python","code","function","api",
    "sql","javascript","class","debug",
    "error","algorithm","model","ai","Programming",
     "database","library","framework","development",
]


def analyze_learning_trend(messages):

    if not messages:
        return {}

    messages = sorted(messages, key=lambda x: x.get("time") or 0)

    mid = len(messages) // 2

    early = messages[:mid]
    recent = messages[mid:]


    def tech_ratio(msgs):

        if not msgs:
            return 0

        tech = 0

        for m in msgs:

            text = str(m.get("text","")).lower()

            if any(k in text for k in TECH_KEYWORDS):
                tech += 1

        return round(tech / len(msgs), 2)


    early_ratio = tech_ratio(early)
    recent_ratio = tech_ratio(recent)

    trend = "Stable"

    if recent_ratio - early_ratio > 0.1:
        trend = "Increasing"

    elif early_ratio - recent_ratio > 0.1:
        trend = "Decreasing"


    return {

        "trend": trend,
        "early_period_technical_ratio": early_ratio,
        "recent_period_technical_ratio": recent_ratio
    }