# from fastapi import FastAPI,Depends,status,HTTPException
# from .schemas import Product,UserOut,User
# from .database import session,engine
# from . import models,utils
# from sqlalchemy.orm import Session
# from .routers import post,user,auth

# # from app.routers import post,user


# app=FastAPI()

# models.Base.metadata.create_all(bind=engine)





# def get_db():
#     with session() as db:
#         yield db




# @app.get("/products")
# def get_all_products(db:Session=Depends(get_db)):
#     db_products=db.query(models.Product).all()

#     return db_products

# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)



# @app.get("/products/{id}")
# def get_product_by_id(db:Session=Depends(get_db)):
#     db_product=db.query(models.Product).filter(models.Product.id==id).first()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth
# from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}

    



