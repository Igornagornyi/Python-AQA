from startup import StartUp
from takeoff import TakeOff
from land import Land
from fly import Fly


class Aircraft(StartUp, TakeOff, Fly, Land):

    def __init__(self, ac_type: str, ac_range: int) -> None:
        self.__ac_type = ac_type
        self.__ac_range = ac_range
        self.__ac_speed = 0
        self.__engine_rotation = 0
        self.__altitude = 0

    @property
    def increase_rotation(self) -> int:
        return self.__engine_rotation

    @increase_rotation.setter
    def increase_rotation(self, increase_rotation: int):
        self.__engine_rotation += increase_rotation

    @property
    def increase_altitude(self) -> int:
        return self.__altitude

    @increase_altitude.setter
    def increase_altitude(self, increase_altitude: int):
        self.__altitude += increase_altitude

    @property
    def increase_speed(self) -> int:
        return self.__ac_speed

    @increase_speed.setter
    def increase_speed(self, increase_speed: int):
        self.__ac_speed += increase_speed

    def touching_ground(self):
        self.__altitude = 0
        self.__ac_speed = 100

    def startup_engines(self):
        print("We are starting both engines")
        return f"Now engines are {self.__engine_rotation} % of their power"

    def take_off(self):
        print("We are taking off")
        return f"Now our altitude is {self.__altitude} feet and speed" \
               f" {self.__ac_speed} km/h"

    def fly(self):
        print("We are flying above clouds")

    def land(self):
        return f"Our aircraft is touching ground at altitude " \
               f"{self.__altitude} feet and speed is {self.__ac_speed} km/h"
