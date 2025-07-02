from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Annotated
from datetime import datetime
from databases.mysql import get_db
from databases.faiss_db import faiss_index
from models import schemas
from models.vlm_utils import generate_image_embedding, generate_text_embedding
from sqlalchemy.orm import Session
import os
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/submit", response_model=schemas.Diagnosis)
async def submit_case(
    symptoms: str = Form(...),  # ✅ Move this before 'image'
    image: UploadFile = File(...),
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    try:
        # Save uploaded image
        file_ext = os.path.splitext(image.filename)[1]
        filename = f"{uuid.uuid4()}{file_ext}"
        filepath = os.path.join(UPLOAD_DIR, filename)
        
        with open(filepath, "wb") as buffer:
            buffer.write(await image.read())

        # Generate embeddings
        image_embedding = generate_image_embedding(filepath)
        text_embedding = generate_text_embedding(symptoms)

        # Create diagnosis record
        db_diagnosis = schemas.DiagnosisCreate(
            image_path=filepath,
            symptoms=symptoms,
            user_id=current_user.id
        )
        # TODO: Save to database
        # db.add(db_diagnosis)
        # db.commit()
        # db.refresh(db_diagnosis)

        # Add to FAISS index
        combined_embedding = image_embedding + text_embedding
        faiss_index.add(combined_embedding)

        return JSONResponse(
            content={
                "message": "Case submitted successfully",
                "diagnosis_id": 1,  # Replace with actual ID
                "status": "processing"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing case: {str(e)}"
        )

@router.get("/results/{diagnosis_id}", response_model=schemas.DiagnosisResult)
async def get_diagnosis_results(
    diagnosis_id: int,
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        # TODO: Retrieve diagnosis from database
        # diagnosis = db.query(...).filter(...).first()
        
        # Mock results - replace with actual FAISS search
        mock_result = {
            "diagnosis_id": diagnosis_id,
            "disease_name": "Ehlers-Danlos Syndrome",
            "confidence": 0.87,
            "description": "A group of inherited disorders affecting connective tissues",
            "similar_cases": [
                {
                    "case_id": 101,
                    "similarity_score": 0.85,
                    "diagnosis": "Ehlers-Danlos Syndrome",
                    "patient_age": 32,
                    "patient_gender": "Female",
                    "symptoms": "Joint hypermobility, chronic pain"
                }
            ],
            "research_papers": [
                {
                    "title": "Genetic basis of Ehlers-Danlos Syndrome",
                    "source": "PubMed",
                    "year": 2022,
                    "url": "#"
                }
            ]
        }
        return mock_result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving results: {str(e)}"
        )

@router.get("/history", response_model=List[schemas.Diagnosis])
async def get_case_history(
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        # TODO: Query user's case history
        return []
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving case history: {str(e)}"
        )
        