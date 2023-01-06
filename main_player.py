import os

import pygame
import pygame.sprite
from pygame.locals import *
import pytmx


class MainPlayer(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super(MainPlayer, self).__init__()
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.sprite_dir = f'src/player/'

        self.image = pygame.image.load(f'{self.sprite_dir}6.png')
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 20
        self.image1 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}1.png'), (300, 200))
        self.image2 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}2.png'), (300, 200))
        self.image3 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}3.png'), (300, 200))
        self.image4 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}4.png'), (300, 200))
        self.image5 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}5.png'), (300, 200))
        self.image6 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}6.png'), (300, 200))
        self.sprite_pac = [
            self.image1, self.image2,
            self.image3, self.image4,
            self.image5, self.image6,
        ]
        self.speed = 4
        self.cur_sprite = 0


    def update_pos(self, key):
        if key.get_pressed()[K_LEFT] or key.get_pressed()[K_a]:
            self.rect.x -= self.speed
        if key.get_pressed()[K_RIGHT] or key.get_pressed()[K_d]:
            self.rect.x += self.speed
        if key.get_pressed()[K_UP] or key.get_pressed()[K_w]:
            self.rect.y -= self.speed
        if key.get_pressed()[K_DOWN] or key.get_pressed()[K_s]:
            self.rect.y += self.speed
        pygame.event.pump()

    def update_spr(self):
        self.image = self.sprite_pac[self.cur_sprite]
        self.cur_sprite = (self.cur_sprite + 1) % len(self.sprite_pac)


