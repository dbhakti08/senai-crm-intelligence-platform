from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.schemas.email_schema import EmailIngest
from app.models.email_model import Email
from app.db.session import get_db
from app.services.classifier_service import (
    classify_sentiment,
    classify_priority
)
from app.services.summary_service import generate_summary
from app.services.reply_service import generate_ai_reply
from app.services.reply_service import generate_ai_reply

router = APIRouter()


@router.post("/api/ingest")
def ingest_email(email: EmailIngest, db: Session = Depends(get_db)):

    new_email = Email(
        message_id=email.message_id,
        thread_id=email.thread_id,
        sender=email.sender,
        subject=email.subject,
        body=email.body,
        timestamp=email.timestamp,
        sentiment=classify_sentiment(email.body),
        priority=classify_priority(email.body),
        summary=generate_summary(email.body)
    ) 

    try:
        db.add(new_email)
        db.commit()
        db.refresh(new_email)

        return {
            "status": "success",
            "message": "Email stored successfully"
        }

    except IntegrityError:
        db.rollback()

        return {
            "status": "duplicate",
            "message": "Email already exists"
        }
@router.get("/api/thread/{thread_id}")
def get_thread(thread_id: str, db: Session = Depends(get_db)):

    emails = db.query(Email).filter(
        Email.thread_id == thread_id
    ).all()

    return {
        "thread_id": thread_id,
        "emails": emails
    }
@router.get("/api/emails/high-priority")
def get_high_priority_emails(db: Session = Depends(get_db)):

    emails = db.query(Email).filter(
        Email.priority == "high"
    ).all()

    return {
        "count": len(emails),
        "emails": emails
    }
@router.get("/api/search")
def search_emails(query: str, db: Session = Depends(get_db)):

    emails = db.query(Email).filter(
        Email.body.ilike(f"%{query}%")
    ).all()

    return {
        "query": query,
        "count": len(emails),
        "results": emails
    }
@router.get("/api/analytics/overview")
def analytics_overview(db: Session = Depends(get_db)):

    total_emails = db.query(Email).count()

    high_priority = db.query(Email).filter(
        Email.priority == "high"
    ).count()

    negative_sentiment = db.query(Email).filter(
        Email.sentiment == "negative"
    ).count()

    return {
        "total_emails": total_emails,
        "high_priority_emails": high_priority,
        "negative_sentiment_emails": negative_sentiment
    }
@router.get("/api/emails")
def get_all_emails(db: Session = Depends(get_db)):

    emails = db.query(Email).all()

    return emails
@router.get("/api/analytics/sentiments")
def sentiment_analytics(db: Session = Depends(get_db)):

    positive = db.query(Email).filter(
        Email.sentiment == "positive"
    ).count()

    negative = db.query(Email).filter(
        Email.sentiment == "negative"
    ).count()

    neutral = db.query(Email).filter(
        Email.sentiment == "neutral"
    ).count()

    return [
        {"name": "Positive", "count": positive},
        {"name": "Negative", "count": negative},
        {"name": "Neutral", "count": neutral},
    ]
@router.get("/api/analytics/sentiments")
def sentiment_analytics(db: Session = Depends(get_db)):

    positive = db.query(Email).filter(
        Email.sentiment == "positive"
    ).count()

    negative = db.query(Email).filter(
        Email.sentiment == "negative"
    ).count()

    neutral = db.query(Email).filter(
        Email.sentiment == "neutral"
    ).count()

    return [
        {"name": "Positive", "count": positive},
        {"name": "Negative", "count": negative},
        {"name": "Neutral", "count": neutral},
    ]
@router.get("/api/reply/{thread_id}")
def generate_reply(thread_id: str, db: Session = Depends(get_db)):

    emails = db.query(Email).filter(
        Email.thread_id == thread_id
    ).all()

    if not emails:
        return {
            "reply": "No conversation found."
        }

    latest_email = emails[-1]

    reply = generate_ai_reply(latest_email.body)

    return {
        "thread_id": thread_id,
        "reply": reply
    }
@router.get("/api/reply/{thread_id}")
def generate_reply(thread_id: str, db: Session = Depends(get_db)):

    emails = db.query(Email).filter(
        Email.thread_id == thread_id
    ).all()

    if not emails:
        return {
            "reply": "No conversation found."
        }

    latest_email = emails[-1]

    reply = generate_ai_reply(latest_email.body)

    return {
        "thread_id": thread_id,
        "reply": reply
    }