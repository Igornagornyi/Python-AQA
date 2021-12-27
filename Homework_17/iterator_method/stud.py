class Student:
    def __init__(self, name: str, gender: str, age: int, specialization: str) -> None:
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__specialization = specialization

    def __modify_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    def __str__(self) -> str:
        start = "{\n"
        content = ""
        end = "}"
        for key, value in self.__dict__.items():
            content += f"\t{self.__modify_key(key)}: {value}\n"
        return f"{start}{content}{end}"
