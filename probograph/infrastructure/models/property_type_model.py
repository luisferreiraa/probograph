# infrastructure/models/property_type_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class PropertyTypeDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com PropertySubType (One-to-Many)
    property_subtypes: List[PropertySubTypeDB] = Relationship(back_populates='property_type')

    # Relacionamento com Property
    properties: List[PropertyDB] = Relationship(back_populates='property_type')
