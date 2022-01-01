from typing import Type


def singleton(_type: Type):
    def decorate(name: str, id_number: int):
        if hasattr(_type, "__instance"):
            return getattr(_type, "__instance")
        else:
            instance = _type(name, id_number)
            setattr(_type, "__instance", instance)
            return getattr(_type, "__instance")
    return decorate
