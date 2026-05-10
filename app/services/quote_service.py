# services/quote_service.py
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.quote import QuoteCreate, Quote

async def create_quote(db: AsyncSession, quote_in: QuoteCreate) -> Quote:
    return Quote(
        id=1,
        quote_request_id=quote_in.quote_request_id,
        contractor_id=quote_in.contractor_id,
        amount=quote_in.amount,
        details=quote_in.details,
        created_at=datetime.utcnow(),
    )
