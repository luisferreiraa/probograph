# infrastructure/models/city_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.state_model import StateDB


class CityDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    state_id: Optional[int] = Field(default=None, foreign_key='state.id')
    is_active: bool = Field(default=True)

    # Relacionamento com District (Many-to-One)
    state: Optional[StateDB] = Relationship(back_populates='cities')

    # Relacionamento com Neighborhood (One-to-Many)
    neighborhoods: List[NeighborhoodDB] = Relationship(back_populates='city')

    # Relacionamento com Property (One-to-Many)
    properties: List[PropertyDB] = Relationship(back_populates='city')
    