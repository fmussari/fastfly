from models import Item
from crud import CRUD
from database import engine
from sqlalchemy.ext.asyncio import async_sessionmaker
import asyncio

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
db = CRUD()

dictionary = {
  "name": "Coffee",
  "description": "Good Coffee",
  "price": 12.5,
  "on_offer": True
}

      
async def create_an_item():
    new_item = Item(
        name=dictionary['name'],
        description=dictionary['description'],
        price=dictionary['price'],
        on_offer=dictionary['on_offer']
    )
    item = await db.add(session, new_item)
    return item

asyncio.run(create_an_item())
