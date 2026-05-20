import os

KB_PATH = "backend/knowledge_base"


def search_knowledge_base(query: str):

    query = query.lower()

    results = []

    if not os.path.exists(KB_PATH):

        return [{
            "error": f"Knowledge base folder not found: {KB_PATH}"
        }]

    for filename in os.listdir(KB_PATH):

        filepath = os.path.join(KB_PATH, filename)

        with open(filepath, "r") as file:

            content = file.read()

            content_lower = content.lower()

            score = 0

            for word in query.split():

                if word in content_lower:
                    score += 1

            if score > 0:

                results.append({
                    "source": filename,
                    "score": score,
                    "content": content[:1000]
                })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:3]