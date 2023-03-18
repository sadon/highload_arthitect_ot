from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
#from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) #change spec
    is_active = Column(Boolean, default=True)

    # https://github.com/OtusTeam/highload/blob/master/homework/openapi.json
    first_name = Column(String, unique=False, index=False)
    second_name = Column(String, unique=False, index=False)
    birthday = Column(Date, unique=False, index=False)
    male_sign = Column(Boolean, unique=False, index=False)
    biography = Column(String, unique=False, index=True)
    city = Column(String, unique=False, index=True)

    #items = relationship("Item", back_populates="owner")
