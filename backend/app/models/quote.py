# models/quote.py
from pydantic import BaseModel
from typing import List

class Quote(BaseModel):
    id: int
    quote_request_id: int
    contractor_id: int
    amount: float
    details: List[str]
    created_at: str

class QuoteCreate(Quote):
    pass
