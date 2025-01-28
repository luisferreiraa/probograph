# models.py
from datetime import datetime
from typing import Optional, List

from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)
from pydantic import model_validator, field_validator

# Cria engine da base de dados
engine = create_engine('sqlite:///test_db.db')


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(default=None, nullable=False)
    last_name: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)
    password: str = Field(default=None, nullable=False)
    phone: int = Field(default=None, nullable=False)
    is_company: bool = Field(default=None, nullable=False)
    created_on: Optional[datetime] = Field(default_factory=datetime.now)
    last_login: Optional[datetime] = Field(default_factory=datetime.now)

    # Relacionameto com Property
    properties: List['Property'] = Relationship(back_populates='user')

    # Relacionamento com Image
    images: List['Image'] = Relationship(back_populates='uploaded_by')

    # Relacionamento com Message (como Sender)
    messages: List['Message'] = Relationship(back_populates='sender')

    # Relacionamento com UserProfileImage
    user_profile_image: Optional['UserProfileImage'] = Relationship(back_populates='user')


class UserProfileImage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    file_path: str

    # Relacionamento com User
    user: Optional['User'] = Relationship(back_populates='user_profile_image')


class AdType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False)
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='ad_type')


class Floor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='floor')


class PropertyType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com PropertySubType (One-to-Many)
    property_subtypes: List['PropertySubType'] = Relationship(back_populates='property_type')

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='property_type')


class PropertySubType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    property_type_id: Optional[int] = Field(default=None, foreign_key='propertytype.id')

    # Relacionamento com PropertyType
    property_type: Optional['PropertyType'] = Relationship(back_populates='property_subtypes')

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='property_sub_type')


class Rent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='rent')


class EnergyClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='energy_class')


class Condition(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com Property
    properties: List['Property'] = Relationship(back_populates='condition')


class State(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)

    # Relacionamento com City (One-to-Many)
    cities: List['City'] = Relationship(back_populates='state')

    # Relacionamento com Property (One-to-Many)
    properties: List['Property'] = Relationship(back_populates='state')


class City(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    state_id: Optional[int] = Field(default=None, foreign_key='state.id')
    is_active: bool = Field(default=True)

    # Relacionamento com District (Many-to-One)
    state: Optional['State'] = Relationship(back_populates='cities')

    # Relacionamento com Neighborhood (One-to-Many)
    neighborhoods: List['Neighborhood'] = Relationship(back_populates='city')

    # Relacionamento com Property (One-to-Many)
    properties: List['Property'] = Relationship(back_populates='city')


class Neighborhood(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city_id: Optional[int] = Field(default=None, foreign_key='city.id')
    is_active: bool = Field(default=True)

    # Relacionamento com City (Many-to-One)
    city: Optional['City'] = Relationship(back_populates='neighborhoods')

    # Relacionamento com Property (One-to-Many)
    properties: List['Property'] = Relationship(back_populates='neighborhood')


class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    uploaded_on: datetime = Field(default_factory=datetime.now)
    uploaded_by_id: Optional[int] = Field(default=None, foreign_key='user.id')
    property_id: Optional[int] = Field(default=None, foreign_key='property.id')

    # Relacionamento com User
    uploaded_by: Optional['User'] = Relationship(back_populates='images')

    # Relacionamento com Property
    property: Optional['Property'] = Relationship(back_populates='images')


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: float
    date: Optional[datetime] = Field(default_factory=datetime.now)
    is_paid: bool = Field(default=False)
    property_id: Optional[int] = Field(default=None, foreign_key='property.id')
    order_type_id: Optional[int] = Field(default=None, foreign_key='ordertype.id')

    # Relacionamento com Property
    property: Optional['Property'] = Relationship(back_populates='orders')

    # Relacionamento com OrderType
    order_type: Optional['OrderType'] = Relationship(back_populates='orders')


class OrderType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    value: float
    is_active: bool = Field(default=True)

    # Relacionamento com Order
    orders: List['Order'] = Relationship(back_populates='order_type')


class Chat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    property_id: Optional[int] = Field(default=None, foreign_key='property.id')
    buyer_id: Optional[int] = Field(default=None, foreign_key='user.id')
    seller_id: Optional[int] = Field(default=None, foreign_key='user.id')
    created_on: Optional[datetime] = Field(default_factory=datetime.now)
    last_message_on: Optional[datetime] = Field(default_factory=datetime.now)
    is_archived: bool = Field(default=False)

    # Relacionamento com Property
    property: Optional['Property'] = Relationship(back_populates='chats')

    # Relacionamento com Message
    messages: List['Message'] = Relationship(back_populates='chat')


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    chat_id: Optional[int] = Field(default=None, foreign_key='chat.id')
    sender_id: Optional[int] = Field(default=None, foreign_key='user.id')
    content: str
    sent_on: Optional[datetime] = Field(default_factory=datetime.now)
    is_read: bool = Field(default=False)

    # Relacionamento com Chat
    chat: Optional['Chat'] = Relationship(back_populates='messages')

    # Relacionamento com User (Sender)
    sender: Optional['User'] = Relationship(back_populates='messages')


class Property(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ad_type_id: Optional[int] = Field(default=None, foreign_key='adtype.id')
    user_id: int = Field(default=None, foreign_key='user.id')
    address: str
    price: float
    rooms: int
    area: float
    m2_price: Optional[float] = Field(default=None)  # Campo calculado
    bathrooms: int
    has_garage: bool = Field(default=False)
    has_balcony: bool = Field(default=False)
    year: int
    floor_id: Optional[int] = Field(default=None, foreign_key='floor.id')
    has_elevator: bool = Field(default=False)
    has_ac: bool = Field(default=False)
    has_cabinets: bool = Field(default=False)
    has_garden: bool = Field(default=False)
    has_pool: bool = Field(default=False)
    has_storage: bool = Field(default=False)
    is_adapted: bool = Field(default=False)
    has_seaview: bool = Field(default=False)
    is_luxury: bool = Field(default=False)
    property_type_id: Optional[int] = Field(default=None, foreign_key='propertytype.id')
    property_subtype: Optional[int] = Field(default=None, foreign_key='propertysubtype.id')
    rent_id: Optional[int] = Field(default=None, foreign_key='rent.id')
    energy_class_id: Optional[int] = Field(default=None, foreign_key='energyclass.id')
    condition_id: Optional[int] = Field(default=None, foreign_key='condition.id')
    state_id: Optional[int] = Field(default=None, foreign_key='state.id')
    city_id: Optional[int] = Field(default=None, foreign_key='city.id')
    neighborhood_id: Optional[int] = Field(default=None, foreign_key='neighborhood.id')
    description: str
    created_on: datetime = Field(default_factory=datetime.now)
    modified_on: Optional[datetime] = Field(default_factory=datetime.now)
    is_active: bool = Field(default=False)
    is_paid: bool = Field(default=False)

    # Relacionamentos (Many-to-One)
    user: Optional[User] = Relationship(back_populates='properties')
    ad_type: Optional[AdType] = Relationship(back_populates='properties')
    floor: Optional[Floor] = Relationship(back_populates='properties')
    rent: Optional[Rent] = Relationship(back_populates='properties')
    energy_class: Optional[EnergyClass] = Relationship(back_populates='properties')
    condition: Optional[Condition] = Relationship(back_populates='properties')
    state: Optional[State] = Relationship(back_populates='properties')
    city: Optional[City] = Relationship(back_populates='properties')
    neighborhood: Optional[Neighborhood] = Relationship(back_populates='properties')
    property_type: Optional[PropertyType] = Relationship(back_populates='properties')
    property_sub_type: Optional[PropertySubType] = Relationship(back_populates='properties')

    # Relacionamento com Image (One-to-Many)
    images: List['Image'] = Relationship(back_populates='property')

    # Relacionamento com Order
    orders: List['Order'] = Relationship(back_populates='property')

    # Relacionamento com Chat
    chats: List['Chat'] = Relationship(back_populates='property')

    @model_validator(mode='before')
    def calculate_m2_price(cls, values):
        if 'area' in values and 'price' in values:
            area = values['area']
            price = values['price']
            if area and price > 0:  # Evita divisão por zero ou valores inválidos
                values['m2_price'] = price / area
        return values

    @field_validator("year")
    def validate_year(cls, value):
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError('Construction year cannot be in the future')
        return value


# Cria a base de dados
SQLModel.metadata.create_all(engine)
