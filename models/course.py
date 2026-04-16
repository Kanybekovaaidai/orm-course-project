from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    teacher_id = Column(Integer, ForeignKey("users.id"))

    teacher = relationship("User", back_populates="courses")
    students = relationship("Student", secondary="enrollments", back_populates="courses")