from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["chatgpt_learning_analyzer"]

conversations_collection = db["conversations"]
metrics_collection = db["metrics"]
productivity_collection = db["productivity_analysis"]
quiz_collection = db["quiz"]
quiz_submission_collection = db["quiz_submissions"]
quiz_evaluation_collection = db["quiz_evaluations"]