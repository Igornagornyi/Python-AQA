from enum import Enum


class Time(Enum):
    morning = 0
    lunch = 1
    evening = 2
    night = 3


class Weather(Enum):
    sunny = 0
    cold = 1
    rainy = 2
    hot = 3


class Pet:
    def __init__(self, name) -> None:
        self.__name = name

    def today(self, time: Time, weather: Weather) -> None:
        if time == Time.morning:
            print(f"It's time to walk with {self.__name}")
        elif time == Time.lunch:
            print(f"It's time for lunch for {self.__name}")
        elif time == Time.evening:
            print(f"It's time for evening walk with {self.__name}")
        elif time == Time.night:
            print(f"It's time to sleep for {self.__name}")
        if weather == Weather.sunny:
            print("It's sunny today")
        elif weather == Weather.cold:
            print("It's cold outside")
        elif weather == Weather.rainy:
            print("It's rainy outside")
        elif weather == Weather.hot:
            print("It's hot outside")


if __name__ == '__main__':

    my_pet = Pet('Zak')
    my_pet.today(Time.night, Weather.rainy)