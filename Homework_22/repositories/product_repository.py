from typing import List

from .base_repository import BaseRepository

from ..models.product import Products


class ProductRepository(BaseRepository):
    def get_products(self) -> List[Products]:
        products = self.session.query(Products).all()
        return products
