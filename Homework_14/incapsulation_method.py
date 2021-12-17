from enum import Enum


class Time(Enum):
    MORNING = 0
    LUNCH = 1
    EVENING = 2
    NIGHT = 3


class Weather(Enum):
    SUNNY = 0
    COLD = 1
    RAINY = 2
    HOT = 3


class Pet:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__min_time = 3

    def today(self, time: Time, weather: Weather, max_time: int) -> None:
        if time == Time.MORNING:
            print(f"It's time to walk with {self.__name}")
            res_time = (self.__min_time + max_time) // 2
            print(f"Now time recommended for walk is {res_time}")

        elif time == Time.LUNCH:
            print(f"It's time for lunch for {self.__name}")
            res_time = (self.__min_time + max_time) // 2
            print(f"Now time recommended for walk is {res_time}")

        elif time == Time.EVENING:
            print(f"It's time for evening walk with {self.__name}")
            res_time = (self.__min_time + max_time) // 2
            print(f"Now time recommended for walk is {res_time}")

        elif time == Time.NIGHT:
            print(f"It's time to sleep for {self.__name}")
            res_time = 0
            print(f"Now time recommended for walk is {res_time}")

        if weather == Weather.SUNNY:
            print("It's sunny today")

        elif weather == Weather.COLD:
            print("It's cold outside")

        elif weather == Weather.RAINY:
            print("It's rainy outside")

        elif weather == Weather.HOT:
            print("It's hot outside")


if __name__ == '__main__':
    my_pet = Pet('Zak')
    my_pet.today(Time.MORNING, Weather.RAINY, 15)
