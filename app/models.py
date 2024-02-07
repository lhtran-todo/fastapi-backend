from sqlalchemy import String, Text, Integer, Boolean, Column, text, TIMESTAMP
from app.database import Base

class Todo(Base):
  __tablename__ = 'todos'

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String(120), nullable=False)
  description = Column(Text, nullable=True)
  completed = Column(Boolean, default=True)
