# infrastructure/models/image_model.py
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.user_model import UserDB


class ImageDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    uploaded_on: datetime = Field(default_factory=datetime.now)
    uploaded_by_id: Optional[int] = Field(default=None, foreign_key='user.id')
    property_id: Optional[int] = Field(default=None, foreign_key='property.id')

    # Relacionamento com User
    uploaded_by: Optional[UserDB] = Relationship(back_populates='images')

    # Relacionamento com Property
    property: Optional[PropertyDB] = Relationship(back_populates='images')
