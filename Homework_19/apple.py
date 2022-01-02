from product import Product


class Apple(Product):
    def __init__(self) -> None:
        self.__name = "apple"
        self.__color = "green"
        self.__weight = 50

    @property
    def print_prod_name(self):
        return f"This is fresh {self.__name}"

    @property
    def print_prod_color(self):
        return f"The color is {self.__color}"

    @property
    def print_prod_weight(self):
        return f"The weight is {self.__weight}"

    def __str__(self) -> str:
        return f"This is fresh {self.__name}\n" \
               f"The color is {self.__color}\n" \
               f"The weight is {self.__weight}"
