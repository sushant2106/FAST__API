from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import Base
from sqlalchemy import Column,Integer,String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

class Blog(Base):
    __tablename__ = "Blog"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




