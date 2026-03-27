def process_quiz_submission(quiz, answers):

    answer_map = {a["question_id"]: a["answer"] for a in answers}

    submission = []

    for q in quiz:

        qid = q["id"]

        submission.append({
            "id": qid,
            "type": q["type"],
            "question": q["question"],
            "correct_answer": q.get("correct_answer"),
            "reference_answer": q.get("reference_answer"),
            "user_answer": answer_map.get(qid),
            "marks": q["marks"],
            "topic": q["topic"]
        })

    return submission
