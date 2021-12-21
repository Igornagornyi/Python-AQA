from abc import ABC, abstractmethod


@abstractmethod
class StartUp(ABC):
    def startup_engines(self):
        ...
