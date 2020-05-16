import pygame
from universum import Universum


pygame.init()

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Coronanananana')

universum = Universum(SCREEN, WIDTH, HEIGHT)
universum.addPersons(100)
universum.addPersons(5, True)

is_running = True
while is_running:
    universum.draw()
    universum.tick()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()