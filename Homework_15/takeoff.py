from abc import ABC, abstractmethod


@abstractmethod
class TakeOff(ABC):
    def take_off(self):
        ...
