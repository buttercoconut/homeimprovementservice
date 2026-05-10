# models/quote_request.py
from pydantic import BaseModel
from typing import List

class QuoteRequest(BaseModel):
    user_id: int
    items: List[str]
    budget: float
    request_datetime: str

class QuoteRequestCreate(QuoteRequest):
    pass
