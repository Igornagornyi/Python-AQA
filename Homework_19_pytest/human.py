from Homework_19_pytest.race import Race


class Human:
    def __init__(self, name: str, age: int, gender: str, race: Race) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__race = race

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def race(self) -> Race:
        return self.__race

    def __validate_gender(self, gender: str) -> str:
        if gender not in ["male", "female"]:
            raise Exception("Unknown gender")
        else:
            return gender

    def grow(self) -> int:
        self.__age += 1
        return self.__age

    def change_name(self, name: str) -> str:
        if name != self.__name:
            self.__name = name
            return self.__name
        else:
            raise Exception("Provided name is the same...")

    def change_gender(self, gender: str) -> str:
        self.__gender = self.__validate_gender(gender)
        return self.__gender
