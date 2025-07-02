from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import diagnosis, literature, auth
from databases.mysql import get_db
from sqlalchemy.orm import Session
import uvicorn
from models import schemas

app = FastAPI(
    title="RareDx AI API",
    description="API for AI-powered rare disease diagnosis system",
    version="0.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(diagnosis.router, prefix="/diagnosis", tags=["Diagnosis"])
app.include_router(literature.router, prefix="/literature", tags=["Literature"])

@app.get("/")
async def root():
    return {"message": "Welcome to RareDx AI API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)