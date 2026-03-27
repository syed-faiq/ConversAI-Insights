import requests
import json
import os

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_quiz(metrics):

    dominant_topics = metrics.get("dominant_topics", [])
    learning_behavior = metrics.get("learning_behavior", {})
    productivity = metrics.get("productivity_analysis", {})

    prompt = f"""
You are an AI tutor.

Generate a quiz to evaluate whether the user actually learned from ChatGPT.

User learning profile:
Dominant Topics: {dominant_topics}

Learning Behavior:
{learning_behavior}

Productivity Score:
{productivity}

Rules:

1. Generate 5 MCQ questions
2. Generate 3 short conceptual questions
3. Focus on dominant topics
4. Questions must test understanding not memorization
5. Difficulty should be medium

Return STRICT JSON format:

{{
 "quiz":[
   {{
     "type":"mcq",
     "question":"question text",
     "options":["A","B","C","D"],
     "answer":"correct option",
     "topic":"programming",
     "marks":1
   }},
   {{
     "type":"short",
     "question":"conceptual question",
     "topic":"ai_ml",
     "reference_answer":"reference answer",
     "marks":5
   }}
 ]
}}
"""

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

    try:
        quiz = json.loads(content)
    except:
        quiz = {"quiz": []}

    return quiz
