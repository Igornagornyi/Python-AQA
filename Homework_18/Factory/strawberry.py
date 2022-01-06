from __future__ import annotations
from Homework_18.Factory.product import Product


class Strawberry(Product):
    def __init__(self) -> None:
        self.__name = "strawberry"
        self.__color = "red"
        self.__shape = "tapered"
        self.__size = ["small", "medium", "big"]

    def __str__(self) -> str:
        return f"This could be a fresh and ripe {self.__name}\n" \
               f"It's color is {self.__color}\n" \
               f"The shape is {self.__shape}\n"
