from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    os = Column(String)
    source = Column(String)
    exp_group = Column(Integer)


if __name__ == "__main__":
    with SessionLocal() as session:
        result = (
            session.query(User.country, User.os, func.count().label('count'))
            .filter_by(exp_group=3)
            .group_by(User.country, User.os)
            .having(func.count() > 100)
            .order_by(func.count().desc())
            .all()
        )


    result_list = [(row.country, row.os, row.count) for row in result]


    print(result_list)