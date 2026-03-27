import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

import requests
import json

def call_llm(prompt):

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    return content


def generate_summary(metrics):

    prompt = f"""
You are an AI learning analytics expert.

Based on the following ChatGPT usage metrics, generate a short summary of the user's learning behavior.

Metrics:
{metrics}

Return ONLY 2-3 sentences summary.
"""

    return call_llm(prompt)


def generate_strengths(metrics):

    prompt = f"""
Analyze the following ChatGPT learning metrics and identify the user's strengths.

Metrics:
{metrics}

Return a 2-3 bullet points of strengths.

Example:
"Strong technical engagement", "Consistent learning habit"
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except:
        return [response]


def generate_weaknesses(metrics):

    prompt = f"""
Analyze the following ChatGPT learning metrics and identify weaknesses in the user's learning pattern.

Metrics:
{metrics}

Return 2-3 bullet points of weaknesses.
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except:
        return [response]


def generate_recommendations(metrics):

    prompt = f"""
Based on these ChatGPT usage metrics, suggest recommendations to improve learning productivity.

Metrics:
{metrics}

Return 2-3 bullet points of recommendations.
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except:
        return [response]


def ai_productivity_analysis(metrics):

    summary = generate_summary(metrics)

    strengths = generate_strengths(metrics)

    weaknesses = generate_weaknesses(metrics)

    recommendations = generate_recommendations(metrics)

    return {
        "summary": summary,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }

def analyze_productivity(metrics):

    productivity_score = calculate_productivity_score(metrics)

    ai_analysis = ai_productivity_analysis(metrics)

    return {
        "productivity_score": productivity_score,
        "productivity_level": classify_productivity(productivity_score),
        "ai_analysis": ai_analysis
    }


def calculate_productivity_score(metrics):

    score = 0

    # activity
    if metrics["messages_per_day"] > 10:
        score += 25
    elif metrics["messages_per_day"] > 5:
        score += 15
    else:
        score += 5

    # consistency
    if metrics["consistency_score"] > 70:
        score += 25
    elif metrics["consistency_score"] > 40:
        score += 15
    else:
        score += 5

    # learning intensity
    behavior = metrics.get("learning_behavior", {})

    if behavior.get("learning_intensity") == "High":
        score += 25
    elif behavior.get("learning_intensity") == "Moderate":
        score += 15
    else:
        score += 5

    # technical usage
    code_ratio = metrics.get("code_vs_noncode_ratio", 0)

    if code_ratio > 0.6:
        score += 25
    elif code_ratio > 0.3:
        score += 15
    else:
        score += 5

    return min(score, 100)


def classify_productivity(score):

    if score >= 75:
        return "Highly Productive"

    if score >= 50:
        return "Moderately Productive"

    if score >= 30:
        return "Low Productivity"

    return "Very Low Productivity"
