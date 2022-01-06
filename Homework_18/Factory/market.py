from Homework_18.Factory.apple import Apple
from Homework_18.Factory.bannana import Bannana
from Homework_18.Factory.cellery import Cellery
from strawberry import Strawberry
from product import Product


class Market:
    @staticmethod
    def get_product(prod_color: str, prod_shape: str, prod_size: str) -> Product:
        """Return product name by attributes"""
        apple = Apple()
        bannana = Bannana()
        cellery = Cellery()
        strawberry = Strawberry()
        if prod_color.lower() in apple.color \
                and prod_shape.lower() in apple.shape \
                and prod_size.lower() in apple.size:
            return Apple()
        elif prod_color.lower() in bannana.color \
                and prod_shape.lower() in bannana.shape \
                and prod_size.lower() in bannana.size:
            return Bannana()
        elif prod_color.lower() in cellery.color \
                and prod_shape.lower() in cellery.shape \
                and prod_size.lower() in cellery.size:
            return Cellery()
        elif prod_color.lower() in strawberry.color\
                and prod_shape.lower() in strawberry.shape\
                and prod_size.lower() in strawberry.size:
            return Strawberry()
        else:
            raise Exception("Undefined product")
