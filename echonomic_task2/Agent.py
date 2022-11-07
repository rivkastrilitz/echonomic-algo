class Agent:

    values = []

    def __init__(self, values: list[float]):
        self.values = values

    def value(self, option: int) -> float:
        if option > len(self.values) or option < 0:
            raise IndexError("option out of range")
        return self.values[option]

