import random

class Place():
    def __init__(self, universum, pos = None, capacity = 100):
        if pos is None:
            pos = universum.get_random_position()

        self.pos = pos
        self.capacity = capacity