from enum import Enum


class Time(Enum):
    morning = 0
    lunch = 1
    evening = 2
    night = 3


class Pet:
    def __init__(self, name) -> None:
        self.__name = name

    def todo(self, time: Time) -> None:
        if time == Time.morning:
            print(f"It's time to walk with {self.__name}")
        elif time == Time.lunch:
            print(f"It's time for lunch for {self.__name}")
        elif time == Time.evening:
            print(f"It's time for evening walk with {self.__name}")
        elif time == Time.night:
            print(f"It's time to sleep for {self.__name}")
        else:
            raise Exception('Time not defined')


if __name__ == '__main__':

    my_pet = Pet('Zak')
    my_pet.todo(Time.night)
