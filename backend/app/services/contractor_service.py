# services/contractor_service.py
from typing import List
from ..models.contractor import Contractor

# Dummy data for contractors
CONTRACTORS = [
    Contractor(id=1, name="ABC Construction", phone="010-1111-1111", specialties=["kitchen", "bathroom"], rating=4.5),
    Contractor(id=2, name="XYZ Renovations", phone="010-2222-2222", specialties=["roof", "basement"], rating=4.0),
]

def find_matching_contractors(items: List[str], budget: float) -> List[Contractor]:
    # Simple matching: return contractors that have at least one specialty in items and rating > 4.0
    matches = []
    for c in CONTRACTORS:
        if any(item in c.specialties for item in items) and c.rating >= 4.0:
            matches.append(c)
    return matches
