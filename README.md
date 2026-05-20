# SenAI CRM Intelligence Platform

AI-powered CRM intelligence platform for customer support operations.

Built using:
- FastAPI
- PostgreSQL
- Next.js
- Tailwind CSS
- SQLAlchemy

---

# Features

## AI Email Intelligence
- Sentiment analysis
- Priority classification
- Email summarization
- AI-generated support replies

---

## CRM Operations
- Email ingestion APIs
- Conversation thread viewer
- Search functionality
- High-priority escalation tracking

---

## Analytics Dashboard
- Total emails overview
- Negative sentiment tracking
- Priority monitoring
- Sentiment visualization charts

---

# Architecture

Frontend:
- Next.js
- Tailwind CSS
- Recharts

Backend:
- FastAPI
- SQLAlchemy
- PostgreSQL

AI Layer:
- Rule-based NLP pipeline
- Sentiment classification
- AI response generation

---

# API Endpoints

## Email APIs
- POST /api/ingest
- GET /api/emails
- GET /api/thread/{thread_id}

## Search APIs
- GET /api/search

## Analytics APIs
- GET /api/analytics/overview
- GET /api/analytics/sentiments

## AI APIs
- GET /api/reply/{thread_id}

---

# Screenshots

## Dashboard
(Add screenshot here)

## AI Reply Generation
(Add screenshot here)

---

# Local Setup

## Backend

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Future Improvements

- OpenAI/Gemini integration
- Vector database support
- Semantic search
- RAG pipelines
- Multi-user authentication
- Real-time notifications

---

# Author

Bhakti Dudile