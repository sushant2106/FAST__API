from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
from  . import models


app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()

    try:
        yield db
    
    finally:
        db.close()




class Blog(BaseModel):
    title:str
    body:str


@app.post('/blog')
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog=Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



