import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("MEOW")
col = input("What color? ")
if col == "red":
    col = RED
elif col == "green":
    col = GREEN
elif col == "blue":
    col = BLUE
pygame.draw.circle(screen, col, (400,300), 50)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False