from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def print_prod_name(self):
        ...

    @abstractmethod
    def print_prod_color(self):
        ...

    @abstractmethod
    def print_prod_weight(self):
        ...
