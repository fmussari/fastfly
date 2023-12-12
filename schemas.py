from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ItemModel(BaseModel):
    id:int
    name:str
    description:str
    price:float
    on_offer:bool
    date_created:datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class ItemCreateModel(BaseModel):
    name:str
    description:str
    price:float
    on_offer:bool|None = False

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Sample name",
                "description": "Sample description",
                "price": 1.50,
                "on_offer": False
            }
        }
    )

class ItemPatchModel(BaseModel):
    name:str|None=None
    description:str|None=None
    price:float|None=None
    on_offer:bool|None=None

    model_config = ConfigDict(
        from_attributes=True
    )

class ItemDeleteModel(BaseModel):
    detail:str