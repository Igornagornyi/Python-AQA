from abc import ABC, abstractmethod


@abstractmethod
class Land(ABC):
    def land(self):
        ...
