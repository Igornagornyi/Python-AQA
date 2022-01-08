from Homework_18.Factory.apple import Apple
from Homework_18.Factory.bannana import Bannana
from Homework_18.Factory.cellery import Cellery
from strawberry import Strawberry
from product import Product
from typing import List


class Market:
    @staticmethod
    def get_product(values: List[str]) -> Product:
        """Return product name by attributes"""
        if all([value in Apple().attributes for value in values]):
            return Apple()
        elif all([value in Bannana().attributes for value in values]):
            return Bannana()
        elif all([value in Cellery().attributes for value in values]):
            return Cellery()
        elif all([value in Strawberry().attributes for value in values]):
            return Strawberry()
        else:
            raise Exception("Undefined product")
