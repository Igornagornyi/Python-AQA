from product import Product


class Apple(Product):
    def __init__(self) -> None:
        self.__name = "apple"
        self.__attributes = ["green", "yellow", "red", "round", "small", "medium", "big"]

    @property
    def attributes(self) -> str:
        return self.__attributes

    def __str__(self) -> str:
        return f"This could be fresh {self.__name}"
