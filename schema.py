import datetime
from pydantic import BaseModel

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

class FeedGet(BaseModel):
    action : str = ""
    post_id: int 
    time : datetime.datetime
    user_id: int
    user : UserGet
    post : PostGet
    class Config:
        orm_mode = True