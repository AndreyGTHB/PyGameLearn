import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str):
        super(Player, self).__init__()

        self.max_speed = 5

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 20

        self.current_speed = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.current_speed = - self.max_speed
        elif keys[pygame.K_RIGHT]:
            self.current_speed = self.max_speed
        else:
            self.current_speed = 0

        self.rect.move_ip(self.current_speed, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super(Background, self).__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.bottom = SCREEN_HEIGHT