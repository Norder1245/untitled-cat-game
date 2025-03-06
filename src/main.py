import pygame, os
import sys
from PyCol import *
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("MEOW")
os.system('cls' if os.name == 'nt' else 'clear')
print("Hello, welcome to the circle thingy")
col = input("What color? ")
if col == "red":
    col = RED
elif col == "green":
    col = GREEN
elif col == "blue":
    col = BLUE
else :
    print("Invalid color")
    exit()
pygame.draw.circle(screen, col, (400,300), 50)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False