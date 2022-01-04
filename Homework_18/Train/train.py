from train_car import TrainCar
from typing import List


class Train:
    def __init__(self) -> None:
        self.__train_cars = []
        self.__name = 'Intercity'
        self.__destination = 'Kyiv'

    def add_traincar(self, train_car: TrainCar) -> None:
        return self.__train_cars.append(train_car.get_tc_number())

    def add_traincars(self, train_cars: List[TrainCar]) -> List[str]:
        for car in train_cars:
            self.__train_cars.append(car.get_tc_number())
        return self.__train_cars

    def len(self) -> List[str]:
        return self.__train_cars
