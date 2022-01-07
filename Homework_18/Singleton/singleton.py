from typing import Type


def singleton(_type: Type):
    def decorate(name: str, id_number: int):
        if hasattr(_type, "_instance"):
            return getattr(_type, "_instance")
        else:
            instance = _type(name, id_number)
            setattr(_type, "_instance", instance)
            return getattr(_type, "_instance")
    return decorate
