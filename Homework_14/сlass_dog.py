class Dog:
    def __init__(self, name: str, age: int, color: str) -> None:
        self.__name = name
        self.__age = age
        self.__color = color

    def print_color(self) -> str:
        return self.__color

    def print_age(self) -> int:
        return self.__age

    @property
    def get_older(self) -> int:
        return self.__age

    @get_older.setter
    def get_older(self, get_older) -> int:
        self.__age = get_older

    def first_meeting(self) -> str:
        return f'Hello {self.__name}'


if __name__ == '__main__':

    my_dog = Dog('Chack', 4, 'brown')
    my_dog.get_older += 10
    my_dog.print_age()
    print(my_dog.print_color())
