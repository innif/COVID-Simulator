from place import Place
import vectorcalc
import random
import pygame

MOVE_DESTINATION_W = .4
MOVE_AVOID_W = .8
MOVE_RANDOM_W = .2
MOMENTUM = .9
INFECTION_CHANCE = 0.02

HEALING_TIME = 14*24
HEALING_VAR = 4*24

COLORS = ((0,255,0),(255,10,5),(100,100,100))


class Person():
    def __init__(self, universum, infected = False):
        self.status = 0 # 0 - uninfected; 1 - infected; 2 - removed
        self.position = universum.get_random_position()
        self.move_direction = (0,0)
        self.home = Place(universum)
        self.universum = universum
        self.destination = self.home
        self.avoid_radius = 20
        self.avoid_vector = (0,0)
        self.infection_radius = 25
        self.healing_time = -1

        universum.persons += [self]

        if infected:
            self.infect()

    # 1 tick = 1 h
    def tick(self):
        if self.status == 1:
            self.healing_time -= 1
            if self.healing_time == 0:
                self.status = 2
        self.calculate_direction()
        self.move()

    def move(self):
        self.position = vectorcalc.add(self.position, self.move_direction)

        x, y = self.position
        w, h = self.universum.size

        if x < 0:
            x = 0
        if x > w-1:
            x = w
        if y < 0:
            y = 0
        if y > h-1:
            y = h

        self.position = x,y

    def calculate_direction(self):
        m_dest = vectorcalc.diff_unitvector(self.destination.pos, self.position)
        m_dest = vectorcalc.scale(m_dest, MOVE_DESTINATION_W)
        m_avoid = vectorcalc.scale(self.avoid_vector, MOVE_AVOID_W)
        m_random = vectorcalc.angle_vect(random.random() * 2 * 3.14)
        m_random = vectorcalc.scale(m_random, MOVE_RANDOM_W)

        self.move_direction = vectorcalc.scale(self.move_direction, MOMENTUM)
        self.move_direction = vectorcalc.add(self.move_direction, m_random)
        self.move_direction = vectorcalc.add(self.move_direction, m_dest)
        self.move_direction = vectorcalc.add(self.move_direction, m_avoid)

    def avoid_and_infect(self, person_list):
        self.avoid_vector = (0,0)
        for p in person_list:
            d = vectorcalc.distance(self.position, p.position)
            if d < self.avoid_radius:
                avoid_factor = d-self.avoid_radius
                vect = vectorcalc.diff_vector(p.position, self.position)
                vect = vectorcalc.scale(vect, avoid_factor)
                self.avoid_vector = vectorcalc.add(self.avoid_vector, vect)
            if self.status == 1 and d < self.infection_radius:
                if random.random() < INFECTION_CHANCE:
                    p.infect()
        self.avoid_vector = vectorcalc.unitvector(self.avoid_vector)

    def draw(self):
        pygame.draw.circle(self.universum.surface, COLORS[self.status], vectorcalc.to_int(self.position), 4)

    def infect(self):
        if self.status == 0:
            self.healing_time = random.gauss(HEALING_TIME, HEALING_VAR)
            self.status = 1
