from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UserCreateModel, UserModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .service import UserService
from .schemas import UserLoginModel
from .utils import verify_password, create_access_token
from datetime import timedelta
from fastapi.responses import JSONResponse


auth_routes = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2

@auth_routes.post('/signup', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user(user_data:UserCreateModel, session:AsyncSession = Depends(get_session)):
    user_exits = await user_service.user_exist(user_data.email, session)
    if user_exits:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user already exist")
    new_user = await user_service.create_user(user_data, session)

    return new_user

@auth_routes.post('/login')
async def login_user(login_data:UserLoginModel, session:AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user_by_email(email, session) 

    if user is not None:
        password_valid = verify_password(password, user.password_hash)
        if password_valid:
            access_token = create_access_token(
                user_data = {
                    "email": user.email,
                    "user_uid": str(user.uid)
                }
            )

            refresh_token = create_access_token(
                user_data = {
                    "email": user.email,
                    "user_uid": str(user.uid)
                },
                refresh = True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content={
                    "message": "Login Successfull",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "user_uid": str(user.uid)
                    }
                }
            )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail= "Invalid user or Email"
    )