from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: EmailStr
    mobile_no: str

class UserResponseSchema(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    mobile_no: str
class LoginSchema(BaseModel):
    username: str
    password: str