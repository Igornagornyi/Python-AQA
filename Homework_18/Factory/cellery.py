from product import Product


class Cellery(Product):
    def __init__(self) -> None:
        self.__name = "cellery"
        self.__color = "red"
        self.__weight = 20

    @property
    def print_prod_name(self):
        return f"This is testy {self.__name}"

    @property
    def print_prod_color(self):
        return f"The color is {self.__color}"

    @property
    def print_prod_weight(self):
        return f"The weight is {self.__weight}"

    def __str__(self) -> str:
        return f"This is unknown {self.__name}\n" \
               f"The color is {self.__color}\n" \
               f"The weight is {self.__weight}"
