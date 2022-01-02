from singleton import singleton


@singleton
class Identification:
    def __init__(self, name: str, id_number: int) -> None:
        self.__name = name
        self.__id_number = id_number

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id_number(self) -> int:
        return self.__id_number
