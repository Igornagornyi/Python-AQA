from typing import Type


class TrainNumber:
    def __init__(self, train_number: str) -> None:
        self.__train_number = train_number

    def __call__(self, _type: Type) -> Type:
        setattr(_type, f"_{_type.__name__}__train_number", self.__train_number)
        return _type
