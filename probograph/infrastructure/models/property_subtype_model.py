# infrastructure/models/property_subtype_model.py
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.property_type_model import PropertyTypeDB


class PropertySubTypeDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    property_type_id: Optional[int] = Field(default=None, foreign_key='propertytype.id')

    # Relacionamento com PropertyType
    property_type: Optional[PropertyTypeDB] = Relationship(back_populates='property_subtypes')

    # Relacionamento com Property
    properties: List[PropertyDB] = Relationship(back_populates='property_sub_type')
