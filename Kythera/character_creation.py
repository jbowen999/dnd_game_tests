import calculations as calc


class Character:
    def __init__(self, name: str, char_class: int) -> None:
        self.name = name
        self.char_class = char_class
        self.stats = calc.calc_stats(self.char_class)


class Creature:
    def __init__(self, name: str, type: str, alignment: str) -> None:
        self.name = name
        self.type = type
        self.alignment = alignment
