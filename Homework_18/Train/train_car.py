from typing import List
from traincar_number import TrainNumber


@TrainNumber("1")
class TrainCar:
    def __init__(self) -> None:
        self.__passengers = []

    @property
    def train_number(self) -> str:
        return self.__train_number

    def len(self) -> int:
        return len(self.__passengers)

    def add_passenger(self, passenger: str) -> None:
        return self.__passengers.append(passenger)

    def add_passengers(self, passengers: List[str]) -> None:
        return self.__passengers.extend(passengers)
