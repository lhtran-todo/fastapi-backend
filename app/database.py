from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DB_STRING

engine = create_engine(DB_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()