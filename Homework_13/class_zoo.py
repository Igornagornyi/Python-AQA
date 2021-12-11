class Zoo:
    def __init__(self, name: str, type: str,
                 order: str, gender: str, age: int) -> None:
        self._name = name
        self._type = type
        self._order = order
        self._gender = gender
        self._age = age

    def return_age(self) -> str:
        print(f"Now age is {self._age}")

    def say_hello(self) -> str:
        print(f'Hello {self._name}')

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> int:
        self._age = age

    def age_once_increase(self) -> str:
        print(f"Age is increased only once {self._age + 5}")


if __name__ == '__main__':

    class_examle = Zoo('chimpanzee', 'monkey', 'Primates',
                       'female', 18)

    class_examle.say_hello()

    class_examle.age_once_increase()

    class_examle.age = 28

    print(f"And now age is already {class_examle.age}")
