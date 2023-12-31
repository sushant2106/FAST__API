from fastapi import FastAPI,Depends,status,Response
from schemas import Blog
from database import engine,Base,SessionLocal
import models,schemas
from sqlalchemy.orm import Session 


models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    
    finally:
        db.close()



app=FastAPI()

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def show(response:Response,id:int,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'details':f"Id is not present in {id}"}
    return blog




   