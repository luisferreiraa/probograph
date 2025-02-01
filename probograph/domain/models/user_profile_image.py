# domain/models/user_profile_image.py
from typing import Optional


class UserProfileImageDomain:
    """
    Represents UserProfileImage entity on the domain.

    Attributes:
        id (Optional[int]): Unique image identifier
        user_id (int): Identifier of the user associated with the image
        file_path (str): Full path to the image file
    """
    def __init__(
            self,
            id: Optional[int] = None,
            user_id: int = None,
            file_path: str = ''
    ):
        self.id = id
        self.user_id = user_id
        self.file_path = file_path
