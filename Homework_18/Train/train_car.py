from typing import List, Dict


class TrainCar:
    def __init__(self, tc_number: int) -> None:
        self.__passengers = []
        self.__tc_number = tc_number
        self.__destination = "Kyiv"

    def __str__(self) -> str:
        return f"[{self.__tc_number}]"

    def get_tc_number(self) -> int:
        return self.__tc_number

    def len(self) -> int:
        return len(self.__passengers)

    def add_passenger(self, passenger: str) -> None:
        return self.__passengers.append(passenger)

    def add_passengers(self, passengers: List[str]) -> None:
        return self.__passengers.extend(passengers)

    def __modify_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    def print_passengers_json(self) -> Dict[str, str]:
        start = "[{\n"
        content = ""
        end = "}]"
        for value in self.__passengers:
            content += f"\tPassenger: {value},\n" \
                       f"\tWagon: {self.__tc_number},\n" \
                       f"\tDestination: {self.__destination}\n\n"
        return f"\n{start}{content}{end}\n"

    def print_one_passenger_json(self, index: int) -> Dict[str, str]:
        start = "[{\n"
        content = ""
        end = "}]"
        content += f"\tPassenger: {self.__passengers[index]},\n" \
                   f"\tWagon: {self.__tc_number},\n" \
                   f"\tDestination: {self.__destination}\n"
        return f"\n{start}{content}{end}\n"
