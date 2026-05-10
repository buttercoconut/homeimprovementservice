# api/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..config import async_session
from ..services.user_service import create_user
from ..models.user import UserCreate, User

# Dependency to get DB session
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await create_user(db, user_in)
    return user
