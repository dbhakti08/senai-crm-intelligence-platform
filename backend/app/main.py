from fastapi import FastAPI
from app.api.email_routes import router as email_router
from app.db.database import engine, Base
from app.models.email_model import Email
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="SenAI CRM Intelligence Platform")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "SenAI CRM Backend Running"}


app.include_router(email_router)