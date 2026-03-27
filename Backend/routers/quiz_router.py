from fastapi import APIRouter
from router_utils.quiz_utils import generate_quiz
from router_utils.quiz_submission_utils import process_quiz_submission
from router_utils.quiz_evaluation_utils import evaluate_quiz
from database.mongodb import quiz_collection
from schemas.quiz_schema import QuizResponse
from schemas.quiz_submission_schema import QuizSubmissionRequest, QuizSubmissionResponse
from database.mongodb import quiz_submission_collection
from database.mongodb import quiz_evaluation_collection
from schemas.quiz_evaluation_schema import QuizEvaluationRequest, QuizEvaluationResponse
router = APIRouter()


@router.post("/generate-quiz", response_model=QuizResponse)
async def generate_quiz_endpoint(data: dict):

    metrics = data

    quiz_result = generate_quiz(metrics)

    data_to_store = {
        "metrics": metrics,
        "quiz": quiz_result.get("quiz", [])
    }

    result = await quiz_collection.insert_one(data_to_store)

    data_to_store["_id"] = str(result.inserted_id)

    return {
        "message": "Quiz generated successfully",
        "quiz": quiz_result.get("quiz", [])
    }


@router.post("/submit-quiz", response_model=QuizSubmissionResponse)
async def submit_quiz(data: QuizSubmissionRequest):

    quiz = data.quiz
    answers = data.answers

    submission = process_quiz_submission(
        [q.dict() for q in quiz],
        [a.dict() for a in answers]
    )

    data_to_store = {
        "quiz": [q.dict() for q in quiz],
        "answers": [a.dict() for a in answers],
        "submission": submission
    }

    result = await quiz_submission_collection.insert_one(data_to_store)

    data_to_store["_id"] = str(result.inserted_id)

    return {
        "message": "Quiz submitted successfully",
        "submission": submission
    }




@router.post("/evaluate-quiz", response_model=QuizEvaluationResponse)
async def evaluate_quiz_endpoint(data: QuizEvaluationRequest):

    submission = data.submission

    evaluation_result = evaluate_quiz(submission)

    data_to_store = {
        "submission": submission,
        "evaluation": evaluation_result
    }

    result = await quiz_evaluation_collection.insert_one(data_to_store)

    data_to_store["_id"] = str(result.inserted_id)

    return {
        "message": "Quiz evaluated successfully",
        "evaluation": evaluation_result
    }