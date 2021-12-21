from abc import ABC, abstractmethod


class StartUp(ABC):
    @abstractmethod
    def startup_engines(self):
        ...
