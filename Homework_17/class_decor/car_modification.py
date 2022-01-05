from typing import Type, List


class Modification:
    def __init__(self, names: List[str]) -> None:
        self.__names = names

    def __call__(self, _type: Type) -> Type:
        setattr(_type, f"_{_type.__name__}__modifications", self.__names)
        return _type
