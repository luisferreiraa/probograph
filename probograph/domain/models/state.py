# domain/models/state.py
from typing import Optional


class StateDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            name: str = '',
            is_active: bool = True
    ):
        self.id = id
        self.name = name
        self.is_active = is_active
