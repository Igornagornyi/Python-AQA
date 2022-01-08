from product import Product


class Cellery(Product):
    def __init__(self) -> None:
        self.__name = "cellery"
        self.__attributes = ["green", "herbaceous", "small", "medium", "big"]

    @property
    def attributes(self) -> str:
        return self.__attributes

    def __str__(self) -> str:
        return f"This could be aroma and delicious {self.__name}"
