import json

from app.db.database import SessionLocal
from app.models.email_model import Email

from app.services.classifier_service import (
    classify_priority,
    classify_sentiment
)

from app.services.summary_service import generate_summary

db = SessionLocal()

with open("data/email-data-advanced.json", "r") as file:

    emails = json.load(file)

    for email in emails:

        existing_email = db.query(Email).filter(
            Email.message_id == email["message_id"]
        ).first()

        if existing_email:
            continue

        sentiment = classify_sentiment(email["body"])

        priority = classify_priority(email["body"])

        summary = generate_summary(email["body"])

        new_email = Email(

            message_id=email["message_id"],
            sender=email["sender"],
            subject=email["subject"],
            body=email["body"],
            timestamp=email["timestamp"],
            thread_id=email["thread_id"],

            sentiment=sentiment,
            priority=priority,
            summary=summary
        )

        db.add(new_email)

    db.commit()

print("Enterprise email dataset ingested successfully.")