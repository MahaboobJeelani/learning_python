from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UserCreateModel, UserModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .service import UserService


auth_routes = APIRouter()
user_service = UserService()

@auth_routes.post('/signup', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user(user_data:UserCreateModel, session:AsyncSession = Depends(get_session)):
    user_exits = await user_service.user_exist(user_data.email, session)
    if user_exits:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user already exist")
    new_user = await user_service.create_user(user_data, session)

    return new_user
    