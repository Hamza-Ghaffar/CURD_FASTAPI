from jose import JWTError, jwt
from datetime import datetime, timedelta,timezone  
from fastapi import Depends,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import secrets,user,database,logging,db_models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login/')

#Secret Key
#Algo
#Expriatio Time

random_bytes = secrets.token_hex(32)

SECRET_KEY = random_bytes
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

#create access_token -
def create_access_token(data:dict):
    to_encode=data.copy()
    
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt_token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded_jwt_token
 
 #verify access_token--
  
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = user.Token_data(username=username) 
        return token_data
    except JWTError as e:
        # Log the error for debugging purposes
        logging.error(f"JWT verification failed: {e}")
        raise credentials_exception from e 
  
def Token_Payload_verify(token:str=Depends(oauth2_scheme),db: Session=Depends(database.get_db)):
    
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail=f'Could not validate user', headers={"WWW-Authenticate": "Bearer"})
    
    
    token=verify_access_token(token, credential_exception)
    Payload_verify= db.query(db_models.Users).filter(db_models.Users.username==token.username).first()

    return Payload_verify