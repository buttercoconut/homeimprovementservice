# services/contractor_service.py
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.contractor import ContractorCreate, Contractor

async def create_contractor(db: AsyncSession, contractor_in: ContractorCreate) -> Contractor:
    return Contractor(
        id=1,
        name=contractor_in.name,
        phone=contractor_in.phone,
        specialties=contractor_in.specialties,
        rating=4.5,
    )
