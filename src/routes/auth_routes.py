from fastapi import APIRouter, Depends
from src.functions.auth import register_user, login_user, validate_otp
from src.database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register")
def register(user_data: dict, db: Session = Depends(get_db)):
    return register_user(user_data, db)

@router.post("/login")
def login(username_or_email: str, password: str, db: Session = Depends(get_db)):
    return login_user(username_or_email, password, db)

@router.post("/verify-otp")
def verify_otp(email: str, otp: int, db: Session = Depends(get_db)):
    return validate_otp(email, otp, db)
