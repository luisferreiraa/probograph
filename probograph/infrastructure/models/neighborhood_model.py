# infrastructure/models/neighborhood_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.city_model import CityDB


class NeighborhoodDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city_id: Optional[int] = Field(default=None, foreign_key='city.id')
    is_active: bool = Field(default=True)

    # Relacionamento com City (Many-to-One)
    city: Optional[CityDB] = Relationship(back_populates='neighborhoods')

    # Relacionamento com Property (One-to-Many)
    properties: List[PropertyDB] = Relationship(back_populates='neighborhood')
    