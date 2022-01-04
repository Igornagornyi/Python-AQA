from typing import List


class TrainCar:
    def __init__(self, tc_number: str) -> None:
        self.__passengers = []
        self.__tc_number = tc_number

    def __str__(self) -> str:
        return self.__tc_number

    def get_tc_number(self) -> str:
        return self.__tc_number

    def len(self) -> int:
        return len(self.__passengers)

    def add_passenger(self, passenger: str) -> None:
        return self.__passengers.append(passenger)

    def add_passengers(self, passengers: List[str]) -> None:
        return self.__passengers.extend(passengers)
