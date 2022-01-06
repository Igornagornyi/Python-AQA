from product import Product


class Cellery(Product):
    def __init__(self) -> None:
        self.__name = "cellery"
        self.__color = "green"
        self.__shape = "herbaceous"
        self.__size = "small", "medium", "big"

    @property
    def color(self) -> str:
        return self.__color

    @property
    def shape(self) -> str:
        return self.__shape

    @property
    def size(self) -> str:
        return self.__size

    def __str__(self) -> str:
        return f"This could be aroma and delicious {self.__name}\n"
