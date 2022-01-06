from Homework_18.Factory.apple import Apple
from Homework_18.Factory.bannana import Bannana
from Homework_18.Factory.cellery import Cellery
from strawberry import Strawberry
from product import Product


class Market:
    @staticmethod
    def get_product(prod_color: str, prod_shape: str, prod_size: str) -> Product:
        """Return product name"""
        apple_attributes = ['green', 'yellow', 'red', 'round', 'small', 'medium', 'big']
        bannana_attributes = ["yellow", "green", "red", "prolonged", "small", "medium", "big"]
        cellery_attributes = ["green", "herbaceous", "small", "medium", "big"]
        strawberry_attributes = ["red", "tapered", "small", "medium", "big"]
        if prod_color.lower() in apple_attributes \
                and prod_shape.lower() in apple_attributes \
                and prod_size.lower() in apple_attributes:
            return Apple()
        elif prod_color.lower() in bannana_attributes \
                and prod_shape.lower() in bannana_attributes \
                and prod_size.lower() in bannana_attributes:
            return Bannana()
        elif prod_color.lower() in cellery_attributes \
                and prod_shape.lower() in cellery_attributes \
                and prod_size.lower() in cellery_attributes:
            return Cellery()
        elif prod_color.lower() in strawberry_attributes\
                and prod_shape.lower() in strawberry_attributes\
                and prod_size.lower() in strawberry_attributes:
            return Strawberry()
        else:
            raise Exception("Undefined product")
