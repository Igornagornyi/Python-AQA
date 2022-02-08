from sqlalchemy import Column, INTEGER, VARCHAR

from ..core.base_model import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(INTEGER)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price}"
