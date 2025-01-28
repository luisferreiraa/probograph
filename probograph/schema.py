# schema.py
from datetime import datetime
from typing import Optional, List
import strawberry


@strawberry.type
class UserType:
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    password: str
    phone: int
    is_company: bool
    created_on: Optional[datetime]
    last_login: Optional[datetime]
    properties: List['PropertyType']
    images: List['ImageType']
    messages: List['MessageType']
    user_profile_image: Optional['UserProfileImageType']


@strawberry.type
class DeleteUserResponse:
    id: int
    message: str


@strawberry.type
class UserProfileImageType:
    id: Optional[int]
    user_id: int
    file_path: str
    user: Optional[UserType]


@strawberry.type
class AdTypeType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']


@strawberry.type
class FloorType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']


@strawberry.type
class PropertyTypeType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']
    property_subtypes: List['PropertySubTypeType']


@strawberry.type
class PropertySubTypeType:
    id: Optional[int]
    name: str
    property_type_id: int
    property_type: Optional[PropertyTypeType]
    properties: List['PropertyType']


@strawberry.type
class RentType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']


@strawberry.type
class EnergyClassType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']


@strawberry.type
class ConditionType:
    id: Optional[int]
    name: str
    is_active: bool
    properties: List['PropertyType']


@strawberry.type
class StateType:
    id: Optional[int]
    name: str
    is_active: bool
    cities: List['CityType']
    properties: List['PropertyType']


@strawberry.type
class CityType:
    id: Optional[int]
    name: str
    state_id: Optional[int]
    is_active: bool
    state: Optional[StateType]
    neighborhoods: List['NeighborhoodType']
    properties: List['PropertyType']


@strawberry.type
class NeighborhoodType:
    id: Optional[int]
    name: str
    city_id: Optional[int]
    is_active: bool
    city: Optional[CityType]
    properties: List['PropertyType']


@strawberry.type
class ImageType:
    id: Optional[int]
    file_path: str
    uploaded_on: datetime
    uploaded_by_id: Optional[int]
    property_id: Optional[int]
    uploaded_by: Optional[UserType]
    property: Optional['PropertyType']


@strawberry.type
class OrderType:
    id: Optional[int]
    value: float
    date: Optional[datetime]
    is_paid: bool
    property_id: Optional[int]
    order_type_id: Optional[int]
    property: Optional['PropertyType']
    order_type: Optional['OrderTypeType']


@strawberry.type
class OrderTypeType:
    id: Optional[int]
    name: float
    value: float
    is_active: bool
    orders: List[OrderType]


@strawberry.type
class ChatType:
    id: Optional[int]
    property_id: Optional[int]
    buyer_id: Optional[int]
    seller_id: Optional[int]
    created_on: Optional[datetime]
    last_message_on: Optional[datetime]
    is_archived: bool
    property: Optional['PropertyType']
    messages: List['MessageType']


@strawberry.type
class MessageType:
    id: Optional[int]
    chat_id: Optional[int]
    sender_id: Optional[int]
    content: str
    sent_on: Optional[datetime]
    is_read: bool
    chat: Optional[ChatType]
    sender: Optional[UserType]


@strawberry.type
class PropertyType:
    id: Optional[int]
    ad_type_id: Optional[int]
    user_id: Optional[int]
    address: str
    price: float
    rooms: int
    area: float
    m2_price: Optional[float]
    bathrooms: int
    has_garage: bool
    has_balcony: bool
    year: int
    floor_id: int
    has_elevator: bool
    has_ac: bool
    has_cabinets: bool
    has_garden: bool
    has_pool: bool
    has_storage: bool
    is_adapted: bool
    has_seaview: bool
    is_luxury: bool
    property_type_id: Optional[int]
    property_subtype_id: Optional[int]
    rent_id: Optional[int]
    energy_class_id: Optional[int]
    condition_id: Optional[int]
    state_id: Optional[int]
    city_id: Optional[int]
    neighborhood_id: Optional[int]
    description: str
    created_on: datetime
    modified_on: Optional[datetime]
    is_active: bool
    is_paid: bool
    user: Optional[UserType]
    ad_type: Optional[AdTypeType]
    floor: Optional[FloorType]
    rent: Optional[RentType]
    energy_class: Optional[EnergyClassType]
    condition: Optional[ConditionType]
    state: Optional[StateType]
    city: Optional[CityType]
    neighborhood: Optional[NeighborhoodType]
    property_type: Optional[PropertyTypeType]
    property_sub_type: Optional[PropertySubTypeType]
    images: Optional[List[ImageType]]
    orders: Optional[List[OrderType]]
    chats: Optional[List[ChatType]]
