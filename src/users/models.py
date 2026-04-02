from sqlalchemy import Column,INTEGER,DateTime,Boolean,String
from src.utils.db import Base

class UserModel(Base):
    __tablename__="user_table"
    id=Column(INTEGER,primary_key=True)
    name=Column(String)
    username=Column(String,nullable=False)
    hash_password=Column(String,nullable=False)
    email=Column(String)
    mobile_no=Column(String)

    

