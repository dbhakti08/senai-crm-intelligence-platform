# SenAI CRM Intelligence Platform

AI-powered enterprise CRM operations platform with:
- Email ingestion
- RAG-based policy retrieval
- Agentic escalation workflows
- AI summarization
- Sentiment analysis
- Operational analytics dashboard

---

# Architecture

```mermaid
flowchart TD

A[Enterprise Email Dataset] --> B[FastAPI Ingestion Pipeline]

B --> C[Heuristic Classification]
C --> D[Sentiment Analysis]
C --> E[Priority Detection]

B --> F[PostgreSQL Database]

G[Knowledge Base Markdown Docs] --> H[RAG Retrieval Engine]

H --> I[Agent Reasoning Engine]

F --> I

I --> J[AI Response Generator]

F --> K[Analytics APIs]

K --> L[Next.js Dashboard]

J --> L

# ER Diagram

```mermaid
erDiagram

EMAILS {

    int id
    string message_id
    string sender
    string subject
    text body
    string timestamp
    string thread_id

    string sentiment
    string priority

    text summary
}

KNOWLEDGE_BASE {

    string document_name
    text content
    string category
}

AGENT_TRACE {

    int id
    string thread_type
    text thought
    text action
    text observation
}