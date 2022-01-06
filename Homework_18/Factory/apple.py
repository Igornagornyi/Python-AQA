from __future__ import annotations
from product import Product


class Apple(Product):
    def __init__(self) -> None:
        self.__name = "apple"
        self.__color = ["green", "yellow", "red"]
        self.__shape = "round"
        self.__size = ["small", "medium", "big"]

    def __str__(self) -> str:
        return f"This could be fresh {self.__name}\n" \
               f"The shape is {self.__shape}\n"
