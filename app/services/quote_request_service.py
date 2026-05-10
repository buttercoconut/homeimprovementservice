# services/quote_request_service.py
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.quote_request import QuoteRequestCreate, QuoteRequest

async def create_quote_request(db: AsyncSession, qr_in: QuoteRequestCreate) -> QuoteRequest:
    return QuoteRequest(
        id=1,
        user_id=qr_in.user_id,
        items=qr_in.items,
        budget=qr_in.budget,
        created_at=datetime.utcnow(),
    )
