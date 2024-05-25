#Logic of user module
from pydantic import BaseModel, ValidationError,EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status,Depends
from typing import Optional
import db_models, utils,oauth2


#Class create_user for BaseModel
class UserRequestModel(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    mobile_number: str
    is_active: bool = True
    is_superuser: bool = False
    #avatar: Optional[bytes]

  
# Response Model
class UserResponseModel(BaseModel):
    
    username: str
    email: str
    class Config:
        orm_mode = True

class UserloginModel(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class Token_Response(BaseModel):
    access_token:str
    token_type:str
    
class Token_data:
    def __init__(self, username: str):
        self.username = username

    
    
#function for ADD_user
def create_user(db: Session, user_data_from_basemodel: UserRequestModel ):
    try:
        existing_user_verify=db.query(db_models.Users).filter(
            (db_models.Users.email==user_data_from_basemodel.email) 
            |(db_models.Users.username==user_data_from_basemodel.username) |
            (db_models.Users.mobile_number== user_data_from_basemodel.mobile_number)
            ).first()
        if existing_user_verify:
            error_message = f"""
            User with this Email ID: {user_data_from_basemodel.email} 
            or Mobile No: {user_data_from_basemodel.mobile_number}
            or Username: {user_data_from_basemodel.username} already exists
            """
            raise HTTPException(status_code=400, detail=error_message)
        #apply hashing to password attribute
        hash_pass=utils.password_hash(user_data_from_basemodel.password)
        user_data_from_basemodel.password=hash_pass
        
        user_data= user_data_from_basemodel.model_dump()
        db_user = db_models.Users(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except ValidationError as e:
        # Handle validation errors from Pydantic models
        raise HTTPException(status_code=400, detail=str(e))
    
#get user by id function
def get_user_by_id(id: int, db: Session):
    user = db.query(db_models.Users).filter(db_models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user

#get all_user function
def get_all_users(db: Session):
    users = db.query(db_models.Users).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users

 #delete user by id function
def delete_user_by_id(id: int, db: Session):
    user = db.query(db_models.Users).filter(db_models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()
    return user

# Update function  
def update_user(id: int, user_data_from_basemodel: UserRequestModel, db: Session):
    update_user = db.query(db_models.Users).filter(db_models.Users.id == id).first()
    
    # Check if the user exists
    if update_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user with id: {id} does not exist")
    #apply hashing to password attribute
    hash_pass=utils.password_hash(user_data_from_basemodel.password)
    user_data_from_basemodel.password=hash_pass
    # Update user data with the new values
    update_user_data = user_data_from_basemodel.model_dump()  # Changed method to get dict representation
    for key, value in update_user_data.items():
        setattr(update_user, key, value)
    
    # Commit the changes to the database
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()  # Rollback the transaction
        error_message = f"Error updating user: {e.orig}"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=error_message) from e
    
    return update_user_data

    