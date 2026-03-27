from fastapi import APIRouter
from router_utils import metrics_router_utils
from schemas.metrics_schema import MessageList

router = APIRouter()


@router.post("/metrices")
def calculate_basic_metrics(data: MessageList):
    return metrics_router_utils.basic_metrics(data.messages)