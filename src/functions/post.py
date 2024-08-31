from fastapi import HTTPException
from src.models.post_model import Post
from sqlalchemy.orm import Session

# Create a new post
def create_post(user_id: int, post_data: dict, db: Session):
    post = Post(content=post_data["content"], user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# Update a post
def update_post(post_id: int, post_data: dict, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    post.content = post_data["content"]
    db.commit()
    return post

# Delete a post
def delete_post(post_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {"msg": "Post deleted"}

# Like a post
def like_post(post_id: int, user_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    post.likes += 1
    db.commit()
    return post

# Comment on a post
def comment_on_post(post_id: int, comment_data: dict, user_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Simple example; you can improve the structure to include Comment models
    post.comments.append(comment_data["comment"])
    db.commit()
    return post
