from car_modification import Modification
from typing import Dict


@Modification(["automat", "climate control", "seats heating"])
class Car:
    def __init__(self, name: str, year: int, color: str) -> None:
        self.__name = name
        self.__year = year
        self.__color = color

    def __modify_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    def json(self) -> Dict[str, str]:
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[self.__modify_key(key)] = value
        return my_dict

    @property
    def modification(self):
        return self.__modifications


if __name__ == '__main__':
    my_car = Car('Peugeot', 2013, 'white')
    print(my_car.json())
    print(my_car.modification)

