# api/quote_request.py
from fastapi import APIRouter, Depends
from typing import List
from ..models.quote_request import QuoteRequestCreate
from ..models.quote import Quote
from ..services.quote_request_service import process_quote_request

router = APIRouter(prefix="/quote-requests", tags=["quote-requests"])

@router.post("/", response_model=List[Quote])
def create_quote_request(req: QuoteRequestCreate):
    return process_quote_request(req)
