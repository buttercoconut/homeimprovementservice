# models/quote.py
from pydantic import BaseModel
from datetime import datetime

class QuoteBase(BaseModel):
    quote_request_id: int
    contractor_id: int
    amount: float
    details: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
