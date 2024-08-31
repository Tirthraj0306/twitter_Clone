from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.models.post_model import Post
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to get user by ID
def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Function to get all posts by a user
def get_user_posts(user_id: int, db: Session):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found for this user")
    return posts

# Function to update user profile
def update_user_profile(user_id: int, user_data: dict, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if "email" in user_data:
        user.email = user_data["email"]
    if "username" in user_data:
        user.username = user_data["username"]
    if "password" in user_data:
        user.password = pwd_context.hash(user_data["password"])
    
    db.commit()
    db.refresh(user)
    return user

# Function to delete a user
def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"msg": "User deleted successfully"}
