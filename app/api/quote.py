# api/quote.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..config import async_session
from ..services.quote_service import create_quote
from ..models.quote import QuoteCreate, Quote

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.post("/", response_model=Quote, status_code=status.HTTP_201_CREATED)
async def submit_quote(quote_in: QuoteCreate, db: AsyncSession = Depends(get_db)):
    quote = await create_quote(db, quote_in)
    return quote
