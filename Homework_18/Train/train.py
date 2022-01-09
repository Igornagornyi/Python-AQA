from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__cars = []
        self.__name = 'Intercity'
        self.__destination = 'Kyiv'

    def add_traincar(self, car: List[TrainCar]) -> List[str]:
        self.__cars.append(str(car).split()[-1][0:-2])
        return self.__cars

    def add_traincars(self, cars: List[List[TrainCar]]) -> List[str]:
        for car in cars:
            self.__cars.append(str(car).split()[-1][0:-2])
        return self.__cars

    def __len__(self) -> int:
        return len(self.__cars)

    def __str__(self) -> str:
        order = ""
        for car in self.__cars[0:len(self.__cars)]:
            order += f"{[car]}"
        return f"<=[HEAD]-{order}"
