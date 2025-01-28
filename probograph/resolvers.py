# resolvers.py
import strawberry
from typing import List

from probograph.schema import UserType, DeleteUserResponse, UserProfileImageType, AdTypeType
from probograph.db_function import (
    get_users,
    create_user,
    update_user,
    delete_user,
    get_user_profile_image,
    get_ad_types, create_ad_type, delete_ad_type
)


@strawberry.type
class Query:
    all_users: List[UserType] = strawberry.field(resolver=get_users)
    get_user_profile_image: UserProfileImageType = strawberry.field(resolver=get_user_profile_image)
    get_ad_types: List[AdTypeType] = strawberry.field(resolver=get_ad_types)


@strawberry.type
class Mutation:
    create_user: UserType = strawberry.field(resolver=create_user)
    create_ad_type: AdTypeType = strawberry.field(resolver=create_ad_type)
    update_user: UserType = strawberry.field(resolver=update_user)
    delete_user: DeleteUserResponse = strawberry.field(resolver=delete_user)
    delete_ad_type: DeleteUserResponse = strawberry.field(resolver=delete_ad_type)

