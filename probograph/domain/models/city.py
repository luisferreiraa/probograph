# domain/models/city.py
from typing import Optional


class CityDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            name: str = '',
            state_id: Optional[int] = None,
            is_active: bool = True
    ):
        self.id = id
        self.name = name
        self.state_id = state_id
        self.is_active = is_active
