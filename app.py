from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal 
from table_user import User  
from table_post import Post 
from table_feed import Feed 
from schema import UserGet, PostGet


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



