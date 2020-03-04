import random

import pygame
from meteorites.settings import *


class Bullet(pygame.sprite.Sprite):
    speed = -15

    def __init__(self, image_path: str, player_pos):
        super(Bullet, self).__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.midbottom = player_pos

    def update(self):
        self.rect.move_ip(0, self.speed)


class Player(pygame.sprite.Sprite):
    speed = 7

    shoot_interval = 500
    time_for_shoot = 0

    def __init__(self, image_path: str, clock, bullets):
        super(Player, self).__init__()

        self.clock = clock
        self.bullets = bullets

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 20

        self.current_speed = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.current_speed = - self.speed
        elif keys[pygame.K_RIGHT]:
            self.current_speed = self.speed
        else:
            self.current_speed = 0

        self.rect.move_ip(self.current_speed, 0)

        self.shooting()

    def shooting(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.time_for_shoot <= 0:
            self.bullets.add(Bullet(BULLET_IMG, self.rect.midtop))
            self.time_for_shoot = self.shoot_interval
        else:
            self.time_for_shoot -= self.clock.get_time()

        for bullet in list(self.bullets):
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super(Background, self).__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.bottom = SCREEN_HEIGHT

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = SCREEN_HEIGHT


class Meteorite(pygame.sprite.Sprite):
    spawn_interval = 500
    time_for_spawn = 0

    speed = 10

    def __init__(self):
        super(Meteorite, self).__init__()

        self.image = pygame.image.load(random.choice(METEORITES_IMGS))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, SCREEN_WIDTH), 0)

    def update(self):
        self.rect.move_ip(0, self.speed)

    @staticmethod
    def spawning(clock, meteorites):
        if Meteorite.time_for_spawn <= 0:
            meteorites.add(Meteorite())
            Meteorite.time_for_spawn = Meteorite.spawn_interval
        else:
            Meteorite.time_for_spawn -= clock.get_time()

        for meteorite in list(meteorites):
            if meteorite.rect.right < 0 or meteorite.rect.left > SCREEN_WIDTH or \
                    meteorite.rect.top > SCREEN_HEIGHT:
                meteorites.remove(meteorite)


class TextObject(pygame.sprite.Sprite):
    def __init__(self, text, size, colour=BLACK, font=None, smoothing=False):
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(text, smoothing, colour)

    def draw(self, screen, pos):
        screen.blit(self.text, pos)


