import random
from person import Person

class Universum():
    def __init__(self, surface, width = 500, height = 500):
        self.size = (width, height)
        self.width = width
        self.height = height
        self.persons = []
        self.surface = surface

    def get_random_position(self):
        x_pos = random.randrange(0, self.width)
        y_pos = random.randrange(0, self.height)
        return x_pos, y_pos

    def tick(self):
        for p in self.persons:
            p.avoid_and_infect(self.persons)
            p.tick()

    def draw(self):
        self.surface.fill((0,0,0))
        for p in self.persons:
            p.draw()

    def addPersons(self, number, infected = False):
        for i in range(number):
            Person(self, infected)
