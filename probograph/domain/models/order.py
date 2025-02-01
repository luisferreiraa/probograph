# domain/models/order.py
from datetime import datetime
from typing import Optional


class OrderDomain:
    def __init__(
            self,
            id: Optional[int] = None,
            value: float = None,
            date: Optional[datetime] = None,
            is_paid: bool = False,
            property_id: Optional[int] = None,
            order_type_id: Optional[int] = None
    ):
        self.id = id
        self.value = value
        self.date = date
        self.is_paid = is_paid
        self.property_id = property_id
        self.order_type_id = order_type_id
