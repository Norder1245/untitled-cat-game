import pygame, os
import sys
from PyCol import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("MEOW")

os.system('cls' if os.name == 'nt' else 'clear')
print("Hello, welcome to the circle thingy")

# Color selection loop
col = None
while col not in [RED, GREEN, BLUE]:
    color_input = input("What color (red, green, blue)? ").strip().lower()
    
    if color_input == "red":
        col = RED
    elif color_input == "green":
        col = GREEN
    elif color_input == "blue":
        col = BLUE
    else:
        print("Invalid color, please try again.")
        
pygame.draw.circle(screen, col, (400, 300), 50)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
