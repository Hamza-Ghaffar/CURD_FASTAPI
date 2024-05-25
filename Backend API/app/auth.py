from fastapi import APIRouter, Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import db_models, utils, oauth2
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from user import UserloginModel

Login_route=APIRouter(tags=["USERS LOGIN"])


@Login_route.post('/login/')
def User_Login(user_credentials:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    
    user=db.query(db_models.Users).filter(db_models.Users.email==user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid credential")
    
    if not utils.verify_hash_pass(user_credentials.password, user.password):
       raise HTTPException(status.HTTP_403_FORBIDDEN, 
                          detail=f'Invalid credential')
    
    #Create Token---impt part---
    access_token=oauth2.create_access_token(data={"username":user.username})
    print("OK")
    
    return {"access_token" : access_token, "token_type": "bearer"}
#"token_type": "bearer" this is by my own choice
