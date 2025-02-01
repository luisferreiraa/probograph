# domain/models/image.py
from datetime import datetime
from typing import Optional


class ImageDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            file_path: str = '',
            uploaded_on: datetime = None,
            uploaded_by_id: Optional[int] = None,
            property_id: Optional[int] = None
    ):
        self.id = id
        self.file_path = file_path
        self.uploaded_on: uploaded_on
        self.uploaded_by_id: uploaded_by_id
        self.property_id = property_id
