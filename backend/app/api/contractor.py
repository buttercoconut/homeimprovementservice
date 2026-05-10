# api/contractor.py
from fastapi import APIRouter
from ..models.contractor import Contractor
from ..services.contractor_service import CONTRACTORS

router = APIRouter(prefix="/contractors", tags=["contractors"])

@router.get("/", response_model=list[Contractor])
def list_contractors():
    return CONTRACTORS
