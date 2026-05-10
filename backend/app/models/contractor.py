# models/contractor.py
from pydantic import BaseModel
from typing import List

class Contractor(BaseModel):
    id: int
    name: str
    phone: str
    specialties: List[str]
    rating: float

class ContractorCreate(Contractor):
    pass
