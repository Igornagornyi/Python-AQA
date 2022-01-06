from __future__ import annotations
from product import Product


class Cellery(Product):
    def __init__(self) -> None:
        self.__name = "cellery"
        self.__color = "green"
        self.__shape = "herbaceous"
        self.__size = ["small", "medium", "big"]

    def __str__(self) -> str:
        return f"This could be aroma and delicious {self.__name}\n"
