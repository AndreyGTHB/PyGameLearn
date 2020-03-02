import pygame
import sys
from meteors.settings import *
from meteors.classes.game_objects import *


# game initialization
pygame.init()
pygame.display.set_caption("Shooter")

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# game objects
background = Background(BACKGROUND_IMG)
player = Player(PLAYER_IMG)

# groups
all_objects = pygame.sprite.Group()

all_objects.add(background)
all_objects.add(player)
all_objects.add(Bullet(BULLET_IMG, player.rect.midtop))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    all_objects.update()
    all_objects.draw(screen)

    pygame.display.flip()
    clock.tick(30)
