from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import SessionLocal 
from table_user import User  
from table_post import Post 
from table_feed import Feed 
from schema import UserGet, PostGet, FeedGet
from typing import List



app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db

@app.get("/user/{id}", response_model=UserGet)
def get_user_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(404, 'id not found')
    else:
        return user

@app.get("/post/{id}", response_model=PostGet)
def get_post_id(id: int,db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(404, 'id not found')
    else:
        return post

@app.get("/user/{id}/feed", response_model = List[FeedGet])
def get_action_user(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed).filter(Feed.user_id == id).order_by(desc(Feed.time)).limit(limit).all()


@app.get("/post/{id}/feed", response_model = List[FeedGet])
def get_action_post(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed).filter(Feed.post_id == id).order_by(desc(Feed.time)).limit(limit).all()



