from typing import List

from .base_repository import BaseRepository

from ..models.order import Orders


class OrderRepository(BaseRepository):
    def get_orders(self) -> List[Orders]:
        orders = self.session.query(Orders).all()
        return orders
