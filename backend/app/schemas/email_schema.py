from pydantic import BaseModel, EmailStr
from datetime import datetime


class EmailIngest(BaseModel):
    message_id: str
    thread_id: str
    sender: EmailStr
    subject: str
    body: str
    timestamp: datetime