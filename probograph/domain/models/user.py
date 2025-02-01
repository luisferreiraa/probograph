# domain/models/user.py
from datetime import datetime
from typing import Optional


class UserDomain:
    """
    Represents User entity on the domain.

    Attributes:
        id (Optional[int]): Unique user identifier
        first_name (str): User first name
        last_name (str): User last name
        email (str): User email
        password (str): User password
        phone (int): User phone number
        is_company (bool): is user for personal use or business
        created_on (Optional[datetime]): date and time of user creation
        modified_on (Optional[datetime]): date and time of user update
        modified_by (Optional[int]): last user to update profile
        last_login (datetime): date and time of the user last login
    """
    def __init__(
            self,
            id: Optional[int] = None,
            first_name: str = '',
            last_name: str = '',
            email: str = '',
            password: str = '',
            phone: int = 0,
            is_company: bool = False,
            created_on: Optional[datetime] = None,
            modified_on: Optional[datetime] = None,
            modified_by: int = None,
            last_login: Optional[datetime] = None,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.is_company = is_company
        self.created_on = created_on or datetime.now()
        self.modified_on = modified_on or datetime.now()
        self.modified_by = modified_by
        self.last_login = last_login or datetime.now()
