# infrastructure/models/state_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class StateDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com City (One-to-Many)
    cities: List[CityDB] = Relationship(back_populates='state')

    # Relacionamento com Property (One-to-Many)
    properties: List[PropertyDB] = Relationship(back_populates='state')
