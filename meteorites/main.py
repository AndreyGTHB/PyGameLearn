import pygame
import sys
from meteorites.settings import *
from meteorites.classes.game_objects import *


# game initialization
pygame.init()
pygame.display.set_caption("Shooter")

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# groups
objects = pygame.sprite.Group()
bullets = pygame.sprite.Group()
meteorites = pygame.sprite.Group()

# game objects
background = Background(BACKGROUND_IMG)
player = Player(PLAYER_IMG, clock, bullets)

objects.add(background)
objects.add(player)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    Meteorite.spawning(clock, meteorites)

    objects.update()
    bullets.update()
    meteorites.update()

    objects.draw(screen)
    bullets.draw(screen)
    meteorites.draw(screen)

    pygame.display.flip()
    clock.tick(30)
