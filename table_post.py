from database import Base,SessionLocal
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    text = Column(String)
    topic = Column(String)


if  __name__ == '__main__':
    with SessionLocal() as session:
        some = (
            session.query(Post.id)
            .filter(Post.topic == 'business')
            .order_by(Post.id.desc())
            .limit(10)
            .all()
        )

    result = [post[0] for post in some]

    print (result)