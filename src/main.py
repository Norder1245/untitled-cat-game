import pygame
RED = (255, 0, 0)
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("MEOW")
pygame.draw.circle(screen, RED, (400,300), 50)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False