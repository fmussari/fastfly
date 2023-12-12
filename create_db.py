from database import Base, engine
from models import Item
import asyncio

print('Create database ...')

#Base.metadata.create_all(engine)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

asyncio.run(create_db())