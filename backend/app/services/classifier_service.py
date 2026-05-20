def classify_sentiment(body: str):

    negative_keywords = [
        "angry",
        "refund",
        "cancel",
        "bad",
        "terrible",
        "issue",
        "problem",
        "unhappy"
    ]

    positive_keywords = [
        "thank you",
        "great",
        "awesome",
        "happy",
        "excellent"
    ]

    body_lower = body.lower()

    for word in negative_keywords:
        if word in body_lower:
            return "negative"

    for word in positive_keywords:
        if word in body_lower:
            return "positive"

    return "neutral"


def classify_priority(body: str):

    urgent_keywords = [
        "urgent",
        "asap",
        "immediately",
        "critical",
        "refund",
        "cancel"
    ]

    body_lower = body.lower()

    for word in urgent_keywords:
        if word in body_lower:
            return "high"

    return "normal"