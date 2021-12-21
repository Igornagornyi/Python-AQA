from carbone import Carbone


class Hydrogen:
    def __init__(self) -> None:
        self.__hydrogen_name = 'H'
        self.__period_number = 1
        self.__electron_number = 1
        self.__atomic_mass = 1.0079
        self.__group_number = 1

    def __str__(self) -> str:
        return self.__hydrogen_name

    @property
    def name(self):
        return self.__hydrogen_name

    def __add__(self, other: Carbone):
        return f"{other.name} + 2{self.__hydrogen_name}2 => CH4"

    def __radd__(self, other: Carbone):
        return f"{other.name} + 2{self.__hydrogen_name}2 => CH4"
