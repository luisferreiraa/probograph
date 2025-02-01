# domain/models/neighborhood.py
from typing import Optional


class NeighborhoodDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            name: str = '',
            city_id: Optional[int] = None,
            is_active: bool = True
    ):
        self.id = id
        self.name = name
        self.city_id = city_id
        self.is_active = is_active
