from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    profile = relationship("Profile", back_populates="user", uselist=False)
    courses = relationship("Course", back_populates="teacher")