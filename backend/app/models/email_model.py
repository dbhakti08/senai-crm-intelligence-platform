from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.database import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, unique=True, nullable=False)
    thread_id = Column(String, nullable=False)
    sender = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    sentiment = Column(String, nullable=True)
    priority = Column(String, nullable=True)
    summary = Column(Text, nullable=True)
