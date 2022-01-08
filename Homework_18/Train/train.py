from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__cars = []
        self.__name = 'Intercity'
        self.__destination = 'Kyiv'

    def add_traincar(self, car: TrainCar) -> None:
        return self.__cars.append(car)

    def add_traincars(self, cars: List[TrainCar]) -> List[TrainCar]:
        for car in cars:
            self.__cars.append(car)
        return self.__cars

    def __len__(self) -> int:
        return len(self.__cars)

    def __str__(self) -> str:
        right_order = ""
        reverse_order = ""
        for car in self.__cars[0:-1]:
            right_order += f"{[car]}-"
        for reverse_car in reversed(self.__cars):
            reverse_order += f"-{[reverse_car]}"
        return f"<=[HEAD]-{right_order}{reverse_order}"
