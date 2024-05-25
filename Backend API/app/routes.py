from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import user, oauth2


main_router = APIRouter(
    prefix="/user",
    tags=['USERS']
    )


#ADD USER
@main_router.post("/")
def create_user_route(user_data_from_basemodel: user.UserRequestModel, db: Session = Depends(get_db),
                      Token_verify: int= Depends(oauth2.Token_Payload_verify)):
    try:
        db_user = user.create_user(db, user_data_from_basemodel)
        
        # Return the newly created user
        return db_user
    except Exception as e:
        # Handle any errors
        raise HTTPException(status_code=500, detail=str(e))

#GET USER BY ID
@main_router.get("/{user_id}", response_model=user.UserResponseModel, )
def get_user_route_id(user_id: int, db: Session = Depends(get_db)):
    db_user = user.get_user_by_id(user_id, db)
    return db_user

# GET ALL USERS
@main_router.get("/",response_model=List[user.UserResponseModel])
def get_all_users_route(db: Session = Depends(get_db),
                      Token_verify: int= Depends(oauth2.Token_Payload_verify)):
        db_users = user.get_all_users(db)
        return db_users

#Delete USER BY ID
@main_router.delete("/{user_id}",)
def delete_user_route(user_id: int, db: Session = Depends(get_db),
                      Token_verify: int= Depends(oauth2.Token_Payload_verify)):
    db_user = user.delete_user_by_id(user_id, db)
    return {"detail": f"User with id {user_id} has been deleted successfully"}

#Update USER
@main_router.put("/{user_id}")
def update_user_route_id(user_id: int, user_data_from_basemodel: user.UserRequestModel, db: Session = Depends(get_db)
                         ,Token_verify: int= Depends(oauth2.Token_Payload_verify)):
    updated_user = user.update_user(user_id, user_data_from_basemodel, db)
    return updated_user 