from product import Product


class Bannana(Product):
    def __init__(self) -> None:
        self.__name = "bannana"
        self.__color = "yellow", "green", "red"
        self.__shape = "prolonged"
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
        return f"This could be a fresh and ripe {self.__name}\n" \
               f"The shape is {self.__shape}\n"
