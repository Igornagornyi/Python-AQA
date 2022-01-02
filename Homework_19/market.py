from apple import Apple
from bannana import Bannana
from cellery import Cellery
from strawbarry import Strawbarry
from product import Product


class Market:
    @staticmethod
    def get_product(product_name: str) -> Product:
        """Return product name"""
        if product_name == "apple":
            return Apple()
        elif product_name == "bannana":
            return Bannana()
        elif product_name == "cellery":
            return Cellery()
        elif product_name == "strawbarry":
            return Strawbarry()
        else:
            raise Exception("Undefined product name")

