# infrastructure/models/floor_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class FloorDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List[PropertyDB] = Relationship(back_populates='floor')
