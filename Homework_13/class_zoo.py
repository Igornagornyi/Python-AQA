class Zoo:
    def __init__(self, name: str, kingdom: str,
                 order: str, family: str, ) -> None:
        self.name = name
        self.kingdom = kingdom
        self.order = order
        self.family = family


class_examle = Zoo('chimpanzee', 'Animalia', 'Primates', 'Hominidae')
print(class_examle.name)
print(class_examle.kingdom)
print(class_examle.order)
print(class_examle.family)
