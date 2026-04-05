from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.users.dtos import UserSchema,LoginSchema
from src.utils.db import get_db
from src.users import controller


user_routes=APIRouter(prefix="/users")


@user_routes.post("/register",status_code=status.HTTP_201_CREATED)
def register(body: UserSchema, db: Session=Depends(get_db)):
    return controller.register(body, db)


@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session):
    return controller.login_user(body,db)