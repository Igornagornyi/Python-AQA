from sqlalchemy import Column, INTEGER

from ..core.base_model import Base


class Orders(Base):
    __tablename__ = "orders"

    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER)
    quantity = Column(INTEGER)

    def __str__(self):
        return f"{self.id} | {self.product_id} | {self.quantity}"
