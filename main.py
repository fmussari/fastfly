# Create A REST API with FastAPI, SQLAlchemy and PostgreSQL.
# https://youtu.be/2g1ZjA6zHRo?si=AhaMkifAUbvOj5Sa
 
from fastapi import FastAPI, status, HTTPException
from http import HTTPStatus

#from pydantic import BaseModel
from schemas import ItemModel, ItemCreateModel, ItemPatchModel, ItemDeleteModel

from typing import Optional, List
from sqlalchemy.ext.asyncio import async_sessionmaker

#from database import SessionLocal
#from database import Session
from crud import CRUD
from database import engine

#import models
from models import Item

app = FastAPI(
    title = 'Noted API',
    description = 'Simple API'
)

""" Before async
db = SessionLocal()
db = Session()
class Item(BaseModel):
    id:int
    name:str
    description:str
    price:float
    on_offer:bool
    date_created:datetime

    class Config:
        orm_mode = True
"""
session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
db = CRUD()

@app.get('/items', response_model=List[ItemModel], status_code=status.HTTP_200_OK)
async def get_all_items():
    items = await db.get_all(session)
    return items

@app.post('/items', response_model=ItemModel, status_code=HTTPStatus.CREATED)
async def create_an_item(item_data:ItemCreateModel):
    new_item = Item(
        name=item_data.name,
        description=item_data.description,
        price=item_data.price,
        on_offer=item_data.on_offer
    )
    item = await db.add(session, new_item)

    return item

@app.get('/item/{item_id}', response_model=ItemModel, status_code=HTTPStatus.OK)
async def get_item_by_id(item_id:int):
    """API endpoint for retrieving an item by its ID
    """
    item = await db.get_by_id(session, item_id)
    if item is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail=f'Item with id={item_id} doesn\'t exist'
        )

    return item

@app.patch("/item/{item_id}", response_model=ItemModel, status_code=HTTPStatus.OK)
async def update_item(item_id:int, data:ItemPatchModel):
    """Update item by ID
    """
    updated_item = await db.update(
        session, item_id, data=data
    )

    return updated_item

@app.delete('/item/{item_id}', response_model=ItemDeleteModel, status_code=HTTPStatus.OK)
async def delete_item(item_id:int):
    """Delete item by id
    """
    item_to_delete = await db.get_by_id(session, item_id)
    if item_to_delete is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail=f'Item with id={item_id} doesn\'t exist'
        )
    
    await db.delete(session, item_to_delete)

    return {"detail": f"Item with id={item_id} successfully deleted"}
    



""" Before asyncio
@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):

    db_item = db.query(models.Item).filter(models.Item.name==item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Item already exists.')

    new_item = models.Item(
        name=item.name, 
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_an_item(item_id:int, item:Item):
    item_to_update = db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def delete_item(item_id:int):

    item_to_delete = db.query(models.Item).filter(models.Item.id==item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item doesn\'t exists.')
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
"""

"""
Before connecting to the database

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
    return {
        "id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "on_offer": item.on_offer
    }

@app.get('/greet/{name}')
def greet_name(name:str):
    return {"greeting": f"Hello {name}"}

@app.get('/greet/')
def greet_opt_name(name:Optional[str]='user'):
    return {"message": f"Hello {name}"}

"""

