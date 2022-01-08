from Homework_18.Factory.product import Product


class Strawberry(Product):
    def __init__(self) -> None:
        self.__name = "strawberry"
        self.__attributes = ["red", "tapered", "small", "medium", "big"]

    @property
    def attributes(self) -> str:
        return self.__attributes

    def __str__(self) -> str:
        return f"This could be a fresh and ripe {self.__name}"
