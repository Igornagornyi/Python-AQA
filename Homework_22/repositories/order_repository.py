from typing import List

from .base_repository import BaseRepository

from ..models.order import Orders


class OrderRepository(BaseRepository):
    def get_orders(self) -> List[Orders]:
        orders = self.session.query(Orders).all()
        return orders

    def add_order(self, data) -> None:
        orders = Orders(**data)
        self.session.add(orders)

    def change_quantity(self, id: int, quantity: int) -> None:
        self.session.query(Orders).filter(Orders.id == id).update({"quantity": quantity})

    def delete_order(self, id: int) -> None:
        self.session.query(Orders).filter(Orders.id == id).delete()
