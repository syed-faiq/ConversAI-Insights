from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    text: str
    time: Optional[float]


class MessageList(BaseModel):
    messages: List[Message]