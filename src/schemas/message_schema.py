from pydantic import BaseModel, Field
from typing import Dict, Any
from datetime import datetime
import uuid


class KafkaMessage(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    payload: Dict[str, Any]
