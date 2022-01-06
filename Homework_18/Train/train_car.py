from typing import List


class TrainCar:
    def __init__(self, number: int) -> None:
        self.__passengers = []
        self.__number = number
        self.__destination = "Kyiv"

    @property
    def number(self) -> str:
        return f"[{self.__number}]"

    def get_number(self) -> int:
        return self.__number

    def __len__(self) -> int:
        return len(self.__passengers)

    def add_passenger(self, passenger: str) -> None:
        return self.__passengers.append(passenger)

    def add_passengers(self, passengers: List[str]) -> None:
        return self.__passengers.extend(passengers)

    def __str__(self) -> str:
        start = "[{\n"
        content = ""
        end = "}]"
        for passenger in self.__passengers:
            content += f"\tPassenger: {passenger},\n" \
                       f"\tWagon: {self.__number},\n" \
                       f"\tDestination: {self.__destination}\n\n"
        return f"\n{start}{content}{end}\n"
