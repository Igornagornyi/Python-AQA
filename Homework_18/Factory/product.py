from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def color(self):
        ...

    @abstractmethod
    def shape(self):
        ...

    @abstractmethod
    def size(self):
        ...
