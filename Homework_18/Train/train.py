from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__train_cars = []

    def add_traincar(self, train_car: TrainCar) -> None:
        return self.__train_cars.append(train_car)

    def add_traincars(self, train_cars: List[TrainCar]) -> None:
        return self.__train_cars.extend(train_cars)

    def len(self) -> List[any]:
        return self.__train_cars
