from fastapi import HTTPException
from src.utils.email_otp import generate_otp, send_otp_email
from src.models.user_model import User
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to register a new user
def register_user(user_data: dict, db: Session):
    email = user_data.get("email")
    username = user_data.get("username")
    password = hash_password(user_data.get("password"))
    
    if db.query(User).filter((User.email == email) | (User.username == username)).first():
        raise HTTPException(status_code=400, detail="Email or Username already exists")
    
    otp = generate_otp()
    send_otp_email(email, otp)
    
    user = User(email=email, username=username, password=password, otp=otp)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Function to validate user login
def login_user(username_or_email: str, password: str, db: Session):
    user = db.query(User).filter((User.email == username_or_email) | (User.username == username_or_email)).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return user

# Function to validate OTP
def validate_otp(email: str, otp: int, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.otp != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    user.is_verified = True
    db.commit()
    return {"msg": "Email verified successfully"}
