# infrastructure/models/user_profile_image_model.py

from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.user_model import UserDB


class UserProfileImageDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    file_path: str

    # Relacionamento com User
    user: Optional[UserDB] = Relationship(back_populates='user_profile_image')
