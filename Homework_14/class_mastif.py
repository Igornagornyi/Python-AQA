from сlass_dog import Dog


class Mastif(Dog):
    def __init__(self, name: str, age: int,
                 color: str, character: str) -> None:
        super().__init__(name, age, color)
        self.__character = character

    def print_color(self) -> str:
        return super().print_color()

    def print_character(self) -> str:
        return self.__character

    def first_meeting(self) -> str:
        return super().first_meeting()


if __name__ == '__main__':

    my_dog = Mastif('Zak', 5, 'black', 'calm')
    my_dog.get_older += 5
    print(my_dog.print_character())
    print(my_dog.print_age())
    print(my_dog.first_meeting())
    print(my_dog.print_color())
