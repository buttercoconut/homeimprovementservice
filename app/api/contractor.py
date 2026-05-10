# api/contractor.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..config import async_session
from ..services.contractor_service import create_contractor
from ..models.contractor import ContractorCreate, Contractor

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

router = APIRouter(prefix="/contractors", tags=["contractors"])

@router.post("/", response_model=Contractor, status_code=status.HTTP_201_CREATED)
async def register_contractor(contractor_in: ContractorCreate, db: AsyncSession = Depends(get_db)):
    contractor = await create_contractor(db, contractor_in)
    return contractor
