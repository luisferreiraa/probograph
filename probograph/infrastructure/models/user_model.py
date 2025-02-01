# infrastructure/models/user_model.py

from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from probograph.infrastructure.models.user_profile_image_model import UserProfileImageDB


class UserDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)
    phone: str = Field(unique=True, nullable=False)
    is_company: bool = Field(nullable=False)
    created_on: Optional[datetime] = Field(default_factory=datetime.now)
    modified_on: Optional[datetime] = Field(default_factory=datetime.now)
    modified_by: Optional[int] = Field(default=None, foreign_key='user.id')
    last_login: Optional[datetime] = Field(default_factory=datetime.now)

    # Relacionamento com User
    modified_by_user: Optional['UserDB'] = Relationship(back_populates='modified_users', sa_relationship_kwargs={
        'foreign_keys': [modified_by]})

    # Relacionameto com Property
    properties: List[PropertyDB] = Relationship(back_populates='user')

    # Relacionamento com Image
    images: List[ImageDB] = Relationship(back_populates='uploaded_by')

    # Relacionamento com Message (como Sender)
    messages: List[MessageDB] = Relationship(back_populates='sender')

    # Relacionamento com UserProfileImage
    user_profile_image: Optional[UserProfileImageDB] = Relationship(back_populates='user')

    # Relacionamento inverso para usuários que modificaram outros usuários (back_populates)
    modified_users: List['UserDB'] = Relationship(back_populates='modified_by_user')
