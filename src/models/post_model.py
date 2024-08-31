# src/models/post_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    likes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="post")
    owner = relationship("User", back_populates="posts")
