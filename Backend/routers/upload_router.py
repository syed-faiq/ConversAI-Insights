from fastapi import APIRouter, UploadFile, File
from router_utils import upload_router_utils
from database.mongodb import metrics_collection
router = APIRouter()

@router.post("/upload_data")
async def upload_chat_file(file: UploadFile = File(...)):

    metrics = await upload_router_utils.handle_upload(file)

    # Save to MongoDB
    result = await metrics_collection.insert_one(metrics)

    metrics["_id"] = str(result.inserted_id)

    return metrics