from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Accessible Map AI Backend")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}