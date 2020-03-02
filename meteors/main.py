import pygame
import sys
from settings import *
from classes.game_objects import *


# game initialization
pygame.init()
pygame.display.set_caption("Shooter")

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# game objects
background = Background("recources/background.png")
player = Player("recources/player.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    player.update()
    screen.blit(background.image, background.rect)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(30)
