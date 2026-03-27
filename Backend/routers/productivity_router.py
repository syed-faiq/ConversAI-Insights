from fastapi import APIRouter
from router_utils import productivity_utils
from database.mongodb import productivity_collection
from schemas.productivity_schema import ProductivityResponse

router = APIRouter()


@router.post("/productivity-analysis", response_model=ProductivityResponse)
async def productivity_analysis(metrics: dict):

    result = productivity_utils.analyze_productivity(metrics)

    data = {
        "metrics": metrics,
        "productivity_analysis": result
    }

    # Save to MongoDB
    db_result = await productivity_collection.insert_one(data)

    data["_id"] = str(db_result.inserted_id)

    return {
        "message": "AI productivity analysis completed",
        "productivity_analysis": result
    }