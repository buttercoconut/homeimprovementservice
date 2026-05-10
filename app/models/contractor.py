# models/contractor.py
from pydantic import BaseModel
from typing import List

class ContractorBase(BaseModel):
    name: str
    phone: str
    specialties: List[str]
    rating: float

class ContractorCreate(ContractorBase):
    pass

class Contractor(ContractorBase):
    id: int

    class Config:
        orm_mode = True
