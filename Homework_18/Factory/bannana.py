from product import Product


class Bannana(Product):
    def __init__(self) -> None:
        self.__name = "bannana"
        self.__attributes = ["yellow", "green", "red", "prolonged", "small", "medium", "big"]

    @property
    def attributes(self) -> str:
        return self.__attributes

    def __str__(self) -> str:
        return f"This could be a fresh and ripe {self.__name}"
