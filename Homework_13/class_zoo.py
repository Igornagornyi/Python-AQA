class Zoo:
    def __init__(self, name: str, zoo_type: str,
                 order: str, gender: str, age: int) -> None:
        self._name = name
        self._zoo_type = zoo_type
        self._order = order
        self._gender = gender
        self._age = age

    def return_age(self):
        print(f"Now age is {self._age}")

    def say_hello(self):
        print(f'Hello {self._name}')

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def age_once_increase(self):
        print(f"Age is increased only once {self._age + 5}")


if __name__ == '__main__':
    class_ex = Zoo('chimpanzee', 'monkey', 'Primates', 'female', 18)
    class_ex.say_hello()
    class_ex.age_once_increase()
    class_ex.age = 28
    print(f"And now age is already {class_ex.age}")
