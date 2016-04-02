# abstract class


class Player:
    def __init__(self, map):
        self.map = map

    def play(self):
        raise NotImplementedError
