# domain/models/energy_class.py
from typing import Optional


class EnergyClassDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            name: str = '',
            is_active: bool = True
    ):
        self.id = id
        self.name = name
        self.is_active = is_active
