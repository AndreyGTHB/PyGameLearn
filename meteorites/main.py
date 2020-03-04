import pygame
import pyganim
import sys
from time import sleep
from meteorites.settings import *
from meteorites.classes.game_objects import *


# game initialization
pygame.init()
pygame.display.set_caption("Shooter")

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# animations
#explosion_animation = pyganim.PygAnimation()


# groups
objects = pygame.sprite.Group()
bullets = pygame.sprite.Group()
meteorites = pygame.sprite.Group()

# game objects
background = Background(BACKGROUND_IMG)
player = Player(PLAYER_IMG, clock, bullets)

objects.add(background)
objects.add(player)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    Meteorite.spawning(clock, meteorites)

    objects.update()
    bullets.update()
    meteorites.update()

    pygame.sprite.groupcollide(meteorites, bullets, True, True)
    player_collided = pygame.sprite.spritecollide(player, meteorites, False)
    if player_collided:
        print("Collided")
        objects.remove(player)

    objects.draw(screen)
    bullets.draw(screen)
    meteorites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

game_over = TextObject("GAME OVER", 40, RED, smoothing=True)
game_over.draw(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
sleep(2)
