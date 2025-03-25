from sqlalchemy import Column, Integer, String
from database.connection import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    npm = Column(String(10), unique=True)