from abc import ABC, abstractmethod


class Aircraft(ABC):
    def __init__(self, altitude: int, speed: int,
                 rotation: int, rate_climb: int) -> None:
        self.__altitude = altitude
        self.__speed = speed
        self.__rotation = rotation
        self.__rate_climb = rate_climb

    @abstractmethod
    def fly(self):
        ...

    @abstractmethod
    def land(self):
        ...

    @abstractmethod
    def startup_engines(self):
        ...

    @abstractmethod
    def take_off(self):
        ...
