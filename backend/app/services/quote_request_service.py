# services/quote_request_service.py
from typing import List
from ..models.quote_request import QuoteRequestCreate
from ..models.quote import Quote
from ..services.contractor_service import find_matching_contractors

# In-memory storage for demo
QUOTE_DB = []
QUOTE_ID_SEQ = 1

def process_quote_request(req: QuoteRequestCreate) -> List[Quote]:
    global QUOTE_ID_SEQ
    matches = find_matching_contractors(req.items, req.budget)
    quotes = []
    for contractor in matches:
        quote = Quote(
            id=QUOTE_ID_SEQ,
            quote_request_id=req.user_id,  # simplified
            contractor_id=contractor.id,
            amount=req.budget * 0.8,  # dummy calculation
            details=[f"Estimate for {item}" for item in req.items],
            created_at=req.request_datetime,
        )
        QUOTE_DB.append(quote)
        QUOTE_ID_SEQ += 1
        quotes.append(quote)
    return quotes
