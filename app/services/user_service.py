# services/user_service.py
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.user import UserCreate, User

# In a real implementation, you would use SQLAlchemy models.
# This is a simplified placeholder.
async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    # Simulate database insertion
    return User(
        id=1,
        name=user_in.name,
        email=user_in.email,
        phone=user_in.phone,
        address=user_in.address,
        created_at=datetime.utcnow(),
    )

async def get_user(db: AsyncSession, user_id: int) -> User | None:
    # Placeholder: return a dummy user
    return User(
        id=user_id,
        name="John Doe",
        email="john@example.com",
        phone="123-456-7890",
        address="123 Main St",
        created_at=datetime.utcnow(),
    )
