from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, LargeBinary, DateTime,func
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,autoincrement=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True,nullable=False)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    mobile_number = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String,nullable=False)
    is_active = Column(Boolean, default=True,nullable=False)
    is_superuser = Column(Boolean, default=False)
    avatar = Column(LargeBinary) 
    created_at = Column(DateTime, default=func.now(), nullable=False)
    

