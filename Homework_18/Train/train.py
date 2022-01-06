from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__cars = []
        self.__name = 'Intercity'
        self.__destination = 'Kyiv'

    def add_traincar(self, car: TrainCar) -> None:
        return self.__cars.append(car.get_number())

    def add_traincars(self, cars: List[TrainCar]) -> List[TrainCar]:
        for car in cars:
            self.__cars.append(car.get_number())
        return self.__cars

    def __len__(self) -> int:
        return len(self.__cars)

    def __str__(self) -> str:
        asc_order = ""
        desc_order = ""
        max_number = max(self.__cars)
        sorted_cars = sorted(self.__cars)
        reversed_cars = sorted(self.__cars, reverse=True)
        for item in sorted_cars[0:-1]:
            asc_order += f"{[item]}-"
        for rev_item in reversed_cars[1:len(reversed_cars)]:
            desc_order += f"-{[rev_item]}"
        return f"<=[HEAD]-{asc_order}{[max_number]}{desc_order}"
