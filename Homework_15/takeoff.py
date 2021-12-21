from abc import ABC, abstractmethod


class TakeOff(ABC):
    @abstractmethod
    def take_off(self):
        ...
