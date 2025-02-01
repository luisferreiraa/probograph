# domain/models/property_subtype.py
from typing import Optional


class PropertySubTypeDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            name: str = '',
            property_type_id: Optional[int] = None
    ):
        self.id = id
        self.name = name
        self.property_type_id = property_type_id
