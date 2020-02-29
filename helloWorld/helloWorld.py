import pygame
import sys
from settings import *


pygame.init()
pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode(SCREEN_SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)