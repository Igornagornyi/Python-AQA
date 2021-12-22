from aircraft import Aircraft


class TurbopropAircraft(Aircraft):

    def __init__(self, name: str, altitude: int, speed: int,
                 rotation: int, rate_climb: int):
        super().__init__(altitude, speed, rotation, rate_climb)
        self.__name = name
        self.__altitude = altitude
        self.__speed = speed
        self.__rotation = rotation
        self.__rate_climb = rate_climb

    def startup_engines(self):
        print("We are starting both engines")
        self.__rotation += 30
        return f"Now engines are {self.__rotation} % of their power"

    def take_off(self):
        print("We are taking off")
        self.__altitude += 1000
        self.__speed += 150
        self.__rate_climb += 20
        return f"Now our altitude is {self.__altitude} feet and speed" \
               f" {self.__speed} km/h, rate of climb {self.__rate_climb}"

    def fly(self):
        return "We are flying above clouds"

    def land(self):
        self.__altitude = 0
        self.__speed = 100
        return f"Our aircraft is touching ground at altitude " \
               f"{self.__altitude} feet and speed is {self.__speed} km/h"
