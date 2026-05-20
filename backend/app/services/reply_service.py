def generate_ai_reply(body: str):

    body_lower = body.lower()

    if "refund" in body_lower:

        return (
            "We are sorry for the inconvenience. "
            "Our support team will process your refund request shortly."
        )

    if "cancel" in body_lower:

        return (
            "We understand your concern. "
            "Our team will assist you with the cancellation process."
        )

    if "issue" in body_lower or "problem" in body_lower:

        return (
            "We apologize for the issue you are facing. "
            "Our technical support team is investigating this matter."
        )

    return (
        "Thank you for contacting support. "
        "Our team will get back to you shortly."
    )