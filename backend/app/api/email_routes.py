from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.email_model import Email

from app.services.reply_service import generate_ai_reply
from app.services.rag_service import search_knowledge_base
from app.services.agent_service import generate_agent_trace

router = APIRouter()


@router.get("/api/emails")
def get_emails():

    db: Session = SessionLocal()

    emails = db.query(Email).all()

    return emails


@router.get("/api/search")
def search_emails(query: str):

    db: Session = SessionLocal()

    emails = db.query(Email).filter(
        Email.subject.contains(query)
    ).all()

    return {
        "results": emails
    }


@router.get("/api/threads/{thread_id}")
def get_thread(thread_id: str):

    db: Session = SessionLocal()

    emails = db.query(Email).filter(
        Email.thread_id == thread_id
    ).all()

    return emails


@router.post("/api/respond/{email_id}")
def generate_reply(email_id: int):

    db: Session = SessionLocal()

    email = db.query(Email).filter(
        Email.id == email_id
    ).first()

    if not email:

        return {
            "error": "Email not found"
        }

    reply = generate_ai_reply(email.body)

    return {
        "reply": reply
    }


@router.get("/api/analytics/overview")
def analytics_overview():

    db: Session = SessionLocal()

    total_emails = db.query(Email).count()

    negative_emails = db.query(Email).filter(
        Email.sentiment == "negative"
    ).count()

    high_priority = db.query(Email).filter(
        Email.priority == "high"
    ).count()

    return {
        "total_emails": total_emails,
        "negative_emails": negative_emails,
        "high_priority": high_priority
    }


@router.get("/api/rag/search")
def rag_search(query: str):

    results = search_knowledge_base(query)

    return {
        "query": query,
        "results": results
    }
@router.get("/api/agent/trace")
def agent_trace(thread_type: str):

    trace = generate_agent_trace(thread_type)

    return {
        "thread_type": thread_type,
        "trace": trace
    }