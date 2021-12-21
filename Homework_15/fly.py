from abc import ABC, abstractmethod


@abstractmethod
class Fly(ABC):
    def fly(self):
        ...
