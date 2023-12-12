from models import Item
from schemas import ItemModel, ItemCreateModel, ItemPatchModel
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

from fastapi import HTTPException
from http import HTTPStatus

class CRUD:
    async def get_all(self, async_session:async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            stmt = select(Item).order_by(Item.id)
            result = await session.execute(stmt)

            return result.scalars()
        
    async def add(self, async_session:async_sessionmaker[AsyncSession], item:ItemCreateModel):
        async with async_session() as session:
            session.add(item)
            await session.commit()
            return item
        

    async def get_by_id(self, async_session:async_sessionmaker[AsyncSession], item_id:int):
        async with async_session() as session:
            stmt = select(Item).filter(Item.id==item_id)
            result = await session.execute(stmt)

            return result.scalars().one_or_none()
        
    async def update(self, async_session:async_sessionmaker[AsyncSession], item_id:int, data:ItemPatchModel):
        async with async_session() as session:
            stmt = select(Item).filter(Item.id==item_id)
            result = await session.execute(stmt)
            stored_item = result.scalars().one_or_none()

            if stored_item is None:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND, 
                    detail=f'Item with id={item_id} doesn\'t exist'
                )

            update_data = data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(stored_item, key, value)

            await session.commit()

            return stored_item

   
        
    async def delete(self, async_session:async_sessionmaker[AsyncSession], item:ItemModel):
        async with async_session() as session:
            await session.delete(item)

            await session.commit()