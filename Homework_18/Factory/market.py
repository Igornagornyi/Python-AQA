from Homework_18.Factory.apple import Apple
from Homework_18.Factory.bannana import Bannana
from Homework_18.Factory.cellery import Cellery
from strawberry import Strawberry
from product import Product


class Market:
    @staticmethod
    def get_product(values) -> Product:
        """Return product name by attributes"""
        apple = Apple()
        bannana = Bannana()
        cellery = Cellery()
        strawberry = Strawberry()
        if all([value in apple.attributes for value in values]):
            return Apple()
        elif all([value in bannana.attributes for value in values]):
            return Bannana()
        elif all([value in cellery.attributes for value in values]):
            return Cellery()
        elif all([value in strawberry.attributes for value in values]):
            return Strawberry()
        else:
            raise Exception("Undefined product")
