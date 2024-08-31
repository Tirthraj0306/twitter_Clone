from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.functions.post import create_post, update_post, delete_post, like_post, comment_on_post
from src.database.database import get_db

router = APIRouter()

@router.post("/")
def create_post_route(post_data: dict, user_id: int, db: Session = Depends(get_db)):
    return create_post(user_id, post_data, db)

@router.put("/{post_id}")
def update_post_route(post_id: int, post_data: dict, db: Session = Depends(get_db)):
    return update_post(post_id, post_data, db)

@router.delete("/{post_id}")
def delete_post_route(post_id: int, db: Session = Depends(get_db)):
    return delete_post(post_id, db)

@router.post("/{post_id}/like")
def like_post_route(post_id: int, user_id: int, db: Session = Depends(get_db)):
    return like_post(post_id, user_id, db)

@router.post("/{post_id}/comment")
def comment_on_post_route(post_id: int, comment_data: dict, user_id: int, db: Session = Depends(get_db)):
    return comment_on_post(post_id, comment_data, user_id, db)
