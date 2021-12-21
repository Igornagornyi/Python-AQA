class Carbone:
    def __init__(self) -> None:
        self.__carbone_name = 'C'
        self.__period_number = 2
        self.__electron_number = 6
        self.__atomic_mass = 12.011
        self.__group_number = 4

    def __str__(self) -> str:
        return self.__carbone_name

    @property
    def name(self):
        return self.__carbone_name
