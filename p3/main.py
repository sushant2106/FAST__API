from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True


db=SessionLocal()

# @app.get('/')
# def index():
#     return {"msg":'Hello'}


# @app.get('/greet/{name}')
# def greet_name(name:str):
#     return {"greeting":f"Hello {name}"}

# @app.get('/greet')
# def greet_optional_name(name:Optional[str]="user"):
#     return {"message":f"Hello {name}"}


# @app.put('/item/{item_id}')
# def update_item(item_id:int,item:Item):
#     return {'name':item.name,
            
#             'description':item.description,
#             'price':item.price,
#             'on_offer':item.on_offer
#             }

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()

    return item

@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    
    )
    
    db_item=db.query(models.Item).filter(item.name==new_item.name).first()
    
    if db_item is not None:
        raise HTTPException(status_code=400,detail='Item is already exists')
    


    db.add(new_item)
    db.commit()
    return new_item

@app.put('item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer

    db.commit()
    return item_to_update


@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass