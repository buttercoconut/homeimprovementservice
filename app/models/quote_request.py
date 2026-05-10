# models/quote_request.py
from pydantic import BaseModel
from datetime import datetime
from typing import List

class QuoteRequestBase(BaseModel):
    user_id: int
    items: List[str]
    budget: float

class QuoteRequestCreate(QuoteRequestBase):
    pass

class QuoteRequest(QuoteRequestBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
