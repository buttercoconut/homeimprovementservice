# api/quote_request.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..config import async_session
from ..services.quote_request_service import create_quote_request
from ..models.quote_request import QuoteRequestCreate, QuoteRequest

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

router = APIRouter(prefix="/quote-requests", tags=["quote-requests"])

@router.post("/", response_model=QuoteRequest, status_code=status.HTTP_201_CREATED)
async def submit_quote_request(qr_in: QuoteRequestCreate, db: AsyncSession = Depends(get_db)):
    qr = await create_quote_request(db, qr_in)
    return qr
