from abc import ABC, abstractmethod


class Land(ABC):
    @abstractmethod
    def land(self):
        ...
