from fastapi import HTTPException
from src.users.dtos import UserSchema,LoginSchema
from sqlalchemy.orm import Session
from src.users.models import UserModel
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta
import jwt

password_hasher = PasswordHash.recommended()

jwt_secret = settings.SECRET_KEY
jwt_algorithm = settings.ALGORITHM

def get_password_hash(password):
  return password_hasher.hash(password)

def register(body:UserSchema,db:Session):
  is_user=db.query(UserModel).filter(UserModel.username==body.username).first()
  if is_user:
    raise HTTPException(status_code=400, detail="Username already exists")
  is_user=db.query(UserModel).filter(UserModel.email==body.email).first()
  if is_user:
    raise HTTPException(status_code=400, detail="Email already exists")
  hash_password=get_password_hash(body.password)
  new_user=UserModel(
    name=body.name,
    username=body.username,
    hash_password=hash_password,
    email=body.email,
    mobile_no=body.mobile_no
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return{"message": "User registered successfully"}
def login_user(body:LoginSchema,db:Session):
  user=db.query(UserModel).filter(UserModel.username==body.username).first()
  if not user:
    raise HTTPException(status_code=400, detail="Invalid username or password")
  if not password_hasher.verify(body.password, user.hash_password):
    raise HTTPException(status_code=400, detail="Invalid username or password")
  exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
  token=jwt.encode({"_id": user.id,"exp": exp_time}, settings.SECRET_KEY, settings.ALGORITHM)
  
  return{"token":token}
  return{"message": "Login successful", "user": user}
