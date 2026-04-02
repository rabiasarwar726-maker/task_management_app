from fastapi import HTTPException
from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.users.models import UserModel
from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()

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