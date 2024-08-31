from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.functions.post import create_post
from src.models.post_model import Post
from src.database.database import get_db

router = APIRouter()

# View posts by user
@router.get("/posts/{user_id}")
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    return posts
