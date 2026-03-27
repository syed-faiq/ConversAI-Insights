from collections import defaultdict
from datetime import datetime


PROGRAMMING_KEYWORDS = [
    "code","python","javascript","java","api",
    "function","class","bug","error","debug",
    "algorithm","database","sql","react","node"
]

AI_KEYWORDS = [
    "ai","machine learning","ml","llm",
    "neural network","deep learning",
    "model","training","dataset"
]

CAREER_KEYWORDS = [
    "job","career","interview","resume",
    "hiring","salary","internship"
]


CODE_KEYWORDS = [
    "python","code","function","class",
    "debug","error","sql","api"
]


def detect_topic(text):

    text = text.lower()

    if any(k in text for k in PROGRAMMING_KEYWORDS):
        return "programming"

    if any(k in text for k in AI_KEYWORDS):
        return "ai_ml"

    if any(k in text for k in CAREER_KEYWORDS):
        return "career"

    return "general"



def categorize_topics(messages):

    topic_messages = defaultdict(list)

    for msg in messages:

        text = str(msg.get("text",""))

        topic = detect_topic(text)

        topic_messages[topic].append(msg)


    topic_metrics = {}

    for topic, msgs in topic_messages.items():

        timestamps = []
        conversations = set()
        code_messages = 0
        days = set()

        msgs = sorted(msgs, key=lambda x: x.get("time") or 0)

        total_seconds = 0

        for i, msg in enumerate(msgs):

            text = str(msg.get("text","")).lower()

            time = msg.get("time")

            convo = msg.get("conversation_id")

            if convo:
                conversations.add(convo)

            if time:
                timestamps.append(time)

                dt = datetime.fromtimestamp(time)
                days.add(dt.date())

            if any(k in text for k in CODE_KEYWORDS):
                code_messages += 1

            if i > 0:

                prev = msgs[i-1]

                t1 = prev.get("time")
                t2 = msg.get("time")

                if t1 and t2:

                    gap = t2 - t1

                    if 0 < gap < 600:
                        total_seconds += gap


        messages_count = len(msgs)
        conversations_count = len(conversations)

        time_minutes = round(total_seconds/60,2)

        messages_per_convo = 0
        avg_session_duration = 0
        code_ratio = 0

        if conversations_count:
            messages_per_convo = round(messages_count/conversations_count,2)
            avg_session_duration = round(time_minutes/conversations_count,2)

        if messages_count:
            code_ratio = round(code_messages/messages_count,2)


        topic_metrics[topic] = {

            "messages":messages_count,
            "conversations":conversations_count,
            "time_spent_minutes":time_minutes,
            "messages_per_conversation":messages_per_convo,
            "avg_session_duration_minutes":avg_session_duration,
            "active_days":len(days),
            "code_ratio":code_ratio
        }


    dominant_topics = sorted(
        topic_metrics,
        key=lambda t: topic_metrics[t]["messages"],
        reverse=True
    )


    return {

        "dominant_topics":dominant_topics,
        "topic_metrics":topic_metrics
    }