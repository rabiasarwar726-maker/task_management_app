from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: EmailStr
    mobile_no: str