import datetime
from typing import Optional
from pydantic import BaseModel, Field

class FeedGet(BaseModel):
    action : str = ""
    post_id: int 
    time : datetime.datetime
    user_id: int
    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id : int
    text : str = ""
    topic : str = ""
    class Config:
        orm_mode = True

class UserGet(BaseModel):
   id: int
   gender: int
   age : int
   country : str = "" 
   city : str = ""
   os : str = ""
   source : str = "" 
   exp_group : int
   class Config:
        orm_mode = True 