class Zoo:
    def __init__(self, name: str, kingdom: str,
                 order: str, family: str, gender: str, age: int) -> None:
        self._name = name
        self._kingdom = kingdom
        self._order = order
        self._family = family
        self._gender = gender
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> int:
        self._age = age


if __name__ == '__main__':

    class_examle = Zoo('chimpanzee', 'Animalia', 'Primates',
                       'Hominidae', 'female', 18)


class_examle.age = 28

print(class_examle.age)
