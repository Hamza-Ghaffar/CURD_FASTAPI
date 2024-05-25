from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# when user create 1st time to signup
def password_hash(password:str):
    return pwd_context.hash(password)

# when user Login
def verify_hash_pass(plain_password, hased_password):
    return pwd_context.verify(plain_password,hased_password)