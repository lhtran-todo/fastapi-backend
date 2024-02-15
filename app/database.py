from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DB_STRING_FILE_PATH

SQLALCHEMY_DATABASE_URL = ""
with open(DB_STRING_FILE_PATH, 'r') as file:
  SQLALCHEMY_DATABASE_URL = file.read()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()