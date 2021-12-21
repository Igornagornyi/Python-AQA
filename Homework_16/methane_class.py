class Methane:
    def __init__(self) -> None:
        self.__methane_name = 'CH4'
        self.__molecular_mass = 16.04
        self.__melting_temperature = -182.49
        self.__boiling_temperature = -161.58
        self.__self_ignition_temperature = 537.8

    def __str__(self) -> str:
        return self.__methane_name
