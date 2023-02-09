from sqlalchemy import Column, Integer, String,Table
from database import Base 

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))