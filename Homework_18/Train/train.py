from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__train_cars = []
        self.__name = 'Intercity'
        self.__destination = 'Kyiv'

    def add_traincar(self, train_car: TrainCar) -> None:
        return self.__train_cars.append(train_car.get_tc_number())

    def add_traincars(self, train_cars: List[TrainCar]) -> List[int]:
        for car in train_cars:
            self.__train_cars.append(car.get_tc_number())
        return self.__train_cars

    def len(self) -> List[int]:
        return self.__train_cars

    def print_train(self) -> str:
        item = 0
        asc_result = ""
        desc_result = ""
        value_max = max(self.__train_cars)
        value = max(self.__train_cars)
        while item != value-1:
            item += 1
            asc_result += f"{[item]}-"
        while value != 1:
            value -= 1
            desc_result += f"-{[value]}"
        return f"<=[HEAD]-{asc_result}{[value_max]}{desc_result}"
