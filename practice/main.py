from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sales.db"

engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session=SessionLocal()
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)

Base.metadata.create_all(engine)

cust=session.query(Customers)





app=FastAPI()

@app.get('/')
def get_some():
    return {"key":"value"}

@app.get("/get-student/{student_id}")
def check(student_id:int):
    cust=session.query(Customers).filter(Customers.id==student_id).first()
    return {"Name":cust.name}




