from database import Base
#from sqlalchemy import String, Text, Boolean, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean, Integer, Float

from datetime import datetime
from sqlalchemy.sql import func

class Item(Base):
    __tablename__ = 'async_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    on_offer: Mapped[bool] = mapped_column(Boolean, default=False)
    #date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    date_created: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return f'<Item name={self.name} price={self.price} created={self.date_created}>'
    

"""
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)

    def __repr__():
        return f'<Item name={self.name} price={self.price}>'
"""

