def analyze_learning_behavior(global_metrics, topic_metrics, dominant_topics):

    total_messages = global_metrics.get("total_messages", 0)
    messages_per_day = global_metrics.get("messages_per_day", 0)
    consistency_score = global_metrics.get("consistency_score", 0)
    code_ratio = global_metrics.get("code_vs_noncode_ratio", 0)

    primary_interest = None
    secondary_interest = None

    if dominant_topics:
        primary_interest = dominant_topics[0]

    if len(dominant_topics) > 1:
        secondary_interest = dominant_topics[1]

    # Learning intensity
    if messages_per_day > 20:
        learning_intensity = "Very High"
    elif messages_per_day > 10:
        learning_intensity = "High"
    elif messages_per_day > 5:
        learning_intensity = "Moderate"
    else:
        learning_intensity = "Low"

    # Technical usage
    if code_ratio > 0.7:
        technical_usage = "Very Technical"
    elif code_ratio > 0.4:
        technical_usage = "Technical"
    elif code_ratio > 0.2:
        technical_usage = "Mixed"
    else:
        technical_usage = "Mostly Non-Technical"

    # Consistency
    if consistency_score > 70:
        learning_consistency = "Highly Consistent"
    elif consistency_score > 40:
        learning_consistency = "Moderately Consistent"
    else:
        learning_consistency = "Irregular"

    # Engagement depth
    avg_msgs = global_metrics.get("avg_messages_per_conversation", 0)

    if avg_msgs > 15:
        engagement_depth = "Very Deep Discussions"
    elif avg_msgs > 8:
        engagement_depth = "Deep"
    elif avg_msgs > 4:
        engagement_depth = "Moderate"
    else:
        engagement_depth = "Short Queries"

    # AI dependency score
    ai_dependency_score = min(
        100,
        round(
            (messages_per_day * 2)
            + (consistency_score * 0.5)
            + (code_ratio * 30)
        )
    )

    return {

        "primary_interest": primary_interest,
        "secondary_interest": secondary_interest,
        "learning_intensity": learning_intensity,
        "technical_usage": technical_usage,
        "learning_consistency": learning_consistency,
        "engagement_depth": engagement_depth,
        "ai_dependency_score": ai_dependency_score
    }