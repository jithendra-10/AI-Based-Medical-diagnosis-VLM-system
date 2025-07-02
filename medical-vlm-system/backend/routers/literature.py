from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from databases.mysql import get_db
from sqlalchemy.orm import Session
from models import schemas
from .auth import get_current_user

router = APIRouter()

@router.post("/search", response_model=List[schemas.ResearchPaper])
async def search_literature(
    query: schemas.LiteratureSearchQuery,
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        # TODO: Implement actual literature search (PubMed API, etc.)
        # Mock response for development
        mock_papers = [
            {
                "title": f"Research on {query.query}",
                "authors": ["Author A", "Author B"],
                "abstract": f"This paper discusses important findings about {query.query}",
                "source": "PubMed",
                "year": 2023,
                "url": "#",
                "relevance_score": 0.95
            }
        ]
        return mock_papers[:query.limit]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error searching literature: {str(e)}"
        )

@router.get("/paper/{paper_id}", response_model=schemas.ResearchPaper)
async def get_paper_details(
    paper_id: str,
    current_user: schemas.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        # TODO: Implement actual paper retrieval
        return {
            "title": "Detailed Research Paper",
            "authors": ["Researcher X", "Researcher Y"],
            "abstract": "Detailed abstract of the research paper...",
            "source": "PubMed",
            "year": 2022,
            "url": "#",
            "relevance_score": 0.92
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving paper: {str(e)}"
        )