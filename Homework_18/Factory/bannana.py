from __future__ import annotations
from product import Product


class Bannana(Product):
    def __init__(self) -> None:
        self.__name = "bannana"
        self.__color = ["yellow", "green", "red"]
        self.__shape = "prolonged"
        self.__size = ["small", "medium", "big"]

    def __str__(self) -> str:
        return f"This could be a fresh and ripe {self.__name}\n" \
               f"The shape is {self.__shape}\n"
