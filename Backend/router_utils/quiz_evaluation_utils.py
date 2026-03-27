import requests
import os
import json

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
def evaluate_short_answer(question, reference_answer, user_answer, marks):

    prompt = f"""
You are an exam evaluator.

Question:
{question}

Reference Answer:
{reference_answer}

User Answer:
{user_answer}

Maximum Marks:
{marks}

Evaluate the user's answer based on conceptual correctness.

Return STRICT JSON format:

{{
 "score": number_between_0_and_{marks},
 "feedback": "short explanation"
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
            "messages":[
                {"role":"user","content":prompt}
            ]
        }
    )

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"score":0,"feedback":"Evaluation failed"}


def generate_feedback_summary(evaluation):

    prompt = f"""
You are an AI learning mentor.

Based on the quiz evaluation results below, analyze the learner's knowledge.

Evaluation Data:
{evaluation}

Provide a structured learning feedback including:

1. Summary of knowledge level
2. Strengths
3. Weaknesses
4. Recommendations for improvement

Return STRICT JSON format:

{{
 "summary": "...",
 "strengths": ["..."],
 "weaknesses": ["..."],
 "recommendations": ["..."]
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
            "messages":[
                {"role":"user","content":prompt}
            ]
        }
    )

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "summary":"Feedback generation failed",
            "strengths":[],
            "weaknesses":[],
            "recommendations":[]
        }



def evaluate_quiz(submission):

    total_marks = 0
    obtained_marks = 0

    results = []

    for q in submission:

        total_marks += q["marks"]

        if q["type"] == "mcq":

            if q["user_answer"] == q["correct_answer"]:
                score = q["marks"]
                feedback = "Correct answer"

            else:
                score = 0
                feedback = "Incorrect answer"

        else:

            evaluation = evaluate_short_answer(
                q["question"],
                q["reference_answer"],
                q["user_answer"],
                q["marks"]
            )

            score = evaluation["score"]
            feedback = evaluation["feedback"]

        obtained_marks += score

        results.append({
            "id": q["id"],
            "score": score,
            "feedback": feedback
        })

    percentage = round((obtained_marks/total_marks)*100,2)

    level = "Low"

    if percentage >= 80:
        level = "Strong Understanding"
    elif percentage >= 60:
        level = "Moderate Understanding"
    elif percentage >= 40:
        level = "Basic Understanding"

    evaluation_result = {
    "total_marks": total_marks,
    "obtained_marks": obtained_marks,
    "percentage": percentage,
    "knowledge_level": level,
    "question_results": results
}

    feedback_summary = generate_feedback_summary(evaluation_result)

    evaluation_result["feedback_summary"] = feedback_summary

    return evaluation_result

