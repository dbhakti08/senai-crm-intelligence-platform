def generate_summary(body: str):

    sentences = body.split(".")

    if len(sentences) > 0:
        return sentences[0].strip()

    return body[:100]